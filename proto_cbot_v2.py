# FAE chatbot with Basic Memory Retention

import json

# File to store memory
MEMORY_FILE = "fae_memory.json"

# Fucntion to load memory from file
def load_memory():
    try:
        with open(MEMORY_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
    
# Function to save memory to file
def save_memory(conversation_memory):
    with open(MEMORY_FILE, "w") as file:
        json.dump(conversation_memory, file, indent=4)

# Initialize memory
conversation_memory = load_memory()

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
        user_input = input("You").lower()

        if user_input.startswith("my name is"):
            user_name = user_input.split("my name is")[-1].strip()
            conversation_memory["user_name"] = user_name
            reply = f"I'll remember that. Hello, {user_name}!"

        elif user_input == "what is my name":
            reply = f"Your name is {conversation_memory.get('user_name', 'not stored yet')}, based on our last chat."

        else:
            reply = responses.get(user_input, "I don't have a predefined response for that. But I'm always learning.")

        conversation_memory[len(conversation_memory) + 1] = user_input
        save_memory(conversation_memory) # Save memory after each interaction

        print(f"FAE: {reply}")

        if user_input == "exit":
            break
# Run chatbot
fae_chat()
