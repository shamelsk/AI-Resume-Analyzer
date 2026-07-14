from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def create_report(analysis):

    doc = SimpleDocTemplate("Resume_Report.pdf")

    styles = getSampleStyleSheet()

    story = []

    story.append(Paragraph("<b>AI Resume Analysis Report</b>", styles["Title"]))

    story.append(
        Paragraph(
            f"<b>Overall Score:</b> {analysis['overall_score']}/100",
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph(
            f"<b>ATS Score:</b> {analysis['ats_score']}",
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph(
            f"<b>Skills Score:</b> {analysis['skills_score']}",
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph(
            f"<b>Projects Score:</b> {analysis['projects_score']}",
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph(
            f"<b>Experience Score:</b> {analysis['experience_score']}",
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph(
            f"<b>Education Score:</b> {analysis['education_score']}",
            styles["BodyText"]
        )
    )

    story.append(Paragraph("<br/><b>Strengths</b>", styles["Heading2"]))

    for item in analysis["strengths"]:
        story.append(Paragraph(f"• {item}", styles["BodyText"]))

    story.append(Paragraph("<br/><b>Weaknesses</b>", styles["Heading2"]))

    for item in analysis["weaknesses"]:
        story.append(Paragraph(f"• {item}", styles["BodyText"]))

    story.append(Paragraph("<br/><b>Missing Skills</b>", styles["Heading2"]))

    for item in analysis["missing_skills"]:
        story.append(Paragraph(f"• {item}", styles["BodyText"]))

    story.append(Paragraph("<br/><b>Suggestions</b>", styles["Heading2"]))

    for item in analysis["suggestions"]:
        story.append(Paragraph(f"• {item}", styles["BodyText"]))

    story.append(Paragraph("<br/><b>Recommended Roles</b>", styles["Heading2"]))

    for item in analysis["recommended_roles"]:
        story.append(Paragraph(f"• {item}", styles["BodyText"]))

    doc.build(story)

    return "Resume_Report.pdf"