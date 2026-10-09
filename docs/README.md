# Public hackathon documents (Saturday, October 10, 2026)

This repo is the public package. The Meetup event page is the source of truth for public details. If a file here disagrees with it, fix the file.

Internal team documents (event plan, checklist, budget, Judge Guide, Judge Form, Volunteer Cheat Sheet, meeting notes) live in the CPPUG SharePoint site: `CPPUG - Documents/Hackathon/2026-10-10 Hackathon/Team (internal)/`. Do not add them here.

| Source file | PDF in `../assets/downloads/` | Audience |
|---|---|---|
| `CPPUG Hackathon - Participant Handout.docx` | Participant Handout | Participants: schedule, rules, rubric |
| `CPPUG Hackathon - Know Before You Go.docx` | Know Before You Go | Participants: getting there, getting in, parking, what to bring |
| `CPPUG Hackathon - Challenge Case Studies.docx` | Challenge Case Studies | Participants: the seven prepared challenges |
| `CPPUG Hackathon - Team Summary Card.docx` | Team Summary Card | Teams: hand in by 1:45 PM |

`build-day-of-docs.py` generates the Know Before You Go, Challenge Case Studies, and Team Summary Card Word files and `../assets/images/checkin-qr.png`. It also writes two internal files to a third folder: the Check-in Sheet (it lists organizer cell numbers) and the paper Judge Score Sheet. The challenges come from `../_data/challenges.yml`, the same file the website uses. Run it from the repo root: `python docs/build-day-of-docs.py docs assets/images "<SharePoint>/Hackathon/2026-10-10 Hackathon/Print pack"` (needs `python-docx`, `qrcode`, and `pyyaml`). Never pass `docs` as the third folder. The Participant Handout is edited by hand.

Export PDFs from Word (File, Save as, PDF) on a machine with Norwester and Open Sans installed. Word does not embed the OpenType (CFF) Norwester file, so install a TrueType copy.

The `docs/` folder is excluded from the Jekyll site build.

The Word documents follow the `cppug-brand` skill: Norwester headings, Open Sans body, black cover banner, and the pink, blue, purple, yellow, green and light blue accent cycle on table headers.
