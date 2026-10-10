"""Build the CPPUG hackathon print documents (cppug-brand).

Usage, from the repo root:
    python docs/build-day-of-docs.py <work_dir> [hosts.json]

Writes three Word files to <work_dir> (a scratch folder, not the repo):
  - CPPUG Hackathon - Participant Pack.docx   public, 6 pages, duplex
  - ... Participant Pack (print, with host numbers).docx   same pack with host phone numbers (only with hosts.json)
  - CPPUG Hackathon - Check-in Sheet.docx      internal, lists organizer phone numbers
  - CPPUG Hackathon - Volunteer and Judge Pack.docx   public, 3 pages (volunteer guide, judge guide, score sheet)
  - ... Volunteer and Judge Pack (print, with host numbers).docx   same pack with host phone numbers at the top (only with hosts.json)
and the check-in QR code to assets/images/checkin-qr.png.
Export each one to PDF from Word. The pack PDF goes to assets/downloads/ and the
SharePoint print pack; the other two go to the print pack only.

hosts.json holds [["Name", "phone"], ...]. It lives in SharePoint, never in this repo.
Challenges come from _data/challenges.yml, the same file the website uses.
"""
import sys, os, json, yaml, qrcode
from docx import Document
from docx.shared import Pt, RGBColor, Inches, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.enum.section import WD_ORIENT
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ROW_HEIGHT_RULE
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WORK = sys.argv[1]
HAS_HOSTS = len(sys.argv) > 2
HOSTS = json.load(open(sys.argv[2], encoding="utf-8")) if HAS_HOSTS else [["[HOST NAME]", "[PHONE]"]] * 3
CASES = yaml.safe_load(open(os.path.join(REPO, "_data", "challenges.yml"), encoding="utf-8"))
FORM = "https://forms.cloud.microsoft/r/B4kKv3YLdp"
SITE = "ryley-bauer.github.io/cppug-hackathon"

BLACK = RGBColor(0, 0, 0); WHITE = RGBColor(0xFF, 0xFF, 0xFF); GREY = RGBColor(0x59, 0x59, 0x59)
ACC = ["91338C", "5086F2", "4940AF", "EBCC45", "7DCF81", "8ED0F8"]
DARK_TEXT = {"EBCC45", "7DCF81", "8ED0F8"}
CUT = "- - - - - - - - - - - - - - - - - - - - - - - - - -   cut here   - - - - - - - - - - - - - - - - - - - - - - - - - -"

qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=20, border=2)
qr.add_data(FORM); qr.make(fit=True)
QR = os.path.join(REPO, "assets", "images", "checkin-qr.png")
qr.make_image(fill_color="black", back_color="white").save(QR)


# ---------------------------------------------------------------- helpers
def shade(el_pr, fill):
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear"); shd.set(qn("w:color"), "auto"); shd.set(qn("w:fill"), fill)
    el_pr.append(shd)


def run(p, text, size=9, bold=False, color=BLACK, font="Open Sans", italic=False):
    r = p.add_run(text)
    r.font.name = font; r.font.size = Pt(size); r.font.bold = bold; r.font.italic = italic
    r.font.color.rgb = color
    r._element.rPr.rFonts.set(qn("w:eastAsia"), font)
    return r


def page_field(p, size=8):
    """'Page N of M' using Word fields, so duplex order is easy to check."""
    for label, instr in (("Page ", "PAGE"), (" of ", "NUMPAGES")):
        run(p, label, size)
        fld = OxmlElement("w:fldSimple"); fld.set(qn("w:instr"), instr)
        r = OxmlElement("w:r"); t = OxmlElement("w:t"); t.text = "1"; r.append(t); fld.append(r)
        p._p.append(fld)


def new_doc(landscape=False, numbered=False):
    d = Document()
    s = d.sections[0]
    s.page_width, s.page_height = (Inches(11), Inches(8.5)) if landscape else (Inches(8.5), Inches(11))
    if landscape:
        s.orientation = WD_ORIENT.LANDSCAPE
    s.left_margin = s.right_margin = Inches(0.6)
    s.top_margin = s.bottom_margin = Inches(0.4); s.footer_distance = Inches(0.25)
    st = d.styles["Normal"]
    st.font.name = "Open Sans"; st.font.size = Pt(9)
    st.element.rPr.rFonts.set(qn("w:eastAsia"), "Open Sans")
    st.paragraph_format.space_after = Pt(2)
    st.paragraph_format.line_spacing = 1.05
    f = s.footer.paragraphs[0]
    run(f, f"CPPUG  |  communityleader@cppug.onmicrosoft.com  |  {SITE}", 8)
    if numbered:
        run(f, "      ", 8); page_field(f)
    return d


