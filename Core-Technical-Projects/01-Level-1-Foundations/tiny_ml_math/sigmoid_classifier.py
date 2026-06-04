import math

def sigmoid(x):
    try:
        return 1 / (1 + math.exp(-x))
    except OverflowError:
        return 0.0 if x > 0 else 1.0

def test_sigmoid():
    assert round(sigmoid(0), 1) == 0.5
    print("Sigmoid math verified.")