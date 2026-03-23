from svg2json import svg2json
import os
import json
# TODO:
#  1. turn the .svg files into formal dataset
#  2.







# json_object = svg2json(target_file)

# import xml.etree.ElementTree as ET
#
# tree = ET.parse(target_file)
# root = tree.getroot()
#
# for elem in root.iter():
#     print(elem.tag, elem.attrib)

# from svgpathtools import svg2paths
# paths, attributes = svg2paths(target_file)

# target_dirs = ['kaggle_LLM_architectural_diagrams', 'kaggle_software_architecture_dataset', 'microserviceDataset']
#
# for target_dir in target_dirs:
#     tmp_file_list = os.listdir(dir_path + target_dir)
#     for svg_file in tmp_file_list:
#         if svg_file.endswith('.svg'):
#             svg_file_path = dir_path + target_dir + '/' + svg_file
#
#
#     break

# json_object = {
#     'entity': {
#         'entity_0': {'name': 'API Gateway'},
#         'entity_1': {'name': 'Cognito Authorize'},
#         'entity_2': {'name': 'OpenSearch Handler'},
#         'entity_3': {'name': 'API Handler'},
#         'entity_4': {'name': 'SNS Alarms topic'},
#         'entity_5': {'name': 'CloudWatch logs/alarms/metrics/dashboard'},
#         'entity_6': {'name': 'OpenSearch Catalog'},
#         'entity_7': {'name': 'Aurora Serverless Metadata DB'},
#         'entity_8': {'name': 'Worker'},
#         'entity_9': {'name': 'ECS Fargate'},
#         'entity_10': {'name': 'SQS Queue'},
#     },
#
#     'relation': [
#         {'source': '', 'target': 'entity_0', 'name': '', 'direction': 'single'},
#         {'source': 'entity_0', 'target': 'entity_1', 'name': '', 'direction': 'single'},
#         {'source': 'entity_1', 'target': 'entity_2', 'name': '', 'direction': 'single'},
#         {'source': 'entity_1', 'target': 'entity_3', 'name': '', 'direction': 'single'},
#         {'source': 'entity_3', 'target': 'entity_10', 'name': '', 'direction': 'single'},
#         {'source': 'entity_3', 'target': 'entity_7', 'name': '', 'direction': 'single'},
#         {'source': 'entity_2', 'target': 'entity_6', 'name': '', 'direction': 'single'},
#         {'source': 'entity_7', 'target': 'entity_6', 'name': '', 'direction': 'single'},
#         {'source': 'entity_10', 'target': 'entity_8', 'name': '', 'direction': 'single'},
#         {'source': 'entity_8', 'target': 'entity_9', 'name': '', 'direction': 'single'},
#         {'source': 'entity_8', 'target': 'entity_7', 'name': '', 'direction': 'single'},
#         {'source': 'entity_9', 'target': 'entity_7', 'name': '', 'direction': 'single'},
#         {'source': 'entity_7', 'target': 'entity_9', 'name': '', 'direction': 'none'},
#     ],
#
#     'cluster': {
#         'cluster_0': {'name': 'VPC', 'include_entity': ['entity_1', 'entity_2', 'entity_3', 'entity_4', 'entity_5', 'entity_6', 'entity_7', 'entity_8', 'entity_9']},
#         'cluster_1': {'name': 'Private subnet', 'include_entity': ['entity_1', 'entity_2', 'entity_3', 'entity_4', 'entity_5', 'entity_6', 'entity_7', 'entity_8', 'entity_9']},
#         'cluster_2': {'name': 'Infrastructure Monitoring', 'include_entity': ['entity_4', 'entity_5']},
#         'cluster_3': {'name': '/search', 'include_entity': ['entity_2']},
#         'cluster_4': {'name': '/graphql', 'include_entity': ['entity_3']},
#         'cluster_5': {'name': 'Short running asynchronous tasks', 'include_entity': ['entity_8', 'entity_10']},
#         'cluster_6': {'name': 'Long running asynchronous tasks', 'include_entity': ['entity_9']},
#     },
#
#     'difficulty': 'medium', # easy, medium, and hard
#     'diagram_type': 'architecture' # architecture (flowchat with icon), C4, Class, ER, flowchart, handwritten
# }
#
#
# json_object1 = {
#     'entity': {
#         'entity_0': {'name': 'Server'},
#         'entity_1': {'name': 'Database'},
#         'entity_2': {'name': 'Storage'},
#         'entity_3': {'name': 'Storage'},
#     },
#
#     'relation': [
#         {'source': 'entity_0', 'target': 'entity_1', 'name': '', 'direction': 'none'},
#         {'source': 'entity_0', 'target': 'entity_2', 'name': '', 'direction': 'none'},
#         {'source': 'entity_1', 'target': 'entity_2', 'name': '', 'direction': 'none'},
#     ],
#
#     'cluster': {
#         'cluster_0': {'name': 'API', 'include_entity': ['entity_0', 'entity_1', 'entity_2', 'entity_3']},
#     },
#
#     'difficulty': 'easy',
#     'diagram_type': 'architecture'
# }
#


# json_object2 = {
#     'entity': {
#         'entity_0': {'name': 'User'},
#         'entity_1': {'name': 'Client certificate'},
#         'entity_2': {'name': 'Intelligent application'},
#         'entity_3': {'name': 'API key'},
#         'entity_4': {'name': 'gpt-35-turbo'},
#     },
#
#     'relation': [
#         {'source': 'entity_0', 'target': 'entity_1', 'name': '', 'direction': 'none'},
#         {'source': 'entity_1', 'target': 'entity_2', 'name': '', 'direction': 'single'},
#         {'source': 'entity_2', 'target': 'entity_3', 'name': '', 'direction': 'none'},
#         {'source': 'entity_3', 'target': 'entity_4', 'name': '', 'direction': 'single'},
#     ],
#
#     'cluster': {
#         'cluster_0': {'name': 'Azure OpenAI Service', 'include_entity': ['entity_4'], 'include_cluster': []},
#         'cluster_1': {'name': 'rg-aoai-eastus', 'include_entity': ['entity_4'], 'include_cluster': ['cluster_0']},
#     },
#
#     'difficulty': 'easy',
#     'diagram_type': 'architecture'
# }


# json_object3 = {
#     'entity': {
#         'entity_0': {'name': 'Documents'},
#         'entity_1': {'name': 'Images'},
#         'entity_2': {'name': 'Document cracking'},
#         'entity_3': {'name': 'Text analytics'},
#         'entity_4': {'name': 'Translator'},
#         'entity_5': {'name': 'Vision'},
#         'entity_6': {'name': 'Azure Functions'},
#         'entity_7': {'name': 'AI DocumentIntelligence'},
#         'entity_8': {'name': 'Azure Machine Learning'},
#         'entity_9': {'name': 'Enriched documents'},
#         'entity_10': {'name': 'Search index'},
#         'entity_11': {'name': 'Web application'},
#         'entity_12': {'name': 'Blob Storage'},
#         'entity_13': {'name': 'Table Storage'},
#     },
#
#     'cluster': {
#         'cluster_0': {'name': 'Unstructured data', 'include_entity': ['entity_0', 'entity_1'], 'include_cluster': []},
#         'cluster_1': {'name': 'Blob Storage', 'include_entity': ['entity_0', 'entity_1'], 'include_cluster': ['cluster_0']},
#         'cluster_2': {'name': 'Built-in skills', 'include_entity': ['entity_3', 'entity_4', 'entity_5'], 'include_cluster': []},
#         'cluster_3': {'name': 'Custom skills', 'include_entity': ['entity_6', 'entity_7', 'entity_8'], 'include_cluster': []},
#         'cluster_4': {'name': 'AI enrichment', 'include_entity': ['entity_3', 'entity_4', 'entity_5', 'entity_6', 'entity_7', 'entity_8'], 'include_cluster': ['cluster_2', 'cluster_3']},
#         'cluster_5': {'name': 'AI Search', 'include_entity': ['entity_3', 'entity_4', 'entity_5', 'entity_6', 'entity_7', 'entity_8', 'entity_9', 'entity_10'], 'include_cluster': ['cluster_2', 'cluster_3', 'cluster_4']},
#         'cluster_6': {'name': 'Knowledge store', 'include_entity': ['entity_12', 'entity_13'], 'include_cluster': []},
#     },
#
#
#
#     'relation': [
#         {'source': 'cluster_1', 'target': 'entity_2', 'name': 'Ingestion', 'direction': 'single'},
#         {'source': 'entity_2', 'target': 'cluster_4', 'name': 'Enrich', 'direction': 'single'},
#         {'source': 'cluster_4', 'target': 'entity_9', 'name': '', 'direction': 'single'},
#         {'source': 'entity_9', 'target': 'entity_10', 'name': 'Index', 'direction': 'single'},
#         {'source': 'entity_9', 'target': 'cluster_6', 'name': 'Projections', 'direction': 'single'},
#         {'source': 'entity_11', 'target': 'entity_10', 'name': 'Query', 'direction': 'single'},
#         {'source': 'entity_11', 'target': 'cluster_6', 'name': 'Query', 'direction': 'single'},
#     ],
#
#
#
#     'difficulty': 'difficult',
#     'diagram_type': 'architecture'
# }


# json_object4 = {
#     'entity': {
#         'entity_0': {'name': 'Subscription'},
#         'entity_1': {'name': 'Public IP addresses'},
#         'entity_2': {'name': 'Application Gateway'},
#         'entity_3': {'name': 'Web Application Firewall polices (WAF)'},
#         'entity_4': {'name': 'API Management (Premium)'},
#         'entity_5': {'name': 'Private endpoint'},
#         'entity_6': {'name': 'Log Analytics workspaces'},
#         'entity_7': {'name': 'Application Insights'},
#         'entity_8': {'name': 'azure-api.net'},
#         'entity_9': {'name': 'Key vaults'},
#     },
#
#     'cluster': {
#         'cluster_0': {'name': 'Application Gateway subnet', 'include_entity': ['entity_2', 'entity_3'], 'include_cluster': []},
#         'cluster_1': {'name': 'API Management subnet', 'include_entity': ['entity_4'], 'include_cluster': []},
#         'cluster_2': {'name': 'Private endpoint subnet', 'include_entity': ['entity_5'], 'include_cluster': []},
#         'cluster_3': {'name': 'Azure API Management – Secure baseline', 'include_entity': ['entity_2', 'entity_3', 'entity_4', 'entity_5', 'entity_6', 'entity_7', 'entity_8', 'entity_9'], 'include_cluster': ['cluster_0', 'cluster_1', 'cluster_2']},
#
#     },
#
#
#     'relation': [
#         {'source': 'entity_1', 'target': 'entity_2', 'name': '', 'direction': 'single'},
#         {'source': 'entity_2', 'target': 'entity_4', 'name': 'Enrich', 'direction': 'double'},
#         {'source': 'entity_5', 'target': 'entity_9', 'name': '', 'direction': 'single'},
#     ],
#
#
#     'difficulty': 'medium',
#     'diagram_type': 'architecture'
# }


# json_object5 = {
#     'entity': {
#         'entity_0': {'name': 'Azure web app'},
#         'entity_1': {'name': 'Azure Service Bus queue'},
#         'entity_2': {'name': 'Analyze activity'},
#         'entity_3': {'name': 'Metadata store activity'},
#         'entity_4': {'name': 'Embedding activity'},
#         'entity_5': {'name': 'Azure Blob Storage'},
#         'entity_6': {'name': 'Azure AI Document Intelligence'},
#         'entity_7': {'name': 'Azure Cosmos DB'},
#         'entity_8': {'name': 'Azure AI Search (Vector store)'},
#         'entity_9': {'name': 'Azure OpenAI Service'},
#     },
#
#     'cluster': {
#         'cluster_0': {'name': 'Ingestion', 'include_entity': ['entity_0'], 'include_cluster': []},
#         'cluster_1': {'name': 'Activation', 'include_entity': ['entity_1'], 'include_cluster': []},
#         'cluster_2': {'name': 'Azure Functions orchestration', 'include_entity': ['entity_2', 'entity_3', 'entity_4'], 'include_cluster': []},
#         'cluster_3': {'name': 'Document store', 'include_entity': ['entity_5'], 'include_cluster': []},
#         'cluster_4': {'name': 'Document processing', 'include_entity': ['entity_6'], 'include_cluster': []},
#         'cluster_5': {'name': 'Document metadata collection', 'include_entity': ['entity_7'], 'include_cluster': []},
#         'cluster_6': {'name': 'Vectorize and index', 'include_entity': ['entity_8'], 'include_cluster': []},
#         'cluster_7': {'name': 'Chat with your data', 'include_entity': ['entity_9'], 'include_cluster': []},
#     },
#
#
#     'relation': [
#         {'source': 'entity_0', 'target': 'entity_1', 'name': '', 'direction': 'single'},
#         {'source': 'entity_0', 'target': 'entity_5', 'name': '', 'direction': 'single'},
#         {'source': 'entity_2', 'target': 'entity_1', 'name': '', 'direction': 'single'},
#         {'source': 'entity_2', 'target': 'entity_3', 'name': '', 'direction': 'single'},
#         {'source': 'entity_2', 'target': 'entity_6', 'name': '', 'direction': 'single'},
#         {'source': 'entity_3', 'target': 'entity_4', 'name': '', 'direction': 'single'},
#         {'source': 'entity_3', 'target': 'entity_7', 'name': '', 'direction': 'single'},
#         {'source': 'entity_4', 'target': 'entity_8', 'name': '', 'direction': 'single'},
#         {'source': 'entity_6', 'target': 'entity_5', 'name': '', 'direction': 'single'},
#         {'source': 'cluster_0', 'target': 'cluster_6', 'name': '', 'direction': 'single'},
#         {'source': 'cluster_0', 'target': 'cluster_7', 'name': '', 'direction': 'single'},
#     ],
#
#
#     'difficulty': 'medium',
#     'diagram_type': 'architecture'
# }

