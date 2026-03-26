import json
from openai import OpenAI
from dotenv import load_dotenv
import os

from .tools import TOOLS
from .prompt import SYSTEM_PROMPT
from .tool_executor import execute_tool

def env_path(levels_up=3, filename=".env.docker.secret"):
    path = __file__
    for _ in range(levels_up):
        path = os.path.dirname(path)
    return os.path.join(path, filename)

load_dotenv(env_path())

def route_intent(user_message: str) -> str:
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_message},
    ]

    api_key = os.getenv("LLM_API_KEY")
    base_url = os.getenv("LLM_API_BASE_URL")
    model = os.getenv("LLM_API_MODEL")

    client = OpenAI(api_key=api_key, base_url=base_url)

    MAX_STEPS = 10

    for step in range(MAX_STEPS):
    
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            tools=TOOLS,
            temperature = 0,
        )


        msg = response.choices[0].message

        # ✅ CASE 1: LLM wants to call tools
        if msg.tool_calls:
            messages.append(msg)

            for tool_call in msg.tool_calls:
                tool_name = tool_call.function.name

                try:
                    args = json.loads(tool_call.function.arguments or "{}")
                except json.JSONDecodeError:
                    args = {}

                result = execute_tool(tool_name, args)

                messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": json.dumps(result),
                })

        # ✅ CASE 2: Final answer
        else:
            return msg.content.strip()