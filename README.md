# 🚀 precollege-blitz (May - August 2026)

Welcome to my pre-college launchpad repository. This space serves as a central hub for my technical explorations, cloud automation pipelines, and foundational hardware-software systems engineered before my undergraduate classes commence.

The primary objective of this sprint is to establish a **high-leverage technical baseline** at the intersection of **VLSI Silicon Architecture, Cybersecurity, and Applied Machine Learning**, eliminating academic friction and providing a strong portfolio for advanced research lab access from Day 1.

---

## 🛠️ The Power-User Stack & Environment

Optimized for high performance using cloud-native compute environments, avoiding local system overhead while maximizing execution scale:

* **Primary IDE:** [Replit](https://replit.com/) (For persistent multi-file system emulations) & [Google Colab](https://colab.research.google.com/) (For sandboxing and data-heavy tracks).
* **Documentation Format:** Academic/Industry standard Markdown (`.md`) & $\LaTeX$ for mathematical modeling and architecture logs.
* **Version Control:** Git via terminal interfaces for repository management.

---

## 🗺️ Roadmap & Milestones

### 📍 Phase 1: Documentation & Core Theories (In Progress)
* **Objective:** Master markdown formatting and academic $\LaTeX$ typesetting to log low-level computing mechanics, register states, and cryptographic foundations.
* **Core Projects & Deliverables:**
    * `Master_Readme_Portfolio.md`: Deep-dive learning logs tracking bits, logic gates, and processor execution pipelines.
    * `FirstNotebook.ipynb`: Sandbox environment tracking data matrices and memory allocations.
    * **Future Project — Silicon-Foundations.md:** A comprehensive $\LaTeX$-heavy compilation tracking Boolean algebra minimization using Karnaugh maps ($K\text{-maps}$) to map directly to future digital electronics coursework.
    * **Future Project — Cyber-Forensics-Theory.md:** An analytical breakdown of Linux filesystem structures ($ext4$ vs $NTFS$) and memory volatile analysis vectors.

### ⏳ Phase 2: API Integration & Data Ingestion (June Focus)
* **Objective:** Leverage APIs to ingest threat intelligence feeds, network logs, and live silicon telemetry data.
* **Core Projects & Deliverables:**
    * `vuln_feed_fetcher.py`: Automated retrieval of open-source vulnerability databases (CVEs) and malicious IP logs.
    * `log_payload_parser.py`: Python parsing scripts to clean raw, unstructured server text logs into structured JSON payloads.
    * **Future Project — Shodan-Threat-Ingestor.py:** A script targeting the Shodan API to dynamically query, filter, and extract open ports and exposed firmware versions of critical industrial hardware nodes.
    * **Future Project — Silicon-Telemetry-Parser.py:** A simulation script that parses streaming JSON payloads representing simulated thermal and clock-frequency variations across multi-core CPU architectures.

### ⏳ Phase 3: Automation Pipelines & Incident Response (July Focus)
* **Objective:** Build self-sustaining, 24/7 cloud pipelines that handle monitoring, analytics, and instant alert dispatches.
* **Core Projects & Deliverables:**
    * `cron_security_auditor.py`: Script schedulers running continuous security audits on mock cloud infrastructure.
    * `incident_webhook_dispatcher.py`: Automated webhook integrations (Discord/Slack/Email alerts) triggered instantly by system anomalies detected in Phase 2 data streams.
    * **Future Project — Live-Blacklist-Sync.py:** An autonomous cloud fetch-and-commit security sync that runs every 12 hours.
    * **Future Project — Automated-Report-Generator.py:** A pipeline that converts parsed weekly security logs into clear Markdown metrics summaries.

### ⏳ Phase 4: Core Technical Projects (August & Onward Track)
* **Objective:** Apply concepts across a 3-tier practical project architecture designed to demonstrate cross-disciplinary mastery to university faculty.
* **Core Deliverables:**
    * **Level 1 (Foundations):** From-scratch mathematical optimization engines (TinyML basics) and bit-level cryptographic data scramblers (`tiny_ml_math`, `aes_visualizer`).
    * **Level 2 (Simulations):** Virtual 8-bit CPU architecture emulators and software-side hardware trojan/timing-leak models (`cpu_emulator`, `side_channel_trojan`).
    * **Level 3 (Edge AI):** Network log anomaly detectors deploying machine learning libraries to catch malicious infrastructure attacks (`network_anomaly_detector`).

---

## 📂 Repository Structure

```text
├── Core-Technical-Projects/          # Practical implementations of hardware/software systems
│   ├── 01-Level-1-Foundations/       
│   │   ├── tiny_ml_math/             # Matrix math and algebraic regression engines from scratch
│   │   └── aes_visualizer/           # String-to-hex transposition ciphers and round trackers
│   ├── 02-Level-2-Simulations/       
│   │   ├── cpu_emulator/             # Register, PC, and instruction-set virtual execution loop
│   │   └── side_channel_trojan/      # Simulation of password timing-leak hardware vulnerabilities
│   └── 03-Level-3-Edge-AI/           
│       └── network_anomaly_detector/ # Scikit-learn classification engines parsing threat profiles
├── Phase-1-Documentation/
│   ├── Master_Readme_Portfolio.md    # Hands-on Markdown & LaTeX compilation
│   ├── FirstNotebook.ipynb           # Cloud notebook for proof-of-concept calculations
│   ├── Silicon-Foundations.md        # [Future] K-Map and logic gate minimization reference sheet
│   └── Cyber-Forensics-Theory.md     # [Future] Memory forensics and OS storage architecture logs
├── Phase-2-API-Parsing/              
│   ├── vuln_feed_fetcher.py          # Script querying live threat databases via HTTP requests
│   ├── log_payload_parser.py         # Regex-heavy parser mapping server logs to structured JSON arrays
│   ├── Shodan-Threat-Ingestor.py     # [Future] External query architecture targeting open IoT infrastructure
│   └── Silicon-Telemetry-Parser.py   # [Future] Hardware thermal and metrics stream parser
├── Phase-3-Automation/               
│   ├── cron_security_auditor.py      # Scheduled task controller executing infrastructure checks
│   ├── incident_webhook_dispatcher.py# REST endpoint signaling warning payloads to Discord endpoints
│   ├── Live-Blacklist-Sync.py        # [Future] Autonomous cloud fetch-and-commit security sync
│   └── Automated-Report-Generator.py # [Future] Dynamic markdown compilation and logging automated emails
├── brainstorming/                    # Active sandboxes, conceptual blueprints, and architectural schemas
│   ├── Base-X_Two-Way_Conversion_Engine/ # Core math engine mapping numeric bases (Binary/Hex)—foundational for VLSI memory tracking
│   ├── login_page/                   # Prototyping authentication flow mechanisms, input handling, and secure code validation
│   ├── hardware_trojan_blueprint.txt # Structural logic flow mapping out hardware state execution leaks
│   ├── edge_ai_pipeline_sketch.md   # Mathematical pipelines mapping data downscaling for TinyML
│   ├── rru_lab_leverage_strategy.txt # Academic roadmap targeting specific university research labs
│   └── custom_instruction_sets.json  # Custom opcode definitions for the Level 2 virtual CPU simulator
└── README.md                         # Target portfolio landing page
