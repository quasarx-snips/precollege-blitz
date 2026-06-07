import numpy as np
import os
from tokenizer import Tokenizer

# 1. Configuration
block_size = 5
learning_rate = 0.1 # Increased learning rate for batch training
weights_file = "my_weights.npy"

# Load Data
with open("../../assets/datasets/raw_text.txt", "r") as f:
    raw_text = f.read()

tokenizer = Tokenizer()
tokenizer.fit(raw_text)
inputs_list, targets_list = tokenizer.get_training_pairs(raw_text, block_size)
vocab_size = len(tokenizer.stoi)

# Convert to Matrix Format (The secret to speed)
X = np.array(inputs_list) / vocab_size 
Y = np.zeros((len(targets_list), vocab_size))
for i, target in enumerate(targets_list):
    Y[i, target - 1] = 1 # 1-based indexing adjustment

# 2. Load or Initialize
if os.path.exists(weights_file):
    print("Loading existing brain...")
    weights = np.load(weights_file)
else:
    print("No memory found. Starting new brain...")
    weights = np.random.randn(block_size, vocab_size) * 0.01

# 3. Training Loop (Vectorized)
print("Training started...")
for epoch in range(1000):
    # Forward Pass: Entire dataset at once
    logits = np.dot(X, weights)

    # Stable Softmax
    shifted_logits = logits - np.max(logits, axis=1, keepdims=True)
    probs = np.exp(shifted_logits) / np.sum(np.exp(shifted_logits), axis=1, keepdims=True)

    # Gradient: Calculate how all weights should change across the whole dataset
    error = probs - Y
    gradient = np.dot(X.T, error) / len(targets_list)

    # Update
    weights -= learning_rate * gradient

    if (epoch + 1) % 100 == 0:
        print(f"Epoch {epoch + 1} completed.")

# 4. Save
np.save(weights_file, weights)
print("Training saved!")