from complex_ml import run_experiment, detect_anomaly
import random

def main():
    print("--- TinyML Foundation: Threshold Discovery ---")
    split = float(input("Enter split fraction (e.g., 0.8): "))
    SECRET_THRESHOLD = random.randint(1, 7)/10

    # Run the experiment
    learned_threshold, test_data = run_experiment(split, SECRET_THRESHOLD)

    # Test
    total_errors = 0
    for x, y in test_data:
        if detect_anomaly(x, learned_threshold)[1] != y:
            total_errors += 1

    print(f"\nExperiment Complete.")
    print(f"Test Data Size: {len(test_data)}")
    print(f"Split Fraction: {split:.2f}")
    print(f"Accuracy: {(1 - total_errors / len(test_data)) * 100:.2f}%")
    print(f"Secret Threshold: {SECRET_THRESHOLD:.4f}")
    print(f"Learned Threshold: {learned_threshold:.4f}")
    print(f"Total mistakes on test data: {total_errors}")

if __name__ == "__main__":
    main()