def banner(d, title, subtitle):
    p = d.add_paragraph(); shade(p._p.get_or_add_pPr(), "000000"); p.paragraph_format.space_after = Pt(0)
    run(p, " " + title, 28, font="Norwester", color=WHITE)
    p = d.add_paragraph(); shade(p._p.get_or_add_pPr(), "000000"); p.paragraph_format.space_after = Pt(6)
    run(p, "  " + subtitle, 10.5, color=WHITE)


def h(d, text, i, size=12, before=5):
    p = d.add_paragraph(); p.paragraph_format.space_before = Pt(before); p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.keep_with_next = True
    run(p, text, size, bold=True, color=RGBColor.from_string("4940AF" if ACC[i % 6] in DARK_TEXT else ACC[i % 6]))
    return p


def para(d, parts, size=9, after=2):
    p = d.add_paragraph(); p.paragraph_format.space_after = Pt(after)
    for t, b in ([(parts, False)] if isinstance(parts, str) else parts):
        run(p, t, size, bold=b)
    return p


def bullet(d, parts, size=9):
    p = para(d, parts, size, after=1); p.style = d.styles["List Bullet"]
    return p


def table(d, rows, widths, accent, size=9, header=True, height=None):
    t = d.add_table(rows=len(rows), cols=len(widths))
    t.style = d.styles["Table Grid"]; t.alignment = WD_TABLE_ALIGNMENT.CENTER; t.autofit = False
    fill = ACC[accent % 6]
    for i, row in enumerate(rows):
        tr = t.rows[i]
        if height:
            tr.height = height; tr.height_rule = WD_ROW_HEIGHT_RULE.AT_LEAST
        for j, txt in enumerate(row):
            c = tr.cells[j]; c.width = widths[j]
            p = c.paragraphs[0]; p.paragraph_format.space_after = Pt(1)
            p.paragraph_format.keep_with_next = i < len(rows) - 1  # keep each table on one page
            hdr = header and i == 0
            if hdr:
                shade(c._tc.get_or_add_tcPr(), fill)
            col = (BLACK if fill in DARK_TEXT else WHITE) if hdr else BLACK
            run(p, txt, size, bold=hdr or ((not header or i > 0) and j == 0 and len(widths) == 2), color=col)
    for j, w in enumerate(widths):
        for cell in t.columns[j].cells:
            cell.width = w
    return t


def page_break(d):
    d.add_paragraph().add_run().add_break(WD_BREAK.PAGE)


def cut_line(d):
    p = d.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(6); p.paragraph_format.space_after = Pt(6)
    run(p, CUT, 8, color=GREY)


def box(d, height, label):
    """An empty bordered box for writing or sketching."""
    t = d.add_table(rows=1, cols=1); t.style = d.styles["Table Grid"]; t.alignment = WD_TABLE_ALIGNMENT.CENTER
    t.rows[0].height = height; t.rows[0].height_rule = WD_ROW_HEIGHT_RULE.EXACTLY; t.rows[0].cells[0].width = Inches(7.3)
    run(t.rows[0].cells[0].paragraphs[0], label, 8, color=GREY)


def hosts_strip(d, size=10):
    t = d.add_table(rows=1, cols=len(HOSTS) + 1); t.alignment = WD_TABLE_ALIGNMENT.CENTER
    cells = t.rows[0].cells
    shade(cells[0]._tc.get_or_add_tcPr(), ACC[2])
    run(cells[0].paragraphs[0], "Need anything? Call or text a host", size, bold=True, color=WHITE)
    for c, (n, ph) in zip(cells[1:], HOSTS):
        shade(c._tc.get_or_add_tcPr(), "F5F5F5")
        run(c.paragraphs[0], n, size, bold=True); c.paragraphs[0].add_run().add_break(); run(c.paragraphs[0], ph, size)


