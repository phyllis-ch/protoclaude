from agent.loop import Agent

def main():
    agent = Agent()
    print("Tom is here. Enter \"?\" for help.")

    while True:
        try:
            user_input = input("\nUser: ").strip()

            if not user_input:
                continue

            if user_input.lower() in ("?", "?help"):
                print("""
                    Commands: [prefix][command] e.g. ?help
                    help: Displays this help message
                    exit: Exit the program
                """)
                continue

            if user_input.lower() in ("?exit"):
                print("Fuck off nigga")
                break

            agent.run(user_input)

        except KeyboardInterrupt:
            print("Fuck off nigga")
            break

if __name__ == "__main__":
    main()
