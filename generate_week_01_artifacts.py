"""Script to generate Week 1 artifacts: architecture.png, project_timeline.xlsx,
Week_01_NIDS_Project_Plan.docx, and literature_review.docx.
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT

PROJECT_ROOT = Path(__file__).resolve().parent
WEEK_01_DIR = PROJECT_ROOT / "reports" / "week_01_project_planning"
WEEK_01_DIR.mkdir(parents=True, exist_ok=True)


def generate_architecture_diagram():
    """Generate high-resolution architecture diagram for NIDS pipeline."""
    fig, ax = plt.subplots(figsize=(14, 8), dpi=300)
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 8)
    ax.axis('off')

    # Color palette
    c_bg = "#F8FAFC"
    fig.patch.set_facecolor(c_bg)

    c_box = "#1E293B"      # Dark slate
    c_blue = "#2563EB"     # Royal blue
    c_teal = "#0D9488"     # Teal
    c_purple = "#7C3AED"   # Purple
    c_orange = "#EA580C"   # Orange
    c_green = "#16A34A"    # Green
    c_border = "#E2E8F0"

    title_text = "End-to-End Machine Learning NIDS Pipeline Architecture"
    plt.text(7, 7.5, title_text, fontsize=16, fontweight='bold', ha='center', color="#0F172A")
    plt.text(7, 7.15, "Benchmark Dataset: CICIDS2017 | Multi-Class Flow Classification",
             fontsize=11, fontstyle='italic', ha='center', color="#475569")

    # Define stage boxes: (x, y, w, h, title, desc, color)
    stages = [
        (0.6, 4.8, 2.6, 1.8, "1. Data Ingestion", "• CICIDS2017 Dataset\n• 56,661 Flow Records\n• 78 Network Attributes\n• 7 Attack Categories", c_blue),
        (3.8, 4.8, 2.6, 1.8, "2. Preprocessing & Clean", "• Infinite / NaN Imputation\n• Constant Feature Pruning\n• Outlier Inspection\n• Duplicate Removal", c_teal),
        (7.0, 4.8, 2.6, 1.8, "3. Feature Pipeline", "• Stratified Split (80/20)\n• Robust / Standard Scaling\n• Mutual Info Selection\n• Class Weight / Resampling", c_purple),
        (10.2, 4.8, 2.6, 1.8, "4. ML Model Suite", "• Logistic Regression\n• CART Decision Tree\n• Random Forest (Bagging)\n• XGBoost & LightGBM", c_orange),
        (2.2, 1.4, 4.2, 2.0, "5. Diagnostics & Evaluation", "• Macro / Weighted F1-Score\n• Attack Detection Rate (Recall)\n• False Alarm Rate (FAR on Benign)\n• Multi-Class Confusion Matrix & ROC", c_teal),
        (7.6, 1.4, 4.2, 2.0, "6. Optimization & Final Artifacts", "• Hyperparameter Tuning (Optuna / CV)\n• Inference Latency Benchmarking\n• Serialized Models (joblib)\n• 6-Week Audited Technical Reports", c_green),
    ]

    for x, y, w, h, title, desc, color in stages:
        rect = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.1,rounding_size=0.15",
                                     linewidth=1.8, edgecolor=color, facecolor="#FFFFFF")
        ax.add_patch(rect)
        # Header banner inside box
        header_rect = patches.FancyBboxPatch((x, y + h - 0.45), w, 0.45,
                                             boxstyle="round,pad=0.08,rounding_size=0.1",
                                             facecolor=color, edgecolor="none")
        ax.add_patch(header_rect)
        ax.text(x + w / 2, y + h - 0.23, title, color="white", fontsize=10.5,
                fontweight='bold', ha='center', va='center')
        ax.text(x + 0.15, y + (h - 0.45) / 2, desc, color="#334155", fontsize=9,
                va='center', linespacing=1.4)

    # Arrows for flow
    arrow_props = dict(facecolor="#64748B", edgecolor="#475569", width=1.5, headwidth=7, headlength=7)
    
    # 1 -> 2
    ax.annotate("", xy=(3.8, 5.7), xytext=(3.2, 5.7), arrowprops=arrow_props)
    # 2 -> 3
    ax.annotate("", xy=(7.0, 5.7), xytext=(6.4, 5.7), arrowprops=arrow_props)
    # 3 -> 4
    ax.annotate("", xy=(10.2, 5.7), xytext=(9.6, 5.7), arrowprops=arrow_props)

    # 4 -> 5 (downward and back)
    ax.annotate("", xy=(6.4, 2.4), xytext=(11.5, 4.8),
                arrowprops=dict(facecolor="#64748B", edgecolor="#475569", width=1.5,
                                headwidth=7, headlength=7, connectionstyle="arc3,rad=-0.2"))

    # 5 -> 6
    ax.annotate("", xy=(7.6, 2.4), xytext=(6.4, 2.4), arrowprops=arrow_props)

    plt.tight_layout()
    output_png = WEEK_01_DIR / "architecture.png"
    plt.savefig(output_png, facecolor=fig.get_facecolor(), bbox_inches='tight')
    plt.close()
    print(f"[+] Generated: {output_png}")


def generate_project_timeline_excel():
    """Generate Excel workbook for the 6-week project timeline with styling."""
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "NIDS 6-Week Timeline"
    ws.views.sheetView[0].showGridLines = True

    # Header styling
    header_font = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
    header_fill = PatternFill(start_color="1E3A8A", end_color="1E3A8A", fill_type="solid")
    center_align = Alignment(horizontal="center", vertical="center", wrap_text=True)
    left_align = Alignment(horizontal="left", vertical="center", wrap_text=True)
    border_thin = Border(
        left=Side(style='thin', color='CBD5E1'),
        right=Side(style='thin', color='CBD5E1'),
        top=Side(style='thin', color='CBD5E1'),
        bottom=Side(style='thin', color='CBD5E1')
    )

    # Title Block
    ws.merge_cells("A1:G1")
    title_cell = ws["A1"]
    title_cell.value = "Network Intrusion Detection System (NIDS) — 6-Week Internship Timeline"
    title_cell.font = Font(name="Calibri", size=14, bold=True, color="0F172A")
    title_cell.alignment = Alignment(horizontal="center", vertical="center")
    ws.row_dimensions[1].height = 32

    headers = ["Task ID", "Week", "Phase / Task Description", "Assigned Milestone", "Deliverables", "Duration", "Status"]
    ws.append([])  # Row 2 empty
    ws.append(headers)  # Row 3 headers
    ws.row_dimensions[3].height = 24

    for col_idx, header in enumerate(headers, 1):
        cell = ws.cell(row=3, column=col_idx)
        cell.font = header_font
        cell.fill = header_fill
        cell.alignment = center_align
        cell.border = border_thin

    tasks = [
        ("T1.1", "Week 1", "Project Initiation, Scope Definition & Requirements", "Phase 1: Planning", "Project charter & environment", "3 Days", "Completed"),
        ("T1.2", "Week 1", "Literature Review on ML-based Intrusion Detection", "Phase 1: Planning", "literature_review.docx", "2 Days", "Completed"),
        ("T1.3", "Week 1", "System Architecture & Pipeline Design", "Phase 1: Planning", "architecture.png, config.py", "2 Days", "Completed"),
        ("T2.1", "Week 2", "Data Ingestion & Quality Audit (CICIDS2017)", "Phase 2: Preprocessing", "data_dictionary.xlsx, raw CSV", "2 Days", "Scheduled"),
        ("T2.2", "Week 2", "Data Cleaning, Inf/NaN Handling & Formatting", "Phase 2: Preprocessing", "cleaned_data.csv, clean_data.py", "2 Days", "Scheduled"),
        ("T2.3", "Week 2", "Exploratory Data Analysis & Class Imbalance Analysis", "Phase 2: Preprocessing", "01_data_exploration.ipynb, report", "3 Days", "Scheduled"),
        ("T3.1", "Week 3", "Feature Engineering, Scaling & Encoding", "Phase 3: Modeling", "encoded_data.csv, scale.py", "2 Days", "Scheduled"),
        ("T3.2", "Week 3", "Baseline Model Implementation (LR, CART, RF)", "Phase 3: Modeling", "04_baseline_models.ipynb, train.py", "3 Days", "Scheduled"),
        ("T3.3", "Week 3", "Initial Baseline Evaluation & Serialization", "Phase 3: Modeling", "baseline_metrics.csv, models/", "2 Days", "Scheduled"),
        ("T4.1", "Week 4", "Comprehensive Multi-Class Performance Diagnostics", "Phase 4: Evaluation", "classification_report.xlsx", "2 Days", "Scheduled"),
        ("T4.2", "Week 4", "Confusion Matrix, ROC-AUC & Error Analysis", "Phase 4: Evaluation", "confusion_matrix.png, error_analysis.py", "3 Days", "Scheduled"),
        ("T4.3", "Week 4", "Cross-Validation & Robustness Verification", "Phase 4: Evaluation", "cross_validation_results.xlsx", "2 Days", "Scheduled"),
        ("T5.1", "Week 5", "Feature Selection & Dimensionality Reduction", "Phase 5: Optimization", "feature_importance plots", "2 Days", "Scheduled"),
        ("T5.2", "Week 5", "Hyperparameter Tuning (Random Forest & XGBoost)", "Phase 5: Optimization", "hyperparameter_results.xlsx", "3 Days", "Scheduled"),
        ("T5.3", "Week 5", "Ensemble Evaluation & Latency Benchmarks", "Phase 5: Optimization", "final_metrics.csv, models/tuned/", "2 Days", "Scheduled"),
        ("T6.1", "Week 6", "Final Quality & Codebase Verification Audit", "Phase 6: Final Deliverables", "Passing pytest test suite", "2 Days", "Scheduled"),
        ("T6.2", "Week 6", "Final Technical Internship Report Drafting", "Phase 6: Final Deliverables", "Final_NIDS_Internship_Report.docx/.pdf", "3 Days", "Scheduled"),
        ("T6.3", "Week 6", "Final Presentation & Poster Preparation", "Phase 6: Final Deliverables", "final_presentation.pptx, poster.png", "2 Days", "Scheduled")
    ]

    for row_data in tasks:
        ws.append(list(row_data))
        current_row = ws.max_row
        ws.row_dimensions[current_row].height = 20
        status_val = row_data[6]

        for col_idx in range(1, 8):
            cell = ws.cell(row=current_row, column=col_idx)
            cell.font = Font(name="Calibri", size=10)
            cell.border = border_thin
            if col_idx in [1, 2, 4, 6, 7]:
                cell.alignment = center_align
            else:
                cell.alignment = left_align

            # Highlight Completed vs Scheduled
            if col_idx == 7:
                if status_val == "Completed":
                    cell.fill = PatternFill(start_color="DCFCE7", end_color="DCFCE7", fill_type="solid")
                    cell.font = Font(name="Calibri", size=10, bold=True, color="166534")
                else:
                    cell.fill = PatternFill(start_color="FEF9C3", end_color="FEF9C3", fill_type="solid")
                    cell.font = Font(name="Calibri", size=10, color="854D0E")

    # Column widths
    col_widths = [10, 12, 38, 24, 34, 12, 14]
    for i, w in enumerate(col_widths, 1):
        ws.column_dimensions[openpyxl.utils.get_column_letter(i)].width = w

    output_xlsx = WEEK_01_DIR / "project_timeline.xlsx"
    wb.save(output_xlsx)
    print(f"[+] Generated: {output_xlsx}")


def generate_week_01_project_plan_docx():
    """Generate professional Word document for Week 1 Project Plan."""
    doc = Document()

    # Title
    title = doc.add_heading("Week 1 Deliverable: NIDS Project Plan & Specification", level=0)
    title.alignment = WD_ALIGN_PARAGRAPH.CENTER

    doc.add_paragraph("Author: Prithviraj Pol | Internship Track: Machine Learning & Cybersecurity")
    doc.add_paragraph("Target Dataset: CICIDS2017 Benchmark | Project: Network Intrusion Detection System")
    doc.add_paragraph("Date: 2026-09-29 | Phase: Phase 1 — Project Planning & Environment Setup")
    doc.add_paragraph("-" * 80)

    # 1. Executive Summary
    doc.add_heading("1. Executive Summary", level=1)
    doc.add_paragraph(
        "Network security is a fundamental pillar of modern digital infrastructure. As cyber threats evolve in "
        "complexity, scale, and stealth, traditional Signature-based Intrusion Detection Systems (SIDS) struggle "
        "to detect zero-day exploits and polymorphic network attacks. This project establishes an advanced, reproducible, "
        "and production-grade Machine Learning-based Network Intrusion Detection System (ML-NIDS)."
    )
    doc.add_paragraph(
        "Leveraging the authoritative CICIDS2017 benchmark dataset, this project investigates and implements an "
        "end-to-end data science lifecycle over 6 weeks. The system evaluates linear, ensemble, and gradient-boosted "
        "architectures (including Logistic Regression, Decision Trees, Random Forests, XGBoost, and LightGBM) "
        "to deliver robust multi-class threat classification with strict optimization for low false alarm rates (FAR) "
        "and sub-millisecond inference latency."
    )

    # 2. Problem Statement
    doc.add_heading("2. Problem Statement", level=1)
    doc.add_paragraph(
        "Enterprise network perimeters handle millions of bidirectional network flows per second. An effective NIDS must:\n"
        "1. Discriminate between benign background operations and multi-vector malicious intrusions.\n"
        "2. Accurately categorize distinct attack types: Denial of Service (DoS), PortScan reconnaissance, "
        "SSH/FTP Brute Force, Web Attacks, Botnet command & control, and advanced Infiltration.\n"
        "3. Mitigate severe class imbalance without inducing excessive false alarms that cause operator alert fatigue.\n"
        "4. Process high-dimensional network flow statistics efficiently to maintain line-rate throughput."
    )

    # 3. Objectives & Key Results (OKRs)
    doc.add_heading("3. Objectives & Key Deliverables", level=1)
    table = doc.add_table(rows=1, cols=3)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    hdr = table.rows[0].cells
    hdr[0].text = "Objective"
    hdr[1].text = "Key Metric / Deliverable"
    hdr[2].text = "Target Threshold"

    okrs = [
        ("O1: Data Pipeline Integrity", "Cleaned & stratified CICIDS2017 datasets", "0 invalid Inf/NaN values; 0 leakage"),
        ("O2: High Threat Detection", "Macro-averaged F1-Score & Attack Recall", "Macro F1 > 0.95; Attack Recall > 98%"),
        ("O3: Minimal False Positives", "False Alarm Rate (FAR) on Benign", "FAR < 1.0% on held-out test data"),
        ("O4: Low Latency Inference", "Execution time per flow sample", "< 0.5 ms per flow for line-rate support"),
        ("O5: Industry-Grade Codebase", "Modular architecture with pytest suite", "100% test pass rate across all modules")
    ]
    for obj, dlv, tgt in okrs:
        row = table.add_row().cells
        row[0].text = obj
        row[1].text = dlv
        row[2].text = tgt

    # 4. Scope & System Architecture
    doc.add_heading("4. Architectural Overview", level=1)
    doc.add_paragraph(
        "The project architecture is organized into five functional layers:\n"
        "• Data Ingestion Layer: Reads raw flow captures from CICIDS2017.\n"
        "• Preprocessing Layer: Cleans mathematical infinities, removes constant zero-variance features, and resolves missing data.\n"
        "• Feature Engineering Layer: Performs stratified splitting (80/20 train/test), robust scaling, and mutual-information feature selection.\n"
        "• Modeling & Optimization Layer: Trains baseline algorithms, evaluates diagnostic curves, and applies Bayesian/Grid hyperparameter search.\n"
        "• Evaluation & Reporting Layer: Exports confusion matrices, cross-validation metrics, and formatted weekly deliverables."
    )

    # 5. Risk Assessment & Mitigation
    doc.add_heading("5. Risk Assessment & Mitigation Strategy", level=1)
    risk_table = doc.add_table(rows=1, cols=3)
    risk_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    r_hdr = risk_table.rows[0].cells
    r_hdr[0].text = "Risk Description"
    r_hdr[1].text = "Impact Severity"
    r_hdr[2].text = "Mitigation Technique"

    risks = [
        ("Extreme Class Imbalance (Infiltration < 0.1%)", "High", "Employ stratified k-fold splits, class-weighted loss, and SMOTE resampling."),
        ("Data Leakage during Scaling/Selection", "Critical", "Strictly fit scalers and selectors on training partitions only."),
        ("Infinite values in Flow Bytes/s", "High", "Explicit conversion of inf values to NaN and capped median imputation."),
        ("Overfitting on Training Traffic", "Medium", "5-fold cross-validation, regularization, and max-depth bounds on decision trees.")
    ]
    for r, s, m in risks:
        row = risk_table.add_row().cells
        row[0].text = r
        row[1].text = s
        row[2].text = m

    output_docx = WEEK_01_DIR / "Week_01_NIDS_Project_Plan.docx"
    doc.save(output_docx)
    print(f"[+] Generated: {output_docx}")


def generate_literature_review_docx():
    """Generate Word document for Week 1 Literature Review."""
    doc = Document()

    title = doc.add_heading("Week 1 Deliverable: Literature Review on ML-based NIDS", level=0)
    title.alignment = WD_ALIGN_PARAGRAPH.CENTER

    doc.add_paragraph("Author: Prithviraj Pol | Focus: Network Security & Machine Learning")
    doc.add_paragraph("Target Dataset: CICIDS2017 | Context: Network Intrusion Detection Systems")
    doc.add_paragraph("-" * 80)

    # 1. Introduction
    doc.add_heading("1. Introduction & Background", level=1)
    doc.add_paragraph(
        "Network Intrusion Detection Systems (NIDS) are critical defensive technologies tasked with inspecting packet "
        "headers, payload metadata, and traffic flow characteristics to identify malicious activity. Traditional "
        "approaches depend primarily on signature matching (e.g., Snort, Suricata, Bro/Zeek). While signature matching "
        "achieves near-zero false alarms for recognized attack vectors, it is fundamentally ineffective against zero-day "
        "vulnerabilities, polymorphic malware, and fast-evolving attack variants."
    )
    doc.add_paragraph(
        "In contrast, Anomaly-based Intrusion Detection Systems (AIDS) utilize Machine Learning (ML) and statistical "
        "modeling to establish a baseline profile of normal network behavior, flagging substantial statistical deviations "
        "as potential intrusions. This review synthesizes key research on ML-based NIDS, benchmarking datasets, "
        "algorithmic performance, and open operational challenges."
    )

    # 2. Benchmark Datasets
    doc.add_heading("2. Evolution of NIDS Benchmark Datasets", level=1)
    doc.add_paragraph(
        "The validity of any ML-NIDS critically depends on the quality, diversity, and realism of its training data:\n"
        "• KDD Cup 1999 & NSL-KDD: While historically foundational, these datasets suffer from outdated traffic patterns, "
        "unrealistic synthetic packet generation, duplicate records, and lack of modern attack representations (e.g., modern DDoS, botnets).\n"
        "• UNSW-NB15: Introduced to address modern low-footprint attack scenarios, containing 49 features and 9 attack categories.\n"
        "• CICIDS2017: Developed by the Canadian Institute for Cybersecurity (UNB). Recorded over a 5-day period in a realistic "
        "testbed environment, CICIDS2017 reflects realistic human background traffic (HTTP, HTTPS, SSH, FTP, Email) alongside "
        "modern attack vectors (Brute Force, DoS, DDoS, Web Attacks, Infiltration, PortScan, and Botnet traffic). Extracted via "
        "CICFlowMeter into 78 bidirectional flow attributes, it stands as the de-facto standard for modern ML-NIDS benchmarking."
    )

    # 3. Machine Learning Architectures
    doc.add_heading("3. Machine Learning Algorithms in NIDS", level=1)
    doc.add_paragraph(
        "1. Tree-Based Ensembles (Random Forest, CART):\n"
        "Research by Sharafaldin et al. (2018) demonstrated that Random Forest consistently achieves superior detection "
        "rates on CICIDS2017 (exceeding 98% accuracy) due to its resistance to overfitting, handling of non-linear feature "
        "relationships, and native ability to handle mixed continuous/discrete network attributes.\n\n"
        "2. Gradient Boosted Decision Trees (XGBoost & LightGBM):\n"
        "Recent investigations (e.g., Ferrag et al., 2020; Sarhan et al., 2021) demonstrate that XGBoost and LightGBM "
        "outperform traditional shallow models by iteratively minimizing residual errors. LightGBM's leaf-wise tree growth "
        "and histogram-based binning provide dramatically reduced training and inference latency, making it ideal for "
        "near-real-time packet analysis.\n\n"
        "3. Deep Learning Approaches (MLP, CNN, LSTM):\n"
        "While deep neural networks can extract temporal sequence dependencies, they require substantial computational "
        "resources and lack interpretability. In high-speed flow classification where feature representations are already "
        "engineered by CICFlowMeter, tabular gradient boosting frequently matches or exceeds deep learning accuracy "
        "at a fraction of the computational and inference cost."
    )

    # 4. Critical Challenges & Open Issues
    doc.add_heading("4. Key Challenges in ML-NIDS Research", level=1)
    doc.add_paragraph(
        "• Extreme Class Imbalance: Certain attack categories, such as Infiltration, account for less than 0.1% of "
        "the total traffic, causing standard classifiers to optimize exclusively for majority classes.\n"
        "• False Alarm Fatigue: In production enterprise environments, an error rate of 1% on 1,000,000 flows produces "
        "10,000 false alerts per day, overwhelming security operations centers (SOCs).\n"
        "• Real-Time Latency: To avoid packet drops, flow classification must complete in microseconds."
    )

    # 5. References
    doc.add_heading("5. References", level=1)
    refs = [
        "1. Sharafaldin, I., Lashkari, A. H., & Ghorbani, A. A. (2018). Toward Generating a New Dataset for Intrusion Detection and Intrusion Prevention with Systematic Approach. In Proceedings of the 4th International Conference on Information Systems Security and Privacy (ICISSP), pp. 108-116.",
        "2. Ferrag, M. A., Maglaras, L., Moschoyiannis, S., & Janicke, H. (2020). Deep learning for cyber security intrusion detection: Approaches, datasets, and comparative study. Journal of Information Security and Applications, 50, 102419.",
        "3. Sarhan, M., Layeghy, S., & Portmann, M. (2021). Towards a systematic framework for evaluating intrusion detection systems. IEEE Access, 9, 90802-90816.",
        "4. Tavallaee, M., Bagheri, E., Lu, W., & Ghorbani, A. A. (2009). A detailed analysis of the KDD CUP 99 data set. IEEE Symposium on Computational Intelligence for Security and Defense Applications, pp. 1-6.",
        "5. Zhou, Y., Cheng, G., Jiang, S., & Dai, M. (2020). Building an efficient intrusion detection system based on feature selection and ensemble classifier. Computer Networks, 174, 107247."
    ]
    for r in refs:
        p = doc.add_paragraph(r)
        p.paragraph_format.left_indent = Inches(0.25)

    output_docx = WEEK_01_DIR / "literature_review.docx"
    doc.save(output_docx)
    print(f"[+] Generated: {output_docx}")


if __name__ == "__main__":
    generate_architecture_diagram()
    generate_project_timeline_excel()
    generate_week_01_project_plan_docx()
    generate_literature_review_docx()
    print("[SUCCESS] All Week 1 planning artifacts successfully generated.")
