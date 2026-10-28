"""Generate a clean, ATS-friendly CV PDF from the portfolio data."""
from reportlab.lib import colors
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import (
    BaseDocTemplate, Frame, PageTemplate, Paragraph, Spacer, Table, TableStyle,
    KeepTogether, HRFlowable,
)

ACCENT = colors.HexColor("#4c3fd6")
ACCENT_SOFT = colors.HexColor("#6d5efc")
INK = colors.HexColor("#10162e")
MUTED = colors.HexColor("#4d5877")
LINE = colors.HexColor("#d8dcE9")

OUT = "assets/Md-Nizam-Uddin-Tuhin-CV.pdf"

ss = getSampleStyleSheet()
S = {}
S["name"] = ParagraphStyle("name", fontName="Helvetica-Bold", fontSize=21, leading=24,
                           textColor=INK, spaceAfter=2)
S["role"] = ParagraphStyle("role", fontName="Helvetica-Bold", fontSize=10.5, leading=14,
                           textColor=ACCENT, spaceAfter=5)
S["contact"] = ParagraphStyle("contact", fontName="Helvetica", fontSize=8.6, leading=12,
                              textColor=MUTED)
S["h2"] = ParagraphStyle("h2", fontName="Helvetica-Bold", fontSize=10, leading=12,
                         textColor=ACCENT, spaceBefore=9, spaceAfter=3)
S["body"] = ParagraphStyle("body", fontName="Helvetica", fontSize=8.8, leading=12.4,
                           textColor=INK, alignment=TA_JUSTIFY)
S["bullet"] = ParagraphStyle("bullet", parent=S["body"], fontSize=8.7, leading=12,
                             leftIndent=9, bulletIndent=1, spaceAfter=1.4)
S["job"] = ParagraphStyle("job", fontName="Helvetica-Bold", fontSize=9.6, leading=12, textColor=INK)
S["jobmeta"] = ParagraphStyle("jobmeta", fontName="Helvetica-Oblique", fontSize=8.4, leading=11,
                              textColor=MUTED)
S["small"] = ParagraphStyle("small", fontName="Helvetica", fontSize=8.2, leading=11, textColor=MUTED)


def rule(space_before=1, space_after=4):
    return HRFlowable(width="100%", thickness=0.7, color=LINE,
                      spaceBefore=space_before, spaceAfter=space_after)


def bullets(items):
    return [Paragraph(t, S["bullet"], bulletText="•") for t in items]


def heading(text):
    return Paragraph(text.upper(), S["h2"])


def job(title, company, meta, items, stack=None):
    block = [
        Paragraph(title, S["job"]),
        Paragraph(f"{company} &nbsp;|&nbsp; {meta}", S["jobmeta"]),
        Spacer(1, 2.5),
    ]
    block += bullets(items)
    if stack:
        block.append(Paragraph(f"<font color='#4d5877'>Tech:</font> {stack}", S["small"]))
    block.append(Spacer(1, 4))
    return KeepTogether(block)


story = []

# ---------- Header ----------
story.append(Paragraph("MD. NIZAM UDDIN TUHIN", S["name"]))
story.append(Paragraph("Software Engineer &nbsp;·&nbsp; .NET &amp; Angular &nbsp;·&nbsp; ERP Systems Specialist", S["role"]))
story.append(Paragraph(
    "27 Link Road, Banglamotor, Dhaka &nbsp;·&nbsp; +880 1580 816671, +880 1767 915221 &nbsp;·&nbsp; "
    "<link href='mailto:nizamddin2001@gmail.com' color='#4c3fd6'>nizamddin2001@gmail.com</link><br/>"
    "<link href='https://nizambhl2001.github.io/' color='#4c3fd6'>nizambhl2001.github.io</link> &nbsp;·&nbsp; "
    "<link href='https://www.linkedin.com/in/nizambhl2001' color='#4c3fd6'>linkedin.com/in/nizambhl2001</link> &nbsp;·&nbsp; "
    "<link href='https://github.com/nizambhl2001' color='#4c3fd6'>github.com/nizambhl2001</link>",
    S["contact"]))
story.append(rule(6, 2))

# ---------- Summary ----------
story.append(heading("Professional Summary"))
story.append(Paragraph(
    "Motivated and results-driven .NET Software Engineer with <b>3.6+ years</b> of hands-on experience "
    "developing and maintaining ERP systems using .NET Core, Angular and MS SQL Server. Experienced in "
    "clean architecture (CQRS, Repository, Unit of Work), JWT-secured REST APIs, query optimisation and "
    "responsive UI development. Recognised for delivering scalable, high-quality solutions, quickly "
    "adapting to emerging technologies and collaborating effectively within agile teams.",
    S["body"]))

