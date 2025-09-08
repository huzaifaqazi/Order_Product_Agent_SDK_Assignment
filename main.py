from agents import Agent, ModelSettings, RunContextWrapper, Runner, function_tool ,enable_verbose_stdout_logging , set_tracing_disabled  , InputGuardrailTripwireTriggered
from configuration.config import model
from data_schema.order import enable_data , orders_db
from guardrail.input import input_function
from handoff.human import human_agent
enable_verbose_stdout_logging()


# Enable functionality for function tool
def is_enable_function(ctx:RunContextWrapper[enable_data] , agent:Agent):
    if ctx.context.query_about_order:
        return True
    else:
        return False
    


# Function for error_handling 
def custome_handling_error(ctx:RunContextWrapper , error:Exception):
    """A custom function to provide a user-friendly error message."""
    print(f"This product is not available {error}.")    


# FUNCTION TOOL 
@function_tool(failure_error_function=custome_handling_error , is_enabled=is_enable_function)
def get_details_of_product(ctx:RunContextWrapper , order_id:str)->str :
    if order_id in orders_db:
        details = orders_db[order_id]
        return f"The Order {details["status"]} and the order will arrive in {details["delivery_date"]} "
    else:  
        raise ValueError(f"This {order_id} is not found.Please first order. ")

# Triage Agent 
bot_agent = Agent(
    name="Bot Agent",
    instructions="You are helpful bot assistant that help user common query about products. if user ask negative question that delegate task to another agent.",
    model=model,
    tools=[get_details_of_product],
    input_guardrails=[input_function],
    handoffs=[human_agent],
    model_settings=ModelSettings(tool_choice="auto")
)
# Runner
try:
    enable_obj = enable_data(query_about_order=True)
    res = Runner.run_sync(
    bot_agent,
    input="can i cancel order will arrive the id id_123",
    context=enable_obj
    )
    print(res.final_output)
    print(res.last_agent.name)
except InputGuardrailTripwireTriggered as e:
    print(e)