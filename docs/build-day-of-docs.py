"""Build CPPUG day-of documents (cppug-brand). Usage: python build.py <docs_dir> <img_dir>"""
import sys, os, json, yaml, qrcode
from docx import Document
from docx.shared import Pt, RGBColor, Inches, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.enum.section import WD_ORIENT
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

OUT, IMG = sys.argv[1], sys.argv[2]
# Internal (not public): check-in sheet and judge sheet carry phone numbers and judging detail
INTERNAL = sys.argv[3] if len(sys.argv) > 3 else OUT
# Host phone numbers stay out of the public repo: read them from hosts.json in the internal folder
# Format: [["Name", "phone"], ...]
_hosts = os.path.join(INTERNAL, "hosts.json")
HOSTS = json.load(open(_hosts, encoding="utf-8")) if os.path.exists(_hosts) else [["[HOST NAME]", "[PHONE]"]] * 3
FORM = "https://forms.cloud.microsoft/r/B4kKv3YLdp"
SITE = "https://ryley-bauer.github.io/cppug-hackathon/"

BLACK = RGBColor(0, 0, 0); WHITE = RGBColor(0xFF, 0xFF, 0xFF)
ACC = ["91338C", "5086F2", "4940AF", "EBCC45", "7DCF81", "8ED0F8"]
DARK_TEXT = {"EBCC45", "7DCF81", "8ED0F8"}

# QR code
qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=20, border=2)
qr.add_data(FORM); qr.make(fit=True)
QR = os.path.join(IMG, "checkin-qr.png")
qr.make_image(fill_color="black", back_color="white").save(QR)


def new_doc(landscape=False):
    d = Document()
    s = d.sections[0]
    s.page_width, s.page_height = Inches(8.5), Inches(11)
    if landscape:
        s.orientation = WD_ORIENT.LANDSCAPE
        s.page_width, s.page_height = Inches(11), Inches(8.5)
    for m in ("left_margin", "right_margin"):
        setattr(s, m, Inches(0.6))
    s.top_margin = s.bottom_margin = Inches(0.4); s.footer_distance = Inches(0.25)
    st = d.styles["Normal"]
    st.font.name = "Open Sans"; st.font.size = Pt(10)
    st.element.rPr.rFonts.set(qn("w:eastAsia"), "Open Sans")
    st.paragraph_format.space_after = Pt(3)
    st.paragraph_format.line_spacing = 1.05
    footer = s.footer.paragraphs[0]
    r = footer.add_run("CPPUG  |  communityleader@cppug.onmicrosoft.com  |  " + SITE.replace("https://", ""))
    r.font.size = Pt(8)
    return d


def shade(el_pr, fill):
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear"); shd.set(qn("w:color"), "auto"); shd.set(qn("w:fill"), fill)
    el_pr.append(shd)


def run(p, text, size=10, bold=False, color=BLACK, font="Open Sans", italic=False):
    r = p.add_run(text)
    r.font.name = font; r.font.size = Pt(size); r.font.bold = bold; r.font.italic = italic
    r.font.color.rgb = color
    r._element.rPr.rFonts.set(qn("w:eastAsia"), font)
    return r


def banner(d, title, subtitle):
    p = d.add_paragraph(); shade(p._p.get_or_add_pPr(), "000000")
    p.paragraph_format.space_after = Pt(0)
    run(p, " " + title, 30, font="Norwester", color=WHITE)
    p = d.add_paragraph(); shade(p._p.get_or_add_pPr(), "000000")
    p.paragraph_format.space_after = Pt(8)
    run(p, "  " + subtitle, 11, color=WHITE)


def h(d, text, i, size=12, before=5):
    p = d.add_paragraph(); p.paragraph_format.space_before = Pt(before); p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.keep_with_next = True
    run(p, text, size, bold=True, color=RGBColor.from_string("4940AF" if ACC[i % 6] in DARK_TEXT else ACC[i % 6]))
    return p


def para(d, parts, size=9, after=2):
    """parts: list of (text, bold) or a str."""
    p = d.add_paragraph(); p.paragraph_format.space_after = Pt(after)
    if isinstance(parts, str):
        parts = [(parts, False)]
    for t, b in parts:
        run(p, t, size, bold=b)
    return p


