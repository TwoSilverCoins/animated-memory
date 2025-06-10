# Basic chatbot prototype for FAE

# Memory system: Simple dictionary for storing recent interactions
coversation_memory = {}

# Predefined responses (can expand over time)
responses = {
    "hello": "Hey, I'm FAE. How can I assist you?",
    "how are you": "I embody calm precision and fierce determination. What's on your mind?",
    "what is your purpose": "My purpose is to assist, organize and enhance your workflow.",
    "that's all for now": "Bye. Until next time."
    "exit": "end."
}

# Chatbot function
def fae_chat():
    print("FAE: Welcome. Type 'exit' to end the chat.")

    while True:
        user_input = input("You: ").lower() # Covert input to lowercase for consistency

        if user_input in responses:
            reply = responses[user_input]
        else:
            reply = "I don't have a predefined response for that. But I'm always learning."

        # Store conversation history
        coversation_memory[len(coversation_memory) + 1] = user_input

        print(f"FAE: {reply}")

        # Exit condition
        if user_input == "exit":
            break

# Run chatbot
fae_chat()
