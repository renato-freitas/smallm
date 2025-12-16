from crewai import Crew
from agents import ontology_agent, ner_agent, dataset_query_agent
from task import ontology_task, ner_task, dataset_query_task

####################################################
################## PUBLISING TEAM ##################
####################################################
mashup_team = Crew(
	agents=[
      ontology_agent
      # dataset_query_agent
   ],
   tasks=[
      ontology_task
   ],
   verbose=True,
	process='sequential'
)



