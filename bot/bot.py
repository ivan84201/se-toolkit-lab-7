import argparse
from dotenv import load_dotenv
from handlers.test_handlers.test_handlers import handle_command

# Load environment variables
load_dotenv(".env.bot.secret")

# Example bot logic
def handle_command(command: str) -> str:
    try:
        if command == "/start":
            return "hi hi hi hi hi"
        elif command == "/help":
            return "Available commands: /start, /help, /health, /scores lab-##"
        elif command == "/health":
            return "Backend status: OK (trust me)"
        elif command.startswith("/scores"):
            return f"Scores for {command.split(' ', 1)[1]}" if ' ' in command else "No lab specified"
        elif "labs" in command.lower():
            return "Available labs: lab-01, lab-02, lab-03, lab-04"
        else:
            return "Unknown command."
    except Exception as e:
            # Safety net: never crash in test mode
            return f"Error handling command: {e}"

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--test", type=str, help="Test a bot command")
    args = parser.parse_args()

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