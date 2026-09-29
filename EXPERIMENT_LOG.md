# NIDS Machine Learning Internship: Experiment Log

This file systematically tracks all machine learning experiments, hypotheses, configurations, and quantitative outcomes across baseline and optimized phases.

---

## 1. Experiment Summary Table

| Exp ID | Date | Model | Features | Sampling / Scaling | Accuracy | Precision (Macro) | Recall (Macro) | F1-Score (Macro) | Status | Artifacts / Notes |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `EXP-001` | Planned (W3) | Logistic Regression | All 78 | Standard Scaler | TBD | TBD | TBD | TBD | Scheduled | Linear baseline |
| `EXP-002` | Planned (W3) | Decision Tree (CART)| All 78 | Standard Scaler | TBD | TBD | TBD | TBD | Scheduled | Non-linear tree baseline |
| `EXP-003` | Planned (W3) | Random Forest | All 78 | None / Robust | TBD | TBD | TBD | TBD | Scheduled | Ensemble bagging baseline |
| `EXP-004` | Planned (W3) | XGBoost | All 78 | Standard Scaler | TBD | TBD | TBD | TBD | Scheduled | Gradient boosted baseline |
| `EXP-005` | Planned (W3) | LightGBM | All 78 | Standard Scaler | TBD | TBD | TBD | TBD | Scheduled | High-speed gradient boosting |
| `EXP-006` | Planned (W4) | RF + Feature Selection | Top K (Mutual Info / Importance) | MinMax / Robust | TBD | TBD | TBD | TBD | Scheduled | Dimensionality reduction |
| `EXP-007` | Planned (W4) | XGBoost + SMOTE / Class Weights | Top K | Robust Scaler | TBD | TBD | TBD | TBD | Scheduled | Handling severe class imbalance (Infiltration, Bot) |
| `EXP-008` | Planned (W5) | Tuned Random Forest | Top K | Tuned via GridSearch | TBD | TBD | TBD | TBD | Scheduled | Hyperparameter optimization |
| `EXP-009` | Planned (W5) | Tuned XGBoost / LightGBM | Top K | Tuned via Optuna / GridSearch | TBD | TBD | TBD | TBD | Scheduled | Final high-performance intrusion classifier |

---

## 2. Evaluation Criteria & Objectives
1. **Primary Metric:** Macro-averaged F1-Score (critical due to extreme class imbalance: Infiltration with 36 samples vs. BENIGN with 22,731 samples).
2. **Secondary Metrics:**
   - Detection Rate (Recall) on attack classes (minimizing False Negatives).
   - False Alarm Rate (FAR) on Benign traffic (minimizing False Positives).
   - Inference latency per network flow (must support real-time network throughput).
3. **Validation Strategy:**
   - 80/20 Stratified Train-Test split.
   - 5-Fold Stratified Cross-Validation on training set.
