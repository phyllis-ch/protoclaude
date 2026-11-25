from llm.client import LLM
from tools.definitions import tools
from security.permissions import check_permission
import tools.registry as reg

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
                    result = reg.execute_tool(name, args)
                else:
                    result = "Permission denied"

                self.messages.append({
                    "role": "tool",
                    "tool_name": name,
                    "content": str(result)
                })
