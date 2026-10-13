print("Welcome to your practice copilot!")

while True:
    question = input("You: ").strip()

    if question.lower() == "exit" or question.lower() == "quit":
        print("Goodbye!")
        break

    if question == "":
        print("Please enter a question.")
        continue

    if len(question) < 5:
        print("Please enter at least 5 characters.")
        continue

    print(f"You asked: {question}")

print("Session finished.")