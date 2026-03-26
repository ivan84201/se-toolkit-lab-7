from LMS_backend.commands import check_health, get_items, get_pass_rates
from LLM_backend.router import route_intent
#from LLM_backend.router import route_intent

def handle_command(command: str) -> str:
    try:
        if command.startswith("/"):
            if command == "/start":
                return "welcome"
            
            elif command == "/help":
                return "Available commands:\n/start\n/help\n/health\n/scores lab-##"

            elif command == "/health":
                return check_health()

            elif "labs" in command.lower():
                items = get_items()
                if isinstance(items, str):
                    return items  # error message
                labs = [item for item in items if item.get("type") == "lab"]
                if not labs:
                    return "No labs available."
                out = "Available labs:\n"
                for lab in labs:
                    out += f"- {lab.get('title')} — {lab.get('description','')}\n"
                return out.strip()

            elif command.startswith("/scores"):
                parts = command.split(maxsplit=1)
                if len(parts) < 2:
                    return "Usage: /scores <lab-id>"
                lab_id = parts[1]
                scores = get_pass_rates(lab_id)

                if isinstance(scores, str):
                    return scores  # backend error
        
                if not scores:
                    return f"No scores available for {lab_id}"

                lines = [f"Pass rates for {lab_id}:"]
                for task in scores:
                    name = task.get("task", "Unknown task")
                    attempts = task.get("attempts", 0)
                    avg_score = task.get("avg_score", 0)
                    lines.append(f"- {name}: {avg_score:.1f}% ({attempts} attempts)")

                return "\n".join(lines)
        
            else:
                return "Unknown command."
        else:
            return route_intent(command);
    except Exception as e:
            # Safety net: never crash in test mode
            return f"Error handling command: {e}"