# ---------------------------------------------------------------- Rubric (shared by both packs; the site, Judge Form, and event plan must match)
RUBRIC = [
    ("Functionality (30%, score x 6 points)",
     "Does the solution do what the team said it would do? Judges compare the live demo with the core features on the team summary card.",
     ["All listed core features work live. No errors. The team also shows one edge case handled well (for example, an empty field or a wrong entry).",
      "All listed core features work live. One small glitch at most.",
      "Most listed core features work live (for example, 2 of 3). Some bugs.",
      "Fewer than half of the listed core features work live (for example, 1 of 3). The team needs workarounds.",
      "No core feature works live, or the demo fails."]),
    ("Effective use of Power Platform (35%, score x 7 points)",
     "Did the team pick the right Power Platform parts and use them well? Judges count only what the demo shows working. Parts are Power Apps, Power Automate, "
     "Power BI, Power Pages, Copilot Studio, AI Builder, a data store (Dataverse or SharePoint list), and connectors (such as Outlook or Teams).",
     ["3 or more parts work together as one solution. The team explains why they chose each part. At least one platform strength is used (for example, approvals, shared data, a connector, or AI).",
      "3 or more parts work together and each one fits the problem.",
      "2 parts, and both fit the problem (for example, an app plus a flow).",
      "1 part with basic use only, or 2 parts where one does not fit.",
      "No Power Platform part is central, or the tools do not fit the problem."]),
    ("Design and user experience (25%, score x 5 points)",
     "Did the team think before they built, and is the result easy to use? Judges count how many of these 5 items the team shows: (A) Idea: how they chose it, "
     "such as the user need or the options they weighed. (B) Plan: a sketch, wireframe, mock-up, or flow diagram made before building (paper, whiteboard photo, "
     "or sticky notes all count). (C) Match: the built screens follow the plan, and the team says what changed and why. (D) Use: a new user could finish the main "
     "task with no explanation. (E) Polish: the layout is consistent and the text is easy to read.",
     ["All 5 items shown (A, B, C, D, E).", "4 of the 5 items shown.", "3 of the 5 items shown.", "2 of the 5 items shown.", "1 item shown, or none."]),
    ("Presentation quality (10%, score x 2 points)",
     "Did the team cover the 4 required parts: (1) the problem and who it helps, (2) a live demo, (3) the Power Platform parts used, (4) what the team learned?",
     ["All 4 parts covered, inside the time limit, and the team answers questions clearly.",
      "All 4 parts covered, inside the time limit. Answers to questions are adequate.",
      "3 of the 4 parts covered.", "2 of the 4 parts covered, or the team cannot answer most questions.", "1 part or none covered."]),
]


def rubric_tables(d):
    for i, (title, question, anchors) in enumerate(RUBRIC):
        h(d, title, i, size=11, before=4)
        p = para(d, question, size=7.5); p.runs[0].italic = True
        table(d, [["Score", "What the judge sees"]] + [[str(5 - k), a] for k, a in enumerate(anchors)], [Inches(0.6), Inches(6.7)], i, size=7.5)


