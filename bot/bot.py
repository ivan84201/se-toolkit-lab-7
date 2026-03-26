import argparse
from handlers.test_handlers.test_handlers import handle_command

#remove later
from LLM_backend.tool_executor import *



def main():
    print("\n--- trigger_sync ---")
    print(execute_tool("trigger_sync", {}))

    print("\n--- get_items ---")
    print(execute_tool("get_items", {}))

    print("\n--- get_learners ---")
    print(execute_tool("get_learners", {}))

    print("\n--- get_scores ---")
    print(execute_tool("get_scores", {"lab": "lab-01"}))

    print("\n--- get_pass_rates ---")
    print(execute_tool("get_pass_rates", {"lab": "lab-01"}))

    print("\n--- get_timeline ---")
    print(execute_tool("get_timeline", {"lab": "lab-01"}))

    print("\n--- get_groups ---")
    print(execute_tool("get_groups", {"lab": "lab-01"}))

    print("\n--- get_top_learners (default limit) ---")
    print(execute_tool("get_top_learners", {}))

    print("\n--- get_top_learners (limit=3) ---")
    print(execute_tool("get_top_learners", {"limit": 3}))

    print("\n--- get_top_learners (lab specific) ---")
    print(execute_tool("get_top_learners", {"lab": "lab-01", "limit": 5}))

    print("\n--- get_completion_rate ---")
    print(execute_tool("get_completion_rate", {"lab": "lab-01"}))

    print("\n--- unknown tool ---")
    print(execute_tool("fake_tool", {}))
    parser.add_argument("--test", type=str, help="Test a bot command")

    if args.test:
        # Test mode: process the command and exit
        response = handle_command(args.test)
        print(response)
        exit(0)

    # Normal bot startup here (Telegram connection)
    print("Starting bot normally... (Telegram connection)")
    # bot.run() or whatever your Telegram startup is

if __name__ == "__main__":
    main()