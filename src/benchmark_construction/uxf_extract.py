#!/usr/bin/env python3
"""
Extract entities and relations from a UMLet .uxf diagram into the desired JSON format.

Usage:
    python uxf_extract.py input.uxf output.json
"""
import sys
import xml.etree.ElementTree as ET
import json
import math
from pprint import pprint
from typing import Tuple, Dict, List


def color_to_hex(s: str) -> str:
    if not s:
        return "FFFFFF"
    s = s.strip()
    if s.startswith("#"):
        s = s[1:]
    if all(c in "0123456789abcdefABCDEF" for c in s) and len(s) in (3, 6):
        if len(s) == 3:
            s = "".join(ch*2 for ch in s)
        return s.upper()
    NAMED = {
        "white": "FFFFFF", "black": "000000", "red": "FF0000", "green": "008000", "blue": "0000FF",
        "yellow": "FFFF00", "purple": "800080", "orange": "FFA500", "gray": "808080", "grey": "808080",
        "lightgray": "D3D3D3", "lightgrey": "D3D3D3", "darkgray": "A9A9A9", "darkgrey": "A9A9A9",
        "pink": "FFC0CB", "cyan": "00FFFF", "magenta": "FF00FF", "brown": "A52A2A"
    }
    return NAMED.get(s.lower(), "FFFFFF")

def rect_distance_to_point(rect, pt) -> float:
    x, y, w, h = rect
    rx1, ry1, rx2, ry2 = x, y, x + w, y + h
    px, py = pt
    dx = max(rx1 - px, 0, px - rx2)
    dy = max(ry1 - py, 0, py - ry2)
    return math.hypot(dx, dy)

def parse_polyline(additional_text: str):
    if not additional_text:
        return []
    parts = [p for p in additional_text.strip().split(";") if p.strip()]
    nums = []
    for p in parts:
        try:
            nums.append(float(p))
        except:
            pass
    pts = []
    for i in range(0, len(nums)-1, 2):
        pts.append((nums[i], nums[i+1]))
    return pts

def infer_relation_type(lt_line: str) -> str:
    if not lt_line:
        return "association"
    s = lt_line.strip().replace("&lt;", "<").replace("&gt;", ">")
    if "<|-" in s or "-|>" in s:
        return "inheritance"
    if "o-" in s or "-o" in s:
        return "aggregation"
    if "*-" in s or "-*" in s or "<>" in s:
        return "composition"
    if ".." in s:
        if "<|.." in s or "..|>" in s:
            return "implementation"
        return "dependency"
    if "<-" in s or "->" in s:
        return "association"
    return "association"


def extract_entity(uxf_path: str) -> dict:

    tree = ET.parse(uxf_path)
    root = tree.getroot()

    elements = []
    for el in root.findall("element"):
        el_id = el.findtext("id", default="")
        x = float(el.find("coordinates/x").text)
        y = float(el.find("coordinates/y").text)
        w = float(el.find("coordinates/w").text)
        h = float(el.find("coordinates/h").text)
        panel = el.findtext("panel_attributes", default="")
        addi = el.findtext("additional_attributes", default="")
        elements.append({"type": el_id, "rect": (x,y,w,h), "panel": panel, "addi": addi})

    node_elems = [e for e in elements if e["type"] == "UMLClass"]
    rel_elems  = [e for e in elements if e["type"] == "Relation"]

    # entities
    entities = {}
    node_index_map = {}
    for idx, e in enumerate(node_elems):
        lines = [ln.strip() for ln in (e["panel"] or "").splitlines() if ln.strip()]
        name = e["panel"].split('bg=')[0].replace('\n', ' ').strip()
        bg = "FFFFFF"
        color = []
        for ln in (e["panel"] or "").splitlines():
            ln = ln.strip()
            if ln.lower().startswith("bg="):
                color = ln.split("=", 1)[1]
                bg = color_to_hex(color)
                break
        if color == []:
            color = 'white'
        ent_key = f"entity_{idx}"
        node_index_map[idx] = ent_key
        entities[ent_key] = {"name": name, "color": color} # color or bg

    return entities, elements, node_elems, rel_elems

# relations


# relations = []
# for r in rel_elems:
#     panel_lines = [ln for ln in (r["panel"] or "").splitlines()]
#     lt_line = ""
#     name_lines = []
#     for ln in panel_lines:
#         if ln.strip().startswith("lt="):
#             lt_line = ln.strip()
#         else:
#             if ln.strip():
#                 name_lines.append(ln.strip())
#     rel_name = " ".join(name_lines).strip()
#     rel_type = infer_relation_type(lt_line)
#     pts = parse_polyline(r["addi"] or "")
#     if len(pts) >= 2:
#         src_pt, tgt_pt = pts[0], pts[-1]
#         src_key = nearest_entity_key(src_pt)
#         tgt_key = nearest_entity_key(tgt_pt)
#     else:
#         cx = r["rect"][0] + r["rect"][2] / 2.0
#         cy = r["rect"][1] + r["rect"][3] / 2.0
#         center = (cx, cy)
#         dists = sorted([(rect_distance_to_point(rects[i], center), i) for i in range(len(rects))], key=lambda t: t[0])
#         src_key = node_index_map[dists[0][1]] if dists else ""
#         tgt_key = node_index_map[dists[1][1]] if len(dists) > 1 else src_key
#     relations.append({"source": src_key, "target": tgt_key, "name": rel_name, "type": rel_type})

# association, aggregation, inheritance

relation = [
    {'source': 'entity_0', 'target': 'entity_3', 'name': 'sends', 'type': 'association'},
]


    # {'source': 'entity_', 'target': 'entity_', 'name': '', 'type': ''},

uxf_path = 'dataset/SAD/structural/g15-UC.uxf'
entity, elements, node_elems, rel_elems = extract_entity(uxf_path)

for key in entity:
    print(key, entity[key])

json_object = {
    'entity': entity,
    'cluster': {},
    'relation': relation
}
