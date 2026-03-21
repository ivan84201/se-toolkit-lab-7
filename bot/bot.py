import argparse
from handlers.test_handlers.test_handlers import handle_command


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