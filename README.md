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
│       └── autograding.yml
├── Core-Technical-Projects/
│   ├── 01-Level-1-Foundations/
│   │   ├── tiny_ml_math/
│   │   │   ├── main.py
│   │   │   ├── complex_ml.py
│   │   │   └── sigmoid_classifier.py
│   │   └── aes_visualizer/
│   │       ├── main.py
│   │       └── block_cipher.py
│   ├── 02-Level-2-Simulations/
│   │   ├── cpu_emulator/
│   │   │   ├── main.py
│   │   │   ├── opcodes.py
│   │   │   └── test_programs.asm
│   │   └── side_channel_trojan/
│   │       ├── leak_simulator.py
│   │       └── trace_analyzer.py
│   └── 03-Level-3-Edge-AI/
│       └── network_anomaly_detector/
│           ├── packet_sniffer.py
│           ├── model_trainer.py
│           └── live_defense_sh.sh
├── Phase-1-Documentation/
│   ├── Master_Readme_Portfolio.md
│   ├── FirstNotebook.ipynb
│   ├── Silicon-Foundations.md
│   └── Cyber-Forensics-Theory.md
├── Phase-2-API-Parsing/
│   ├── vuln_feed_fetcher.py
│   ├── log_payload_parser.py
│   ├── Shodan-Threat-Ingestor.py
│   └── Silicon-Telemetry-Parser.py
├── Phase-3-Automation/
│   ├── cron_security_auditor.py
│   ├── incident_webhook_dispatcher.py
│   ├── Live-Blacklist-Sync.py
│   └── Automated-Report-Generator.py
├── brainstorming/
│   ├── Base-X_Two-Way_Conversion_Engine/
│   ├── login_page/
│   ├── hardware_trojan_blueprint.txt
│   ├── edge_ai_pipeline_sketch.md
│   ├── rru_lab_leverage_strategy.txt
│   └── custom_instruction_sets.json
└── README.md
