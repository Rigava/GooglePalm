from langchain.llms import GooglePalm
from langchain.utilities import SQLDatabase
import sqlite3

# import os
# from dotenv import load_dotenv
# load_dotenv()

api_key = "AIzaSyAKEaaM7fWIErN3VbikjP_T5m0UfhBy5iE"
llm = GooglePalm(google_api_key=api_key,temperature=0.2)
# print(llm("what is the definition of emission intensity in Fuel EU regulation"))

db = SQLDatabase.from_uri("sqlite:///dummy.db")
# print(db.get_usable_table_names())
print(db.table_info)

from langchain.agents import create_sql_agent
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.agents.agent_types import AgentType
agent_executor = create_sql_agent (llm=llm,toolkit=SQLDatabaseToolkit(db=db,llm=llm),verbose=False,agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,)
print(agent_executor.run("How many vessel have draft more than 9 metres"))