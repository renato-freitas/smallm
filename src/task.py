from crewai import Task
from pydantic import BaseModel
from agents import ontology_agent, ner_agent, dataset_query_agent

OUTPUTS_FOLDER = "src/outputs"

####################################################
##################### MASHUP TEAM ##################
####################################################

# 0 - Funcional
ontology_task = Task(
   description="""
Analyze the text below and generate an RDF/OWL ontology.

Text:
\"\"\"
{user_text}
\"\"\"

Requirements:
1. Identify main concepts → owl:Class
2. Identify relationships between concepts → owl:ObjectProperty
3. Identify attributes → owl:DatatypeProperty
4. Define rdfs:domain and rdfs:range when possible
5. Use meaningful IRIs
6. Use owl:Class, owl:ObjectProperty, owl:DatatypeProperty
7. Return the ontology in Turtle (TTL) format
8. Do NOT add explanations — return ONLY the ontology

Namespaces to use:
@prefix ex: <http://example.org/ontology#>
@prefix owl: <http://www.w3.org/2002/07/owl#>
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>
@prefix xsd: <http://www.w3.org/2001/XMLSchema#>
""",
   expected_output="A valid RDF/OWL ontology in Turtle format.",
   agent=ontology_agent
)


ner_task = Task(
   description="""
Analyze the text below and extract named entities.

Text:
\"\"\"
{user_text}
\"\"\"

Identify and classify entities into the following types:
- Pessoa
- Organização
- Empresa
- Data
- Lugar
- Cidade
- País
- Atividade Econômica

Rules:
1. Return ONLY valid JSON.
2. Use arrays for each entity type.
3. If no entity is found for a type, return an empty array.
4. Do not infer entities that are not explicitly mentioned.
5. Normalize entity names (no duplicates).


""",
   expected_output="A JSON object containing extracted named entities.",
   agent=ner_agent
)
# JSON structure of output:
# {
#   "Pessoa": [],
#   "Organização": [],
#   "Empresa": [],
#   "Data": [],
#   "Lugar": [],
#   "Cidade": [],
#   "Pais": [],
#   "Atividade_Economica": []
# }



dataset_query_task = Task(
   description="""
Analyze the following text and generate a valid SPARQL query that:

1. Searches for dcat:Dataset
2. Matches by similarity using rdfs:label
3. Uses FILTER + CONTAINS for similarity
4. Returns dataset URI, dataset label

Text:
"{user_text}"

SPARQL endpoint:
{endpoint}
""",
   expected_output="A valid SPARQL query and execution results.",
   agent=dataset_query_agent
)
# dataset_query_task = Task(
#    description="""
# Analyze the following text and generate a valid SPARQL query that:

# 1. Searches for dcat:Dataset and vekg:Column
# 2. Matches by similarity using rdfs:label
# 3. Restricts results to the provided vekg:DataSchema version
# 4. Uses FILTER + CONTAINS for similarity
# 5. Returns dataset URI, dataset label, column URI, column label

# Text:
# "{user_text}"

# DataSchema URI:
# <{schema_uri}>

# SPARQL endpoint:
# {endpoint}
# """,
#    expected_output="A valid SPARQL query and execution results.",
#    agent=dataset_query_agent
# )
