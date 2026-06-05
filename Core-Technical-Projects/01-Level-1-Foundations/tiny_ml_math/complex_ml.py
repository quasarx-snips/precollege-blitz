import math
from sigmoid_classifier import sigmoid
import random

def normalize(x):
    return max(0, min(x, 100)) / 100

def detect_anomaly(x, thresh):
    return (sigmoid(normalize(x)), sigmoid(normalize(x)) > thresh)

def run_experiment(split_fraction, secret_threshold=0.7):
    # Setup data
    data = []
    for i in range(1000):
        val = sigmoid(normalize(i / 10))
        truth = val > secret_threshold
        data.append((i / 10, truth))

    random.shuffle(data)
    split_idx = int(split_fraction * len(data))
    training_data, test_data = data[:split_idx], data[split_idx:]

    # Training
    threshold = 0.4
    base_inc = 0.01

    for i in range(100000):
        inc = base_inc * (1 - (i / 100000))
        for x, y in training_data:
            prediction = detect_anomaly(x, threshold)[1]
            if prediction != y:
                if y == True:
                    threshold -= inc
                else:
                    threshold += inc
        threshold = max(0, min(threshold, 1))

    return threshold, test_data