# json_object6 = {
#     'entity': {
#         'entity_0': {'name': 'Intelligent Application'},
#         'entity_1': {'name': 'Federated Authentication'},
#         'entity_2': {'name': 'Rate Limiter'},
#         'entity_3': {'name': 'Monitoring'},
#         'entity_4': {'name': 'Router'},
#         'entity_5': {'name': 'Compute'},
#         'entity_6': {'name': 'Cost'},
#         'entity_7': {'name': 'Usage'},
#         'entity_8': {'name': 'Load Balancer'},
#         'entity_9': {'name': 'Message Queue'},
#         'entity_10': {'name': 'Authentication'},
#         'entity_11': {'name': 'OpenAI Deployment'},
#         'entity_12': {'name': 'LLM'},
#         'entity_13': {'name': 'OpenAI Deployment'},
#         'entity_14': {'name': 'LLM'},
#         'entity_15': {'name': 'LLM'},
#     },
#
#     'cluster': {
#         'cluster_0': {'name': 'Gateway', 'include_entity': ['entity_1', 'entity_2', 'entity_3', 'entity_4', 'entity_5', 'entity_6', 'entity_7', 'entity_8', 'entity_9', 'entity_10'], 'include_cluster': []},
#         'cluster_1': {'name': 'Location A', 'include_entity': ['entity_11', 'entity_12'], 'include_cluster': []},
#         'cluster_2': {'name': 'Location B', 'include_entity': ['entity_13', 'entity_14'], 'include_cluster': []},
#         'cluster_3': {'name': 'On Premises', 'include_entity': ['entity_15'], 'include_cluster': []},
#     },
#
#
#     'relation': [
#         {'source': 'entity_0', 'target': 'entity_2', 'name': '', 'direction': 'single'},
#         {'source': 'entity_2', 'target': 'entity_4', 'name': '', 'direction': 'single'},
#         {'source': 'entity_4', 'target': 'entity_3', 'name': '', 'direction': 'single'},
#         {'source': 'entity_4', 'target': 'entity_5', 'name': '', 'direction': 'single'},
#         {'source': 'entity_4', 'target': 'entity_8', 'name': '', 'direction': 'single'},
#         {'source': 'entity_4', 'target': 'entity_9', 'name': '', 'direction': 'single'},
#         {'source': 'entity_3', 'target': 'entity_6', 'name': '', 'direction': 'single'},
#         {'source': 'entity_3', 'target': 'entity_7', 'name': '', 'direction': 'single'},
#         {'source': 'entity_8', 'target': 'entity_11', 'name': '', 'direction': 'single'},
#         {'source': 'entity_8', 'target': 'entity_12', 'name': '', 'direction': 'single'},
#         {'source': 'entity_8', 'target': 'entity_13', 'name': '', 'direction': 'single'},
#         {'source': 'entity_8', 'target': 'entity_14', 'name': '', 'direction': 'single'},
#         {'source': 'entity_8', 'target': 'entity_15', 'name': '', 'direction': 'single'},
#         {'source': 'entity_9', 'target': 'entity_8', 'name': '', 'direction': 'single'},
#     ],
#
#
#     'difficulty': 'difficult',
#     'diagram_type': 'architecture'
# }

# json_object7 = {
#     'entity': {
#         'entity_0': {'name': 'Intelligent Application'},
#         'entity_1': {'name': 'Azure API Management(gateway only)'},
#         'entity_2': {'name': 'Managed Identity'},
#         'entity_3': {'name': 'Azure API Management'},
#         'entity_4': {'name': 'Managed Identity'},
#         'entity_5': {'name': 'Azure Event Hubs'},
#         'entity_6': {'name': 'Azure Function'},
#         'entity_7': {'name': 'Azure OpenAI'},
#         'entity_8': {'name': 'Azure OpenAI Instance'},
#         'entity_9': {'name': 'Azure OpenAI Instance'},
#         'entity_10': {'name': 'Microsoft Entra ID'},
#         'entity_11': {'name': 'Azure Traffic Manager'},
#         'entity_12': {'name': 'Application Insights'},
#         'entity_13': {'name': 'Azure Monitor'},
#     },
#
#     'cluster': {
#         'cluster_0': {'name': '', 'include_entity': ['entity_1', 'entity_2'], 'include_cluster': []},
#         'cluster_1': {'name': 'Region B', 'include_entity': ['entity_1', 'entity_2', 'entity_7'], 'include_cluster': ['cluster_1']},
#         'cluster_2': {'name': '', 'include_entity': ['entity_3', 'entity_4'], 'include_cluster': []},
#         'cluster_3': {'name': 'Region A', 'include_entity': ['entity_3', 'entity_4', 'entity_5', 'entity_6', 'entity_8', 'entity_9'], 'include_cluster': ['cluster_2']},
#         'cluster_4': {'name': '', 'Monitoring': ['entity_12', 'entity_13'], 'include_cluster': []}
#     },
#
#
#     'relation': [
#         {'source': 'entity_0', 'target': 'cluster_0', 'name': '', 'direction': 'single'},
#         {'source': 'entity_0', 'target': 'cluster_2', 'name': '', 'direction': 'single'},
#         {'source': 'cluster_0', 'target': 'entity_7', 'name': '', 'direction': 'single'},
#         {'source': 'cluster_0', 'target': 'entity_8', 'name': '', 'direction': 'single'},
#         {'source': 'cluster_0', 'target': 'entity_9', 'name': '', 'direction': 'single'},
#         {'source': 'cluster_2', 'target': 'entity_7', 'name': '', 'direction': 'single'},
#         {'source': 'cluster_2', 'target': 'entity_8', 'name': '', 'direction': 'single'},
#         {'source': 'cluster_2', 'target': 'entity_9', 'name': '', 'direction': 'single'},
#         {'source': 'cluster_2', 'target': 'entity_5', 'name': 'Batch request', 'direction': 'single'},
#         {'source': 'cluster_2', 'target': 'entity_6', 'name': 'Compute service', 'direction': 'single'},
#         {'source': 'entity_6', 'target': 'cluster_2', 'name': 'Replay batched request', 'direction': 'single'},
#         {'source': 'entity_6', 'target': 'cluster_2', 'name': 'Batched request', 'direction': 'single'},
#     ],
#
#
#     'difficulty': 'difficult',
#     'diagram_type': 'architecture'
# }


# json_object8 = {
#     'entity': {
#         'entity_0': {'name': 'Intelligent Application'},
#         'entity_1': {'name': 'Identity provider'},
#         'entity_2': {'name': 'API key'},
#         'entity_3': {'name': 'gpt-35-turbo'},
#     },
#
#     'cluster': {
#         'cluster_0': {'name': 'Azure OpenAI Service', 'include_entity': ['entity_3'], 'include_cluster': []},
#         'cluster_1': {'name': 'rg-aoai-eastus', 'include_entity': ['entity_3'], 'include_cluster': ['cluster_0']},
#
#     },
#
#
#     'relation': [
#         {'source': 'entity_0', 'target': 'entity_1', 'name': '', 'direction': 'single'},
#         {'source': 'entity_0', 'target': 'entity_3', 'name': '', 'direction': 'single'},
#     ],
#
#     'difficulty': 'easy',
#     'diagram_type': 'architecture'
# }


# json_object9 = {
#     'entity': {
#         'entity_0': {'name': 'On-premises hosted intelligent application'},
#         'entity_1': {'name': 'Alternative cloud-hosted intelligent application'},
#         'entity_2': {'name': 'Shared API key'},
#         'entity_3': {'name': 'Shared API key'},
#         'entity_4': {'name': 'gpt-35-turbo'},
#     },
#
#     'cluster': {
#         'cluster_0': {'name': 'Azure OpenAI Service', 'include_entity': ['entity_4'], 'include_cluster': []},
#         'cluster_1': {'name': 'rg-aoai-eastus', 'include_entity': ['entity_4'], 'include_cluster': ['cluster_0']},
#
#     },
#
#
#     'relation': [
#         {'source': 'entity_0', 'target': 'entity_4', 'name': '', 'direction': 'single'},
#         {'source': 'entity_1', 'target': 'entity_4', 'name': '', 'direction': 'single'},
#     ],
#
#     'difficulty': 'easy',
#     'diagram_type': 'architecture'
# }

# json_object10 = {
#     'entity': {
#         'entity_0': {'name': 'Intelligent application'},
#         'entity_1': {'name': 'API key'},
#         'entity_2': {'name': 'API key'},
#         'entity_3': {'name': 'gpt-35-turbo(1106 | 30K TPM)'},
#         'entity_4': {'name': 'gpt-35-turbo(1106 | 30K TPM)'},
#     },
#
#     'cluster': {
#         'cluster_0': {'name': 'Azure OpenAI Service', 'include_entity': ['entity_3'], 'include_cluster': []},
#         'cluster_1': {'name': 'Azure OpenAI Service', 'include_entity': ['entity_4'], 'include_cluster': []},
#         'cluster_2': {'name': 'rg-aoai-eastus', 'include_entity': ['entity_3'], 'include_cluster': ['cluster_0']},
#         'cluster_3': {'name': 'rg-aoai-westus', 'include_entity': ['entity_4'], 'include_cluster': ['cluster_1']},
#     },
#
#
#     'relation': [
#         {'source': 'entity_0', 'target': 'entity_3', 'name': '', 'direction': 'single'},
#         {'source': 'entity_0', 'target': 'entity_4', 'name': '', 'direction': 'single'},
#     ],
#
#     'difficulty': 'easy',
#     'diagram_type': 'architecture'
# }


# json_object11 = {
#     'entity': {
#         'entity_0': {'name': 'Intelligent application'},
#         'entity_1': {'name': 'API key'},
#         'entity_2': {'name': 'API key'},
#         'entity_3': {'name': 'gpt-35-turbo(1106 | 30K TPM)'},
#         'entity_4': {'name': 'gpt-35-turbo(1106 | 30K TPM)'},
#     },
#
#     'cluster': {
#         'cluster_0': {'name': 'Azure OpenAI Service', 'include_entity': ['entity_3'], 'include_cluster': []},
#         'cluster_1': {'name': 'Azure OpenAI Service', 'include_entity': ['entity_4'], 'include_cluster': []},
#         'cluster_2': {'name': 'rg-aoai-eastus', 'include_entity': ['entity_3'], 'include_cluster': ['cluster_0']},
#         'cluster_3': {'name': 'rg-aoai-westus', 'include_entity': ['entity_4'], 'include_cluster': ['cluster_1']},
#     },
#
#
#     'relation': [
#         {'source': 'entity_0', 'target': 'entity_3', 'name': '', 'direction': 'single'},
#         {'source': 'entity_0', 'target': 'entity_4', 'name': '', 'direction': 'single'},
#     ],
#
#     'difficulty': 'easy',
#     'diagram_type': 'architecture'
# }

# json_object12 = {
#     'entity': {
#         'entity_0': {'name': 'Intelligent application'},
#         'entity_1': {'name': 'JWT and dedicated subscription key 1'},
#         'entity_2': {'name': 'Identity provider'},
#         'entity_3': {'name': 'Gateway'},
#         'entity_4': {'name': 'Azure managed identity'},
#         'entity_5': {'name': 'gpt-35-turbo(1106 | 30K TPM)'},
#         'entity_6': {'name': 'gpt-35-turbo(1106 | 30K TPM)'},
#     },
#
#     'cluster': {
#         'cluster_0': {'name': 'rg-gateway', 'include_entity': ['entity_3', 'entity_4'], 'include_cluster': []},
#         'cluster_1': {'name': 'Azure OpenAI Service', 'include_entity': ['entity_5'], 'include_cluster': []},
#         'cluster_2': {'name': 'rg-aoai-eastus', 'include_entity': ['entity_5'], 'include_cluster': ['cluster_1']},
#         'cluster_3': {'name': 'Azure OpenAI Service', 'include_entity': ['entity_6'], 'include_cluster': []},
#         'cluster_4': {'name': 'rg-aoai-westus', 'include_entity': ['entity_6'], 'include_cluster': ['cluster_3']},
#     },
#
#
#     'relation': [
#         {'source': 'entity_0', 'target': 'entity_3', 'name': '', 'direction': 'single'},
#         {'source': 'entity_0', 'target': 'entity_2', 'name': '', 'direction': 'double'},
#         {'source': 'entity_2', 'target': 'entity_3', 'name': 'Validate JWT', 'direction': 'double'},
#         {'source': 'entity_3', 'target': 'entity_5', 'name': '', 'direction': 'single'},
#         {'source': 'entity_3', 'target': 'entity_6', 'name': '', 'direction': 'single'},
#     ],
#
#     'difficulty': 'medium',
#     'diagram_type': 'architecture'
# }

# json_object13 = {
#     'entity': {
#         'entity_0': {'name': 'Intelligent application'},
#         'entity_1': {'name': 'Alternative cloud-hosted intelligent application'},
#         'entity_2': {'name': 'Dedicated subscription key 1'},
#         'entity_3': {'name': 'Dedicated subscription key 2'},
#         'entity_4': {'name': 'Gateway'},
#         'entity_5': {'name': 'Azure managed identity'},
#         'entity_6': {'name': 'gpt-35-turbo'},
#     },
#
#     'cluster': {
#         'cluster_0': {'name': 'Azure OpenAI Service', 'include_entity': ['entity_6'], 'include_cluster': []},
#         'cluster_1': {'name': 'rg-aoai-eastus', 'include_entity': ['entity_4', 'entity_5', 'entity_6'], 'include_cluster': ['cluster_0']},
#     },
#
#
#     'relation': [
#         {'source': 'entity_0', 'target': 'entity_4', 'name': '', 'direction': 'single'},
#         {'source': 'entity_1', 'target': 'entity_4', 'name': '', 'direction': 'single'},
#         {'source': 'entity_4', 'target': 'entity_6', 'name': '', 'direction': 'single'},
#     ],
#
#     'difficulty': 'easy',
#     'diagram_type': 'architecture'
# }

