#!/usr/bin/env python3
"""
General SVG → JSON converter for Graphviz-style SVGs.

Produces:
{
  "Entity": { "entity_0": {"name": "..."}, ... },
  "Relation": [ {"source": "entity_0", "target": "entity_1"}, ... ]
}

Usage:
  python svg_to_json.py input.svg [-o output.json] [--include-clusters] [--dedupe-labels]
"""
import argparse
import json
from pathlib import Path
import xml.etree.ElementTree as ET
from collections import OrderedDict, defaultdict

def _strip_ns(tag: str) -> str:
    return tag.split("}", 1)[1] if "}" in tag else tag

def _gather_text(el):
    """Collect visible text under an element, preserving order."""
    lines = []
    for child in el.iter():
        if _strip_ns(child.tag) == "text":
            t = (child.text or "").strip()
            if t:
                lines.append(t)
    return lines

def parse_graphviz_svg(svg_path: Path, include_clusters: bool = False):
    """
    Parse a Graphviz SVG.
    Returns:
      nodes: OrderedDict of node_key -> label (where node_key is the <title> of the node)
      edges: list of (src_key, dst_key)
      clusters: OrderedDict of cluster_id -> label (if include_clusters=True)
    """
    tree = ET.parse(svg_path)
    root = tree.getroot()

    # Nodes: Graphviz puts nodes into <g class="node"><title>NODE_ID</title> ... <text>...</text></g>
    nodes = OrderedDict()          # node_id -> text label
    node_order = []                # preserve discovery order
    for g in root.iter():
        if _strip_ns(g.tag) == "g" and g.attrib.get("class") == "node":
            node_id = None
            for child in g:
                if _strip_ns(child.tag) == "title" and (child.text or "").strip():
                    node_id = child.text.strip()
                    break
            if not node_id:
                # If no <title>, skip (Graphviz normally includes it)
                continue
            label = " ".join(_gather_text(g)).strip()
            nodes[node_id] = label
            node_order.append(node_id)

    # Edges: <g class="edge"><title>SRC->DST</title>...</g>
    edges = []
    for g in root.iter():
        if _strip_ns(g.tag) == "g" and g.attrib.get("class") == "edge":
            t = None
            for child in g:
                if _strip_ns(child.tag) == "title" and (child.text or "").strip():
                    t = child.text.strip()
                    break
            if t and "->" in t:
                src, dst = t.split("->", 1)
                edges.append((src, dst))

    clusters = OrderedDict()
    if include_clusters:
        # Clusters: <g class="cluster"> ... <text>Cluster Label</text> ...
        # There may be multiple clusters; keep them all.
        cluster_idx = 0
        for g in root.iter():
            if _strip_ns(g.tag) == "g" and g.attrib.get("class") == "cluster":
                lines = _gather_text(g)
                if lines:
                    clusters[f"cluster_{cluster_idx}"] = " ".join(lines).strip()
                    cluster_idx += 1

    return nodes, edges, clusters

def build_entities_and_relations(nodes, edges, clusters, dedupe_labels=False):
    """
    Map discovered nodes to entity_i keys and translate edges accordingly.
    Optionally deduplicate nodes with identical labels (merging to first occurrence).
    """
    # If deduping, map label -> canonical node_id
    label_to_first_id = {}
    node_id_to_entity = OrderedDict()   # original node_id -> entity key
    entities = OrderedDict()
    relations = []

    def normalize_label(s: str) -> str:
        return " ".join((s or "").split())

    # Assign entity ids in discovery order
    next_entity_idx = 0
    for node_id, label in nodes.items():
        label = normalize_label(label) or node_id
        if dedupe_labels:
            if label in label_to_first_id:
                # Map this node_id to the existing entity
                canonical = label_to_first_id[label]
                node_id_to_entity[node_id] = node_id_to_entity[canonical]
                continue
            else:
                label_to_first_id[label] = node_id

        entity_key = f"entity_{next_entity_idx}"
        next_entity_idx += 1
        node_id_to_entity[node_id] = entity_key
        entities[entity_key] = {"name": label}

    # Optionally add clusters at the end (entity ids continue)
    cluster_entity_keys = []
    for _, clabel in clusters.items():
        clabel = normalize_label(clabel)
        entity_key = f"entity_{next_entity_idx}"
        next_entity_idx += 1
        entities[entity_key] = {"name": clabel}
        cluster_entity_keys.append(entity_key)

    # Build relations
    for src, dst in edges:
        if src in node_id_to_entity and dst in node_id_to_entity:
            relations.append({
                "source": node_id_to_entity[src],
                "target": node_id_to_entity[dst],
            })

    return entities, relations

def svg2json(svg_file):
    include_clusters = True
    dedupe_labels = False
    nodes, edges, clusters = parse_graphviz_svg(svg_file, include_clusters)
    entities, relations = build_entities_and_relations(
        nodes, edges, clusters, dedupe_labels
    )

    json_object = {"Entity": entities, "Relation": relations}
    return json_object
