# CICIDS2017 Dataset Information

## 1. Overview
- **Dataset Name:** CICIDS2017 (Canadian Institute for Cybersecurity Intrusion Detection System 2017)
- **Originating Institution:** Canadian Institute for Cybersecurity (CIC) / University of New Brunswick (UNB)
- **Traffic Capture Period:** 5 Days (Monday, July 3, 2017 to Friday, July 7, 2017)
- **Feature Extraction Engine:** `CICFlowMeter` (generates bidirectional flow statistical features)
- **Dataset File:** `data/raw/CICIDS2017/CICIDS2017_sample.csv`
- **Total Records:** 56,661 network flows
- **Feature Dimensionality:** 78 continuous/discrete numeric attributes + 1 class label (`Label`)

---

## 2. Attack Classes & Distribution

| Class Label | Description | Sample Count | Percentage |
| :--- | :--- | :--- | :--- |
| **BENIGN** | Normal, benign day-to-day enterprise background traffic | 22,731 | 40.12% |
| **DoS** | Denial of Service attacks (Hulk, GoldenEye, Slowloris, Slowhttptest) | 19,035 | 33.59% |
| **PortScan** | Network reconnaissance / port scanning | 7,946 | 14.02% |
| **BruteForce** | SSH and FTP authentication brute force attempts | 2,767 | 4.88% |
| **WebAttack** | SQL Injection, Cross-Site Scripting (XSS), Web Brute Force | 2,180 | 3.85% |
| **Bot** | Ares botnet malicious command & control communications | 1,966 | 3.47% |
| **Infiltration** | Multi-stage infiltration via vulnerable Dropbox/file download | 36 | 0.06% |
| **Total** | **All Traffic Types** | **56,661** | **100.00%** |

---

## 3. Feature Taxonomy & Groupings

1. **Flow Volume & Duration:**
   - `Flow Duration`, `Total Fwd Packets`, `Total Backward Packets`, `Total Length of Fwd Packets`, `Total Length of Bwd Packets`
2. **Packet Length Distributions:**
   - `Fwd Packet Length Max/Min/Mean/Std`, `Bwd Packet Length Max/Min/Mean/Std`, `Min/Max/Mean/Std/Variance Packet Length`, `Average Packet Size`
3. **Flow Throughput & Rates:**
   - `Flow Bytes/s`, `Flow Packets/s`, `Fwd Packets/s`, `Bwd Packets/s`
4. **Inter-Arrival Time (IAT):**
   - `Flow IAT Mean/Std/Max/Min`, `Fwd IAT Total/Mean/Std/Max/Min`, `Bwd IAT Total/Mean/Std/Max/Min`
5. **TCP Protocol Flags:**
   - `FIN Flag Count`, `SYN Flag Count`, `RST Flag Count`, `PSH Flag Count`, `ACK Flag Count`, `URG Flag Count`, `CWE Flag Count`, `ECE Flag Count`, `Fwd PSH Flags`, `Bwd PSH Flags`, `Fwd URG Flags`, `Bwd URG Flags`
6. **TCP Window & Header Characteristics:**
   - `Fwd Header Length`, `Bwd Header Length`, `Init_Win_bytes_forward`, `Init_Win_bytes_backward`, `min_seg_size_forward`, `act_data_pkt_fwd`
7. **Active & Idle Time Windows:**
   - `Active Mean/Std/Max/Min`, `Idle Mean/Std/Max/Min`

---

## 4. Key Preprocessing Challenges & Plan

1. **Infinite & Missing Values:**
   - Network flows with `Flow Duration = 0` yield `inf` in `Flow Bytes/s` and `Flow Packets/s`.
   - Action: Replace `inf` and `-inf` with `NaN`, then impute or drop invalid records.
2. **High Multicollinearity & Zero Variance:**
   - Features such as `Fwd Avg Bytes/Bulk`, `Fwd Avg Packets/Bulk`, `Fwd Avg Bulk Rate`, `Bwd Avg Bytes/Bulk`, `Bwd Avg Packets/Bulk`, `Bwd Avg Bulk Rate` have zero variance (all 0s).
   - Action: Drop constant zero-variance columns and redundant duplicate headers.
3. **Severe Class Imbalance:**
   - `Infiltration` contains only 36 flows compared to 22,731 `BENIGN` flows.
   - Action: Apply stratified sampling in train-test splits, class-weighted loss functions, and SMOTE/ADASYN during optimization.
4. **Feature Scaling:**
   - Features span disparate scales (from binary flags $[0, 1]$ to `Flow Duration` in millions of microseconds).
   - Action: Use `RobustScaler` or `StandardScaler` fitted strictly on training data to prevent data leakage.
