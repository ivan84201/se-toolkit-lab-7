TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "get_items",
            "description": "List all labs and tasks",
            "parameters": {"type": "object", "properties": {}},
        },
    },
    {
        "type": "function",
        "function": {
            "name": "get_pass_rates",
            "description": "Get per-task average scores and attempts for a lab",
            "parameters": {
                "type": "object",
                "properties": {
                    "lab": {"type": "string"},
                },
                "required": ["lab"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "get_top_learners",
            "description": "Get top learners by score",
            "parameters": {
                "type": "object",
                "properties": {
                    "lab": {"type": "string"},
                    "limit": {"type": "integer"},
                },
            },
        },
    },
    # TODO: add remaining endpoints the same way
]