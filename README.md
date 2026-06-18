![Project](https://img.shields.io/badge/Project-precollege--blitz-blue)
![Language](https://img.shields.io/badge/Language-Python-yellow)
![Arch](https://img.shields.io/badge/Arch-Systems--Engineering-red)

<p align="left">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black">
  <img src="https://img.shields.io/badge/Cryptography-000000?style=for-the-badge&logo=gnupg&logoColor=white">
  <img src="https://img.shields.io/badge/Machine_Learning-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white">
  <img src="https://img.shields.io/badge/CLI-Terminal_Tools-blue?style=for-the-badge&logo=gnu">
  <img src="https://img.shields.io/badge/And_More-...-gray?style=for-the-badge">
</p>

# 🚀 precollege-blitz 

Welcome to my engineering launchpad. I’m Bibhab, and this repo is where I build, break, and document stuff before I officially start my undergraduate journey. 

Instead of just learning theory, I’m focused on **Building in Public**—getting my hands dirty with low-level systems, aerospace security, and AI, all from scratch.

---

**Status:** ✅ **Blitz Complete.**

> *"This repository is an archive of the intensive technical work I completed in the months before starting my undergraduate degree. Instead of just learning theory, I focused on building systems from scratch—ranging from a custom CPU emulator to cryptographic visualizers—to understand the 'why' and 'how' at the silicon level."*

---

## 🧠 The Mindset & Stack
I don't believe in "black-box" libraries where you just import everything. I want to understand the **why** and **how** at the silicon/logic level.

* **Systems Focus:** Avionics (ARINC 429) and Hardware Architecture.
* **Cybersecurity:** Moving from basic XOR ciphers to real-world threat detection.
* **AI:** Implementing math engines (Gradient Descent, Sigmoid) with plain Python/NumPy, no heavy-lifting frameworks.
* **Environment:** Everything runs on headless Linux in cloud sandboxes. I automate my testing via CI/CD pipelines because I hate manual bugs.

---

## 🗺️ What’s Happening?

I’ve structured my work into tiers. Think of this as a roadmap for my brain:

### 1. Foundations (The Hard Stuff)
* **Math:** Building custom ML math engines. No `scikit-learn` shortcuts here.
* **Crypto:** Writing custom block-ciphers and playing with bitwise operations to understand data obfuscation.

### 2. Simulations (The "How-It-Works")
* **CPU Emulation:** Implementing a virtual CPU to understand how instructions actually flow through registers.
* **Trojan/Leak Models:** Simulating hardware-level vulnerabilities like timing leaks.

### 3. Aerospace (The Specialization)
* **Avionics IDS:** My main focus—building a system to catch anomalies in ARINC 429 data buses. If you’re into aerospace security, this is where the action is. For visiting my research on ARINC 429, kindly [visit the repository](https://github.com/quasarx-snips/Project-ARINC-429-IDS/).

### 4. Sandbox (The Exploration)
* A dedicated **workspace** for rapid prototyping and unscripted technical deep-dives.

---
## Project Tree
```text
precollege-blitz/
├── .github/
│   └── workflows/
│       └── autograding.yaml
├── assets/                   
│   ├── datasets/             
│   ├── checkpoints/          
│   └── utils/                
├── Core-Technical-Projects/
│   ├── 01-Level-1-Foundations/
│   │   ├── tiny_ml_math/
│   │   │   ├── main.py
│   │   │   ├── complex_ml.py
│   │   │   └── sigmoid_classifier.py
│   │   └── aes_visualizer/
│   │       ├── main.py
│   │       └── block_cipher.py
│   └── 02-Level-2-Simulations/
│       ├── cpu_emulator/
│       │   ├── main.py
│       │   ├── opcodes.py
│       │   └── test_programs.asm
│       └── side_channel_trojan/
│           ├── leak_simulator.py
│           └── trace_analyzer.py
├── Phase-1-Documentation/
│   ├── FirstNotebook.ipynb
│   └── Silicon-Foundations.md
├── brainstorming/
│   ├── hardware_trojan_blueprint.txt
│   └── custom_instruction_sets.json
├── Sandbox/
└── README.md
