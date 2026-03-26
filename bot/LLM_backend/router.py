from openai import OpenAI
from llm_tools import TOOLS
from tool_executor import execute_tool

client = OpenAI()

SYSTEM_PROMPT = """

"""

def route_intent(user_message: str):
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_message},
    ]

    while True:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=messages,
            tools=TOOLS,
        )

        msg = response.choices[0].message

        # If LLM wants to call a tool
        if msg.tool_calls:
            for tool_call in msg.tool_calls:
                name = tool_call.function.name
                args = eval(tool_call.function.arguments)

                result = execute_tool(name, args)

                messages.append(msg)
                messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": str(result),
                })

        else:
            return msg.content