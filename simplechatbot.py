import sys

RESPONSES = {
    "greetings": ["hello", "hi", "hey"],
    "farewells": ["bye", "goodbye", "exit", "quit"],
    "how_are_you": ["how are you", "how's it going", "how do you do"],
    "help": "I'm here to chat with you or answer simple questions!",
    "name_query": "I am an AI chatbot created to assist you."
}

def get_response(user_input):
    user_input = user_input.lower()

    if any(word in user_input for word in RESPONSES["greetings"]):
        return "Hello! How can I assist you today?"
    if any(phrase in user_input for phrase in RESPONSES["how_are_you"]):
        return "I'm just a program, but I'm doing great! How about you?"
    if "help" in user_input:
        return RESPONSES["help"]
    if any(word in user_input for word in RESPONSES["farewells"]):
        return "Goodbye! Have a wonderful day!"
    if "your name" in user_input:
        return RESPONSES["name_query"]
    return "Sorry, I don't understand that. Could you rephrase?"

def main():
    print("Chatbot: Hi! Type something or 'bye' to exit.")
    try:
        while True:
            user_input = input("You: ").strip()
            if not user_input:
                print("Chatbot: Please say something.")
                continue
            if user_input.lower() in RESPONSES["farewells"]:
                print("Chatbot: Goodbye!")
                break
            response = get_response(user_input)
            print("Chatbot:", response)
    except KeyboardInterrupt:
        print("\nChatbot: Goodbye! (Interrupted)")
        sys.exit(0)

if __name__ == "__main__":
    main()
