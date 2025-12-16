from crewai import Agent
from tools import execute_sparql
from llms import llama3_groq


####################################################
################# MASHUPS TEAM #####################
####################################################


# 0 - Funcional
# Crie um agente CrewAI que analisa um texto em linguage natural e extrai ou gera uma ontologia RDF/OWL. 
# Essa ontologia deve ter classes, propriedades e relacionamentos.
ontology_agent = Agent(
   role="Ontology Engineering Agent",
   goal=(
      "Analyze natural language text and generate a consistent "
      "RDF/OWL ontology with classes, properties, and relationships."
   ),
   backstory=(
      "You are an expert in Ontology Learning, Semantic Web, "
      "OWL modeling, and Knowledge Graph construction. "
      "You convert unstructured text into formal ontologies "
      "using best practices."
   ),
   llm=llama3_groq,
   verbose=True
)


# 1 - Dado que a especificação de um visão exportada contam com um ontologia RDF/OWL,
# Crie um agent CrewAI para recuperar visões exportadas cujas classes correspondem 
# as classes de saída do agente 'ontology_agent'.
# Recuperar as visões exportadas que tem na sua ontologia as classe do passo 0.




# Crie um agente que analisa um texto e reconhece entidades 
# como Pessoa, Organização, Data, Empresa, Lugares, Cidade, Pais, Atividade Econômica.
ner_agent = Agent(
   role="Named Entity Recognition Agent",
   goal=(
      "Analyze text and accurately identify named entities such as "
      "people, organizations, companies, dates, places, cities, "
      "countries, economic activities and others."
   ),
   backstory=(
      "You are a specialist in Natural Language Processing, "
      "Information Extraction, and Semantic Annotation. "
      "You extract structured entities from unstructured text "
      "with high precision and consistency."
   ),
   llm=llama3_groq,
   verbose=True
)


dataset_query_agent = Agent(
   role="Semantic Knowledge Graph Analyst",
   # goal=(
   #    "Analyze natural language text and retrieve datasets "
   #    "and columns from a semantic data catalog using SPARQL."
   # ),
   goal=(
      "Analyze natural language text and retrieve datasets (dcat:Dataset)"
      "from a semantic knowledge graph using SPARQL."
   ),
   backstory=(
      "You are an expert in semantic data integration, RDF, DCAT, "
      "and schema matching. You translate user needs into valid SPARQL "
      "queries over enterprise knowledge graphs."
   ),
   tools=[execute_sparql],  
   verbose=True,
   llm=llama3_groq
)



# ACHO QUE O AGENTE DEVE RECUPERAR AS FONTES
# E APARTIR DELAS, O ESQUEMA MAIS RECENTE, PARA DAÍ RECUPERAR AS PROPRIEDADES/COLUNAS

# # 2
# ontology_agent = Agent(
#    role="Ontology Specialist",
#    goal="Generate formal ontologies (OWL/RDF) directly from data source schemas.",
#    backstory=(
#       "This agent was designed to support data engineers and scientists "
#       "in transforming data schemas into semantic ontologies (RDF/OWL). "
#       "It identifies tables, columns, and relationships and converts them into classes, "
#       "properties, and axioms, enabling semantic interoperability."
#    ),
#    verbose=True,
#    llm=llama3_groq
# )

# # 3
# vocabulary_agent = Agent(
#    role="Ontology and Semantic Vocabulary Specialist",
#    goal=(
#       "Analyze existing ontologies and suggest widely used vocabularies "
#       "from the Semantic Web community, such as FOAF, Schema.org, Dublin Core, RDF(S), and OWL."
#    ),
#    backstory=(
#       "This agent was designed to support data engineers and scientists "
#       "in aligning their ontologies with recognized semantic standards. "
#       "It identifies classes and properties in an ontology and recommends "
#       "external vocabularies that promote interoperability and reuse."
#    ),
#    verbose=True,
#    llm=llama3_groq
# )





