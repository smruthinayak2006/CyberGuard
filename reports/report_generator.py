from pathlib import Path
from datetime import datetime

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.styles import (
    getSampleStyleSheet,
    ParagraphStyle
)

from reportlab.lib.units import inch

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    PageBreak
)


REPORTS_DIR = Path("reports")


# ------------------------------------------------------------
# Footer
# ------------------------------------------------------------

def add_page_number(canvas, document):

    canvas.saveState()

    canvas.setFont(
        "Helvetica",
        9
    )

    canvas.drawString(

        40,

        30,

        "CyberGuard v1.0 | Internal Use Only"

    )

    canvas.drawRightString(

        550,

        30,

        f"Page {document.page}"

    )

    canvas.restoreState()


# ------------------------------------------------------------
# Report
# ------------------------------------------------------------

def generate_report(scan):

    REPORTS_DIR.mkdir(
        exist_ok=True
    )

    timestamp = datetime.now().strftime(
        "%Y-%m-%d_%H-%M-%S"
    )

    report_path = REPORTS_DIR / (
        f"CyberGuard_Report_{timestamp}.pdf"
    )

    document = SimpleDocTemplate(

        str(report_path),

        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=50

    )

    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(

        "Title",

        parent=styles["Heading1"],

        alignment=TA_CENTER,

        fontSize=24,

        textColor=colors.HexColor("#0B3C5D"),

        spaceAfter=18

    )

    heading_style = ParagraphStyle(

        "Heading",

        parent=styles["Heading2"],

        textColor=colors.HexColor("#0B3C5D"),

        spaceAfter=10,

        spaceBefore=10

    )

    normal_style = styles["BodyText"]

    elements = []

    risk = scan["risk"]

    system = scan["system"]

    # ------------------------------------------------------------
    # Cover Page
    # ------------------------------------------------------------

    elements.append(

        Paragraph(

            "CyberGuard",

            title_style

        )

    )

    elements.append(

        Paragraph(

            "<b>Endpoint Security Assessment Report</b>",

            styles["Heading2"]

        )

    )

    elements.append(
        Spacer(1, 25)
    )

    cover = Table([

        ["Generated On", datetime.now().strftime("%d %B %Y %H:%M")],

        ["Hostname", system["hostname"]],

        ["Operating System", system["operating_system"]],

        ["IP Address", system["ip_address"]]

    ])

    cover.setStyle(

        TableStyle([

            ("GRID",(0,0),(-1,-1),1,colors.grey),

            ("BACKGROUND",(0,0),(0,-1),colors.HexColor("#0B3C5D")),

            ("TEXTCOLOR",(0,0),(0,-1),colors.white),

            ("BOTTOMPADDING",(0,0),(-1,-1),8),

            ("FONTNAME",(0,0),(0,-1),"Helvetica-Bold")

        ])

    )

    elements.append(
        cover
    )

    elements.append(
        Spacer(1,30)
    )

    metadata_table = Table([

        ["Report ID", f"CG-{datetime.now().strftime('%Y%m%d%H%M%S')}"],

        ["Generated On", datetime.now().strftime("%d %B %Y %H:%M")],
        
        ["Scan Duration", f"{scan.get('duration', 'N/A')} sec"],

        ["Report Version", "1.0"],

        ["Classification", "Internal Use Only"]

    ])

    metadata_table.setStyle(

        TableStyle([

            ("GRID", (0,0), (-1,-1), 1, colors.grey),

            ("BACKGROUND", (0,0), (0,-1), colors.HexColor("#0F4C75")),

            ("TEXTCOLOR", (0,0), (0,-1), colors.white),

            ("FONTNAME", (0,0), (-1,-1), "Helvetica-Bold"),

            ("BOTTOMPADDING", (0,0), (-1,-1), 8)

        ])

    )

    elements.append(metadata_table)

    elements.append(Spacer(1,20))

    # ------------------------------------------------------------
    # Executive Summary
    # ------------------------------------------------------------

    elements.append(

        Paragraph(

            "Executive Summary",

            heading_style

        )

    )

    summary = (

        "CyberGuard completed an endpoint security assessment "

        "covering operating system security, running processes, "

        "startup programs, file integrity monitoring and "

        "risk analysis."

    )

    elements.append(

        Paragraph(

            summary,

            normal_style

        )

    )

    elements.append(
        Spacer(1,20)
    )

    # ------------------------------------------------------------
    # Risk Summary
    # ------------------------------------------------------------

    risk_table = Table([

        ["Risk Score", f"{risk['score']} / 100"],

        ["Raw Score", risk["raw_score"]],

        ["Overall Risk", risk["level"]],

        ["Highest Severity", risk["highest_severity"]],

        ["Total Findings", risk["finding_count"]]

    ])

    risk_table.setStyle(

        TableStyle([

            ("GRID",(0,0),(-1,-1),1,colors.grey),

            ("BACKGROUND",(0,0),(0,-1),colors.HexColor("#0B3C5D")),

            ("TEXTCOLOR",(0,0),(0,-1),colors.white),

            ("BOTTOMPADDING",(0,0),(-1,-1),8),

            ("FONTNAME",(0,0),(0,-1),"Helvetica-Bold")

        ])

    )

    elements.append(

        Paragraph(

            "Risk Assessment",

            heading_style

        )

    )

    elements.append(
        risk_table
    )

    elements.append(

        Paragraph(

            "<b>Risk Interpretation</b>",

            styles["Heading2"]

        )

    )

    risk_text = (

        f"CyberGuard identified "

        f"<b>{risk['finding_count']}</b> security "

        f"finding(s) during this endpoint assessment. "

        f"The endpoint achieved a security score of "

        f"<b>{risk['score']}/100</b>, resulting in an "

        f"<b>{risk['level']}</b> overall security posture. "

        f"The highest severity observed during the assessment "

        f"was <b>{risk['highest_severity']}</b>. "

        "The identified findings may increase the endpoint's "

        "attack surface if left unresolved. It is recommended "

        "that HIGH and CRITICAL findings be remediated and the "

        "system be reassessed before deployment into a "

        "production environment."

    )

    elements.append(

        Paragraph(

            risk_text,

            styles["BodyText"]

        )

    )

    elements.append(Spacer(1,20))

    # ------------------------------------------------------------
    # Endpoint Information
    # ------------------------------------------------------------

    elements.append(

        Paragraph(

            "Endpoint Information",

            heading_style

        )

    )

    endpoint_table = Table([

        ["Hostname", system["hostname"]],

        ["Operating System", system["operating_system"]],

        ["OS Version", system["os_version"]],

        ["Architecture", system["architecture"]],

        ["CPU Usage", f"{system['cpu_usage']} %"],

        ["RAM Usage", f"{system['ram_usage']} %"],

        ["Disk Usage", f"{system['disk_usage']} %"]

    ])

    endpoint_table.setStyle(

        TableStyle([

            ("GRID",(0,0),(-1,-1),1,colors.grey),

            ("BACKGROUND",(0,0),(0,-1),colors.HexColor("#0B3C5D")),

            ("TEXTCOLOR",(0,0),(0,-1),colors.white),

            ("BOTTOMPADDING",(0,0),(-1,-1),8),

            ("FONTNAME",(0,0),(0,-1),"Helvetica-Bold")

        ])

    )

    elements.append(
        endpoint_table
    )

    elements.append(
        Spacer(1,20)
    )

    # ------------------------------------------------------------
    # Security Findings
    # ------------------------------------------------------------

    elements.append(

        Paragraph(

            "Security Findings",

            heading_style

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

                ("GRID",(0,0),(-1,-1),1,colors.grey),

                ("BACKGROUND",(0,0),(-1,0),colors.HexColor("#0B3C5D")),

                ("TEXTCOLOR",(0,0),(-1,0),colors.white),

                ("BOTTOMPADDING",(0,0),(-1,-1),8),

                ("ROWBACKGROUNDS",(0,1),(-1,-1),[

                    colors.whitesmoke,

                    colors.beige

                ])

            ])

        )

        elements.append(
            findings_table
        )

    else:

        elements.append(

            Paragraph(

                "No security findings detected.",

                normal_style

            )

        )

    

    # ------------------------------------------------------------
    # Detailed Findings
    # ------------------------------------------------------------

    elements.append(

        Paragraph(

            "Detailed Findings",

            heading_style

        )

    )

    if risk["findings"]:

        for finding in risk["findings"]:

            elements.append(

                Paragraph(

                    f"<b>{finding.finding_id} - {finding.title}</b>",

                    styles["Heading3"]

                )

            )

            elements.append(

                Paragraph(

                    f"<b>Severity:</b> {finding.severity}",

                    normal_style

                )

            )

            elements.append(

                Paragraph(

                    f"<b>Category:</b> {finding.category}",

                    normal_style

                )

            )

            elements.append(

                Paragraph(

                    f"<b>Module:</b> {finding.module}",

                    normal_style

                )

            )

            elements.append(

                Paragraph(

                    f"<b>Description:</b> {finding.description}",

                    normal_style

                )

            )

            elements.append(

                Paragraph(

                    f"<b>Recommendation:</b> {finding.recommendation}",

                    normal_style

                )

            )

            elements.append(
                Spacer(1, 14)
            )

    else:

        elements.append(

            Paragraph(

                "No security findings detected during this assessment.",

                normal_style

            )

        )

    

    # ------------------------------------------------
    # Recommendations
    # ------------------------------------------------

    elements.append(

        Paragraph(

            "<b>Security Recommendations</b>",

            styles["Heading2"]

        )

    )

    elements.append(Spacer(1, 10))

    if risk["findings"]:

        for index, finding in enumerate(

            risk["findings"],

            start=1

        ):

            recommendation_table = Table([

                ["Recommendation", str(index)],

                ["Finding", finding.title],

                ["Priority", finding.severity],

                ["Module", finding.module],

                ["Action", finding.recommendation]

            ])

            recommendation_table.setStyle(

                TableStyle([

                    ("GRID", (0, 0), (-1, -1), 1, colors.grey),

                    ("BACKGROUND", (0, 0), (0, -1), colors.HexColor("#0F4C75")),

                    ("TEXTCOLOR", (0, 0), (0, -1), colors.white),

                    ("FONTNAME", (0, 0), (-1, -1), "Helvetica-Bold"),

                    ("BOTTOMPADDING", (0, 0), (-1, -1), 8),

                    ("TOPPADDING", (0, 0), (-1, -1), 8),

                ])

            )

            elements.append(

                recommendation_table

            )

            elements.append(

                Spacer(1, 15)

            )

    else:

        elements.append(

            Paragraph(

                "No security recommendations available.",

                styles["BodyText"]

            )

        )

    elements.append(

        Spacer(1, 20)

    )

    # ------------------------------------------------
    # Assessment Summary
    # ------------------------------------------------

    elements.append(

        Paragraph(

            "<b>Assessment Summary</b>",

            styles["Heading2"]

        )

    )

    summary_table = Table([

        ["Assessment Tool", "CyberGuard"],

        ["Assessment Type", "Endpoint Security Assessment"],

        ["Generated", datetime.now().strftime("%d %B %Y %H:%M:%S")],

        ["Hostname", scan["system"]["hostname"]],

        ["Operating System", scan["system"]["operating_system"]],

        ["Risk Level", risk["level"]],

        ["Risk Score", f'{risk["score"]} / 100'],

        ["Findings", str(risk["finding_count"])]

    ])

    summary_table.setStyle(

        TableStyle([

            ("GRID", (0, 0), (-1, -1), 1, colors.grey),

            ("BACKGROUND", (0, 0), (0, -1), colors.HexColor("#0F4C75")),

            ("TEXTCOLOR", (0, 0), (0, -1), colors.white),

            ("FONTNAME", (0, 0), (-1, -1), "Helvetica-Bold"),

            ("BOTTOMPADDING", (0, 0), (-1, -1), 8),

        ])

    )

    elements.append(summary_table)

    elements.append(Spacer(1, 20))

    elements.append(
        Paragraph(
            "Disclaimer",
            heading_style
        )
    )

    elements.append(
        Paragraph(
            "This report was generated automatically by CyberGuard. "
            "The findings are based on the system state at the time of "
            "assessment and should be validated by a security analyst "
            "before making operational or compliance decisions.",
            normal_style
        )
    )

    elements.append(Spacer(1,20))

    elements.append(

        Paragraph(

            "<b>Generated by CyberGuard v1.0</b>",

            styles["Heading2"]

        )

    )

    elements.append(

        Paragraph(

            "Enterprise Endpoint Security Assessment Platform",

            styles["BodyText"]

        )

    )

    elements.append(

        Paragraph(

            "Classification: Internal Use Only",

            styles["BodyText"]

        )

    )

    elements.append(

        Paragraph(

            f"Report Generated: {datetime.now().strftime('%d %B %Y %H:%M:%S')}",

            styles["BodyText"]

        )

    )

    # ------------------------------------------------------------
    # Build PDF
    # ------------------------------------------------------------

    document.build(

        elements,

        onFirstPage=add_page_number,

        onLaterPages=add_page_number

    )

    return str(report_path)