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

## 🛠️ The Mindset & Stack
I don't believe in "black-box" libraries where you just import everything. I want to understand the **why** and **how** at the silicon/logic level.

* **Systems Focus:** Avionics (ARINC 429), VLSI logic, and Hardware Architecture.
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

### 3. Aerospace & Edge AI (The Specialization)
* **Avionics IDS:** My main focus—building a system to catch anomalies in ARINC 429 data buses. If you’re into aerospace security, this is where the action is.

### 4. Automation (The "Set-it-and-forget-it")
* **API Ingestion:** Fetching live vulnerability feeds and telemetry.
* **Security Auditor:** Automated scripts that ping me if my mock infrastructure has a "breach."

---

## 📂 Project Tree
```text
precollege-blitz/
├── .github/
│   └── workflows/
│       └── autograding.yml # (June 3)
├── Core-Technical-Projects/
│   ├── 01-Level-1-Foundations/
│   │   ├── tiny_ml_math/
│   │   │   ├── main.py # (June 4)
│   │   │   ├── complex_ml.py # (June 5)
│   │   │   └── sigmoid_classifier.py # (June 4)
│   │   └── aes_visualizer/
│   │       ├── main.py # (June 3)
│   │       └── block_cipher.py # (June 3) 
│   ├── 02-Level-2-Simulations/
│   │   ├── cpu_emulator/
│   │   │   ├── main.py # (June 12)
│   │   │   ├── opcodes.py # (June 11)
│   │   │   └── test_programs.asm # (June 13)
│   │   └── side_channel_trojan/
│   │       ├── leak_simulator.py # (June 16)
│   │       └── trace_analyzer.py # (June 17)
│   └── 03-Level-3-Edge-AI/
│       ├── network_anomaly_detector/
│       │   ├── packet_sniffer.py # (June 20)
│       │   ├── model_trainer.py # (June 21)
│       │   └── live_defense_sh.sh # (June 22)
│       └── crypto_anomaly_detector/
│           ├── stream_monitor.py # (June 23)
│           ├── model_trainer.py # (June 24)
│           └── defense_trigger.sh # (June 25)
├── Phase-1-Documentation/
│   ├── Master_Readme_Portfolio.md # (June 27)
│   ├── FirstNotebook.ipynb # (June 5)
│   ├── Silicon-Foundations.md # (June 14)
│   └── Cyber-Forensics-Theory.md # (June 18)
├── Phase-2-API-Parsing/
│   ├── vuln_feed_fetcher.py # (June 28)
│   ├── log_payload_parser.py # (June 28)
│   ├── Shodan-Threat-Ingestor.py # (June 29)
│   └── Silicon-Telemetry-Parser.py # (June 29)
├── Phase-3-Automation/
│   ├── cron_security_auditor.py # (June 26)
│   ├── incident_webhook_dispatcher.py # (June 26)
│   ├── Live-Blacklist-Sync.py # (June 27)
│   └── Automated-Report-Generator.py # (June 27)
├── brainstorming/
│   ├── Base-X_Two-Way_Conversion_Engine/ # (June 30)
│   ├── login_page/ # (June 30)
│   ├── hardware_trojan_blueprint.txt # (June 15)
│   ├── edge_ai_pipeline_sketch.md # (June 22)
│   ├── rru_lab_leverage_strategy.txt # (June 30)
│   └── custom_instruction_sets.json # (June 12)
└── README.md # (June 3)