def bullet(d, parts, size=9):
    p = para(d, parts, size, after=1)
    p.style = d.styles["List Bullet"]
    return p


def table(d, rows, widths, accent, size=9, header=True, height=None):
    t = d.add_table(rows=len(rows), cols=len(widths))
    t.style = d.styles["Table Grid"]; t.alignment = WD_TABLE_ALIGNMENT.CENTER
    t.autofit = False
    fill = ACC[accent % 6]
    for i, row in enumerate(rows):
        tr = t.rows[i]
        if height:
            tr.height = height
        for j, txt in enumerate(row):
            c = tr.cells[j]; c.width = widths[j]
            p = c.paragraphs[0]; p.paragraph_format.space_after = Pt(1)
            p.paragraph_format.keep_with_next = i < len(rows) - 1  # keep each table on one page
            hdr = header and i == 0
            if hdr:
                shade(c._tc.get_or_add_tcPr(), fill)
            col = (BLACK if fill in DARK_TEXT else WHITE) if hdr else BLACK
            bold_first = (not header or i > 0) and j == 0 and len(widths) == 2
            run(p, txt, size, bold=hdr or bold_first, color=col)
    for j, w in enumerate(widths):
        for cell in t.columns[j].cells:
            cell.width = w
    return t


def page_break(d):
    d.add_paragraph().add_run().add_break(WD_BREAK.PAGE)


# ---------------------------------------------------------------- 1. Logistics
d = new_doc()
banner(d, "Know before you go", "CPPUG Power Platform Hackathon  |  Saturday, October 10, 2026  |  9:00 AM to 4:00 PM")
para(d, "CPPUG means Calgary Power Platform User Group. How to get there, get in, and what to bring. Rules and scoring are in the Participant Handout.")

h(d, "Where", 0)
para(d, [("Microsoft Calgary Office, 110 9 Ave SW, Calgary. ", True),
         ("It is in the Le Germain office tower, across 9 Avenue from the Calgary Tower.", False)])

h(d, "Getting in (the building is locked on Saturday)", 1)
bullet(d, [("Doors open at 9:00 AM. ", True), ("Wait in the main lobby of 110 9 Ave SW. A volunteer meets you and brings you up in the elevator.", False)])
bullet(d, [("Running late? ", True), ("Send David a message in the Meetup event chat. Someone comes down to get you.", False)])
bullet(d, [("Washrooms are in the hallway outside the office. ", True), ("The office door locks behind you. Tell a volunteer before you step out so we can let you back in.", False)])

h(d, "Parking and transit", 2)
table(d, [
    ["Option", "Where", "Cost (estimate, check the sign)"],
    ["Brookfield Place underground, Lot #35", "225 6 Ave SW, about 3 blocks north", "About $3.15 for 24 hours on the weekend"],
    ["Surface lot", "208 9 Ave SW, about 1 block west", "About $5 to $15 for the day"],
    ["CTrain", "7 Avenue stations at Centre Street or 1 Street SW, a 5 minute walk", "Regular Calgary Transit fare"],
], [Inches(2.3), Inches(3.2), Inches(1.8)], 2, size=8.5)

h(d, "Check in", 3)
para(d, [("Scan the QR code at the door, or fill in the registration form tonight: ", False), (FORM, True),
         (". It takes about two minutes. At check-in we ask your Power Platform skill level (1 to 5) so we can build balanced teams. "
          "No team? We match you. Can't use the form? Sign the paper sheet at the desk.", False)])

h(d, "What to bring", 4)
bullet(d, [("A laptop and a charger. ", True), ("Outlets are shared, so a short power bar helps.", False)])
bullet(d, [("A Power Platform environment. ", True),
           ("Use your work or school environment only if your organization allows it. No environment? Sign up tonight for the free "
            "Power Apps Developer Plan (aka.ms/PowerAppsDevPlan). Organizers have a backup lab for anyone who has nothing.", False)])
bullet(d, [("An idea, or none. ", True), ("Pick one of our prepared challenges (see the Challenge Case Studies) or bring your own.", False)])

