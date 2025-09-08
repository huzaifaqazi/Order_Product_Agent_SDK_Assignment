from agents import Agent
from configuration.config import model

# Handoff agent

human_agent = Agent(
    name="Human Agent",
    instructions="You are helpfull assistant that help user negative and complex query.",
    model=model,
    handoff_description="help user with their complex and negative query."
)