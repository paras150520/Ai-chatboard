import nltk
import random
import string
import warnings
from nltk.chat.util import Chat, reflections

warnings.filterwarnings("ignore")

# Sample chatbot responses (modify as needed)
pairs = [
    ["hello|hi|hey", ["Hello! How can I help you?", "Hey there!", "Hi, what can I do for you?"]],
    ["how are you", ["I'm just a bot, but I'm doing fine!", "I'm great! How about you?"]],
    ["what is your name", ["I'm a chatbot created by Paras!", "You can call me ChatBot."]],
    ["bye|goodbye", ["Goodbye! Have a great day!", "See you later!", "Bye! Take care."]],
    ["(.*) your name", ["I am a simple chatbot!", "My name is AI ChatBot."]],
    ["(.*) help (.*)", ["I'm here to assist you!", "Sure, what do you need help with?"]],
    ["(.*)", ["I'm not sure I understand. Can you rephrase that?", "Can you clarify?", "I'm learning! Try asking something else."]]
]

# Create chatbot
chatbot = Chat(pairs, reflections)

# Run chatbot
def start_chat():
    print("🤖 AI ChatBot: Hello! Type 'bye' to exit.")
    while True:
        user_input = input("You: ").lower()
        if user_input == "bye":
            print("🤖 AI ChatBot: Goodbye! 👋")
            break
        response = chatbot.respond(user_input)
        print(f"🤖 AI ChatBot: {response}")

# Start chatting
if __name__ == "__main__":
    start_chat()
