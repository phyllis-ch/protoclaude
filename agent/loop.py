import json
import tools.registry as reg
from pathlib import Path
from datetime import datetime
from llm.client import LLM
from tools.definitions import tools
from security.permissions import check_permission
from security.audit import log_event

class Agent:
    def __init__(self):
        self.llm = LLM()
        self.messages = [{
            'role': 'system',
            'content': """
            You are Tom, a Coding Assistant.
            When you don't need to use a tool, respond normally.
            You can interact with the filesystem using tools.
            Never invent tool results.
            If a tool returns "Permission denied", stop the action and inform the user clearly.
            """
        }]

    def save_msg(self):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        path = Path("conversations") / f"conversation-{timestamp}.json"
        path.parent.mkdir(parents=True, exist_ok=True)

        with path.open("w") as f:
            json.dump(self.messages, f, indent=4, ensure_ascii=False)

        return path

    def run(self, user_input):
        self.messages.append({
            "role": "user",
            "content": user_input
        })

        while True:
            print("\nTom: ", end="", flush=True)

            content = ""
            tool_calls = []

            stream = self.llm.generate(
                self.messages,
                tools=tools
            )

            for chunk in stream:
                message = chunk.message

                if message.content:
                    print(message.content, end="", flush=True)
                    content += message.content

                if message.tool_calls:
                    tool_calls.extend(message.tool_calls)

            print()

            assistant_message = {
                "role": "assistant",
                "content": content
            }

            if tool_calls:
                assistant_message["tool_calls"] = [
                    call.model_dump(exclude_none=True) for call in tool_calls
                ]

            self.messages.append(assistant_message)

            if not tool_calls:
                break

            for call in tool_calls:
                name = call.function.name
                args = call.function.arguments

                print(f"\n[Executing: {name}]")
                if check_permission(name, args):
                    try:
                        result = reg.execute_tool(name, args)
                        log_event("SUCCESS", f"Tool: {name}")

                    except Exception as e:
                        result = f"Tool execution failed: {e}"
                        log_event("FAILED", f"Tool: {name}, Error: {e}")
                else:
                    result = "Permission denied"

                self.messages.append({
                    "role": "tool",
                    "tool_name": name,
                    "content": str(result)
                })
