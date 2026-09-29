# NIDS Machine Learning Internship: Run Log

All runs, commands, script executions, and pipeline operations are sequentially logged here with timestamps, commands, targets, and exit statuses.

---

### [2026-09-29 14:22:21 IST] Directory Scaffolding
- **Action:** Initialized empty repository folder structure and placeholder files as specified in project structure template.
- **Command:** `New-Item -ItemType Directory ...; New-Item -ItemType File ...`
- **Result:** Success (Exit Code: 0). Scaffolding established.

---

### [2026-09-29 14:33:30 IST] Repository Inspection & State Discovery
- **Action:** Inspected workspace tree, checked existing files, discovered all existing files were 0 bytes.
- **Command:** `Get-ChildItem -Recurse -File`
- **Result:** Found empty placeholder files; identified need to initialize governance files (`PROJECT_STATE.md`, `RUN_LOG.md`, `EXPERIMENT_LOG.md`, `DATASET_INFO.md`).
- **Status:** Complete.

---

### [2026-09-29 14:37:45 IST] Authentic Dataset Discovery & Mapping
- **Action:** Searched local filesystem for authentic CICIDS2017 dataset; discovered pre-processed 56,661-row benchmark sample dataset (`CICIDS2017_sample.csv`).
- **Inspection Command:** Python csv inspection for row count (56,661), feature count (78), class distribution (BENIGN: 22,731, DoS: 19,035, PortScan: 7,946, BruteForce: 2,767, WebAttack: 2,180, Bot: 1,966, Infiltration: 36).
- **Ingestion Command:** Copied dataset into `data/raw/CICIDS2017/CICIDS2017_sample.csv`.
- **Result:** Real benchmark data successfully integrated without data fabrication.

---

### [2026-09-29 14:38:45 IST] Virtual Environment Setup
- **Action:** Created isolated Python virtual environment (`.venv`) using Python 3.12.
- **Command:** `python -m venv .venv`
- **Result:** Success (Exit Code: 0).

---

### [2026-09-29 14:39:15 IST] Dependency Management & Installation
- **Action:** Populated `requirements.txt` with numpy, pandas, scipy, scikit-learn, xgboost, lightgbm, matplotlib, seaborn, joblib, pytest, openpyxl, python-docx, reportlab.
- **Command:** `.\.venv\Scripts\python.exe -m pip install -r requirements.txt`
- **Result:** All packages successfully installed (Exit Code: 0).

---

### [2026-09-29 14:40:15 IST] Governance & State Tracking Documentation
- **Action:** Created `PROJECT_STATE.md`, `RUN_LOG.md`, `EXPERIMENT_LOG.md`, `DATASET_INFO.md`, `README.md`, `LICENSE`, `.gitignore`.
- **Result:** State tracking activated.

---

### [2026-09-29 14:41:00 IST] Core Utility Implementation (Config & Logger)
- **Action:** Implemented `src/utils/config.py`, `src/utils/logger.py`, and `src/utils/__init__.py`.
- **Result:** Centralized paths, hyperparameters, attack class taxonomy, and file logging established.

---

### [2026-09-29 14:42:00 IST] Week 1 Planning Deliverables Generation
- **Action:** Generated Week 1 artifacts:
  - `reports/week_01_project_planning/architecture.png` (414 KB)
  - `reports/week_01_project_planning/project_timeline.xlsx` (6.8 KB)
  - `reports/week_01_project_planning/Week_01_NIDS_Project_Plan.docx` (38.8 KB)
  - `reports/week_01_project_planning/literature_review.docx` (39.1 KB)
- **Result:** All Week 1 planning artifacts verified and saved.

---

### [2026-09-29 14:42:45 IST] Automated Testing & Quality Audit (Week 1)
- **Action:** Implemented `tests/test_data.py` and ran pytest suite.
- **Command:** `.\.venv\Scripts\python.exe -m pytest tests/test_data.py -v`
- **Result:** 4/4 tests passed (100% pass rate in 0.55s).
