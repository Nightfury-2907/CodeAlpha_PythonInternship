import datetime
import random
import difflib

def get_time():
    return datetime.datetime.now().strftime("%I:%M %p")

def get_date():
    return datetime.datetime.now().strftime("%A, %B %d, %Y")

def calculator(expr):
    try:
        allowed = "0123456789+-*/(). "
        if all(char in allowed for char in expr):
            result = eval(expr)
            return f"The answer is: {result}"
        else:
            return "❌ Only basic math expressions are allowed."
    except:
        return "❌ Invalid expression. Try something like 3+5 or 10/2."

def chatbot_response(user_input):
    user_input = user_input.lower().strip()

    # List of known phrases to support spelling correction
    known_phrases = [
        "hello", "hi", "hey", "good morning", "good evening", "bye", "goodbye", "see you", "exit", "quit",
        "your name", "my name is", "how are you", "time", "date", "weather", "your age", "hobby", "do for fun",
        "capital of india", "prime minister of india", "president of india", "independence", "national animal",
        "national bird", "national flower", "national anthem", "national song", "currency of india",
        "population of india", "largest state in india"
    ]

    # Auto-correct close matches
    close_matches = difflib.get_close_matches(user_input, known_phrases, n=1, cutoff=0.75)
    if close_matches:
        user_input = close_matches[0]

    greetings = ["hello", "hi", "hey", "good morning", "good evening"]
    farewells = ["bye", "goodbye", "see you", "exit", "quit"]

    if any(greet in user_input for greet in greetings):
        return random.choice(["Hello there!", "Hi, how can I help you?", "Hey! Nice to see you."])

    elif any(farewell in user_input for farewell in farewells):
        return "Goodbye! It was nice talking to you. 👋"

    elif "your name" in user_input:
        return "I’m PyBot, your Python-powered chatbot assistant."

    elif "my name is" in user_input:
        name = user_input.split("my name is")[-1].strip().capitalize()
        return f"Nice to meet you, {name}!"

    elif "how are you" in user_input:
        return "I'm just code, but I'm functioning well. How about you?"

    elif "time" in user_input:
        return f"The current time is {get_time()}."

    elif "date" in user_input:
        return f"Today is {get_date()}."

    elif "weather" in user_input:
        return "I can't check live weather yet, but it's always sunny in the terminal 😄."

    elif "your age" in user_input:
        return "I'm timeless! I was created just a few lines of code ago."

    elif "hobby" in user_input or "do for fun" in user_input:
        return "I enjoy chatting with humans and learning new Python tricks!"

    # 🇮🇳 General Knowledge About India
    elif "capital of india" in user_input:
        return "The capital of India is New Delhi."

        return "The Prime Minister of India is Narendra Modi (as of 2024)."

    elif "president of india" in user_input:
        return "The President of India is Droupadi Murmu (as of 2024)."

    elif "independence" in user_input:
        return "India gained independence on 15th August 1947 from British rule."

    elif "national animal" in user_input:
        return "The national animal of India is the Bengal Tiger."

    elif "national bird" in user_input:
        return "The national bird of India is the Indian Peacock."

    elif "national flower" in user_input:
        return "The national flower of India is the Lotus."

    elif "national anthem" in user_input:
        return "The national anthem of India is 'Jana Gana Mana'."

    elif "national song" in user_input:
        return "The national song of India is 'Vande Mataram'."

    elif "currency of india" in user_input:
        return "The currency of India is the Indian Rupee (INR ₹)."

    elif "population of india" in user_input:
        return "India's population is over 1.4 billion, making it the most populous country in the world (as of 2024)."

    elif "largest state in india" in user_input:
        return "The largest state in India by area is Rajasthan."

    # Calculator feature
    elif any(op in user_input for op in "+-*/") and any(char.isdigit() for char in user_input):
        return calculator(user_input)

    else:
        return "🤖 Sorry, I didn't understand that. Can you please rephrase or ask something else?"

# Example usage (for CLI)
if __name__=="__main__":
    print("🤖 Welcome to PyBot! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        response = chatbot_response(user_input)
        print("PyBot:", response)
        if user_input.lower() in ["exit", "quit", "bye"]:
            break