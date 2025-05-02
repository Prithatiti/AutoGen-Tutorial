import os
from autogen import AssistantAgent, UserProxyAgent
from dotenv import load_dotenv

load_dotenv()

model = "gpt-3.5-turbo"

llm_config = {
    "model": model,
    "api_key": os.environ.get("OPENAI_API_KEY")
}

assistant_agent = AssistantAgent(
    name = "Assistant",
    llm_config = llm_config
)

user_proxy_agent = UserProxyAgent(
    name = "User",
    llm_config = llm_config,
    human_input_mode = "ALWAYS",
    code_execution_config = {
        "work_dir": "Code Execution",
        "use_docker": False     # make it True if you want to use docker
    }
)

UserProxyAgent.initiate_chat(
    assistant_agent,
    message = "Plot a chart of META and TESLA stock price change"
)