# json_object14 = {
#     'entity': {
#         'entity_0': {'name': 'User'},
#         'entity_1': {'name': 'Private DNS zones'},
#         'entity_2': {'name': 'Microsoft Entra ID'},
#         'entity_3': {'name': 'Application Insights'},
#         'entity_4': {'name': 'Azure Monitor'},
#         'entity_5': {'name': 'Application Gateway with Azure WAF'},
#         'entity_6': {'name': 'App Service private endpoint'},
#         'entity_7': {'name': 'Managed identity'},
#         'entity_8': {'name': 'App Service'},
#         'entity_9': {'name': 'App Service instance'},
#         'entity_10': {'name': 'App Service instance'},
#         'entity_11': {'name': 'App Service instance'},
#         'entity_12': {'name': 'Key Vault private endpoint'},
#         'entity_13': {'name': 'Azure Key Vault'},
#         'entity_14': {'name': 'Virtual interface'},
#         'entity_15': {'name': 'Storage private endpoint'},
#         'entity_16': {'name': 'Azure Storage'},
#         'entity_17': {'name': 'Azure AI Foundry private endpoint'},
#         'entity_18': {'name': 'Virtual interface'},
#         'entity_19': {'name': 'Azure AI Search private endpoint'},
#         'entity_20': {'name': 'Azure AI Search'},
#         'entity_21': {'name': 'Azure Cosmos DB private endpoint'},
#         'entity_22': {'name': 'Azure Cosmos DB'},
#         'entity_23': {'name': 'Internet sources'},
#         'entity_24': {'name': 'Azure Firewall'},
#         'entity_25': {'name': 'Storage private endpoint'},
#         'entity_26': {'name': 'Azure Storage'},
#         'entity_27': {'name': 'Azure Bastion'},
#         'entity_28': {'name': 'Jump box'},
#         'entity_29': {'name': 'Knowledge store private endpoint'},
#         'entity_30': {'name': 'Azure AI Search'},
#         'entity_31': {'name': 'Build agents'},
#         'entity_32': {'name': 'Azure AI Foundry account'},
#         'entity_33': {'name': 'Foundry Agent Service'},
#         'entity_34': {'name': 'Managed identities'},
#         'entity_35': {'name': 'Azure OpenAI model'},
#         'entity_36': {'name': 'DDoS Protection'},
#     },
#
#     'cluster': {
#         'cluster_0': {'name': 'Monitoring', 'include_entity': ['entity_3', 'entity_4'], 'include_cluster': []},
#         'cluster_1': {'name': 'Application Gateway subnet', 'include_entity': ['entity_5'], 'include_cluster': []},
#         'cluster_2': {'name': 'App Service integration subnet', 'include_entity': ['entity_14'], 'include_cluster': []},
#         'cluster_3': {'name': 'Azure AI agent integration subnet', 'include_entity': ['entity_18'], 'include_cluster': []},
#         'cluster_4': {'name': 'Azure firewall subnet', 'include_entity': ['entity_24'], 'include_cluster': []},
#         'cluster_5': {'name': 'Azure Bastion subnet', 'include_entity': ['entity_27'], 'include_cluster': []},
#         'cluster_6': {'name': 'Jump box subnet', 'include_entity': ['entity_28'], 'include_cluster': []},
#         'cluster_7': {'name': 'Build agents subnet', 'include_entity': ['entity_31'], 'include_cluster': []},
#         'cluster_8': {'name': 'Private endpoint subnet', 'include_entity': ['entity_6', 'entity_12', 'entity_15', 'entity_17', 'entity_21', 'entity_25', 'entity_29'], 'include_cluster': []},
#         'cluster_9': {'name': 'Virtual network', 'include_entity': ['entity_5', 'entity_6', 'entity_12', 'entity_14', 'entity_15', 'entity_17', 'entity_18', 'entity_21', 'entity_24', 'entity_25', 'entity_27', 'entity_28', 'entity_29' 'entity_31'], 'include_cluster': ['cluster_1', 'cluster_2', 'cluster_3', 'cluster_4', 'cluster_5', 'cluster_6', 'cluster_7', 'cluster_8']},
#         'cluster_10': {'name': '', 'include_entity': ['entity_13'], 'include_cluster': []},
#         'cluster_11': {'name': 'Storage for client app deployment', 'include_entity': ['entity_16'], 'include_cluster': []},
#         'cluster_12': {'name': 'Foundry Agent Service dependencies', 'include_entity': ['entity_20', 'entity_22', 'entity_26'], 'include_cluster': []},
#         'cluster_13': {'name': 'Azure AI Foundry project', 'include_entity': ['entity_33', 'entity_34'], 'include_cluster': []},
#         'cluster_14': {'name': 'Azure AI Foundry', 'include_entity': ['entity_32', 'entity_33', 'entity_34', 'entity_35'], 'include_cluster': ['cluster_13']},
#         'cluster_15': {'name': 'Zone1', 'include_entity': ['entity_9'], 'include_cluster': []},
#         'cluster_16': {'name': 'Zone2', 'include_entity': ['entity_10'], 'include_cluster': []},
#         'cluster_17': {'name': 'Zone3', 'include_entity': ['entity_11'], 'include_cluster': []},
#         'cluster_18': {'name': '', 'include_entity': ['cluster_9', 'cluster_10', 'cluster_11'], 'include_cluster': ['cluster_15', 'cluster_16', 'cluster_17']},
#     },
#
#
#     'relation': [
#         {'source': 'entity_0', 'target': 'entity_5', 'name': '', 'direction': 'single'},
#         {'source': 'entity_1', 'target': 'cluster_1', 'name': 'linked', 'direction': 'single'},
#         {'source': 'entity_5', 'target': 'entity_6', 'name': '', 'direction': 'single'},
#         {'source': 'entity_5', 'target': 'entity_12', 'name': '', 'direction': 'single'},
#         {'source': 'entity_6', 'target': 'cluster_18', 'name': '', 'direction': 'single'},
#         {'source': 'cluster_18', 'target': 'entity_14', 'name': '', 'direction': 'single'},
#         {'source': 'entity_12', 'target': 'entity_13', 'name': '', 'direction': 'single'},
#         {'source': 'entity_14', 'target': 'entity_15', 'name': '', 'direction': 'single'},
#         {'source': 'entity_15', 'target': 'cluster_16', 'name': '', 'direction': 'single'},
#         {'source': 'entity_14', 'target': 'entity_17', 'name': '', 'direction': 'single'},
#         {'source': 'entity_17', 'target': 'cluster_13', 'name': '', 'direction': 'single'},
#         {'source': 'entity_18', 'target': 'entity_17', 'name': '', 'direction': 'single'},
#         {'source': 'entity_18', 'target': 'entity_24', 'name': 'Outbound traffic', 'direction': 'single'},
#         {'source': 'entity_18', 'target': 'entity_19', 'name': '', 'direction': 'single'},
#         {'source': 'entity_19', 'target': 'entity_20', 'name': '', 'direction': 'single'},
#         {'source': 'entity_18', 'target': 'entity_21', 'name': '', 'direction': 'single'},
#         {'source': 'entity_21', 'target': 'entity_22', 'name': '', 'direction': 'single'},
#         {'source': 'entity_18', 'target': 'entity_25', 'name': '', 'direction': 'single'},
#         {'source': 'entity_25', 'target': 'entity_26', 'name': '', 'direction': 'single'},
#         {'source': 'entity_18', 'target': 'entity_29', 'name': '', 'direction': 'single'},
#         {'source': 'entity_29', 'target': 'entity_30', 'name': '', 'direction': 'single'},
#         {'source': 'entity_24', 'target': 'entity_23', 'name': '', 'direction': 'single'},
#         {'source': 'cluster_6', 'target': 'entity_17', 'name': '', 'direction': 'single'},
#         {'source': 'entity_33', 'target': 'entity_18', 'name': '', 'direction': 'single'},
#         {'source': 'entity_32', 'target': 'entity_33', 'name': '', 'direction': 'single'},
#         {'source': 'entity_33', 'target': 'entity_35', 'name': '', 'direction': 'single'},
#     ],
#
#     'difficulty': 'difficult',
#     'diagram_type': 'architecture'
# }

# json_object15 = {
#     'entity': {
#         'entity_0': {'name': 'Client A'},
#         'entity_1': {'name': 'Client B'},
#         'entity_2': {'name': 'Gateway'},
#         'entity_3': {'name': 'Azure OpenAl Service private endpoint'},
#         'entity_4': {'name': 'Azure OpenAl Service private endpoint'},
#         'entity_5': {'name': 'gpt-35-turbo'},
#         'entity_6': {'name': 'gpt-4o'},
#         'entity_7': {'name': 'gpt-4'},
#         'entity_8': {'name': 'gpt-4o'},
#         'entity_9': {'name': 'Azure OpenAl Service'},
#         'entity_10': {'name': 'Azure OpenAl Service'},
#         'entity_11': {'name': 'Azure Monitor'},
#     },
#
#     'cluster': {
#         'cluster_0': {'name': '', 'include_entity': ['entity_2', 'entity_3', 'entity_4'], 'include_cluster': []},
#         'cluster_1': {'name': '', 'include_entity': ['entity_5', 'entity_6', 'entity_9'], 'include_cluster': []},
#         'cluster_2': {'name': '', 'include_entity': ['entity_7', 'entity_8', 'entity_10'], 'include_cluster': []},
#     },
#
#
#     'relation': [
#         {'source': 'entity_0', 'target': 'entity_2', 'name': '', 'direction': 'single'},
#         {'source': 'entity_1', 'target': 'entity_2', 'name': '', 'direction': 'single'},
#         {'source': 'entity_2', 'target': 'entity_3', 'name': '', 'direction': 'single'},
#         {'source': 'entity_2', 'target': 'entity_4', 'name': '', 'direction': 'single'},
#         {'source': 'entity_2', 'target': 'entity_11', 'name': 'Usage metrics, including client IP address, model, and token data', 'direction': 'single'},
#         {'source': 'entity_3', 'target': 'entity_5', 'name': '', 'direction': 'single'},
#         {'source': 'entity_3', 'target': 'entity_6', 'name': '', 'direction': 'single'},
#         {'source': 'entity_4', 'target': 'entity_7', 'name': '', 'direction': 'single'},
#         {'source': 'entity_4', 'target': 'entity_8', 'name': '', 'direction': 'single'},
#         {'source': 'entity_9', 'target': 'entity_11', 'name': 'Azure OpenAl Service metrics and logs', 'direction': 'single'},
#         {'source': 'entity_10', 'target': 'entity_11', 'name': 'Azure OpenAl Service metrics and logs', 'direction': 'single'},
#     ],
#
#     'difficulty': 'medium',
#     'diagram_type': 'architecture'
# }

# json_object16 = {
#     'entity': {
#         'entity_0': {'name': 'Client A'},
#         'entity_1': {'name': 'Client B'},
#         'entity_2': {'name': 'gpt-35-turbo'},
#         'entity_3': {'name': 'gpt-4o'},
#         'entity_4': {'name': 'gpt-4'},
#         'entity_5': {'name': 'gpt-4o'},
#         'entity_6': {'name': 'Azure OpenAl Service'},
#         'entity_7': {'name': 'Azure OpenAl Service'},
#         'entity_8': {'name': 'Azure Monitor'},
#     },
#
#     'cluster': {
#         'cluster_0': {'name': '', 'include_entity': ['entity_2', 'entity_3', 'entity_6'], 'include_cluster': []},
#         'cluster_1': {'name': '', 'include_entity': ['entity_4', 'entity_5', 'entity_7'], 'include_cluster': []},
#     },
#
#
#     'relation': [
#         {'source': 'entity_0', 'target': 'entity_2', 'name': '', 'direction': 'single'},
#         {'source': 'entity_0', 'target': 'entity_3', 'name': '', 'direction': 'single'},
#         {'source': 'entity_1', 'target': 'entity_4', 'name': '', 'direction': 'single'},
#         {'source': 'entity_1', 'target': 'entity_5', 'name': '', 'direction': 'single'},
#         {'source': 'entity_6', 'target': 'entity_8', 'name': 'Azure OpenAl Service metrics and logs', 'direction': 'single'},
#         {'source': 'entity_7', 'target': 'entity_8', 'name': 'Azure OpenAl Service metrics and logs', 'direction': 'single'},
#     ],
#
#     'difficulty': 'medium',
#     'diagram_type': 'architecture'
# }


# json_object17 = {
#     'entity': {
#         'entity_0': {'name': 'Client A'},
#         'entity_1': {'name': 'Client B'},
#         'entity_2': {'name': 'Gateway'},
#         'entity_3': {'name': 'Azure OpenAl Service private endpoint'},
#         'entity_4': {'name': 'Azure OpenAl Service private endpoint'},
#         'entity_5': {'name': 'gpt-35-turbo'},
#         'entity_6': {'name': 'gpt-4o'},
#         'entity_7': {'name': 'gpt-4'},
#         'entity_8': {'name': 'gpt-4o'},
#         'entity_9': {'name': 'Azure OpenAl Service'},
#         'entity_10': {'name': 'Azure OpenAl Service'},
#         'entity_11': {'name': 'Azure Monitor'},
#         'entity_12': {'name': 'Cache'},
#         'entity_13': {'name': 'Message bus'},
#         'entity_14': {'name': 'Storage'},
#         'entity_15': {'name': 'Stream processing'},
#     },
#
#     'cluster': {
#         'cluster_0': {'name': '', 'include_entity': ['entity_2', 'entity_3', 'entity_4'], 'include_cluster': []},
#         'cluster_1': {'name': '', 'include_entity': ['entity_5', 'entity_6', 'entity_9'], 'include_cluster': []},
#         'cluster_2': {'name': '', 'include_entity': ['entity_7', 'entity_8', 'entity_10'], 'include_cluster': []},
#     },
#
#
#     'relation': [
#         {'source': 'entity_0', 'target': 'entity_2', 'name': '', 'direction': 'single'},
#         {'source': 'entity_1', 'target': 'entity_2', 'name': '', 'direction': 'single'},
#         {'source': 'entity_2', 'target': 'entity_3', 'name': '', 'direction': 'single'},
#         {'source': 'entity_2', 'target': 'entity_4', 'name': '', 'direction': 'single'},
#         {'source': 'entity_2', 'target': 'entity_11', 'name': '', 'direction': 'single'},
#         {'source': 'entity_2', 'target': 'entity_12', 'name': '', 'direction': 'single'},
#         {'source': 'entity_2', 'target': 'entity_13', 'name': 'Inputs and outputs', 'direction': 'single'},
#         {'source': 'entity_3', 'target': 'entity_5', 'name': '', 'direction': 'single'},
#         {'source': 'entity_3', 'target': 'entity_6', 'name': '', 'direction': 'single'},
#         {'source': 'entity_4', 'target': 'entity_7', 'name': '', 'direction': 'single'},
#         {'source': 'entity_4', 'target': 'entity_8', 'name': '', 'direction': 'single'},
#         {'source': 'entity_9', 'target': 'entity_11', 'name': 'Azure OpenAl Service metrics and logs', 'direction': 'single'},
#         {'source': 'entity_10', 'target': 'entity_11', 'name': 'Azure OpenAl Service metrics and logs', 'direction': 'single'},
#         {'source': 'entity_13', 'target': 'entity_14', 'name': '', 'direction': 'single'},
#         {'source': 'entity_13', 'target': 'entity_15', 'name': '', 'direction': 'single'},
#     ],
#
#     'difficulty': 'difficult',
#     'diagram_type': 'architecture'
# }

# json_object18 = {
#     'entity': {
#         'entity_0': {'name': 'Call audio files'},
#         'entity_1': {'name': 'Call transcripts'},
#         'entity_2': {'name': 'Sync call data'},
#         'entity_3': {'name': 'Storage account'},
#         'entity_4': {'name': 'Azure AI Content Understanding'},
#         'entity_5': {'name': 'Azure AI Search'},
#         'entity_6': {'name': 'Azure SQL Database'},
#         'entity_7': {'name': 'Topic modeling'},
#         'entity_8': {'name': 'Azure AI Foundry'},
#         'entity_9': {'name': 'Container Registry'},
#         'entity_10': {'name': 'App Service'},
#         'entity_11': {'name': 'App Service'},
#         'entity_12': {'name': 'Semantic Kernel'},
#         'entity_13': {'name': 'Web front end to explore call insights, chat to ask questions, and chart generations'},
#         'entity_14': {'name': 'Azure Cosmos DB'},
#     },
#
#     'cluster': {
#         'cluster_0': {'name': '', 'include_entity': ['entity_5', 'entity_6'], 'include_cluster': []},
#         'cluster_1': {'name': 'Process data pipeline', 'include_entity': ['entity_2', 'entity_3', 'entity_4', 'entity_5', 'entity_6', 'entity_7', 'entity_8'], 'include_cluster': ['cluster_0']},
#         'cluster_2': {'name': 'Orchestration to handle chat requests', 'include_entity': ['entity_10', 'entity_12'], 'include_cluster': []},
#     },
#
#
#     'relation': [
#         {'source': 'entity_2', 'target': 'entity_0', 'name': '', 'direction': 'single'},
#         {'source': 'entity_2', 'target': 'entity_1', 'name': '', 'direction': 'single'},
#         {'source': 'entity_2', 'target': 'entity_3', 'name': '', 'direction': 'single'},
#         {'source': 'entity_2', 'target': 'entity_4', 'name': '', 'direction': 'single'},
#         {'source': 'entity_2', 'target': 'cluster_0', 'name': '', 'direction': 'single'},
#         {'source': 'entity_7', 'target': 'cluster_0', 'name': '', 'direction': 'single'},
#         {'source': 'entity_7', 'target': 'entity_8', 'name': '', 'direction': 'single'},
#         {'source': 'cluster_2', 'target': 'cluster_0', 'name': '', 'direction': 'single'},
#         {'source': 'entity_11', 'target': 'entity_9', 'name': '', 'direction': 'single'},
#         {'source': 'entity_11', 'target': 'cluster_2', 'name': '', 'direction': 'single'},
#         {'source': 'entity_11', 'target': 'entity_13', 'name': '', 'direction': 'single'},
#         {'source': 'entity_11', 'target': 'entity_14', 'name': '', 'direction': 'single'},
#     ],
#
#     'difficulty': 'difficult',
#     'diagram_type': 'architecture'
# }


