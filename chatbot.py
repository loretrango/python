import random

# Define responses for the chatbot
responses = {
    "hello": ["Hi there!", "Hello!", "Hey!"],
    "how are you": ["I'm doing well, thank you!", "I'm great! How about you?", "All good!"],
    "what's your name": ["I am ChatBot.", "You can call me ChatBot.", "My name is ChatBot."],
    "bye": ["Goodbye!", "See you later!", "Bye! Have a great day!"],
    "default": ["I'm not sure how to respond to that.", "Can you please rephrase your question?", "I'm still learning!"],
}

def chatbot_response(user_input):
    """
    Function to generate a response for the chatbot.
    """
    user_input = user_input.lower()
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    return random.choice(responses["default"])

def main():
    print("ChatBot: Hi! I'm ChatBot. How can I assist you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("ChatBot:", chatbot_response(user_input))
            break
        print("ChatBot:", chatbot_response(user_input))

if __name__ == "__main__":
    main()
