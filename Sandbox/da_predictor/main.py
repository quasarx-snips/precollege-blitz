import random

def generate_airport_data(n=100):
    combined_data = []

    for _ in range(n):
        weight = round(random.uniform(0.5, 20.0), 2)
        metal = round(random.uniform(0.0, 1.0), 2)
        organic = random.choice([0, 1])
        threat = 1 if (metal > 0.6 and organic == 0) else 0
        combined_data.append(([weight, metal, organic], threat))

    return combined_data

def normalise(x):
    return min(20,max(0,x))/20
step = 0.0001
epoch = 10000
weights = [random.uniform(0.01, 0.1) for _ in range(4)]
threshold = 0.6
data = generate_airport_data(100)
print(data)
random.shuffle(data)
training_set = data[:80]
test_set = data[80:]
for i in range(epoch):
    current_step = step*(1-i/epoch)
    for x,y in training_set:
        norm_x = [
            normalise(x[0]), 
            x[1], 
            x[2], 
            (1 if x[1] > 0.6 and x[2] == 0 else 0)
        ]
        prediction = 1 if sum(norm_x[n]*weights[n] for n in range(4)) > threshold else 0
        error = y - prediction
        for n in range(len(weights)):
            weights[n] += error*norm_x[n]*current_step

# Assuming you have already run the training loop and 'weights' are final
correct_predictions = 0

print(f"{'Input Features':<30} | {'Actual':<7} | {'Predicted'}")
print("-" * 60)

for x, y in test_set:
    # 1. Normalize the test features (must use same logic as training)
    norm_x = [
        normalise(x[0]), 
        x[1], 
        x[2], 
        (1 if x[1] > 0.6 and x[2] == 0 else 0)
    ]

    # 2. Calculate raw score
    z = sum(norm_x[n] * weights[n] for n in range(4))

    # 3. Predict (using same threshold as training)
    prediction = 1 if z > threshold else 0

    # 4. Compare
    if prediction == y:
        correct_predictions += 1

    print(f"{str(x):<30} | {y:<7} | {prediction}")

# Final Accuracy score
accuracy = (correct_predictions / len(test_set)) * 100
print("-" * 60)
print(f"Final Model Accuracy: {accuracy}%")
    

            
    
