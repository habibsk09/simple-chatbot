import random
import nltk
from nltk.chat.util import Chat, reflections

# Download the necessary NLTK resources
nltk.download('punkt')

# Define pairs of patterns and responses
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I help you today?",]
    ],
    [
        r"hi|hello|hey",
        ["Hello!", "Hi there!", "Hey! How can I assist you?"]
    ],
    [
        r"what is your name?",
        ["I am a chatbot created to assist you!",]
    ],
    [
        r"how are you?",
        ["I'm just a bunch of code, but thanks for asking!", "Doing well, how about you?"]
    ],
    [
        r"quit",
        ["Bye! Take care.", "See you later!"]
    ],
    [
        r"(.*)",
        ["I'm sorry, I don't understand that.", "Can you please rephrase?"]
    ]
]

# Create the chatbot
chatbot = Chat(pairs, reflections)

def chat():
    print("Hi! I'm a chatbot. Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("Chatbot: Bye! Take care.")
            break
        response = chatbot.respond(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    chat()