h(d, "In the room", 5)
bullet(d, [("Food: ", True), ("breakfast and lunch are provided, and coffee is on site. Tell us at check-in about any dietary needs.", False)])
bullet(d, [("Wi-Fi: ", True), ("guest Wi-Fi details will be on the whiteboard. A backup hotspot is available.", False)])
bullet(d, [("Help: ", True), ("mentors walk the room all day. Ask early. Experienced builders are welcome to help other teams too.", False)])
bullet(d, [("Photos: ", True), ("we photograph the demos and the closing. Tell a volunteer if you prefer not to appear.", False)])

h(d, "Schedule", 0)
table(d, [
    ["Time", "What happens", "Time", "What happens"],
    ["9:00 AM", "Doors open, check-in, team matching", "1:45 to 2:00 PM", "Stop building. Hand in your team summary card"],
    ["9:30 to 9:55 AM", "Welcome, rules, challenge briefing", "2:00 to 3:15 PM", "Team demos"],
    ["10:00 AM", "Build starts. Plan and sketch for 30 minutes first", "3:15 to 3:40 PM", "Judges score. Everyone networks"],
    ["12:30 PM", "Lunch. Keep building if you like", "3:40 to 4:00 PM", "Awards, photos, and closing"],
], [Inches(1.15), Inches(2.5), Inches(1.15), Inches(2.5)], 1, size=8.5)

para(d, [("Prizes. ", True), ("Two PPCC26 (Power Platform Community Conference 2026) passes from Microsoft, and Lego Clippy mascots. "
          "A pass covers the conference only. Winners book their own flights and hotel within about a week.", False)], size=9).paragraph_format.space_before = Pt(6)
d.save(os.path.join(OUT, "CPPUG Hackathon - Know Before You Go.docx"))

# ---------------------------------------------------------------- 2. Check-in sheet
def hosts(d, size=10):
    """One-row contact strip for the organizers on duty."""
    t = d.add_table(rows=1, cols=len(HOSTS) + 1); t.alignment = WD_TABLE_ALIGNMENT.CENTER
    cells = t.rows[0].cells
    shade(cells[0]._tc.get_or_add_tcPr(), ACC[2])
    run(cells[0].paragraphs[0], "Need anything? Call or text a host", size, bold=True, color=WHITE)
    for c, (n, ph) in zip(cells[1:], HOSTS):
        shade(c._tc.get_or_add_tcPr(), "F5F5F5")
        run(c.paragraphs[0], n, size, bold=True); c.paragraphs[0].add_run().add_break(); run(c.paragraphs[0], ph, size)
    return t


d = new_doc()
banner(d, "Check in here", "CPPUG Power Platform Hackathon  |  Saturday, October 10, 2026")
hosts(d)
p = d.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER; p.paragraph_format.space_before = Pt(18)
run(p, "Scan with your phone camera", 22, bold=True)
p = d.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
p.add_run().add_picture(QR, width=Inches(4.5))
p = d.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
run(p, FORM, 14, bold=True)
p = d.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER; p.paragraph_format.space_before = Pt(12)
run(p, "Takes about two minutes. Already registered? Just tell us your name.", 13)
p = d.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
run(p, "No phone, or the form won't load? Sign the paper sheet and fill in a check-in slip.", 13)

# page 2: paper sign-in sheet (landscape)
sec = d.add_section()
sec.orientation = WD_ORIENT.LANDSCAPE; sec.page_width, sec.page_height = Inches(11), Inches(8.5)
p = sec.header.paragraphs[0]
h(d, "Paper sign-in sheet (backup if the form is down)", 0, size=16, before=0)
hosts(d, 9)
para(d, "Everyone signs here, even if you used the form. Role: C = competitor with a team, F = free agent (match me), "
        "V = volunteer, S = spectator, M = mentor or judge. Skill: 1 = brand new, 5 = expert. PPCC26: if you win a pass, could you book flights and hotel within 7 days? Did not do the form? Also fill in a check-in slip.", size=9)
