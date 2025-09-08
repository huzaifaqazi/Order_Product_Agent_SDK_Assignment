from agents import Agent , AsyncOpenAI , OpenAIResponsesModel , RunConfig , OpenAIChatCompletionsModel , set_tracing_export_api_key
from decouple import config


# gemini = config("gemini_api_key")
base_url = config("base_url")
# base_url = config("gemini_url")

model = config("openai_model")
open_api_key = config("openai")
client = AsyncOpenAI(
    base_url=base_url,
    api_key=open_api_key
)

model = OpenAIResponsesModel(
    openai_client=client,
    model=model
)
run_config = RunConfig(
    model=model,
    model_provider=client
)