# json_object19 = {
#     'entity': {
#         'entity_0': {'name': 'Document creation requirements'},
#         'entity_1': {'name': 'Template selection agent'},
#         'entity_2': {'name': 'Model,template library, and research tools'},
#         'entity_3': {'name': 'Clause customization agent'},
#         'entity_4': {'name': 'Fine-tuned model'},
#         'entity_5': {'name': 'Regulatory compliance agent'},
#         'entity_6': {'name': 'Model, regulatory knowledge'},
#         'entity_7': {'name': 'Risk assessment agent'},
#         'entity_8': {'name': 'Model, liability knowledge, and persistence tools'},
#         'entity_9': {'name': 'Document state'},
#         'entity_10': {'name': 'Proposed document'},
#     },
#
#     'cluster': {
#     },
#
#
#     'relation': [
#         {'source': 'entity_0', 'target': 'entity_1', 'name': '', 'direction': 'single'},
#         {'source': 'entity_1', 'target': 'entity_2', 'name': '', 'direction': 'none'},
#         {'source': 'entity_1', 'target': 'entity_3', 'name': '', 'direction': 'single'},
#         {'source': 'entity_3', 'target': 'entity_4', 'name': '', 'direction': 'none'},
#         {'source': 'entity_3', 'target': 'entity_5', 'name': '', 'direction': 'single'},
#         {'source': 'entity_5', 'target': 'entity_6', 'name': '', 'direction': 'none'},
#         {'source': 'entity_5', 'target': 'entity_7', 'name': '', 'direction': 'single'},
#         {'source': 'entity_7', 'target': 'entity_8', 'name': '', 'direction': 'single'},
#         {'source': 'entity_7', 'target': 'entity_10', 'name': '', 'direction': 'single'},
#     ],
#
#     'difficulty': 'medium',
#     'diagram_type': 'architecture'
# }

# json_object20 = {
#     'entity': {
#         'entity_0': {'name': 'Input'},
#         'entity_1': {'name': 'Agent 1'},
#         'entity_2': {'name': 'Model, knowledge, and tools'},
#         'entity_3': {'name': 'Agent 2'},
#         'entity_4': {'name': 'Model, knowledge, and tools'},
#         'entity_5': {'name': '...'},
#         'entity_6': {'name': 'Agent n'},
#         'entity_7': {'name': 'Model, knowledge, and tools'},
#         'entity_8': {'name': 'Common state'},
#         'entity_9': {'name': 'Result'},
#     },
#
#     'cluster': {
#     },
#
#
#     'relation': [
#         {'source': 'entity_0', 'target': 'entity_1', 'name': '', 'direction': 'single'},
#         {'source': 'entity_1', 'target': 'entity_2', 'name': '', 'direction': 'none'},
#         {'source': 'entity_1', 'target': 'entity_3', 'name': '', 'direction': 'single'},
#         {'source': 'entity_3', 'target': 'entity_4', 'name': '', 'direction': 'none'},
#         {'source': 'entity_3', 'target': 'entity_5', 'name': '', 'direction': 'single'},
#         {'source': 'entity_5', 'target': 'entity_6', 'name': '', 'direction': 'single'},
#         {'source': 'entity_6', 'target': 'entity_7', 'name': '', 'direction': 'none'},
#         {'source': 'entity_7', 'target': 'entity_9', 'name': '', 'direction': 'single'},
#     ],
#
#     'difficulty': 'medium',
#     'diagram_type': 'architecture'
# }

# json_object21 = {
#     'entity': {
#         'entity_0': {'name': 'User'},
#         'entity_1': {'name': 'Intelligent application'},
#         'entity_2': {'name': 'Identity provider'},
#         'entity_3': {'name': 'Orchestrator'},
#         'entity_4': {'name': 'Foundation models'},
#         'entity_5': {'name': 'Shared data Databases and vector stores'},
#         'entity_6': {'name': 'Multitenant Databases and vector stores'},
#         'entity_7': {'name': 'Tenant 1 Databases and vector stores'},
#         'entity_8': {'name': 'Tenant 2 Databases and vector stores'},
#     },
#
#     'cluster': {
#     },
#
#
#     'relation': [
#         {'source': 'entity_0', 'target': 'entity_1', 'name': '', 'direction': 'single'},
#         {'source': 'entity_1', 'target': 'entity_2', 'name': '', 'direction': 'single'},
#         {'source': 'entity_1', 'target': 'entity_3', 'name': '', 'direction': 'single'},
#         {'source': 'entity_3', 'target': 'entity_4', 'name': '', 'direction': 'single'},
#         {'source': 'entity_3', 'target': 'entity_5', 'name': '', 'direction': 'single'},
#         {'source': 'entity_3', 'target': 'entity_6', 'name': '', 'direction': 'single'},
#         {'source': 'entity_3', 'target': 'entity_7', 'name': '', 'direction': 'single'},
#         {'source': 'entity_3', 'target': 'entity_8', 'name': '', 'direction': 'single'},
#     ],
#
#     'difficulty': 'medium',
#     'diagram_type': 'architecture'
# }

# json_object22 = {
#     'entity': {
#         'entity_0': {'name': 'Client'},
#         'entity_1': {'name': 'gpt-35-turbo (standard)'},
#         'entity_2': {'name': 'Azure OpenAI (Primary)'},
#         'entity_3': {'name': 'Azure RBAC for API access'},
#         'entity_4': {'name': 'gpt-35-turbo (standard)'},
#         'entity_5': {'name': 'Azure OpenAI (Secondary)'},
#         'entity_6': {'name': 'Azure RBAC for API access'},
#     },
#
#     'cluster': {
#         'cluster_0': {'name': 'rg-aoai-eastus', 'include_entity': ['entity_1', 'entity_2', 'entity_3'], 'include_cluster': []},
#         'cluster_1': {'name': 'Workload subscription A', 'include_entity': ['entity_1', 'entity_2', 'entity_3'], 'include_cluster': ['cluster_0']},
#         'cluster_2': {'name': 'rg-aoai-eastus', 'include_entity': ['entity_4', 'entity_5', 'entity_6'], 'include_cluster': []},
#         'cluster_3': {'name': 'Workload subscription B', 'include_entity': ['entity_4', 'entity_5', 'entity_6'], 'include_cluster': ['cluster_2']},
#     },
#
#
#     'relation': [
#         {'source': 'entity_0', 'target': 'entity_1', 'name': '', 'direction': 'single'},
#         {'source': 'entity_0', 'target': 'entity_4', 'name': '', 'direction': 'single'},
#     ],
#
#     'difficulty': 'easy',
#     'diagram_type': 'architecture'
# }

# json_object23 = {
#     'entity': {
#         'entity_0': {'name': 'Client'},
#         'entity_1': {'name': 'Gateway'},
#         'entity_2': {'name': 'Azure OpenAI Private Endpoint'},
#         'entity_3': {'name': 'Azure OpenAI Private Endpoint'},
#         'entity_4': {'name': 'gpt-35-turbo (standard)'},
#         'entity_5': {'name': 'Azure OpenAI (Primary)'},
#         'entity_6': {'name': 'Azure RBAC for API access'},
#         'entity_7': {'name': 'gpt-35-turbo (standard)'},
#         'entity_8': {'name': 'Azure OpenAI (Secondary)'},
#         'entity_9': {'name': 'Azure RBAC for API access'},
#     },
#
#     'cluster': {
#         'cluster_0': {'name': 'rg-gateway-eastus', 'include_entity': ['entity_1', 'entity_2', 'entity_3'], 'include_cluster': []},
#         'cluster_1': {'name': 'Workload gateway subscription', 'include_entity': ['entity_1', 'entity_2', 'entity_3'], 'include_cluster': ['cluster_0']},
#         'cluster_2': {'name': 'rg-aoai-eastus', 'include_entity': ['entity_4', 'entity_5', 'entity_6'], 'include_cluster': []},
#         'cluster_3': {'name': 'Workload subscription A', 'include_entity': ['entity_4', 'entity_5', 'entity_6'], 'include_cluster': ['cluster_2']},
#         'cluster_4': {'name': 'rg-aoai-eastus', 'include_entity': ['entity_7', 'entity_8', 'entity_9'], 'include_cluster': []},
#         'cluster_5': {'name': 'Workload subscription B', 'include_entity': ['entity_7', 'entity_8', 'entity_9'], 'include_cluster': ['cluster_4']},
#     },
#
#
#     'relation': [
#         {'source': 'entity_0', 'target': 'entity_1', 'name': '', 'direction': 'single'},
#         {'source': 'entity_1', 'target': 'entity_2', 'name': '', 'direction': 'single'},
#         {'source': 'entity_1', 'target': 'entity_3', 'name': '', 'direction': 'single'},
#         {'source': 'entity_2', 'target': 'entity_4', 'name': '', 'direction': 'single'},
#         {'source': 'entity_3', 'target': 'entity_7', 'name': '', 'direction': 'single'},
#     ],
#
#     'difficulty': 'easy',
#     'diagram_type': 'architecture'
# }

# json_object24 = {
#     'entity': {
#         'entity_0': {'name': 'Client'},
#         'entity_1': {'name': 'Azure Front Door + Azure WAF'},
#         'entity_2': {'name': 'Traffic Manager'},
#         'entity_3': {'name': 'Gateway compute (gateway and regional control plane)'},
#         'entity_4': {'name': 'Gateway compute (gateway and regional control plane)'},
#         'entity_5': {'name': 'Azure OpenAI Private Endpoint for West US'},
#         'entity_6': {'name': 'Azure OpenAI Private Endpoint for East US'},
#         'entity_7': {'name': 'gpt-4 (provisioned)'},
#         'entity_8': {'name': 'gpt-4 (standard)'},
#         'entity_9': {'name': 'Azure OpenAI (Active & Passive)'},
#         'entity_10': {'name': 'Azure RBAC for API access'},
#         'entity_11': {'name': 'gpt-4 (provisioned)'},
#         'entity_12': {'name': 'gpt-4 (standard)'},
#         'entity_13': {'name': 'Azure OpenAI (Active & Passive)'},
#         'entity_14': {'name': 'Azure RBAC for API access'},
#     },
#
#     'cluster': {
#         'cluster_0': {'name': 'rg-gateway-global', 'include_entity': ['entity_1', 'entity_2'], 'include_cluster': []},
#         'cluster_1': {'name': 'Global', 'include_entity': ['entity_1', 'entity_2'], 'include_cluster': ['cluster_0']},
#         'cluster_2': {'name': 'rg-gateway-westus', 'include_entity': ['entity_3'], 'include_cluster': []},
#         'cluster_3': {'name': 'rg-gateway-eastus', 'include_entity': ['entity_4'], 'include_cluster': []},
#         'cluster_4': {'name': '', 'include_entity': ['entity_7', 'entity_8', 'entity_9', 'entity_10'], 'include_cluster': []},
#         'cluster_5': {'name': '', 'include_entity': ['entity_11', 'entity_12', 'entity_13', 'entity_14'], 'include_cluster': []},
#         'cluster_6': {'name': 'rg-aoai-westus', 'include_entity': ['entity_3', 'entity_7', 'entity_8', 'entity_9', 'entity_10'], 'include_cluster': ['cluster_4']},
#         'cluster_7': {'name': 'rg-aoai-eastus', 'include_entity': ['entity_4', 'entity_11', 'entity_12', 'entity_13', 'entity_14'], 'include_cluster': ['cluster_5']},
#         'cluster_8': {'name': 'West US', 'include_entity': ['entity_3', 'entity_7', 'entity_8', 'entity_9', 'entity_10'], 'include_cluster': ['cluster_4', 'cluster_6']},
#         'cluster_9': {'name': 'East US', 'include_entity': ['entity_4', 'entity_11', 'entity_12', 'entity_13', 'entity_14'], 'include_cluster': ['cluster_5', 'cluster_7']},
#     },
#
#
#     'relation': [
#         {'source': 'entity_0', 'target': 'entity_1', 'name': 'FQDN + TLS + Anycast', 'direction': 'single'},
#         {'source': 'entity_0', 'target': 'entity_2', 'name': 'DNS', 'direction': 'none'},
#         {'source': 'entity_0', 'target': 'cluster_3', 'name': 'CNAME FQDN + TLS', 'direction': 'single'},
#         {'source': 'entity_1', 'target': 'cluster_2', 'name': 'RegionalFQDN', 'direction': 'single'},
#         {'source': 'entity_1', 'target': 'cluster_3', 'name': 'RegionalFQDN', 'direction': 'single'},
#         {'source': 'entity_3', 'target': 'entity_5', 'name': '', 'direction': 'single'},
#         {'source': 'entity_3', 'target': 'entity_6', 'name': 'Failover for regional Azure OpenAI outage', 'direction': 'single'},
#         {'source': 'entity_4', 'target': 'entity_6', 'name': '', 'direction': 'single'},
#         {'source': 'entity_4', 'target': 'entity_5', 'name': 'Failover for regional Azure OpenAI outage', 'direction': 'single'},
#         {'source': 'entity_5', 'target': 'entity_7', 'name': '', 'direction': 'single'},
#         {'source': 'entity_5', 'target': 'entity_8', 'name': '', 'direction': 'single'},
#         {'source': 'entity_6', 'target': 'entity_11', 'name': '', 'direction': 'single'},
#         {'source': 'entity_6', 'target': 'entity_12', 'name': '', 'direction': 'single'},
#     ],
#
#     'difficulty': 'difficult',
#     'diagram_type': 'architecture'
# }


