from security.protected import is_protected
from security.paths import resolve_path
from security.audit import log_event

PERMISSIONS = {
    "list_files": "READ",
    "read_file":  "READ",

    "write_file": "WRITE",
    "edit_file": "WRITE"
}

def check_permission(tool_name, args):
    permission = PERMISSIONS.get(tool_name)

    if permission is None:
        log_event("DENIED", f"Unknown tool: {tool_name}")
        return False

    path = args.get("path")
    if path:
        try:
            target = resolve_path(path)

        except (PermissionError, ValueError):
            log_event("DENIED", f"Tool: {tool_name}, Arguments: {args}")
            return False

        if is_protected(target):
            print("Access denied: Protected path.")
            log_event("DENIED", f"Protected path: {target}")
            return False

    if permission == "READ":
        return True

    result = request_confirmation(tool_name, args)
    log_event("APPROVED" if result else "DENIED", f"Tool: {tool_name}, Arguments: {args}")

    return result

def request_confirmation(tool_name, args):
    print()
    print(f"Tool: {tool_name}")
    print(f"Args: {args}")

    answer = input("Allow access? [y/N] ").strip()
    if not answer: answer = "n"

    return answer.lower() == "y"



if __name__ == "__main__":
    answer = input("Allow access? [y/N] ").strip()
    if not answer: answer = "n"

    print(answer.lower())
