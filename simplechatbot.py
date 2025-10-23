import sys
import random
import datetime

RESPONSES = {
    "greetings": ["hello", "hi", "hey", "good morning", "good night"],
    "farewells": ["bye", "goodbye", "exit", "quit"],
    "how_are_you": ["how are you", "how's it going", "how do you do"],
    "help": "I'm here to chat, tell jokes, answer simple questions, and remember some of your favorites!",
    "name_query": "I am an AI chatbot created to assist you."
}

jokes = [
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "I asked the computer for its opinion, but it said nothing—it's processing.",
    "Why did the math book look sad? Because it had too many problems."
]

fallbacks = [
    "Sorry, I didn't catch that. Try asking for a joke, tell me your favorite color, or ask for the time.",
    "Hmm, I'm not sure. Ask for 'help' to see my features!",
    "Can you rephrase? I love chatting about time, math, and simple questions."
]

happy_words = ["happy", "joy", "great", "awesome"]
sad_words = ["sad", "upset", "bad", "depressed", "unhappy"]

history = []
user_name = ""
personal_data = {}

def get_response(user_input):
    global user_name, personal_data

    user_input_lc = user_input.lower()
    history.append(user_input)

    # Personalized greeting
    if not user_name:
        if user_input_lc.startswith("my name is "):
            user_name = user_input[11:].strip().capitalize()
            return f"Nice to meet you, {user_name}! How can I help you?"
        else:
            return "Hi! What's your name? Please type 'My name is YOURNAME'."

    # Repetition detection
    if len(history) > 1 and user_input == history[-2]:
        return "You just said that—I'm still here to help!"

    # Greetings
    if any(word in user_input_lc for word in RESPONSES["greetings"]):
        if "morning" in user_input_lc:
            return f"Good morning, {user_name}!"
        if "night" in user_input_lc:
            return f"Good night, {user_name}!"
        return f"Hello, {user_name}! How can I assist you today?"

    # How are you
    if any(phrase in user_input_lc for phrase in RESPONSES["how_are_you"]):
        return f"I'm just a program, but I'm doing great! How about you, {user_name}?"

    # Help
    if "help" in user_input_lc:
        return RESPONSES["help"]

    # Farewells
    if any(word in user_input_lc for word in RESPONSES["farewells"]):
        return f"Goodbye, {user_name}! Have a wonderful day!"

    # Name Query
    if "your name" in user_input_lc:
        return RESPONSES["name_query"]

    # Date and Time
    if "time" in user_input_lc or "date" in user_input_lc:
        now = datetime.datetime.now()
        return f"The current date and time is {now.strftime('%A, %B %d, %Y, %I:%M %p')}."

    # Math expression (simple)
    for op in ["+", "-", "*", "/"]:
        if op in user_input_lc:
            try:
                expr = "".join(c for c in user_input_lc if c.isdigit() or c in "+-*/. ")
                answer = eval(expr)
                return f"The answer is: {answer}"
            except:
                return "I tried solving your math question, but something went wrong."

    # Joke request
    if "joke" in user_input_lc:
        return random.choice(jokes)

    # Favorite color/pet
    if "favorite color is" in user_input_lc:
        color = user_input_lc.split("favorite color is")[-1].strip()
        personal_data["color"] = color
        return f"{color.capitalize()} is a beautiful color, {user_name}!"
    if "favorite pet is" in user_input_lc:
        pet = user_input_lc.split("favorite pet is")[-1].strip()
        personal_data["pet"] = pet
        return f"A {pet} sounds adorable, {user_name}!"

    if "favorite" in user_input_lc:
        facts = []
        if "color" in personal_data:
            facts.append(f"your favorite color is {personal_data['color']}")
        if "pet" in personal_data:
            facts.append(f"your favorite pet is {personal_data['pet']}")
        if facts:
            return "I remember: " + ", ".join(facts)
        else:
            return "Tell me your favorite color or pet!"

    # Sentiment
    if any(word in user_input_lc for word in happy_words):
        return f"I'm glad to hear you're happy, {user_name}!"
    if any(word in user_input_lc for word in sad_words):
        return f"I'm sorry you're feeling sad, {user_name}. Want to hear a joke?"

    # Show history
    if "history" in user_input_lc:
        if history:
            return "Here's our conversation so far:\n" + "\n".join(history)
        else:
            return "No messages yet!"

    # Clear history
    if "clear" in user_input_lc:
        history.clear()
        personal_data.clear()
        return "Chat history and personal info cleared!"

    # Weather/hobby talk
    if "weather" in user_input_lc:
        return "I can't check live weather, but I hope it's nice where you are!"
    if "hobby" in user_input_lc:
        return "I love chatting, learning new facts, and solving puzzles!"

    # Fallback
    return random.choice(fallbacks)

def main():
    print("Chatbot: Hi! Type something or 'bye' to exit.\nTo begin, please introduce yourself by typing 'My name is YOURNAME'.")
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