# json_object25 = {
#     'entity': {
#         'entity_0': {'name': 'Client (client-side, active-active load balacing)'},
#         'entity_1': {'name': 'gpt-4 (standard)'},
#         'entity_2': {'name': 'Azure OpenAI'},
#         'entity_3': {'name': 'Azure RBAC for API access'},
#         'entity_4': {'name': 'gpt-4 (standard)'},
#         'entity_5': {'name': 'Azure OpenAI'},
#         'entity_6': {'name': 'Azure RBAC for API access'},
#         'entity_7': {'name': 'Client (client-side failover)'},
#         'entity_8': {'name': 'gpt-4 (standard)'},
#         'entity_9': {'name': 'Azure OpenAI (Secondary)'},
#         'entity_10': {'name': 'Azure RBAC for API access'},
#         'entity_11': {'name': 'gpt-4 (provisioned)'},
#         'entity_12': {'name': 'Azure OpenAI (Primary)'},
#         'entity_13': {'name': 'Azure RBAC for API access'},
#         'entity_14': {'name': 'US client (geo pinned)'},
#         'entity_15': {'name': 'Germany client (geo pinned)'},
#         'entity_16': {'name': 'gpt-4 (provisioned)'},
#         'entity_17': {'name': 'Azure OpenAI'},
#         'entity_18': {'name': 'Azure RBAC for API access'},
#         'entity_19': {'name': 'gpt-4 (provisioned)'},
#         'entity_20': {'name': 'Azure OpenAI'},
#         'entity_21': {'name': 'Azure RBAC for API access'},
#     },
#
#     'cluster': {
#         'cluster_0': {'name': 'rg-aoai-eastus', 'include_entity': ['entity_1', 'entity_2', 'entity_3'], 'include_cluster': []},
#         'cluster_1': {'name': 'West US (active)', 'include_entity': ['entity_1', 'entity_2', 'entity_3'], 'include_cluster': ['cluster_0']},
#         'cluster_2': {'name': 'rg-aoai-westus', 'include_entity': ['entity_4', 'entity_5', 'entity_6'], 'include_cluster': []},
#         'cluster_3': {'name': 'East US (active)', 'include_entity': ['entity_4', 'entity_5', 'entity_6'], 'include_cluster': ['cluster_2']},
#         'cluster_4': {'name': 'rg-aoai-eastus', 'include_entity': ['entity_8', 'entity_9', 'entity_10'], 'include_cluster': []},
#         'cluster_5': {'name': 'West US (passive failover)', 'include_entity': ['entity_8', 'entity_9', 'entity_10'], 'include_cluster': ['cluster_4']},
#         'cluster_6': {'name': 'rg-aoai-westus', 'include_entity': ['entity_11', 'entity_12', 'entity_13'], 'include_cluster': []},
#         'cluster_7': {'name': 'East US', 'include_entity': ['entity_11', 'entity_12', 'entity_13'], 'include_cluster': ['cluster_6']},
#         'cluster_8': {'name': 'rg-aoai-eastus', 'include_entity': ['entity_16', 'entity_17', 'entity_18'], 'include_cluster': []},
#         'cluster_9': {'name': 'East US', 'include_entity': ['entity_16', 'entity_17', 'entity_18'], 'include_cluster': ['cluster_8']},
#         'cluster_10': {'name': 'rg-aoai-eastus', 'include_entity': ['entity_16', 'entity_17', 'entity_18'], 'include_cluster': []},
#         'cluster_11': {'name': 'East US', 'include_entity': ['entity_19', 'entity_20', 'entity_21'], 'include_cluster': ['cluster_10']},
#     },
#
#
#     'relation': [
#         {'source': 'entity_0', 'target': 'entity_1', 'name': '', 'direction': 'single'},
#         {'source': 'entity_0', 'target': 'entity_4', 'name': '', 'direction': 'single'},
#         {'source': 'entity_7', 'target': 'entity_8', 'name': '', 'direction': 'single'},
#         {'source': 'entity_7', 'target': 'entity_11', 'name': '', 'direction': 'single'},
#         {'source': 'entity_14', 'target': 'entity_16', 'name': '', 'direction': 'single'},
#         {'source': 'entity_15', 'target': 'entity_19', 'name': '', 'direction': 'single'},
#     ],
#
#     'difficulty': 'medium',
#     'diagram_type': 'architecture'
# }

# json_object26 = {
#     'entity': {
#         'entity_0': {'name': 'Client'},
#         'entity_1': {'name': 'API Management (Single gateway)'},
#         'entity_2': {'name': 'Azure OpenAI Private Endpoint for West US'},
#         'entity_3': {'name': 'gpt-4 (standard)'},
#         'entity_5': {'name': 'Azure OpenAI (Active)'},
#         'entity_6': {'name': 'Azure RBAC for API access'},
#         'entity_7': {'name': 'Azure OpenAI Private Endpoint for East US'},
#         'entity_8': {'name': 'gpt-4 (standard)'},
#         'entity_9': {'name': 'Azure OpenAI (Active)'},
#         'entity_10': {'name': 'Azure RBAC for API access'},
#     },
#
#     'cluster': {
#         'cluster_0': {'name': 'rg-gateway', 'include_entity': ['entity_1'], 'include_cluster': []},
#         'cluster_1': {'name': '', 'include_entity': ['entity_3', 'entity_4', 'entity_5'], 'include_cluster': []},
#         'cluster_2': {'name': 'rg-aoai-westus', 'include_entity': ['entity_2', 'entity_3', 'entity_4', 'entity_5'], 'include_cluster': ['cluster_1']},
#         'cluster_3': {'name': 'West US', 'include_entity': ['entity_1', 'entity_2', 'entity_3', 'entity_4', 'entity_5'], 'include_cluster': ['cluster_0', 'cluster_1', 'cluster_2']},
#         'cluster_4': {'name': '', 'include_entity': ['entity_8', 'entity_9', 'entity_10'], 'include_cluster': []},
#         'cluster_5': {'name': 'rg-aoai-eastus', 'include_entity': ['entity_7', 'entity_8', 'entity_9', 'entity_10'], 'include_cluster': ['cluster_4']},
#         'cluster_6': {'name': 'East US', 'include_entity': ['entity_7', 'entity_8', 'entity_9', 'entity_10'], 'include_cluster': ['cluster_4', 'cluster_5']},
#     },
#
#
#     'relation': [
#         {'source': 'entity_0', 'target': 'entity_1', 'name': '', 'direction': 'single'},
#         {'source': 'entity_1', 'target': 'entity_2', 'name': '', 'direction': 'single'},
#         {'source': 'entity_1', 'target': 'entity_7', 'name': '', 'direction': 'single'},
#         {'source': 'entity_2', 'target': 'entity_3', 'name': '', 'direction': 'single'},
#         {'source': 'entity_7', 'target': 'entity_8', 'name': '', 'direction': 'single'},
#     ],
#
#     'difficulty': 'medium',
#     'diagram_type': 'architecture'
# }

# json_object27 = {
#     'entity': {
#         'entity_0': {'name': 'Client'},
#         'entity_1': {'name': 'Built-in API Management FQDN (uses performance based routing)'},
#         'entity_2': {'name': 'API Management (gateway and control plane)'},
#         'entity_3': {'name': 'API Management (eastus gateway only)'},
#         'entity_4': {'name': 'Azure OpenAI Private Endpoint for West US'},
#         'entity_5': {'name': 'Azure OpenAI Private Endpoint for East US'},
#         'entity_6': {'name': 'gpt-4 (provisioned)'},
#         'entity_7': {'name': 'Azure OpenAI'},
#         'entity_8': {'name': 'Azure RBAC for API access'},
#         'entity_9': {'name': 'gpt-4 (provisioned)'},
#         'entity_10': {'name': 'Azure OpenAI'},
#         'entity_11': {'name': 'Azure RBAC for API access'},
#     },
#
#     'cluster': {
#         'cluster_0': {'name': 'rg-gateway-westus', 'include_entity': ['entity_1', 'entity_2'], 'include_cluster': []},
#         'cluster_1': {'name': '', 'include_entity': ['entity_5', 'entity_6', 'entity_7'], 'include_cluster': []},
#         'cluster_2': {'name': 'rg-aoai-westus', 'include_entity': ['entity_4', 'entity_5', 'entity_6', 'entity_7'], 'include_cluster': ['cluster_1']},
#         'cluster_3': {'name': 'West US', 'include_entity': ['entity_1', 'entity_4', 'entity_5', 'entity_6', 'entity_7'], 'include_cluster': ['cluster_1', 'cluster_2']},
#
#         'cluster_4': {'name': '', 'include_entity': ['entity_9', 'entity_10', 'entity_11'], 'include_cluster': []},
#         'cluster_5': {'name': 'rg-aoai-eastus', 'include_entity': ['entity_5', 'entity_9', 'entity_10', 'entity_11'], 'include_cluster': ['cluster_4']},
#         'cluster_6': {'name': 'East US', 'include_entity': ['entity_3', 'entity_5', 'entity_9', 'entity_10', 'entity_11'], 'include_cluster': ['cluster_4', 'cluster_5']},
#     },
#
#
#     'relation': [
#         {'source': 'entity_0', 'target': 'entity_2', 'name': '', 'direction': 'single'},
#         {'source': 'entity_0', 'target': 'entity_3', 'name': '', 'direction': 'single'},
#         {'source': 'entity_2', 'target': 'entity_4', 'name': '', 'direction': 'single'},
#         {'source': 'entity_3', 'target': 'entity_5', 'name': '', 'direction': 'single'},
#         {'source': 'entity_4', 'target': 'entity_6', 'name': '', 'direction': 'single'},
#         {'source': 'entity_5', 'target': 'entity_9', 'name': '', 'direction': 'single'},
#     ],
#
#     'difficulty': 'medium',
#     'diagram_type': 'architecture'
# }

# json_object28 = {
#     'entity': {
#         'entity_0': {'name': 'Client'},
#         'entity_1': {'name': 'Built-in API Management FQDN (uses performance based routing)'},
#         'entity_2': {'name': 'API Management (gateway and control plane)'},
#         'entity_3': {'name': 'API Management (eastus gateway only'},
#         'entity_4': {'name': 'Azure OpenAI Private Endpoint for West US'},
#         'entity_5': {'name': 'Azure OpenAI Private Endpoint for East US'},
#         'entity_6': {'name': 'gpt-4 (provisioned)'},
#         'entity_7': {'name': 'gpt-4 (standard)'},
#         'entity_8': {'name': 'Azure OpenAI (Active & Passive)'},
#         'entity_9': {'name': 'Azure RBAC for API access'},
#         'entity_10': {'name': 'gpt-4 (standard)'},
#         'entity_11': {'name': 'gpt-4 (provisioned)'},
#         'entity_12': {'name': 'Azure OpenAI (Active & Passive)'},
#         'entity_13': {'name': 'Azure RBAC for API access'},
#     },
#
#     'cluster': {
#         'cluster_0': {'name': 'rg-gateway-westus', 'include_entity': ['entity_2', 'entity_3'], 'include_cluster': ['']},
#         'cluster_1': {'name': '', 'include_entity': ['entity_6', 'entity_7', 'entity_8', 'entity_9'], 'include_cluster': []},
#         'cluster_2': {'name': 'rg-aoai-westus', 'include_entity': ['entity_4', 'entity_6', 'entity_7', 'entity_8', 'entity_9'], 'include_cluster': ['cluster_1']},
#         'cluster_3': {'name': 'West US', 'include_entity': ['entity_2', 'entity_4', 'entity_6', 'entity_7', 'entity_8', 'entity_9'], 'include_cluster': ['cluster_1', 'cluster_2']},
#         'cluster_4': {'name': '', 'include_entity': ['entity_10', 'entity_11', 'entity_12', 'entity_13'], 'include_cluster': []},
#         'cluster_5': {'name': 'rg-aoai-eastus', 'include_entity': ['entity_5', 'entity_10', 'entity_11', 'entity_12', 'entity_13'], 'include_cluster': ['cluster_4']},
#         'cluster_6': {'name': 'East US', 'include_entity': ['entity_2', 'entity_5', 'entity_10', 'entity_11', 'entity_12', 'entity_13'], 'include_cluster': ['cluster_4', 'cluster_5']},
#     },
#
#
#     'relation': [
#         {'source': 'entity_0', 'target': 'entity_2', 'name': '', 'direction': 'single'},
#         {'source': 'entity_0', 'target': 'entity_3', 'name': '', 'direction': 'single'},
#         {'source': 'entity_2', 'target': 'entity_4', 'name': '', 'direction': 'single'},
#         {'source': 'entity_2', 'target': 'entity_5', 'name': 'Failover for regional Azure OpenAI outage', 'direction': 'single'},
#         {'source': 'entity_3', 'target': 'entity_5', 'name': '', 'direction': 'single'},
#         {'source': 'entity_3', 'target': 'entity_4', 'name': 'Failover for regional Azure OpenAI outage', 'direction': 'single'},
#         {'source': 'entity_4', 'target': 'entity_6', 'name': '', 'direction': 'single'},
#         {'source': 'entity_4', 'target': 'entity_7', 'name': '', 'direction': 'single'},
#         {'source': 'entity_5', 'target': 'entity_10', 'name': '', 'direction': 'single'},
#         {'source': 'entity_5', 'target': 'entity_11', 'name': '', 'direction': 'single'},
#     ],
#
#     'difficulty': 'medium',
#     'diagram_type': 'architecture'
# }

# json_object29 = {
#     'entity': {
#         'entity_0': {'name': 'Client A'},
#         'entity_1': {'name': 'Client B'},
#         'entity_2': {'name': 'Gateway'},
#         'entity_3': {'name': 'Azure OpenAI Private Endpoint'},
#         'entity_4': {'name': 'gpt-4'},
#         'entity_5': {'name': 'gpt-35-turbo (60K TPM)'},
#         'entity_6': {'name': 'gpt-35-turbo (0613 | 30K TPM)'},
#         'entity_7': {'name': 'gpt-35-turbo (1106 | 30K TPM)'},
#         'entity_8': {'name': 'Azure OpenAI'},
#         'entity_9': {'name': 'Azure RBAC for API access'}
#     },
#
#     'cluster': {
#         'cluster_0': {'name': 'rg-gateway-eastus', 'include_entity': ['entity_2', 'entity_3'], 'include_cluster': []},
#         'cluster_1': {'name': '', 'include_entity': [ 'entity_4', 'entity_5', 'entity_6', 'entity_7', 'entity_8', 'entity_9'], 'include_cluster': []},
#         'cluster_2': {'name': 'rg-aoai-eastus', 'include_entity': ['entity_4', 'entity_5', 'entity_6', 'entity_7', 'entity_8', 'entity_9'], 'include_cluster': ['cluster_1']},
#     },
#
#
#     'relation': [
#         {'source': 'entity_0', 'target': 'entity_2', 'name': '', 'direction': 'single'},
#         {'source': 'entity_1', 'target': 'entity_2', 'name': '', 'direction': 'single'},
#         {'source': 'entity_2', 'target': 'entity_3', 'name': '', 'direction': 'single'},
#         {'source': 'entity_3', 'target': 'entity_4', 'name': '', 'direction': 'single'},
#         {'source': 'entity_3', 'target': 'entity_5', 'name': '', 'direction': 'single'},
#         {'source': 'entity_3', 'target': 'entity_6', 'name': '', 'direction': 'single'},
#         {'source': 'entity_3', 'target': 'entity_7', 'name': '', 'direction': 'single'},
#     ],
#
#     'difficulty': 'medium',
#     'diagram_type': 'architecture'
# }


