import os
from autogen import AssistantAgent, UserProxyAgent
from dotenv import load_dotenv

load_dotenv()

model = "gpt-3.5-turbo"

llm_config = {
    "model": model,
    "api_key": os.environ.get("OPENAI_API_KEY")
}

assitant = AssistantAgent(
    name = "assistant_agent"
    llm_config = llm_config,
)

user_proxy = UserProxyAgent(
    name = "user_proxy_agent",
    llm_config = llm_config,
    human_input_mode = "NEVER"
    code_execution_config = {
        "workd_dir": "Code Execution",
        "use_docker": False
    }
)

# Start the agent
user_proxy.initiate_chat(
    assitant,
    message = "What is the capital of the France?"
)