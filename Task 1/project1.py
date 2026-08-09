# Project 1 : AI Chatbot

responses = {
    "hello": "Hi there! How can I help you today?",
    "hi": "Hello! Welcome to DecodeLabs.",
    "how are you": "I'm just a program, but I'm running perfectly!",
    "what is your name": "I am Project 1, your Rule-Based Assistant.",
    "help": "Sure! You can ask me about my name, or just say 'hello'.",
    "bye": "Goodbye! Shutting down the logic engine."
}

print("Bot: Hello! I am your Rule-Based Assistant. Type 'exit' to stop.")

while True:
    user_input = input("You: ")
    
    if user_input.lower() == "exit":
        print("Bot: Shutting down. Goodbye!")
        break
    
    clean_input = user_input.lower().strip()
    
    # Uses .get() to avoid the unstable IF-ELIF ladder 
    response = responses.get(clean_input, "I do not understand that command. Please say 'hello' or 'help'.")
    
    print(f"Bot: {response}")