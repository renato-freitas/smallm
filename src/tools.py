import os
import csv, json
import pandas as pd
from crewai.tools import tool
from SPARQLWrapper import SPARQLWrapper, JSON

####################################################
##################  TEAM ##################
####################################################


@tool("SPARQL Executor")
def execute_sparql(endpoint_url: str, query: str) -> str:
	"""
	Executes a SPARQL query against an RDF endpoint and returns results.
	"""
	sparql = SPARQLWrapper(endpoint_url)
	sparql.setQuery(query)
	sparql.setReturnFormat(JSON)

	results = sparql.query().convert()
	bindings = results["results"]["bindings"]

	if not bindings:
		return "No results found."

	output = []
	for b in bindings:
		output.append({k: v["value"] for k, v in b.items()})

	return str(output)