# ---------------------------------------------------------------- Participant Pack (6 pages, 3 sheets duplex)
# Sheet 1: p1 logistics + schedule | p2 how it works, rules, hand-in, demo
# Sheet 2: p3 scoring rubric       | p4 challenges 1 to 3
# Sheet 3: p5 challenges 4 to 7    | p6 sketch area (top) + team summary card (bottom half, cut out)
# Cutting the card out of p6 only removes the bottom of p5 (challenges 6 and 7), which teams no longer need at 1:45 PM.
def build_pack(filename, with_hosts):
    """The public pack says where to find host numbers; the print copy lists them."""
    global d
    help_hosts = ("Call or text a host: " + ", ".join(f"{n} {ph}" for n, ph in HOSTS) + "."
                  if with_hosts else "Host phone numbers are posted at the check-in desk.")
    d = new_doc(numbered=True)

    # p1
    banner(d, "Participant pack", "CPPUG Power Platform Hackathon  |  Saturday, October 10, 2026  |  9:00 AM to 4:00 PM  |  Microsoft Calgary")
    para(d, "CPPUG means Calgary Power Platform User Group. Keep this pack on your table all day. Page 6 is your team summary card: cut it out and hand it in by 1:45 PM.")
    h(d, "Getting there and getting in", 0)
    para(d, [("Microsoft Calgary Office, 110 9 Ave SW, ", True), ("in the Le Germain office tower across 9 Avenue from the Calgary Tower.", False)])
    bullet(d, [("Doors open at 9:00 AM. ", True), ("The building is locked on Saturday. Wait in the main lobby and a volunteer brings you up.", False)])
    bullet(d, [("Running late? ", True), ("Message David in the Meetup event chat and someone comes down to get you.", False)])
    bullet(d, [("Washrooms ", True), ("are in the hallway outside the office. The door locks behind you, so tell a volunteer before you step out.", False)])
    table(d, [
        ["Parking or transit", "Where", "Cost (estimate, check the sign)"],
        ["Brookfield Place underground, Lot #35", "225 6 Ave SW, about 3 blocks north", "About $3.15 for 24 hours on the weekend"],
        ["Surface lot", "208 9 Ave SW, about 1 block west", "About $5 to $15 for the day"],
        ["CTrain", "7 Avenue stations at Centre Street or 1 Street SW, a 5 minute walk", "Regular Calgary Transit fare"],
    ], [Inches(2.3), Inches(3.2), Inches(1.8)], 2, size=8.5)
    h(d, "Before you arrive", 1)
    bullet(d, [("Check in: ", True), (f"fill in the registration form ({FORM}) or scan the QR code at the door. We ask your skill level (1 to 5) to build balanced teams.", False)])
    bullet(d, [("Bring ", True), ("a laptop, a charger, and a short power bar if you have one. Outlets are shared.", False)])
    bullet(d, [("Environment: ", True), ("use a work or school environment only if your organization allows it. No environment? Sign up for the free Power Apps Developer Plan (aka.ms/PowerAppsDevPlan). Organizers have a backup lab.", False)])
    h(d, "In the room", 3)
    bullet(d, [("Food: ", True), ("breakfast and lunch are provided, and coffee is on site. Tell us about dietary needs at check-in.", False)])
    bullet(d, [("Wi-Fi: ", True), ("details are on the whiteboard. A backup hotspot is available.", False)])
    bullet(d, [("Help: ", True), ("mentors walk the room all day, so ask early. " + help_hosts, False)])
    bullet(d, [("Photos: ", True), ("we photograph the demos and the closing. Tell a volunteer if you prefer not to appear.", False)])
    h(d, "Schedule", 4)
    table(d, [
        ["Time", "What happens", "Time", "What happens"],
        ["9:00 AM", "Doors open, check-in, team matching", "1:45 to 2:00 PM", "Stop building. Hand in your team summary card"],
        ["9:30 to 9:55 AM", "Welcome, rules, challenge briefing", "2:00 to 3:15 PM", "Team demos"],
        ["10:00 AM", "Build starts. Plan and sketch for 30 minutes first", "3:15 to 3:40 PM", "Judges score. Everyone networks"],
        ["12:30 PM", "Lunch. Keep building if you like", "3:40 to 4:00 PM", "Awards, photos, and closing"],
    ], [Inches(1.15), Inches(2.5), Inches(1.15), Inches(2.5)], 4, size=8.5)
    page_break(d)

    # p2
    h(d, "How the day works", 0, size=14, before=0)
    bullet(d, [("Teams. ", True), ("Teams have 2 to 3 people. No team? Organizers match you with other builders.", False)], 10)
    bullet(d, [("Challenge. ", True), ("Pick a prepared challenge (pages 4 and 5) or choose Open Build and bring any idea where Power Platform is central.", False)], 10)
    bullet(d, [("Plan first. ", True), ("Spend your first 30 minutes on the idea, not the build. Pick the problem, list your options, and sketch the screens on page 6. Judges look for this work.", False)], 10)
    bullet(d, [("Goal. ", True), ("Build a minimum viable product (MVP): a simple version that works. A small solution that works beats a large one that does not.", False)], 10)
    bullet(d, [("Prizes. ", True), ("Two individual Power Platform Community Conference 2026 (PPCC26) passes from Microsoft. A pass covers the conference only. "
                                "At check-in, tell us if you could book travel within about a week. Judges place the passes after scoring, starting with the top teams. "
                                "Runners-up receive Lego Clippy mascots.", False)], 10)
    h(d, "Rules", 1, size=14)
    bullet(d, [("Register, and bring a laptop and charger. ", True), ("You may use your own Power Platform environment if your organization allows it.", False)], 10)
    bullet(d, [("Use Power Platform and build during the event. ", True), ("Power Platform must be a main part of the build. Do the main build work between 10:00 AM and 1:45 PM.", False)], 10)
    bullet(d, [("Use any help you like. ", True), ("Documentation, Microsoft Learn, search, and AI tools are allowed. Tell the judges what you used.", False)], 10)
    bullet(d, [("No finished solutions. ", True), ("Do not enter a complete solution built before the event. Reusable snippets and patterns are fine if you can say what you built today.", False)], 10)
    bullet(d, [("Be respectful. ", True), ("Respect participants, organizers, volunteers, judges, and Microsoft staff. Harassment, discrimination, and intimidation are not allowed. "
                                      "Organizers may remove anyone who creates an unsafe or hostile space.", False)], 10)
    h(d, "What to hand in by 1:45 PM", 2, size=14)
    para(d, size=10, parts="Cut out the team summary card on page 6 and give it to the demo organizer. Judges score your demo against it.")
    table(d, [
        ["Field", "What to write"],
        ["Problem", "One sentence. What problem does the solution solve, and for whom?"],
        ["How we chose it", "One sentence. Why this idea? Which other ideas did you weigh?"],
        ["Plan", "What did you sketch or write before building? Show it in your demo."],
        ["Core features", "Up to 3 features. Judges check these in the demo."],
        ["Power Platform parts", "Each part you used (for example Power Apps, Power Automate, Dataverse)."],
        ["Team", "Team name and member names."],
    ], [Inches(1.8), Inches(5.5)], 2, size=9.5)
    h(d, "Your demo", 3, size=14)
    para(d, size=10, parts="Slots: 15 minutes (10 demo, 5 questions) for up to 5 teams, 10 minutes (7 + 3) for 6 to 7 teams, and 7 minutes (5 + 2) for 8 to 10 teams. "
            "Organizers confirm yours at the opening. Slides are optional. Cover 4 parts: (1) the problem you solved and who it helps, (2) a live demo, "
            "(3) the Power Platform parts you used and why, (4) what your team learned. Show your sketch for about 30 seconds.")
    page_break(d)

    # p3: rubric on one side
    h(d, "How you are scored", 0, size=14, before=0)
    para(d, "Each judge scores each team on 4 criteria with a whole number from 1 to 5. Each score turns into points. The most points possible is 100 (30 + 35 + 25 + 10).", size=8.5)
    rubric_tables(d)
    para(d, [("Winners. ", True), ("Judges score alone and compare your demo with your team summary card. Organizers average the totals. The two highest averages are the "
              "winning teams. Tie: higher Effective use points win, then higher Functionality points, then the judges decide.", False)], size=8).paragraph_format.space_before = Pt(5)
    page_break(d)


    # p4 and p5: challenges
    def challenge(i, c):
        h(d, f"{i + 1}. {c['name']}", i, size=11, before=5)
        table(d, [["Scenario", c["scenario"]], ["Users", c["users"]], ["Starter build (MVP)", c["starter"]], ["Stretch ideas", c["stretch"]],
                  ["Suggested data", c["data"]], ["Likely tools", c["tools"]]], [Inches(1.6), Inches(5.7)], i, size=9.5, header=False)


    h(d, "Pick a challenge", 0, size=14, before=0)
    para(d, "Each challenge fits a four-hour build. Build the starter version first and add stretch ideas only when it works. Judges score the core features you "
            "list on your card, so pick 3 you can finish. Tip: start with sample data. Ten realistic rows make a better demo than an empty app.")
    for i in range(3):
        challenge(i, CASES[i])
    page_break(d)
    for i in range(3, len(CASES)):
        challenge(i, CASES[i])
    page_break(d)

    # p6: sketch area on top, card on the bottom half
    h(d, "Plan here first: sketch your main screens (first 30 minutes)", 1, size=12, before=0)
    para(d, "Keep this half. Show it in your demo for about 30 seconds: judges score the plan (item B) and how well your screens match it (item C).", size=8)
    box(d, Inches(4.15), "Sketch: screens, data, and the flow between them")
    cut_line(d)
    h(d, "Team summary card: hand in by 1:45 PM", 0, size=12, before=0)
    table(d, [("Team name", ""), ("Members", ""), ("Challenge", "Inventory / Time Off / Inspection / Expense / Booking / Kudos / Open Build"),
              ("Problem (one sentence: what, and for whom?)", ""), ("How we chose it (which other ideas did we weigh?)", ""),
              ("Plan (what did we sketch before building?)", ""), ("Core feature 1", ""), ("Core feature 2", ""), ("Core feature 3", ""),
              ("Power Platform parts used", "")], [Inches(2.6), Inches(4.7)], 0, size=8.5, header=False, height=Cm(0.86))
    d.save(os.path.join(WORK, filename))


