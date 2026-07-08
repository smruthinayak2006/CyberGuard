from pathlib import Path
from datetime import datetime

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle
)

from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet


REPORTS_DIR = Path("reports")


def generate_report(scan):

    REPORTS_DIR.mkdir(exist_ok=True)

    timestamp = datetime.now().strftime(
        "%Y-%m-%d_%H-%M-%S"
    )

    report_path = REPORTS_DIR / (
        f"CyberGuard_Report_{timestamp}.pdf"
    )

    styles = getSampleStyleSheet()

    document = SimpleDocTemplate(
        str(report_path)
    )

    elements = []

    # ------------------------------------------------

    elements.append(

        Paragraph(

            "CyberGuard Security Assessment Report",

            styles["Heading1"]

        )

    )

    elements.append(Spacer(1, 20))

    # ------------------------------------------------

    elements.append(

        Paragraph(

            "<b>Executive Summary</b>",

            styles["Heading2"]

        )

    )

    elements.append(

        Paragraph(

            "This report summarizes the endpoint security assessment "
            "performed by CyberGuard.",

            styles["BodyText"]

        )

    )

    elements.append(Spacer(1, 20))

    # ------------------------------------------------

    endpoint_table = Table([

        ["Hostname", scan["system"]["hostname"]],

        ["IP Address", scan["system"]["ip_address"]],

        ["Operating System", scan["system"]["operating_system"]],

        ["CPU Usage", f'{scan["system"]["cpu_usage"]}%'],

        ["RAM Usage", f'{scan["system"]["ram_usage"]}%'],

        ["Disk Usage", f'{scan["system"]["disk_usage"]}%']

    ])

    endpoint_table.setStyle(

        TableStyle([

            ("GRID", (0, 0), (-1, -1), 1, colors.black),

            ("BACKGROUND", (0, 0), (0, -1), colors.lightgrey),

            ("BOTTOMPADDING", (0, 0), (-1, -1), 8)

        ])

    )

    elements.append(

        Paragraph(

            "<b>Endpoint Information</b>",

            styles["Heading2"]

        )

    )

    elements.append(endpoint_table)

    elements.append(Spacer(1, 20))

    # ------------------------------------------------

    risk = scan["risk"]

    risk_table = Table([

        ["Risk Score", risk["score"]],

        ["Raw Score", risk["raw_score"]],

        ["Risk Level", risk["level"]],

        ["Highest Severity", risk["highest_severity"]],

        ["Finding Count", risk["finding_count"]]

    ])

    risk_table.setStyle(

        TableStyle([

            ("GRID", (0, 0), (-1, -1), 1, colors.black),

            ("BACKGROUND", (0, 0), (0, -1), colors.lightgrey),

            ("BOTTOMPADDING", (0, 0), (-1, -1), 8)

        ])

    )

    elements.append(

        Paragraph(

            "<b>Risk Assessment</b>",

            styles["Heading2"]

        )

    )

    elements.append(risk_table)

    elements.append(Spacer(1, 20))

    # ------------------------------------------------

    elements.append(

        Paragraph(

            "<b>Security Findings</b>",

            styles["Heading2"]

        )

    )

    if risk["findings"]:

        rows = [[

            "ID",

            "Severity",

            "Module",

            "Title"

        ]]

        for finding in risk["findings"]:

            rows.append([

                finding.finding_id,

                finding.severity,

                finding.module,

                finding.title

            ])

        findings_table = Table(rows)

        findings_table.setStyle(

            TableStyle([

                ("GRID", (0, 0), (-1, -1), 1, colors.black),

                ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),

                ("BOTTOMPADDING", (0, 0), (-1, -1), 8)

            ])

        )

        elements.append(findings_table)

    else:

        elements.append(

            Paragraph(

                "No security findings detected.",

                styles["BodyText"]

            )

        )

    elements.append(Spacer(1, 20))

    # ------------------------------------------------

    elements.append(

        Paragraph(

            "<b>Recommendations</b>",

            styles["Heading2"]

        )

    )

    if risk["findings"]:

        for finding in risk["findings"]:

            elements.append(

                Paragraph(

                    f"• {finding.recommendation}",

                    styles["BodyText"]

                )

            )

    else:

        elements.append(

            Paragraph(

                "No recommendations available.",

                styles["BodyText"]

            )

        )

    document.build(elements)

    return str(report_path)