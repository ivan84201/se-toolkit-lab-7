from LMS_backend.commands import (
    get_items,
    get_pass_rates,
)
from LMS_backend.commands import (
    get_items,
    get_pass_rates,
    get_learners,
    get_scores,
    get_timeline,
    get_groups,
    get_top_learners,
    get_completion_rate,
    trigger_sync,
)

def execute_tool(name, args):
    try:
        if name == "get_items":
            return get_items()

        elif name == "get_pass_rates":
            return get_pass_rates(args["lab"])
        
        elif name == "get_learners":
            return get_learners()

        elif name == "get_scores":
            return get_scores(args["lab"])
        
        elif name == "get_timeline":
            return get_timeline(args["lab"])

        elif name == "get_groups":
            return get_groups(args["lab"])

        elif name == "get_top_learners":
            lab = args.get("lab")
            limit = args.get("limit", 5)
            return get_top_learners(lab, limit)

        elif name == "get_completion_rate":
            return get_completion_rate(args["lab"])

        elif name == "trigger_sync":
            return trigger_sync()

        return {"error": f"Unknown tool: {name}"}

    except Exception as e:
        return {"error": f"Execution error: {str(e)}"}
    