build_pack("CPPUG Hackathon - Participant Pack.docx", with_hosts=False)
if HAS_HOSTS:  # SharePoint print copy only. Never publish it.
    build_pack("CPPUG Hackathon - Participant Pack (print, with host numbers).docx", with_hosts=True)

# ---------------------------------------------------------------- Check-in sheet (internal)
d = new_doc()
banner(d, "Check in here", "CPPUG Power Platform Hackathon  |  Saturday, October 10, 2026")
hosts_strip(d)
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

sec = d.add_section()
sec.orientation = WD_ORIENT.LANDSCAPE; sec.page_width, sec.page_height = Inches(11), Inches(8.5)
h(d, "Paper sign-in sheet (backup if the form is down)", 0, size=16, before=0)
hosts_strip(d, 9)
para(d, "Everyone signs here, even if you used the form. Role: C = competitor with a team, F = free agent (match me), V = volunteer, S = spectator, "
        "M = mentor or judge. Skill: 1 = brand new, 5 = expert. PPCC26: if you win a pass, could you book flights and hotel within 7 days? "
        "Did not do the form? Also fill in a check-in slip.")
rows = [["#", "Name (as on your name tag)", "Role (C F V S M)", "Team name (blank if solo)", "Skill 1 to 5", "Laptop? Y / N", "Form done? Y / N",
         "Photos OK? Y / N", "PPCC26 travel in 7 days? Y / N"]]
