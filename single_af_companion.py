import subprocess

def run_ollama(prompt):
    """Run Ollama with the given prompt and return the output."""
    command = f'ollama run mistral "{prompt}"'
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout.strip()

def print_menu():
    """Print the menu options for the user."""
    print("\nWhat would you like to do?")
    print("1. Hear a joke")
    print("2. Get some advice")
    print("3. Celebrate singlehood")
    print("4. Exit")

def main():
    print("Welcome to your Virtual Companion! 🎉")
    name = input("What's your name? ")
    print(f"Hi {name}! I'm here to make your Valentine's Day awesome. Let's get started!")

    while True:
        print_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            prompt = "Tell me a funny joke about being single."
            response = run_ollama(prompt)
            print(f"\n🎭 Joke: {response}\n")

        elif choice == "2":
            prompt = "Give me some uplifting advice for someone who is single on Valentine's Day."
            response = run_ollama(prompt)
            print(f"\n💡 Advice: {response}\n")

        elif choice == "3":
            prompt = "Write a short celebration message for someone who is proudly single."
            response = run_ollama(prompt)
            print(f"\n🎉 Celebration: {response}\n")

        elif choice == "4":
            print(f"Goodbye, {name}! Remember, being single is awesome. 💪")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()