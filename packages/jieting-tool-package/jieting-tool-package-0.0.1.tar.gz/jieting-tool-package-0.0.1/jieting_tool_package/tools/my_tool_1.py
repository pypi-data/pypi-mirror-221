# from promptflow import tool
# from promptflow.connections import CustomConnection


# @tool
# def my_tool(connection: CustomConnection, input_text: str) -> str:
#     # Replace with your tool code.
#     # Usually connection contains configs to connect to an API.
#     # Use CustomConnection is a dict. You can use it like: connection.api_key, connection.api_base
#     # Not all tools need a connection. You can remove it if you don't need it.
#     connection.deployment_name, api_base, api_key
#     return "Hello " + input_text

from promptflow import tool
from promptflow.connections import CustomConnection
import os
import openai


@tool
def my_tool(connection: CustomConnection, input_text: str) -> str:
    # Replace with your tool code.
    # Usually connection contains configs to connect to an API.
    # Use CustomConnection is a dict. You can use it like: connection.api_key, connection.api_base
    # Not all tools need a connection. You can remove it if you don't need it.
    openai.api_type = "azure"
    openai.api_base = connection.api_base
    openai.api_version = "2022-12-01"
    openai.api_key = connection.api_key

    response = openai.Completion.create(
    engine=connection.deployment_name,
    prompt=input_text,
    temperature=1,
    max_tokens=100,
    top_p=0.5,
    frequency_penalty=0,
    presence_penalty=0,
    best_of=1,
    stop=None)

    return response