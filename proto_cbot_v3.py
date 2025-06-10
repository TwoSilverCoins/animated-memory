import spacy

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