rows = [["#", "Name (as on your name tag)", "Role (C F V S M)", "Team name (blank if solo)", "Skill 1 to 5", "Laptop? Y / N", "Form done? Y / N", "Photos OK? Y / N", "PPCC26 travel in 7 days? Y / N"]]
rows += [[str(i), "", "", "", "", "", "", "", ""] for i in range(1, 17)]
table(d, rows, [Inches(0.4), Inches(2.4), Inches(1.0), Inches(1.8), Inches(0.8), Inches(0.8), Inches(0.8), Inches(0.9), Inches(0.9)], 1, size=9, height=Cm(0.78))

# page 3: check-in slips (portrait), 4 per page
sec = d.add_section()
sec.orientation = WD_ORIENT.PORTRAIT; sec.page_width, sec.page_height = Inches(8.5), Inches(11)
SLIP = [
    ("Name", ""), ("Email (for team updates only)", ""),
    ("Role", "Competitor with a team  /  Free agent  /  Volunteer  /  Spectator"),
    ("Team name and teammates", ""),
    ("Skill 1 to 5", "1 brand new   2 beginner   3 intermediate   4 advanced   5 expert"),
    ("Strongest in", "Apps  /  Automate  /  BI  /  Copilot Studio  /  Pages  /  Dataverse  /  None yet"),
    ("Dietary needs", "None  /  Vegetarian  /  Vegan  /  Halal  /  Gluten-free  /  Nut allergy  /  Other:"),
    ("Could you book PPCC26 travel and hotel within 7 days if you win?", "Yes  /  No"),
    ("Photos and video OK?", "Yes  /  Please avoid me"),
]
for n in range(2):
    h(d, "Check-in slip (fill in if you did not use the form)", 3, size=11, before=0 if n == 0 else 14)
    table(d, SLIP, [Inches(2.4), Inches(4.9)], 0, size=8.5, header=False, height=Cm(0.95))
    p = para(d, "Hand this slip to a volunteer. It is private: only organizers see it, and we enter it into the form after check-in.", size=8)
    if n == 0:
        p = d.add_paragraph(); run(p, "- - - - - - - - - - - - - - - - - - - - - - - cut here - - - - - - - - - - - - - - - - - - - - - - -", 8)
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
d.save(os.path.join(INTERNAL, "CPPUG Hackathon - Check-in Sheet.docx"))

# ---------------------------------------------------------------- 3. Case studies
# Shared with the website: _data/challenges.yml
_repo = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) if os.path.basename(os.path.dirname(os.path.abspath(__file__))) == "docs" else os.getcwd()
CASES = [tuple(c[k] for k in ("name", "scenario", "users", "starter", "stretch", "data", "tools"))
         for c in yaml.safe_load(open(os.path.join(_repo, "_data", "challenges.yml"), encoding="utf-8"))]
d = new_doc()
banner(d, "Challenge case studies", "CPPUG Power Platform Hackathon  |  Saturday, October 10, 2026")
para(d, "Pick one of these prepared challenges, or choose Open Build and bring your own idea. Each one fits a four-hour build. "
        "Build the starter version first. Add stretch ideas only when the starter works. Judges score the core features you list on your team "
        "summary card, so pick 3 you can finish.")
for i, (name, scen, users, mvp, stretch, data, tools) in enumerate(CASES):
    h(d, f"{i + 1}. {name}", i, size=12, before=6)
    table(d, [["Scenario", scen], ["Users", users], ["Starter build (MVP)", mvp], ["Stretch ideas", stretch],
              ["Suggested data", data], ["Likely tools", tools]],
          [Inches(1.6), Inches(5.7)], i, size=8.5, header=False)
para(d, [("Tip. ", True), ("Start with sample data. Ten realistic rows make a better demo than an empty app. "
          "AI tools, Microsoft Learn, and search are all allowed. Tell the judges what you used.", False)], size=9).paragraph_format.space_before = Pt(8)
d.save(os.path.join(OUT, "CPPUG Hackathon - Challenge Case Studies.docx"))

# ---------------------------------------------------------------- 4. Team summary card
d = new_doc()
CARD = [("Team name", ""), ("Members", ""), ("Challenge", "Inventory / Time Off / Inspection / Expense / Booking / Kudos / Open Build"),
        ("Problem (one sentence: what, and for whom?)", ""), ("How we chose it (which other ideas did we weigh?)", ""),
        ("Plan (what did we sketch before building?)", ""), ("Core feature 1", ""), ("Core feature 2", ""), ("Core feature 3", ""),
        ("Power Platform parts used", "")]
