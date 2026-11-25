from tools.filesystem import (
        list_files,
        read_file,
        write_file
)

registry = {
    "list_files": list_files,
    "read_file": read_file,
    "write_file": write_file
}

def execute_tool(name, args):
    if name not in registry:
        return f"Error: Unknown tool {name}"

    try:
        return registry[name](**args)

    except Exception as e:
        return f"Error executing tool: {e}"
