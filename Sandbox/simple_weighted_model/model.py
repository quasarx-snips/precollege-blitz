import random
import matplotlib.pyplot as plt

# Data Generation
raw_data = []
for _ in range(1000):
    features = [random.randint(-100, 500) for _ in range(5)]
    label = 1 if sum(features) >= 500 else 0
    raw_data.append((features, label))

training_data = raw_data[:800]
testing_data = raw_data[800:]

#Parameters
weights = [0.5 for _ in range(5)]
step = 0.0000001
epochs = 900
threshold = 500 
error_list = []
weight_history = []

#Training Loop
for i in range(epochs):
    total_error = 0
    current_step = step * (1 - i / epochs)

    for x, y in training_data: 
        prediction = 1 if sum(weights[j] * x[j] for j in range(5)) > threshold else 0
        error = y - prediction
        total_error += abs(error)
        for j in range(5):
            weights[j] += error * x[j] * current_step

    error_list.append(total_error)
    weight_history.append(list(weights))

#Evaluation
TP, FP, TN, FN = 0, 0, 0, 0
for x, y in testing_data:
    prediction = 1 if sum(weights[j] * x[j] for j in range(5)) > threshold else 0
    if y == 1 and prediction == 1: TP += 1
    elif y == 0 and prediction == 1: FP += 1
    elif y == 0 and prediction == 0: TN += 1
    elif y == 1 and prediction == 0: FN += 1
#Plotting and Saving
formatted_weights = ", ".join([str(round(w, 2)) for w in weights])
stats_text = (f"TP: {TP} | FP: {FP} | TN: {TN} | FN: {FN}\n"
              f"Accuracy: {((TP+TN)/(TP+TN+FP+FN))*100:.1f}%\n"
              f"Precision: {(TP/(TP+FP))*100:.1f}%\n\nWeights: {formatted_weights}")

plt.figure(figsize=(10, 6))
plt.plot(error_list)
plt.title("Training Loss Curve")
plt.xlabel("Epochs")
plt.ylabel("Total Error")

plt.text(0.5, 0.5, stats_text, transform=plt.gca().transAxes, 
         bbox=dict(facecolor='white', alpha=0.8))

plt.savefig("loss_curve_neural_model.png")
print("Loss curve saved as 'loss_curve_neural_model.png'. Weights converged to:", formatted_weights)
plt.figure(figsize=(10, 6))
# Transpose weight_history to get a list of values per weight over time
for j in range(5):
    plt.plot([w[j] for w in weight_history], label=f'Weight {j+1}')

plt.title("Weight Adjustment Over Time")
plt.xlabel("Epochs")
plt.ylabel("Weight Value")
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig("weight_convergence.png")
print("Weight convergence plot saved as 'weight_convergence.png'.")
