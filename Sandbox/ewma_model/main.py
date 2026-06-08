import matplotlib.pyplot as plt
import random

# Randomize 15 data points
data = [random.randint(90, 150) for _ in range(15)]
#simple moving average
def sma(data, window):
    sma = []
    for i in range(len(data)):
        end_index = min(i + window, len(data))
        sma.append(round(sum(data[i : end_index]) / len(data[i : end_index]), 2))
    return sma
#exp weighted moving average
def ewma(data, beta):
    ewma = [data[0]]
    for i in range(1, len(data)):
        ewma.append(beta*data[i] + (1-beta)*ewma[-1])
    return ewma

#Plotting
plt.figure(figsize=(15, 10))
plt.subplots_adjust(top=0.9, right=0.85) 

plt.plot(data, label="Raw Data", marker='o', color='black', alpha=0.3, linewidth=3)
plt.plot(sma(data, 3), label="SMA (window=3)", linestyle='--', linewidth=2)

for i in range(1, 10, 3):
    beta_val = i / 10
    plt.plot(ewma(data, beta_val), label=f"EWMA (beta={beta_val})", linewidth=1.5)

plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.title("Comparison: SMA vs EWMA", fontsize=16)

plt.savefig("sma_vs_ewma.png", bbox_inches='tight')