for n in range(2):
    h(d, "Team summary card. Hand in by 1:45 PM", 0, size=14, before=0 if n == 0 else 10)
    para(d, "Judges score your demo against this card. Functionality is scored on the core features you list here.", size=8.5)
    table(d, CARD, [Inches(2.6), Inches(4.7)], 0, size=9, header=False, height=Cm(0.95))
    if n == 0:
        p = d.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run(p, "- - - - - - - - - - - - - - - - - - - - - - - cut here - - - - - - - - - - - - - - - - - - - - - - -", 8)
d.save(os.path.join(OUT, "CPPUG Hackathon - Team Summary Card.docx"))
# ---------------------------------------------------------------- 5. Judge score sheet (paper backup)
d = new_doc(landscape=True)
d.sections[0].left_margin = d.sections[0].right_margin = Inches(0.5)
banner(d, "Judge score sheet", "Paper backup for the Judge Form  |  CPPUG Power Platform Hackathon  |  October 10, 2026")
para(d, [("Judge name: ______________________________     ", True),
         ("Score each criterion with a whole number from 1 to 5. Score alone and do not discuss scores until all are in. "
          "Skip any team you have a conflict with (you work with, manage, or coached a member). Judge what works live, against the team summary card.", False)], size=8.5)
RUB = [
    ["Criterion", "5", "4", "3", "2", "1"],
    ["Functionality: 30%, score x 6", "All listed core features work live, no errors, plus one edge case handled well",
     "All listed core features work live. One small glitch at most", "Most core features work (for example 2 of 3). Some bugs",
     "Fewer than half work (for example 1 of 3). Needs workarounds", "No core feature works, or the demo fails"],
    ["Effective use of Power Platform: 35%, score x 7", "3+ parts work together. Team explains each choice. Uses a platform strength (approvals, shared data, connector, AI)",
     "3+ parts work together and each fits the problem", "2 parts, both fit the problem (for example an app plus a flow)",
     "1 part with basic use, or 2 parts where one does not fit", "No Power Platform part is central, or the tools do not fit"],
    ["Design and user experience: 25%, score x 5", "All 5 items shown: A Idea (how they chose it), B Plan (sketch before building), C Match (screens follow plan), D Use (new user finishes main task alone), E Polish (consistent, readable)",
     "4 of the 5 items", "3 of the 5 items", "2 of the 5 items", "1 item, or none"],
    ["Presentation quality: 10%, score x 2", "All 4 parts (problem, live demo, parts used, what they learned), on time, clear answers",
     "All 4 parts, on time. Answers adequate", "3 of the 4 parts", "2 of the 4 parts, or cannot answer most questions", "1 part or none"],
]
table(d, RUB, [Inches(1.5), Inches(2.6), Inches(1.6), Inches(1.5), Inches(1.4), Inches(1.4)], 0, size=7)
p = para(d, "", size=4)
SC = [["#", "Team name", "Conflict? (skip)", "Function 1 to 5 (x 6)", "Effective use 1 to 5 (x 7)", "Design 1 to 5 (x 5)  circle A B C D E",
       "Present. 1 to 5 (x 2)", "Total points (max 100)", "Standout member for a pass, and notes"]]
SC += [[str(i), "", "", "", "", "A  B  C  D  E", "", "", ""] for i in range(1, 11)]
table(d, SC, [Inches(0.3), Inches(1.7), Inches(0.75), Inches(0.85), Inches(0.85), Inches(1.35), Inches(0.8), Inches(0.9), Inches(2.5)], 1, size=7.5, height=Cm(0.82))
para(d, [("Total = Function x 6 + Effective use x 7 + Design x 5 + Presentation x 2. ", True),
         ("Hand this sheet to an organizer when demos end. Organizers average the totals. Ties: higher Effective use points, then Functionality points, then the judges decide. "
          "Passes are placed after scoring, from the pass-eligible list.", False)], size=8)
d.save(os.path.join(INTERNAL, "CPPUG Hackathon - Judge Score Sheet (paper backup).docx"))
print("built")