# json_object30 = {
#     'entity': {
#         'entity_0': {'name': 'Client A'},
#         'entity_1': {'name': 'Client B'},
#         'entity_2': {'name': 'Gateway'},
#         'entity_3': {'name': 'Azure OpenAI Private Endpoint'},
#         'entity_4': {'name': 'Azure OpenAI Private Endpoint'},
#         'entity_5': {'name': 'Azure OpenAI Private Endpoint'},
#         'entity_6': {'name': 'gpt-4'},
#         'entity_7': {'name': 'Azure OpenAI | Client A (Provisioned primary)'},
#         'entity_8': {'name': 'Azure RBAC for API access'},
#         'entity_9': {'name': 'gpt-4'},
#         'entity_10': {'name': 'Azure OpenAI | Client A (Standard spillover)'},
#         'entity_11': {'name': 'Azure RBAC for API access'},
#         'entity_12': {'name': 'gpt-4'},
#         'entity_13': {'name': 'Azure OpenAI | Client A (Provisioned)'},
#         'entity_14': {'name': 'Azure RBAC for API access'},
#     },
#
#     'cluster': {
#         'cluster_0': {'name': 'rg-gateway-eastus', 'include_entity': ['entity_2', 'entity_3', 'entity_4', 'entity_5'], 'include_cluster': []},
#         'cluster_1': {'name': '', 'include_entity': ['entity_2', 'entity_3', 'entity_4'], 'include_cluster': []},
#         'cluster_2': {'name': '', 'include_entity': ['entity_5', 'entity_6', 'entity_7'], 'include_cluster': []},
#         'cluster_3': {'name': '', 'include_entity': ['entity_8', 'entity_9', 'entity_10'], 'include_cluster': []},
#         'cluster_4': {'name': 'rg-aoai-eastus', 'include_entity': ['entity_2', 'entity_3', 'entity_4', 'entity_5', 'entity_6', 'entity_7', 'entity_8', 'entity_9', 'entity_10'], 'include_cluster': ['cluster_1', 'cluster_2', 'cluster_3']},
#     },
#
#
#     'relation': [
#         {'source': 'entity_0', 'target': 'entity_2', 'name': '', 'direction': 'single'},
#         {'source': 'entity_1', 'target': 'entity_2', 'name': '', 'direction': 'single'},
#         {'source': 'entity_2', 'target': 'entity_3', 'name': '', 'direction': 'single'},
#         {'source': 'entity_2', 'target': 'entity_4', 'name': '', 'direction': 'single'},
#         {'source': 'entity_2', 'target': 'entity_5', 'name': '', 'direction': 'single'},
#         {'source': 'entity_3', 'target': 'entity_6', 'name': '', 'direction': 'single'},
#         {'source': 'entity_4', 'target': 'entity_9', 'name': '', 'direction': 'single'},
#         {'source': 'entity_5', 'target': 'entity_12', 'name': '', 'direction': 'single'},
#     ],
#
#     'difficulty': 'medium',
#     'diagram_type': 'architecture'
# }

# json_object31 = {
#     'entity': {
#         'entity_0': {'name': 'Azure Cosmos DB'},
#         'entity_1': {'name': 'Azure AI Foundry GPT-4o model'},
#         'entity_2': {'name': 'Knowledge sources and tools'},
#         'entity_3': {'name': 'Container Apps API agent orchestration'},
#         'entity_4': {'name': 'App Service website'},
#         'entity_5': {'name': 'Container Registry'},
#         'entity_6': {'name': 'Source repository'},
#         'entity_7': {'name': 'Docker'},
#         'entity_8': {'name': 'Web front end to request and manage automated solutions'},
#     },
#
#     'cluster': {
#         'cluster_0': {'name': '', 'include_entity': ['entity_0', 'entity_1', 'entity_3', 'entity_4', 'entity_5'], 'include_cluster': []},
#     },
#
#
#     'relation': [
#         {'source': 'entity_8', 'target': 'entity_4', 'name': '', 'direction': 'none'},
#         {'source': 'entity_4', 'target': 'entity_3', 'name': '', 'direction': 'single'},
#         {'source': 'entity_4', 'target': 'entity_5', 'name': '', 'direction': 'single'},
#         {'source': 'entity_3', 'target': 'entity_5', 'name': '', 'direction': 'single'},
#         {'source': 'entity_6', 'target': 'entity_7', 'name': '', 'direction': 'single'},
#         {'source': 'entity_7', 'target': 'entity_5', 'name': '', 'direction': 'single'},
#         {'source': 'entity_3', 'target': 'entity_2', 'name': '', 'direction': 'single'},
#         {'source': 'entity_3', 'target': 'entity_2', 'name': '', 'direction': 'single'},
#         {'source': 'entity_3', 'target': 'entity_1', 'name': '', 'direction': 'single'},
#         {'source': 'entity_3', 'target': 'entity_0', 'name': '', 'direction': 'single'},
#     ],
#
#     'difficulty': 'medium',
#     'diagram_type': 'architecture'
# }

# json_object32 = {
#     'entity': {
#         'entity_0': {'name': 'Azure Cosmos DB'},
#         'entity_1': {'name': 'Azure AI Foundry GPT-4o model'},
#         'entity_2': {'name': 'Knowledge sources and tools'},
#         'entity_3': {'name': 'Container Apps API agent orchestration'},
#         'entity_4': {'name': 'App Service website'},
#         'entity_5': {'name': 'Container Registry'},
#         'entity_6': {'name': 'Source repository'},
#         'entity_7': {'name': 'Docker'},
#         'entity_8': {'name': 'Web front end to request and manage automated solutions'},
#     },
#
#     'cluster': {
#         'cluster_0': {'name': '', 'include_entity': ['entity_0', 'entity_1', 'entity_3', 'entity_4', 'entity_5'], 'include_cluster': []},
#     },
#
#
#     'relation': [
#         {'source': 'entity_8', 'target': 'entity_4', 'name': '', 'direction': 'none'},
#         {'source': 'entity_4', 'target': 'entity_3', 'name': '', 'direction': 'single'},
#         {'source': 'entity_4', 'target': 'entity_5', 'name': '', 'direction': 'single'},
#         {'source': 'entity_3', 'target': 'entity_5', 'name': '', 'direction': 'single'},
#         {'source': 'entity_6', 'target': 'entity_7', 'name': '', 'direction': 'single'},
#         {'source': 'entity_7', 'target': 'entity_5', 'name': '', 'direction': 'single'},
#         {'source': 'entity_3', 'target': 'entity_2', 'name': '', 'direction': 'single'},
#         {'source': 'entity_3', 'target': 'entity_2', 'name': '', 'direction': 'single'},
#         {'source': 'entity_3', 'target': 'entity_1', 'name': '', 'direction': 'single'},
#         {'source': 'entity_3', 'target': 'entity_0', 'name': '', 'direction': 'single'},
#     ],
#
#     'difficulty': 'medium',
#     'diagram_type': 'architecture'
# }

# json_object32 = {
#     'entity': {
#         'entity_0': {'name': 'Client <Browser>'},
#         'entity_1': {'name': 'App Configuration'},
#         'entity_2': {'name': 'Container Registry'},
#         'entity_3': {'name': 'Content processor Container Apps'},
#         'entity_4': {'name': 'Content processor API Container Apps'},
#         'entity_5': {'name': 'Content processor monitor web Container Apps'},
#         'entity_6': {'name': 'Power BI'},
#         'entity_7': {'name': 'Queue Storage'},
#         'entity_8': {'name': 'Azure OpenAI in Foundry Models'},
#         'entity_9': {'name': 'Azure AI Content Understanding'},
#         'entity_10': {'name': 'Blob Storage'},
#         'entity_11': {'name': 'Azure Cosmos DB'},
#     },
#
#     'cluster': {
#         'cluster_0': {'name': '', 'include_entity': ['entity_3', 'entity_4', 'entity_5'], 'include_cluster': []},
#         'cluster_1': {'name': 'Azure AI Foundry', 'include_entity': ['entity_8', 'entity_9'], 'include_cluster': []},
#         'cluster_2': {'name': '', 'include_entity': ['entity_1', 'entity_2', 'entity_3', 'entity_4', 'entity_5', 'entity_6', 'entity_7', 'entity_8', 'entity_9', 'entity_10', 'entity_11'], 'include_cluster': ['cluster_0', 'cluster_1']},
#     },
#
#
#     'relation': [
#         {'source': 'entity_0', 'target': 'entity_4', 'name': 'Upload file', 'direction': 'single'},
#         {'source': 'entity_0', 'target': 'entity_6', 'name': 'Monitor or update process', 'direction': 'single'},
#         {'source': 'entity_4', 'target': 'entity_7', 'name': 'Enqueue', 'direction': 'single'},
#         {'source': 'entity_3', 'target': 'entity_8', 'name': 'Extract or map', 'direction': 'single'},
#         {'source': 'entity_3', 'target': 'entity_9', 'name': 'Extract', 'direction': 'single'},
#         {'source': 'entity_3', 'target': 'entity_10', 'name': 'Task result', 'direction': 'single'},
#         {'source': 'entity_3', 'target': 'entity_11', 'name': 'Task history or result', 'direction': 'single'},
#         {'source': 'entity_11', 'target': 'entity_6', 'name': '', 'direction': 'single'},
#     ],
#
#     'difficulty': 'medium',
#     'diagram_type': 'architecture'
# }

# json_object33 = {
#     'entity': {
#         'entity_0': {'name': 'Enterprise data'},
#         'entity_1': {'name': 'Third-party metadata'},
#         'entity_2': {'name': 'Azure Data Factory'},
#         'entity_3': {'name': 'Azure Stream Analytics'},
#         'entity_4': {'name': 'Azure Data Lake Storage'},
#         'entity_5': {'name': 'Azure Synapse Analytics'},
#         'entity_6': {'name': 'Azure SQL Database'},
#         'entity_7': {'name': 'Azure Machine Learning'},
#         'entity_8': {'name': 'Managed endpoint'},
#         'entity_9': {'name': 'Azure Data Lake Storage'},
#         'entity_10': {'name': 'Azure Synapse Analytics'},
#         'entity_11': {'name': 'Azure SQL Database'},
#         'entity_12': {'name': 'Power BI'},
#         'entity_13': {'name': 'Web application'},
#     },
#
#     'cluster': {
#         'cluster_0': {'name': 'Model data', 'include_entity': ['entity_0', 'entity_1'], 'include_cluster': []},
#         'cluster_1': {'name': 'Data workload', 'include_entity': ['entity_2', 'entity_3'], 'include_cluster': []},
#         'cluster_2': {'name': 'Staging area', 'include_entity': ['entity_4', 'entity_5', 'entity_6'], 'include_cluster': []},
#         'cluster_3': {'name': 'Training', 'include_entity': ['entity_7'], 'include_cluster': []},
#         'cluster_4': {'name': 'Inference', 'include_entity': ['entity_8'], 'include_cluster': []},
#         'cluster_5': {'name': 'Artificial intelligence', 'include_entity': ['entity_7', 'entity_8'], 'include_cluster': ['cluster_3', 'cluster_4']},
#         'cluster_6': {'name': 'Analytical workload', 'include_entity': ['entity_9', 'entity_10', 'entity_11'], 'include_cluster': []},
#         'cluster_7': {'name': 'Front end', 'include_entity': ['entity_12', 'entity_13'], 'include_cluster': []},
#     },
#
#
#     'relation': [
#         {'source': 'entity_0', 'target': 'cluster_0', 'name': '', 'direction': 'single'},
#         {'source': 'entity_1', 'target': 'cluster_0', 'name': '', 'direction': 'single'},
#         {'source': 'cluster_0', 'target': 'cluster_1', 'name': '', 'direction': 'single'},
#         {'source': 'cluster_1', 'target': 'cluster_2', 'name': '', 'direction': 'single'},
#         {'source': 'cluster_2', 'target': 'cluster_3', 'name': '', 'direction': 'single'},
#         {'source': 'cluster_4', 'target': 'cluster_6', 'name': '', 'direction': 'single'},
#         {'source': 'cluster_6', 'target': 'cluster_7', 'name': '', 'direction': 'single'},
#         {'source': 'entity_7', 'target': 'entity_8', 'name': 'Batch Create Azure Machine Learning pipelines for training and promotion.', 'direction': 'single'},
#         {'source': 'entity_7', 'target': 'entity_8', 'name': 'Deploy endpoint', 'direction': 'single'},
#         {'source': 'entity_7', 'target': 'entity_8', 'name': 'Near real-time', 'direction': 'single'},
#     ],
#
#     'difficulty': 'difficult',
#     'diagram_type': 'architecture'
# }


# json_object34 = {
#     'entity': {
#         'entity_0': {'name': 'Input'},
#         'entity_1': {'name': 'Model and general knowledge'},
#         'entity_2': {'name': 'Triage support agent'},
#         'entity_3': {'name': 'Result'},
#         'entity_4': {'name': 'Technical infrastructure agent'},
#         'entity_5': {'name': 'Result'},
#         'entity_6': {'name': 'Model, infrastructure knowledge, and tools'},
#         'entity_7': {'name': 'Financial resolution agent'},
#         'entity_8': {'name': 'Model, billing account knowledge, and billing API access'},
#         'entity_9': {'name': 'Result'},
#         'entity_10': {'name': 'Account access agent'},
#         'entity_11': {'name': 'Result'},
#         'entity_12': {'name': 'Model and customer knowledge'},
#         'entity_13': {'name': 'Customer support employee'},
#         'entity_14': {'name': 'Result'}
#     },
#
#     'cluster': {
#     },
#
#
#     'relation': [
#         {'source': 'entity_0', 'target': 'entity_2', 'name': '', 'direction': 'single'},
#         {'source': 'entity_1', 'target': 'entity_2', 'name': '', 'direction': 'none'},
#         {'source': 'entity_2', 'target': 'entity_3', 'name': '', 'direction': 'single'},
#         {'source': 'entity_2', 'target': 'entity_4', 'name': '', 'direction': 'single'},
#         {'source': 'entity_2', 'target': 'entity_7', 'name': '', 'direction': 'single'},
#         {'source': 'entity_2', 'target': 'entity_10', 'name': '', 'direction': 'single'},
#         {'source': 'entity_4', 'target': 'entity_5', 'name': '', 'direction': 'single'},
#         {'source': 'entity_4', 'target': 'entity_6', 'name': '', 'direction': 'none'},
#         {'source': 'entity_7', 'target': 'entity_8', 'name': '', 'direction': 'none'},
#         {'source': 'entity_7', 'target': 'entity_9', 'name': '', 'direction': 'single'},
#         {'source': 'entity_7', 'target': 'entity_10', 'name': '', 'direction': 'single'},
#         {'source': 'entity_7', 'target': 'entity_13', 'name': '', 'direction': 'single'},
#         {'source': 'entity_10', 'target': 'entity_11', 'name': '', 'direction': 'single'},
#         {'source': 'entity_10', 'target': 'entity_12', 'name': '', 'direction': 'none'},
#         {'source': 'entity_10', 'target': 'entity_13', 'name': '', 'direction': 'single'},
#         {'source': 'entity_13', 'target': 'entity_14', 'name': '', 'direction': 'single'},
#     ],
#
#     'difficulty': 'difficult',
#     'diagram_type': 'architecture'
# }


