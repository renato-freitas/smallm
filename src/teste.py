from pprint import pprint
from workflows import mashup_team
# from tools import load_json_data
# from data import extracted_schema


# def run_agent(user_text, schema_uri, endpoint):
#    return mashup_team.kickoff(
#       inputs={
#          "user_text": user_text,
#          "schema_uri": schema_uri,
#          "endpoint": endpoint
#       }
#    )
def run_agent(user_text):
   return mashup_team.kickoff(
      inputs={
         "user_text": user_text,
      }
   )
user_in = ("Pretendo analisar dados sobre as organizações que possuem "
"estabelecimentos cuja atividade econômica é caracterizada como 'Venda de Eletros' (código CNAE 1112). "
"Esse estudo tem o objetivo de avaliar a distribuição geográfica desses estabelecimentos "
"dentro da cidade de Aracati (código IBGE 2111300)")

run_agent(
   user_text=user_in)
# Baseado no contexto da apliação, a LLM pode recuperar apenas as tabelas e propriedades adequadas.
# - Aqui o usuário explica o que quer no sistema. 
# - Ex: endereço da SEFAZ.
# - Entra do usuário deve ser suficiente. Agente deve retornar que não conseguiu encontrar nada.
# Tem que ficar evidente para o agente a entrada. Isso ajuda na escolha do vocabulário final.
# Focar em um sistema conversacional.
# Na qualidade passar um contexto da aplicação.

# ====

# Ganho no auxílio da construção do contexto de entrada.
# O LLM pode ProcessLookupError
# Preciso construir um mshup disso e disso (o llm auto completa) numa construção guiada 
# uso o conhecimento que tem o EKG