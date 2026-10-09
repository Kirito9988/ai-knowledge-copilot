from ai_knowledge_copilot.llm import LLMService


def main() -> None:
    print("=" * 60)
    print("AI KNOWLEDGE COPILOT")
    print("=" * 60)
    print("Ask me something.")
    print("Type 'exit' or 'quit' to close the application.\n")

    llm = LLMService()

    while True:
        user_message = input("You: ").strip()

        if user_message.lower() in {"exit", "quit"}:
            print("\nAI Copilot: Goodbye!")
            break

        if not user_message:
            print("AI Copilot: Please enter a question.\n")
            continue

        try:
            answer = llm.generate(user_message)

            print("\nAI Copilot:")
            print(answer)
            print()

        except Exception as error:
            print(f"\nSomething went wrong: {error}\n")


if __name__ == "__main__":
    main()