rows += [[str(i)] + [""] * 8 for i in range(1, 17)]
table(d, rows, [Inches(0.4), Inches(2.4), Inches(1.0), Inches(1.8), Inches(0.8), Inches(0.8), Inches(0.8), Inches(0.9), Inches(0.9)], 1, size=9, height=Cm(0.78))

sec = d.add_section()
sec.orientation = WD_ORIENT.PORTRAIT; sec.page_width, sec.page_height = Inches(8.5), Inches(11)
SLIP = [("Name", ""), ("Email (for team updates only)", ""), ("Role", "Competitor with a team  /  Free agent  /  Volunteer  /  Spectator"),
        ("Team name and teammates", ""), ("Skill 1 to 5", "1 brand new   2 beginner   3 intermediate   4 advanced   5 expert"),
        ("Strongest in", "Apps  /  Automate  /  BI  /  Copilot Studio  /  Pages  /  Dataverse  /  None yet"),
        ("Dietary needs", "None  /  Vegetarian  /  Vegan  /  Halal  /  Gluten-free  /  Nut allergy  /  Other:"),
        ("Could you book PPCC26 travel and hotel within 7 days if you win?", "Yes  /  No"), ("Photos and video OK?", "Yes  /  Please avoid me")]
for n in range(2):
    h(d, "Check-in slip (fill in if you did not use the form)", 3, size=11, before=0 if n == 0 else 14)
    table(d, SLIP, [Inches(2.4), Inches(4.9)], 0, size=8.5, header=False, height=Cm(0.95))
    para(d, "Hand this slip to a volunteer. It is private: only organizers see it, and we enter it into the form after check-in.", size=8)
    if n == 0:
        cut_line(d)
d.save(os.path.join(WORK, "CPPUG Hackathon - Check-in Sheet.docx"))

