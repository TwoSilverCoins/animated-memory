import spacy
import os
import subprocess

# Function to execute system commands
def execute_command(command):
    try:
        if command == "open notepad":
            subprocess.run(["notepad.exe"])
        elif command == "open calculator":
            subprocess.run(["calc.exe"])
        elif command.startswith("create file"):
            filename = command.split("create file")[-1].strip()
            with open(filename, "w") as file:
                file.write("This is a new file created by FAE.")
            return f"File '{filename}' created successfully."
        else:
            return "Command not recognized."
    except Exception as e:
            return f"Error executing command: {str(e)}"

# Example Usage
user_command = "open notepad"
response = execute_command(user_command)
print("FAE", response)

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Function to preprocess user input
def preprocess_text(text):
    doc = nlp(text.lower()) # Convert text to lowercase and process with spaCy
    tokens = [token.text for token in doc if not token.is_stop] # Remove stopwords
    return " ".join(tokens) # Return cleaned text

# Example Usage
user_input = "Hello, my name is Carlos. Can you help me with AI?"
processed_input = preprocess_text(user_input)
print("Processed Text:", processed_input)

# Intent Classification system
intent_patterns = {
    "greeting": ["hello", "hi", "hey"],
    "ai_help": ["help with ai", "learn ai", "machine learning"],
    "exit": ["bye", "exit"]
}

# Function to classify text
def classify_intent(text):
    for intent, keywords in intent_patterns.items():
        for keyword in keywords:
            if keyword in text:
                return intent
    return "unknown"

# Example Usage
intent = classify_intent(processed_input)
print("Detected Intent:", intent)
