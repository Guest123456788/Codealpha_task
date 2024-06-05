import nltk
from nltk.chat.util import Chat, reflections

#Define some patterns and responses
patterns = [
    (r'Hi|Hello|Hey', ['Hello', 'Hey there', 'Hi!']),
    (r'How are you?', ["I'm doing well, Thank you!", "I'm good , thanks for asking."]),
    (r'What is your name?', ["you can call me chatbot.", "I'm just a humble chatbot."]),
    (r'quit', ["Bye! Take care.", "Goodbye, have a great day!"]),
]

#create a chatbot object
chatbot = Chat(patterns, reflections)

#start conversation
print("Welcome to the chatbot. Type 'quit' to end the conversation.")
while True:
    user_input = input("you: ")
    response = chatbot.respond(user_input)
    print("chatbot:", response)
    if user_input.lower() == 'quit':
        break