# ---------- Skills ----------
story.append(heading("Technical Skills"))
skills = [
    ("Backend", "C#, ASP.NET Core, ASP.NET Core MVC, Web API / REST, JWT Authentication, Entity Framework Core, Dapper, LINQ, CQRS, Repository &amp; Unit of Work"),
    ("Frontend", "Angular 2+, TypeScript, JavaScript, PrimeNG, Material UI, Bootstrap 5, Tailwind CSS, HTML5, CSS3"),
    ("Database", "MS SQL Server — stored procedures, triggers, views, functions, query optimisation"),
    ("Tools", "Git, GitHub, Serilog, Redis, RDLC &amp; Crystal Reports, Visual Studio, VS Code"),
    ("Other", "Data Structures &amp; Algorithms, Node.js (basic), C/C++, OOP &amp; OOD"),
]
rows = [[Paragraph(f"<b>{k}</b>", S["body"]), Paragraph(v, S["body"])] for k, v in skills]
t = Table(rows, colWidths=[22 * mm, 148 * mm])
t.setStyle(TableStyle([
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("LEFTPADDING", (0, 0), (-1, -1), 0),
    ("RIGHTPADDING", (0, 0), (-1, -1), 2),
    ("TOPPADDING", (0, 0), (-1, -1), 1.5),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 1.5),
]))
story.append(t)

# ---------- Experience ----------
story.append(heading("Professional Experience"))
story.append(Paragraph("<b>Total experience: 3.6 years</b>", S["small"]))
story.append(Spacer(1, 3))
story.append(job(
    "Software Engineer", "Pioneer Group BD, Extension Pallabi, Dhaka",
    "15 Jun 2025 – Present (1.4 yrs)",
    [
        "Develop and maintain ERP software using <b>.NET 10</b>, Angular and MS SQL Server.",
        "Design and implement RESTful APIs with secure JWT authentication.",
        "Manage database operations including stored procedures, triggers and views.",
        "Build responsive, user-friendly UI using Angular, PrimeNG, Tailwind CSS and Bootstrap.",
        "Apply CQRS, Repository and Unit of Work patterns for scalable architecture.",
        "Ensure code quality, version control with Git and structured logging with Serilog.",
        "Implement caching with Redis and generate business reports using RDLC.",
    ],
    ".NET 10, Angular, Web API, SQL Server, Redis, Serilog, RDLC"))

story.append(job(
    "Junior Software Engineer", "Software Arena Limited, Banglamotor, Dhaka",
    "01 Sep 2023 – 14 Jun 2025 (1.8 yrs)",
    [
        "Developed and maintained ERP software ensuring high-quality, scalable solutions.",
        "Designed and implemented software in collaboration with the team.",
        "Created RESTful APIs using ASP.NET Core Web API.",
        "Handled SQL Server operations including stored procedures, views, triggers and functions.",
        "Built responsive UI using Angular, JavaScript, TypeScript and Bootstrap.",
        "Maintained version control using Git and ensured a clean codebase.",
        "Generated business reports using Crystal Reports.",
    ],
    "ASP.NET Core, Angular, TypeScript, SQL Server, Crystal Reports, Git"))

story.append(job(
    "Software Engineer (Internship)", "US Software Limited, Green Road, Panthapath, Dhaka",
    "01 May 2023 – 31 Aug 2023 (0.3 yrs)",
    [
        "Assisted in designing, developing and maintaining web applications with ASP.NET, C# and Angular.",
        "Collaborated with senior developers to understand requirements and specifications.",
        "Wrote clean, efficient, well-documented code following coding standards and best practices.",
        "Tested and debugged web applications, identifying and resolving defects.",
        "Completed assigned tasks within deadlines, managing time and priorities effectively.",
    ],
    "C#, ASP.NET, Angular, SQL Server"))

# ---------- Projects ----------
story.append(heading("Projects"))
projects = [
    ("Human Resource Management System", ".NET Core &amp; Angular",
     "HRM system streamlining employee management, leave applications and shift scheduling, with "
     "multi-level approvals and email notifications. Built with OOP/OOD, CQRS, Dapper, stored procedures, "
     "views and functions for high performance and scalability.",
     "github.com/nizamuddintuhin/Human_Management_System"),
    ("Sales Invoice Management System", "ASP.NET MVC &amp; AJAX",
     "Single-page CRUD web application featuring master–detail data representation in real time without "
     "full-page reloads, delivering a smooth and responsive user experience.",
     "github.com/nizamuddintuhin/MVC-Ajax-Single-Page-CURD-with-MasterDetails"),
    ("Real-time Chat Application", "Node.js, Express &amp; Socket.io",
     "Real-time chat application allowing users to communicate instantly through the browser, with live "
     "socket events and a development setup that reloads without restarting the server.",
     "github.com/nizamuddintuhin/Node.js-Chat-App"),
]
for name, tech, desc, url in projects:
    story.append(KeepTogether([
        Paragraph(f"{name} &nbsp;<font size=8 color='#4d5877'>— {tech}</font>", S["job"]),
        Paragraph(desc, S["body"]),
        Paragraph(f"<link href='https://{url}' color='#4c3fd6'>{url}</link>", S["small"]),
        Spacer(1, 4),
    ]))

