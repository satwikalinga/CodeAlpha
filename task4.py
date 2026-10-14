
def chatbot_response(message):
    message = message.lower().strip()

    if message in ["hello", "hi", "hey"]:
        return "Hi! How can I help you?"

    elif message == "how are you":
        return "I'm fine, thanks! How are you?"

    elif message in ["what is your name", "who are you"]:
        return "I am a simple Python chatbot."

    elif message == "help":
        return "You can greet me, ask how I am, or say bye."

    elif message in ["bye", "goodbye", "exit", "quit"]:
        return "Goodbye! Have a nice day!"

    else:
        return "Sorry, I don't understand that message."


print("Welcome to Python Chatbot!")
print("Type 'bye' to exit.")

while True:
    user_message = input("\nYou: ")
    response = chatbot_response(user_message)

    print("Bot:", response)

    if user_message.lower().strip() in [
        "bye", "goodbye", "exit", "quit"
    ]:
        break
