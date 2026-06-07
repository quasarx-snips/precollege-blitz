import numpy as np
from tokenizer import Tokenizer

# Load the brain you just trained
weights = np.load("my_weights.npy")
tokenizer = Tokenizer()
# Ensure you reload your vocabulary here
tokenizer.load_vocab("../../assets/datasets/vocabulary.json")

def predict(seed_text):
    # Encode input, scale it, and predict
    x = np.array(tokenizer.encode(seed_text)) / len(tokenizer.stoi)
    logits = np.dot(x, weights)
    probs = np.exp(logits - np.max(logits)) / np.sum(np.exp(logits - np.max(logits)))

    # Pick the character with the highest probability
    best_char_idx = np.argmax(probs) + 1
    return tokenizer.decode([best_char_idx])

# Test it!
print(f"Prediction: {predict('Bibha')}")