# ---------- Education ----------
story.append(heading("Education"))
edu = [
    ("Bachelor of Science (BSc) in Computer Science &amp; Engineering", "Sonargaon University",
     "2022 – 2027 (appeared)"),
    ("Diploma in Engineering, Computer Technology", "Bhola Polytechnic Institute",
     "2017 – 2021 · Result 3.77 / 4.00"),
    ("Secondary School Certificate (Science)", "Bhola Govt. High School", "2017 · Result 4.45 / 5.00"),
]
for title, inst, meta in edu:
    story.append(KeepTogether([
        Paragraph(title, S["job"]),
        Paragraph(f"{inst} &nbsp;|&nbsp; {meta}", S["jobmeta"]),
        Spacer(1, 2.5),
    ]))

# ---------- Training & certification ----------
story.append(heading("Training &amp; Certification"))
certs = [
    ("Web Application Development Using ASP.NET (WADA) — IsDB-BISEW IT Scholarship Program",
     "22 Nov 2022 – 28 May 2023 · 6 months"),
    ("Industrial Training: Web Design &amp; Development — Open IT", "2022 · 3 months"),
]
for title, meta in certs:
    story.append(KeepTogether([
        Paragraph(title, S["job"]),
        Paragraph(meta, S["jobmeta"]),
        Spacer(1, 2.5),
    ]))

# ---------- Additional ----------
story.append(heading("Additional Information"))
story.append(Paragraph(
    "<b>Preferred job category:</b> Engineer/Architect, IT/Telecommunication, Research/Consultancy &nbsp;·&nbsp; "
    "<b>Preferred location:</b> Dhaka, Gazipur (open to remote)<br/>"
    "<b>Languages:</b> Bangla (reading/writing/speaking — high), English (reading/writing — high, speaking — medium)<br/>"
    "<b>Extra-curricular:</b> MS Office, Photoshop, Illustrator, network troubleshooting, "
    "computer hardware &amp; software setup and service<br/>"
    "<b>Personal:</b> Father — Md. Mohe Uddin; Mother — Fardaus Begum; DOB 01 Jan 2001; "
    "Male; Single; Bangladeshi; Blood group B+",
    S["body"]))

# ---------- Reference ----------
story.append(heading("Reference"))
story.append(Paragraph(
    "<b>Syed Zahidul Hassan</b> — Project Consultant, IsDB-BISEW IT Scholarship Program<br/>"
    "Mirpur, Dhaka, Bangladesh &nbsp;·&nbsp; +880 1817 015015 &nbsp;·&nbsp; "
    "<link href='mailto:zahid@showtellconsulting.com' color='#4c3fd6'>zahid@showtellconsulting.com</link> "
    "&nbsp;·&nbsp; Professional relation",
    S["body"]))


def on_page(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(LINE)
    canvas.setLineWidth(0.6)
    canvas.line(doc.leftMargin, 14 * mm, A4[0] - doc.rightMargin, 14 * mm)
    canvas.setFont("Helvetica", 7.4)
    canvas.setFillColor(MUTED)
    canvas.drawString(doc.leftMargin, 10 * mm, "Md. Nizam Uddin Tuhin — Curriculum Vitae")
    canvas.drawRightString(A4[0] - doc.rightMargin, 10 * mm, f"nizambhl2001.github.io  ·  Page {doc.page}")
    canvas.restoreState()


doc = BaseDocTemplate(OUT, pagesize=A4,
                      leftMargin=20 * mm, rightMargin=20 * mm,
                      topMargin=15 * mm, bottomMargin=19 * mm,
                      title="Md. Nizam Uddin Tuhin — CV",
                      author="Md. Nizam Uddin Tuhin",
                      subject="Curriculum Vitae — .NET & Angular Software Engineer")
frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="main")
doc.addPageTemplates([PageTemplate(id="cv", frames=[frame], onPage=on_page)])
doc.build(story)
print("written:", OUT)