# json_object35 = {
#     'entity': {
#         'entity_0': {'name': 'Input'},
#         'entity_1': {'name': 'Model and general knowledge'},
#         'entity_2': {'name': 'Agent 1'},
#         'entity_3': {'name': 'Result'},
#         'entity_4': {'name': 'Agent 2'},
#         'entity_5': {'name': 'Result'},
#         'entity_6': {'name': 'Model and knowledge'},
#         'entity_7': {'name': 'Agent 3'},
#         'entity_8': {'name': 'Model, knowledge, and tools'},
#         'entity_9': {'name': 'Result'},
#         'entity_10': {'name': '...'},
#         'entity_11': {'name': 'Result'},
#         'entity_12': {'name': 'Agent n'},
#         'entity_13': {'name': 'Result'},
#         'entity_14': {'name': 'Model and knowledge'},
#         'entity_15': {'name': 'Customer support employee'},
#         'entity_16': {'name': 'Result'}
#     },
#
#     'cluster': {
#     },
#
#     'relation': [
#         {'source': 'entity_0', 'target': 'entity_2', 'name': '', 'direction': 'single'},
#         {'source': 'entity_1', 'target': 'entity_2', 'name': '', 'direction': 'none'},
#         {'source': 'entity_2', 'target': 'entity_3', 'name': '', 'direction': 'single'},
#         {'source': 'entity_2', 'target': 'entity_4', 'name': '', 'direction': 'single'},
#         {'source': 'entity_2', 'target': 'entity_7', 'name': '', 'direction': 'single'},
#         {'source': 'entity_2', 'target': 'entity_12', 'name': '', 'direction': 'single'},
#         {'source': 'entity_4', 'target': 'entity_5', 'name': '', 'direction': 'single'},
#         {'source': 'entity_4', 'target': 'entity_6', 'name': '', 'direction': 'none'},
#         {'source': 'entity_7', 'target': 'entity_8', 'name': '', 'direction': 'none'},
#         {'source': 'entity_7', 'target': 'entity_9', 'name': '', 'direction': 'single'},
#         {'source': 'entity_7', 'target': 'entity_10', 'name': '', 'direction': 'single'},
#         {'source': 'entity_7', 'target': 'entity_12', 'name': '', 'direction': 'single'},
#         {'source': 'entity_7', 'target': 'entity_15', 'name': '', 'direction': 'single'},
#         {'source': 'entity_10', 'target': 'entity_11', 'name': '', 'direction': 'single'},
#         {'source': 'entity_12', 'target': 'entity_14', 'name': '', 'direction': 'none'},
#         {'source': 'entity_12', 'target': 'entity_13', 'name': '', 'direction': 'single'},
#         {'source': 'entity_12', 'target': 'entity_15', 'name': '', 'direction': 'single'},
#         {'source': 'entity_15', 'target': 'entity_16', 'name': '', 'direction': 'single'},
#     ],
#
#     'difficulty': 'difficult',
#     'diagram_type': 'architecture'
# }

# json_object36 = {
#     'entity': {
#         'entity_0': {'name': 'Input'},
#         'entity_1': {'name': 'Model and general knowledge'},
#         'entity_2': {'name': 'Agent 1'},
#         'entity_3': {'name': 'Result'},
#         'entity_4': {'name': 'Agent 2'},
#         'entity_5': {'name': 'Result'},
#         'entity_6': {'name': 'Model and knowledge'},
#         'entity_7': {'name': 'Agent 3'},
#         'entity_8': {'name': 'Model, knowledge, and tools'},
#         'entity_9': {'name': 'Result'},
#         'entity_10': {'name': '...'},
#         'entity_11': {'name': 'Result'},
#         'entity_12': {'name': 'Agent n'},
#         'entity_13': {'name': 'Result'},
#         'entity_14': {'name': 'Model and knowledge'},
#         'entity_15': {'name': 'Customer support employee'},
#         'entity_16': {'name': 'Result'}
#     },
#
#     'cluster': {
#     },
#
#     'relation': [
#         {'source': 'entity_0', 'target': 'entity_2', 'name': '', 'direction': 'single'},
#         {'source': 'entity_1', 'target': 'entity_2', 'name': '', 'direction': 'none'},
#         {'source': 'entity_2', 'target': 'entity_3', 'name': '', 'direction': 'single'},
#         {'source': 'entity_2', 'target': 'entity_4', 'name': '', 'direction': 'single'},
#         {'source': 'entity_2', 'target': 'entity_7', 'name': '', 'direction': 'single'},
#         {'source': 'entity_2', 'target': 'entity_12', 'name': '', 'direction': 'single'},
#         {'source': 'entity_4', 'target': 'entity_5', 'name': '', 'direction': 'single'},
#         {'source': 'entity_4', 'target': 'entity_6', 'name': '', 'direction': 'none'},
#         {'source': 'entity_7', 'target': 'entity_8', 'name': '', 'direction': 'none'},
#         {'source': 'entity_7', 'target': 'entity_9', 'name': '', 'direction': 'single'},
#         {'source': 'entity_7', 'target': 'entity_10', 'name': '', 'direction': 'single'},
#         {'source': 'entity_7', 'target': 'entity_12', 'name': '', 'direction': 'single'},
#         {'source': 'entity_7', 'target': 'entity_15', 'name': '', 'direction': 'single'},
#         {'source': 'entity_10', 'target': 'entity_11', 'name': '', 'direction': 'single'},
#         {'source': 'entity_12', 'target': 'entity_14', 'name': '', 'direction': 'none'},
#         {'source': 'entity_12', 'target': 'entity_13', 'name': '', 'direction': 'single'},
#         {'source': 'entity_12', 'target': 'entity_15', 'name': '', 'direction': 'single'},
#         {'source': 'entity_15', 'target': 'entity_16', 'name': '', 'direction': 'single'},
#     ],
#
#     'difficulty': 'difficult',
#     'diagram_type': 'architecture'
# }

# json_object37 = {
#     'entity': {
#         'entity_0': {'name': 'Park development proposal'},
#         'entity_1': {'name': 'Model'},
#         'entity_2': {'name': 'Group chat manager'},
#         'entity_3': {'name': 'Community engagement agent'},
#         'entity_4': {'name': 'Environmental planning agent'},
#         'entity_5': {'name': 'Parks budget and operations agent'},
#         'entity_6': {'name': 'Model and civic knowledge'},
#         'entity_7': {'name': 'Model and local environmental knowledge'},
#         'entity_8': {'name': 'Model and city knowledge'},
#         'entity_9': {'name': 'Chat output from civic agents'},
#         'entity_10': {'name': 'Parks department employee'},
#         'entity_11': {'name': 'Accumulating conversation'},
#         'entity_12': {'name': 'Park proposal consensus'},
#         'entity_13': {'name': 'Instructions based on accumulated context and fresh insight'}
#     },
#
#     'cluster': {
#     },
#
#     'relation': [
#         {'source': 'entity_0', 'target': 'entity_2', 'name': '', 'direction': 'single'},
#         {'source': 'entity_1', 'target': 'entity_2', 'name': '', 'direction': 'none'},
#         {'source': 'entity_2', 'target': 'entity_3', 'name': '', 'direction': 'single'},
#         {'source': 'entity_2', 'target': 'entity_4', 'name': '', 'direction': 'single'},
#         {'source': 'entity_2', 'target': 'entity_5', 'name': '', 'direction': 'single'},
#         {'source': 'entity_2', 'target': 'entity_11', 'name': '', 'direction': 'single'},
#         {'source': 'entity_3', 'target': 'entity_6', 'name': '', 'direction': 'none'},
#         {'source': 'entity_4', 'target': 'entity_7', 'name': '', 'direction': 'none'},
#         {'source': 'entity_5', 'target': 'entity_8', 'name': '', 'direction': 'none'},
#         {'source': 'entity_3', 'target': 'entity_11', 'name': '', 'direction': 'single'},
#         {'source': 'entity_4', 'target': 'entity_11', 'name': '', 'direction': 'single'},
#         {'source': 'entity_5', 'target': 'entity_11', 'name': '', 'direction': 'single'},
#         {'source': 'entity_11', 'target': 'entity_12', 'name': '', 'direction': 'none'},
#     ],
#
#     'difficulty': 'difficult',
#     'diagram_type': 'architecture'
# }

# json_object38 = {
#     'entity': {
#         'entity_0': {'name': 'Input'},
#         'entity_1': {'name': 'Model'},
#         'entity_2': {'name': 'Group chat manager'},
#         'entity_3': {'name': 'Agent 1'},
#         'entity_4': {'name': 'Agent 2'},
#         'entity_5': {'name': '...'},
#         'entity_6': {'name': 'Agent n'},
#         'entity_7': {'name': 'Model and knowledge'},
#         'entity_8': {'name': 'Model and knowledge'},
#         'entity_9': {'name': 'Model and knowledge'},
#         'entity_10': {'name': 'Chat output from agents'},
#         'entity_11': {'name': 'Human chat participant or observer'},
#         'entity_12': {'name': 'Accumulating chat thread'},
#         'entity_13': {'name': 'Result'},
#         'entity_14': {'name': 'New group instructions based on accumulated context'},
#     },
#
#     'cluster': {
#     },
#
#     'relation': [
#         {'source': 'entity_0', 'target': 'entity_2', 'name': '', 'direction': 'single'},
#         {'source': 'entity_1', 'target': 'entity_2', 'name': '', 'direction': 'none'},
#         {'source': 'entity_2', 'target': 'entity_3', 'name': '', 'direction': 'single'},
#         {'source': 'entity_2', 'target': 'entity_4', 'name': '', 'direction': 'single'},
#         {'source': 'entity_2', 'target': 'entity_5', 'name': '', 'direction': 'single'},
#         {'source': 'entity_2', 'target': 'entity_6', 'name': '', 'direction': 'single'},
#         {'source': 'entity_2', 'target': 'entity_12', 'name': '', 'direction': 'single'},
#         {'source': 'entity_3', 'target': 'entity_7', 'name': '', 'direction': 'none'},
#         {'source': 'entity_4', 'target': 'entity_8', 'name': '', 'direction': 'none'},
#         {'source': 'entity_6', 'target': 'entity_9', 'name': '', 'direction': 'none'},
#         {'source': 'entity_3', 'target': 'entity_12', 'name': '', 'direction': 'single'},
#         {'source': 'entity_4', 'target': 'entity_12', 'name': '', 'direction': 'single'},
#         {'source': 'entity_5', 'target': 'entity_12', 'name': '', 'direction': 'single'},
#         {'source': 'entity_6', 'target': 'entity_12', 'name': '', 'direction': 'single'},
#         {'source': 'entity_11', 'target': 'entity_12', 'name': '', 'direction': 'single'},
#         {'source': 'entity_12', 'target': 'entity_13', 'name': '', 'direction': 'single'},
#     ],
#
#     'difficulty': 'difficult',
#     'diagram_type': 'architecture'
# }


# json_object39 = {
#     'entity': {
#         'entity_0': {'name': 'Enterprise data sync process'},
#         'entity_1': {'name': 'Enterprise data'},
#         'entity_2': {'name': 'Storage account'},
#         'entity_3': {'name': 'Azure AI Foundry'},
#         'entity_4': {'name': 'Azure Cosmos DB'},
#         'entity_5': {'name': 'App Service'},
#         'entity_6': {'name': 'Azure AI Document Intelligence'},
#         'entity_7': {'name': 'Web front end to chat with own data, generate document templates, and export document templates.'},
#     },
#
#     'cluster': {
#         'cluster_0': {'name': 'Model data', 'include_entity': ['entity_0', 'entity_1', 'entity_2', 'entity_3', 'entity_4', 'entity_5', 'entity_6'], 'include_cluster': []},
#     },
#
#     'relation': [
#         {'source': 'entity_0', 'target': 'entity_1', 'name': '', 'direction': 'none'},
#         {'source': 'entity_0', 'target': 'entity_2', 'name': '', 'direction': 'single'},
#         {'source': 'entity_2', 'target': 'entity_6', 'name': 'Load PDF files', 'direction': 'single'},
#         {'source': 'entity_5', 'target': 'entity_4', 'name': '', 'direction': 'single'},
#         {'source': 'entity_5', 'target': 'entity_3', 'name': '', 'direction': 'single'},
#         {'source': 'entity_5', 'target': 'entity_6', 'name': '', 'direction': 'single'},
#         {'source': 'entity_5', 'target': 'entity_2', 'name': '', 'direction': 'single'},
#         {'source': 'entity_5', 'target': 'entity_7', 'name': '', 'direction': 'none'},
#     ],
#
#     'difficulty': 'medium',
#     'diagram_type': 'architecture'
# }


# json_object40 = {
#     'entity': {
#         'entity_0': {'name': 'Enterprise data sync process'},
#         'entity_1': {'name': 'Enterprise data'},
#         'entity_2': {'name': 'Storage account'},
#         'entity_3': {'name': 'Azure AI Foundry'},
#         'entity_4': {'name': 'Azure Cosmos DB'},
#         'entity_5': {'name': 'App Service'},
#         'entity_6': {'name': 'Azure AI Document Intelligence'},
#         'entity_7': {'name': 'Web front end to chat with own data, generate document templates, and export document templates.'},
#     },
#
#     'cluster': {
#         'cluster_0': {'name': 'Model data', 'include_entity': ['entity_0', 'entity_1', 'entity_2', 'entity_3', 'entity_4', 'entity_5', 'entity_6'], 'include_cluster': []},
#     },
#
#     'relation': [
#         {'source': 'entity_0', 'target': 'entity_1', 'name': '', 'direction': 'none'},
#         {'source': 'entity_0', 'target': 'entity_2', 'name': '', 'direction': 'single'},
#         {'source': 'entity_2', 'target': 'entity_6', 'name': 'Load PDF files', 'direction': 'single'},
#         {'source': 'entity_5', 'target': 'entity_4', 'name': '', 'direction': 'single'},
#         {'source': 'entity_5', 'target': 'entity_3', 'name': '', 'direction': 'single'},
#         {'source': 'entity_5', 'target': 'entity_6', 'name': '', 'direction': 'single'},
#         {'source': 'entity_5', 'target': 'entity_2', 'name': '', 'direction': 'single'},
#         {'source': 'entity_5', 'target': 'entity_7', 'name': '', 'direction': 'none'},
#     ],
#
#     'difficulty': 'medium',
#     'diagram_type': 'architecture'
# }

