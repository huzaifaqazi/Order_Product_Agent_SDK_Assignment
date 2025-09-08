from agents import Agent, GuardrailFunctionOutput, RunContextWrapper, Runner, input_guardrail
from pydantic import BaseModel
from configuration.config import model

# Input Guardrails when triggered if user ask and say cancel of my any order.

class data_input_guardrail(BaseModel):
    user_ask_about_order_cancel:bool
    reasoning:str

guardrail_agent= Agent(
    name="Guardrail Agent",
    instructions="check if user say and ask about order cancellation.",
    model=model,
    output_type=data_input_guardrail
)

@input_guardrail
async def input_function(ctx:RunContextWrapper , agent:Agent , input:str) -> GuardrailFunctionOutput:
    ans = await Runner.run(guardrail_agent , input , context=ctx.context)
    return GuardrailFunctionOutput(
        output_info=ans.final_output,
        tripwire_triggered=ans.final_output.user_ask_about_order_cancel
    )