# ---------------------------------------------------------------- Volunteer and Judge Pack (public, 3 pages)
# p1 volunteer guide | p2 judge guide (same rubric as the Participant Pack) | p3 landscape score sheet, one per judge
# Roles only, no names or phone numbers: those are on the check-in sheet. No building-security details.
def build_team_pack(filename, with_hosts):
    """The public pack sends volunteers to the check-in sheet for numbers; the print copy lists them at the top."""
    global d
    d = new_doc(numbered=True)
    banner(d, "Volunteer and judge pack", "CPPUG Power Platform Hackathon  |  Saturday, October 10, 2026  |  Arrive 8:30 AM for the briefing")
    if with_hosts:
        hosts_strip(d, 9.5)
    h(d, "Volunteers: your job in one line", 0, before=2)
    para(d, "Greet people like they belong. Guide teams, but do not build for them. Keep the room tidy. Look for anyone who seems lost, alone, or stuck. "
            "Ask an organizer when unsure.", size=9.5)
    h(d, "The day", 1)
    table(d, [["Time", "What happens"],
              ["8:30 AM", "Volunteer briefing. Set up tables, signs, power, and the check-in desk. Test Wi-Fi and the projector."],
              ["9:00 AM", "Doors open. Bring people up from the lobby. Check-in, name tags, and free-agent matching."],
              ["9:30 to 9:55 AM", "Welcome, rules, and challenge briefing."],
              ["10:00 AM", "Build starts. Mentors roam. Free agents get matched."],
              ["12:30 PM", "Lunch. Teams can eat at their tables."],
              ["1:45 to 2:00 PM", "Teams hand in summary cards and set up demos. Judges meet for 10 minutes."],
              ["2:00 to 3:40 PM", "Team demos until 3:15, then judges score while everyone networks. Collect score sheets."],
              ["3:40 to 4:00 PM", "Awards, photos, and closing."],
              ["4:00 PM", "Cleanup. Clear tables, signs, and trash. Check for lost items. Leave the room spotless."]],
          [Inches(1.4), Inches(5.9)], 1, size=8.5)
    h(d, "Role cards", 2)
    table(d, [["Role", "Before doors open (8:30 to 9:00)", "During the event"],
              ["Door and elevator", "Learn the door plan at the briefing.", "Bring people up from the lobby. Let people back in after washroom trips. Never prop the door open."],
              ["Setup and cleanup", "Tables, chairs, signs, check-in desk, power strips, projector test.", "Fix room issues. At 4:00 PM: clear tables, trash, signs, and lost items."],
              ["Check-in", "Registration list, name tags, role labels, free-agent area.", "Greet people. Note no-shows. Send free agents to matching. Ask each competitor quietly: "
               "'If you won a PPCC26 pass, could you book travel within about a week?' Mark yes on the list."],
              ["Team matcher", "List of free agents with skill levels.", "Mix skill levels. Ask advanced makers if they will anchor a team of beginners."],
              ["Mentor", "Read the challenges and the rules in the Participant Pack.", "Roam. Ask 'What are you trying to do?' Point to the next step. Do not build it for them."],
              ["Food lead", "Confirm meal times and dietary options. Set up the food table.", "Meet the delivery. Keep the table clean and stocked."],
              ["Timekeeper", "Demo order sheet. A timer the presenters can see.", "Announce time checks. Warn each team 2 minutes before the end of its slot."],
              ["Judging assistant", "Print score sheets. Open the Judge Form link.", "Hand out sheets, collect them, and tell judges which team is next."]],
          [Inches(1.4), Inches(2.4), Inches(3.5)], 2, size=8.5)
    h(d, "Who to ask", 3)
    table(d, [["Problem", "Go to"],
              ["Safety, conduct, or anyone who feels unwelcome", "An event lead, right away"],
              ["Wi-Fi, power, projector, or building access", "The Microsoft liaison"],
              ["Tenant or login problem, or a challenge question", "The technical lead"]],
          [Inches(3.6), Inches(3.7)], 3, size=8.5)
    para(d, ("Host phone numbers are at the top of this page. " if with_hosts else "Organizer names and phone numbers are on the check-in sheet at the desk. ") + "Fill in at the 8:30 briefing: "
            "Wi-Fi ____________________   Lunch spot ______________   Volunteer channel ______________", size=8.5).paragraph_format.space_before = Pt(4)
    page_break(d)

    # p2: judge guide
    h(d, "Judges: how to score", 0, size=14, before=0)
    para(d, "Score each team on 4 criteria with a whole number from 1 to 5. Points = score x 6, 7, 5, and 2. The most points possible is 100. "
            "Teams have the same rubric on page 3 of their Participant Pack.", size=8.5)
    rubric_tables(d)

    # p3: score sheet, landscape, one per judge (a new section starts a new page)
    sec = d.add_section()
    sec.orientation = WD_ORIENT.LANDSCAPE; sec.page_width, sec.page_height = Inches(11), Inches(8.5)
    sec.left_margin = sec.right_margin = Inches(0.5)
    h(d, "Judge score sheet: one per judge, all teams", 0, size=14, before=0)
    para(d, [("Judge name: ______________________________     ", True),
             ("At 1:45 PM, judges meet for 10 minutes to agree on how to read 'core features', 'parts used', and what counts as a plan. Read each team's summary card "
              "before its demo and score what works live. Score alone and do not discuss scores until all are in. Skip any team you have a conflict with "
              "(work tie, personal tie, or heavy mentoring) and tell an organizer. Add a short reason to any 1 or 5 in the notes column.", False)], size=8.5)
    table(d, [["Criterion", "5", "4", "3", "2", "1"],
              ["Functionality: 30%, score x 6", "All listed core features work live, no errors, plus one edge case handled well",
               "All listed core features work live. One small glitch at most", "Most core features work (for example 2 of 3). Some bugs",
               "Fewer than half work (for example 1 of 3). Needs workarounds", "No core feature works, or the demo fails"],
              ["Effective use of Power Platform: 35%, score x 7", "3+ parts work together. Team explains each choice. Uses a platform strength (approvals, shared data, connector, AI)",
               "3+ parts work together and each fits the problem", "2 parts, both fit the problem (for example an app plus a flow)",
               "1 part with basic use, or 2 parts where one does not fit", "No Power Platform part is central, or the tools do not fit"],
              ["Design and user experience: 25%, score x 5", "All 5 items shown: A Idea (how they chose it), B Plan (sketch before building), C Match (screens follow plan), "
               "D Use (new user finishes main task alone), E Polish (consistent, readable)", "4 of the 5 items", "3 of the 5 items", "2 of the 5 items", "1 item, or none"],
              ["Presentation quality: 10%, score x 2", "All 4 parts (problem, live demo, parts used, what they learned), on time, clear answers",
               "All 4 parts, on time. Answers adequate", "3 of the 4 parts", "2 of the 4 parts, or cannot answer most questions", "1 part or none"]],
          [Inches(1.5), Inches(2.6), Inches(1.6), Inches(1.5), Inches(1.4), Inches(1.4)], 0, size=7)
    para(d, "", size=4)
    SC = [["#", "Team name", "Conflict? (skip)", "Function 1 to 5 (x 6)", "Effective use 1 to 5 (x 7)", "Design 1 to 5 (x 5)  circle A B C D E",
           "Present. 1 to 5 (x 2)", "Total points (max 100)", "Standout member for a pass, and notes"]]
    SC += [[str(i), "", "", "", "", "A  B  C  D  E", "", "", ""] for i in range(1, 11)]
    table(d, SC, [Inches(0.3), Inches(1.7), Inches(0.75), Inches(0.85), Inches(0.85), Inches(1.35), Inches(0.8), Inches(0.9), Inches(2.5)], 1, size=7.5, height=Cm(0.82))
    para(d, [("Total = Function x 6 + Effective use x 7 + Design x 5 + Presentation x 2. ", True),
             ("Hand this sheet to an organizer when demos end. Organizers average the totals. Ties: higher Effective use points, then Functionality points, "
              "then the judges decide. Passes are placed after scoring, from the pass-eligible list.", False)], size=8)
    d.save(os.path.join(WORK, filename))


build_team_pack("CPPUG Hackathon - Volunteer and Judge Pack.docx", with_hosts=False)
if HAS_HOSTS:  # SharePoint print copy only. Never publish it.
    build_team_pack("CPPUG Hackathon - Volunteer and Judge Pack (print, with host numbers).docx", with_hosts=True)
print("built")