# json_object41 = {
#     'entity': {
#         'entity_0': {'name': 'Client apps'},
#         'entity_1': {'name': 'Microsoft Entra ID'},
#         'entity_2': {'name': 'API Gateway'},
#         'entity_3': {'name': 'Logic app'},
#         'entity_4': {'name': 'Logic app'},
#         'entity_5': {'name': 'Logic app'},
#         'entity_6': {'name': 'Service Bus'},
#         'entity_7': {'name': 'Event Grid'},
#         'entity_8': {'name': 'SaaS service'},
#         'entity_9': {'name': 'Azure services'},
#         'entity_10': {'name': 'Message-based service'},
#         'entity_11': {'name': 'REST or SOAP web service'},
#     },
#
#     'cluster': {
#         'cluster_0': {'name': 'API Management', 'include_entity': ['entity_2'], 'include_cluster': []},
#         'cluster_1': {'name': 'Workflow and orchestration', 'include_entity': ['entity_3', 'entity_4', 'entity_5'], 'include_cluster': []},
#         'cluster_2': {'name': 'Queues, topics, subscriptions, and events', 'include_entity': ['entity_6', 'entity_7'], 'include_cluster': []},
#         'cluster_3': {'name': '', 'include_entity': ['entity_2', 'entity_3', 'entity_4', 'entity_5', 'entity_6', 'entity_7'], 'include_cluster': ['cluster_0', 'cluster_1', 'cluster_2']},
#     },
#
#     'relation': [
#         {'source': 'entity_0', 'target': 'entity_1', 'name': 'Authentication', 'direction': 'single'},
#         {'source': 'entity_0', 'target': 'entity_2', 'name': 'HTTPS', 'direction': 'single'},
#         {'source': 'entity_2', 'target': 'entity_11', 'name': 'HTTPS', 'direction': 'single'},
#         {'source': 'entity_3', 'target': 'entity_6', 'name': '', 'direction': 'single'},
#         {'source': 'entity_4', 'target': 'entity_8', 'name': 'HTTPS', 'direction': 'single'},
#         {'source': 'entity_4', 'target': 'entity_9', 'name': 'HTTPS', 'direction': 'single'},
#         {'source': 'entity_5', 'target': 'entity_8', 'name': 'HTTPS', 'direction': 'single'},
#         {'source': 'entity_5', 'target': 'entity_9', 'name': 'HTTPS', 'direction': 'single'},
#         {'source': 'entity_9', 'target': 'entity_7', 'name': 'Events', 'direction': 'single'},
#         {'source': 'entity_6', 'target': 'entity_4', 'name': '', 'direction': 'single'},
#         {'source': 'entity_7', 'target': 'entity_5', 'name': '', 'direction': 'single'},
#         {'source': 'entity_7', 'target': 'entity_10', 'name': '', 'direction': 'single'},
#         {'source': 'entity_10', 'target': 'entity_6', 'name': '', 'direction': 'single'},
#     ],
#
#     'difficulty': 'difficult',
#     'diagram_type': 'architecture'
# }


# json_object42 = {
#     'entity': {
#         'entity_0': {'name': 'Ticker symbol'},
#         'entity_1': {'name': 'Model, Exchange symbol mapping knowledge'},
#         'entity_2': {'name': 'Stock analysis agent'},
#         'entity_3': {'name': 'Decision with supporting evidence based on combined intermediate results'},
#         'entity_4': {'name': 'Model'},
#         'entity_5': {'name': 'Fundamental analysis agent'},
#         'entity_6': {'name': 'Intermediate result'},
#         'entity_7': {'name': 'Technical analysis agent'},
#         'entity_8': {'name': 'Intermediate result'},
#         'entity_9': {'name': 'Sentiment analysis agent'},
#         'entity_10': {'name': 'Intermediate result'},
#         'entity_11': {'name': 'ESG agent'},
#         'entity_12': {'name': 'Intermediate result'},
#         'entity_13': {'name': 'Financials and revenue analysis agent'},
#         'entity_14': {'name': 'Competitive analysis agent'},
#         'entity_15': {'name': 'Model, reported financials knowledge'},
#         'entity_16': {'name': 'Model, competitive knowledge'},
#         'entity_17': {'name': 'Fine-tuned model, market APIs'},
#         'entity_18': {'name': 'Model, social APIs, news APIs'},
#         'entity_19': {'name': 'Model, ESG knowledge'},
#     },
#
#     'cluster': {
#     },
#
#     'relation': [
#         {'source': 'entity_0', 'target': 'entity_2', 'name': '', 'direction': 'single'},
#         {'source': 'entity_1', 'target': 'entity_2', 'name': '', 'direction': 'none'},
#         {'source': 'entity_2', 'target': 'entity_3', 'name': '', 'direction': 'single'},
#         {'source': 'entity_2', 'target': 'entity_5', 'name': '', 'direction': 'single'},
#         {'source': 'entity_2', 'target': 'entity_7', 'name': '', 'direction': 'single'},
#         {'source': 'entity_2', 'target': 'entity_9', 'name': '', 'direction': 'single'},
#         {'source': 'entity_2', 'target': 'entity_11', 'name': '', 'direction': 'single'},
#         {'source': 'entity_5', 'target': 'entity_4', 'name': '', 'direction': 'none'},
#         {'source': 'entity_5', 'target': 'entity_6', 'name': '', 'direction': 'single'},
#         {'source': 'entity_5', 'target': 'entity_13', 'name': '', 'direction': 'single'},
#         {'source': 'entity_5', 'target': 'entity_14', 'name': '', 'direction': 'single'},
#         {'source': 'entity_7', 'target': 'entity_17', 'name': '', 'direction': 'none'},
#         {'source': 'entity_7', 'target': 'entity_8', 'name': '', 'direction': 'single'},
#         {'source': 'entity_9', 'target': 'entity_18', 'name': '', 'direction': 'none'},
#         {'source': 'entity_9', 'target': 'entity_10', 'name': '', 'direction': 'single'},
#         {'source': 'entity_11', 'target': 'entity_19', 'name': '', 'direction': 'none'},
#         {'source': 'entity_11', 'target': 'entity_12', 'name': '', 'direction': 'single'},
#         {'source': 'entity_13', 'target': 'entity_15', 'name': '', 'direction': 'none'},
#         {'source': 'entity_14', 'target': 'entity_16', 'name': '', 'direction': 'none'},
#     ],
#
#     'difficulty': 'difficult',
#     'diagram_type': 'architecture'
# }


# json_object43 = {
#     'entity': {
#         'entity_0': {'name': 'Input'},
#         'entity_1': {'name': 'Initiator and collector agent'},
#         'entity_2': {'name': 'Aggregated result based on combined, compared, and selected results'},
#         'entity_3': {'name': 'Agent 1'},
#         'entity_4': {'name': 'Intermediate result'},
#         'entity_5': {'name': 'Agent 2'},
#         'entity_6': {'name': 'Intermediate result'},
#         'entity_7': {'name': '...'},
#         'entity_8': {'name': 'Intermediate result(s)'},
#         'entity_9': {'name': 'Agent n'},
#         'entity_10': {'name': 'Intermediate result'},
#         'entity_11': {'name': 'Sub agent 1.1'},
#         'entity_12': {'name': 'Sub agent 1.2'},
#         'entity_13': {'name': 'Model, knowledge, and tools'},
#         'entity_14': {'name': 'Model, knowledge, and tools'},
#         'entity_15': {'name': 'Model, knowledge, and tools'},
#         'entity_16': {'name': 'Model, knowledge, and tools'},
#     },
#
#     'cluster': {
#     },
#
#     'relation': [
#         {'source': 'entity_0', 'target': 'entity_1', 'name': '', 'direction': 'single'},
#         {'source': 'entity_1', 'target': 'entity_2', 'name': '', 'direction': 'single'},
#         {'source': 'entity_1', 'target': 'entity_3', 'name': '', 'direction': 'single'},
#         {'source': 'entity_1', 'target': 'entity_5', 'name': '', 'direction': 'single'},
#         {'source': 'entity_1', 'target': 'entity_7', 'name': '', 'direction': 'single'},
#         {'source': 'entity_1', 'target': 'entity_9', 'name': '', 'direction': 'single'},
#         {'source': 'entity_3', 'target': 'entity_4', 'name': '', 'direction': 'single'},
#         {'source': 'entity_3', 'target': 'entity_11', 'name': '', 'direction': 'single'},
#         {'source': 'entity_3', 'target': 'entity_12', 'name': '', 'direction': 'single'},
#         {'source': 'entity_11', 'target': 'entity_13', 'name': '', 'direction': 'none'},
#         {'source': 'entity_12', 'target': 'entity_14', 'name': '', 'direction': 'none'},
#         {'source': 'entity_5', 'target': 'entity_6', 'name': '', 'direction': 'single'},
#         {'source': 'entity_5', 'target': 'entity_15', 'name': '', 'direction': 'none'},
#         {'source': 'entity_7', 'target': 'entity_8', 'name': '', 'direction': 'single'},
#         {'source': 'entity_9', 'target': 'entity_10', 'name': '', 'direction': 'single'},
#         {'source': 'entity_9', 'target': 'entity_16', 'name': '', 'direction': 'none'},
#     ],
#
#     'difficulty': 'difficult',
#     'diagram_type': 'architecture'
# }


# json_object44 = {
#     'entity': {
#         'entity_0': {'name': 'Email servers'},
#         'entity_1': {'name': 'FTP server'},
#         'entity_2': {'name': 'Web apps'},
#         'entity_3': {'name': 'Logic Apps'},
#         'entity_4': {'name': 'Azure Data Factory'},
#         'entity_5': {'name': 'Azure Functions'},
#         'entity_6': {'name': 'Blob Storage'},
#         'entity_7': {'name': 'Data Lake Storage'},
#         'entity_8': {'name': 'Document Intelligence Studio'},
#         'entity_9': {'name': 'Language Studio'},
#         'entity_10': {'name': 'Machine Learning studio'},
#         'entity_11': {'name': 'Document Intelligence (custom model parameters)'},
#         'entity_12': {'name': 'Azure AI Language (custom model parameters)'},
#         'entity_13': {'name': 'Azure Kubernetes Service'},
#         'entity_14': {'name': 'Batch and online managed endpoints'},
#     },
#
#     'cluster': {
#         'cluster_0': {'name': 'Source', 'include_entity': ['entity_0', 'entity_1', 'entity_2'], 'include_cluster': []},
#         'cluster_1': {'name': 'Data ingestion and orchestration', 'include_entity': ['entity_3', 'entity_4', 'entity_5'], 'include_cluster': []},
#         'cluster_2': {'name': 'Data store', 'include_entity': ['entity_6', 'entity_7'], 'include_cluster': []},
#         'cluster_3': {'name': 'Labeling, tagging, and training', 'include_entity': ['entity_8', 'entity_9', 'entity_10'], 'include_cluster': []},
#         'cluster_4': {'name': '', 'include_entity': ['entity_13', 'entity_14'], 'include_cluster': []},
#         'cluster_5': {'name': 'Deployment', 'include_entity': ['entity_11', 'entity_12', 'entity_13', 'entity_14'], 'include_cluster': ['cluster_4']},
#     },
#
#     'relation': [
#         {'source': 'cluster_0', 'target': 'cluster_1', 'name': '', 'direction': 'single'},
#         {'source': 'cluster_1', 'target': 'cluster_2', 'name': '', 'direction': 'single'},
#         {'source': 'cluster_3', 'target': 'cluster_4', 'name': '', 'direction': 'single'},
#         {'source': 'entity_8', 'target': 'entity_11', 'name': '', 'direction': 'single'},
#         {'source': 'entity_9', 'target': 'entity_12', 'name': '', 'direction': 'single'},
#         {'source': 'entity_10', 'target': 'cluster_4', 'name': '', 'direction': 'single'},
#     ],
#
#     'difficulty': 'medium',
#     'diagram_type': 'architecture'
# }


json_object44 = {
    'entity': {
        'entity_0': {'name': 'Email servers'},
        'entity_1': {'name': 'FTP server'},
        'entity_2': {'name': 'Web apps'},
        'entity_3': {'name': 'Logic Apps'},
        'entity_4': {'name': 'Azure Data Factory'},
        'entity_5': {'name': 'Azure Functions'},
        'entity_6': {'name': 'Blob Storage'},
        'entity_7': {'name': 'Data Lake Storage'},
        'entity_8': {'name': 'Document Intelligence Studio'},
        'entity_9': {'name': 'Language Studio'},
        'entity_10': {'name': 'Machine Learning studio'},
        'entity_11': {'name': 'Document Intelligence (custom model parameters)'},
        'entity_12': {'name': 'Azure AI Language (custom model parameters)'},
        'entity_13': {'name': 'Azure Kubernetes Service'},
        'entity_14': {'name': 'Batch and online managed endpoints'},
    },

    'cluster': {
        'cluster_0': {'name': 'Source', 'include_entity': ['entity_0', 'entity_1', 'entity_2'], 'include_cluster': []},
        'cluster_1': {'name': 'Data ingestion and orchestration', 'include_entity': ['entity_3', 'entity_4', 'entity_5'], 'include_cluster': []},
        'cluster_2': {'name': 'Data store', 'include_entity': ['entity_6', 'entity_7'], 'include_cluster': []},
        'cluster_3': {'name': 'Labeling, tagging, and training', 'include_entity': ['entity_8', 'entity_9', 'entity_10'], 'include_cluster': []},
        'cluster_4': {'name': '', 'include_entity': ['entity_13', 'entity_14'], 'include_cluster': []},
        'cluster_5': {'name': 'Deployment', 'include_entity': ['entity_11', 'entity_12', 'entity_13', 'entity_14'], 'include_cluster': ['cluster_4']},
    },

    'relation': [
        {'source': 'cluster_0', 'target': 'cluster_1', 'name': '', 'direction': 'single'},
        {'source': 'cluster_1', 'target': 'cluster_2', 'name': '', 'direction': 'single'},
        {'source': 'cluster_3', 'target': 'cluster_4', 'name': '', 'direction': 'single'},
        {'source': 'entity_8', 'target': 'entity_11', 'name': 'Built-in deployment', 'direction': 'single'},
        {'source': 'entity_9', 'target': 'entity_12', 'name': '', 'direction': 'single'},
        {'source': 'entity_10', 'target': 'cluster_4', 'name': '', 'direction': 'single'},
    ],

    'difficulty': 'medium',
    'diagram_type': 'architecture'
}


target_file = 'dataset/SAD/architecture/microsoft/build-deploy-custom-models.svg'

with open(target_file.replace('.svg', '.json'), 'w') as f:
    f.write(json.dumps(json_object44))