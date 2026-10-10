# Building the print documents

`build-day-of-docs.py` builds every print document from code, so there are no Word files to keep in sync. Run it from the repo root:

```bash
python docs/build-day-of-docs.py <scratch folder> "<SharePoint>/Hackathon/2026-10-10 Hackathon/Print pack/hosts.json"
```

It needs `python-docx`, `qrcode`, and `pyyaml`. It writes four Word files to the scratch folder (never to the repo):

| File | Where the PDF goes | Notes |
|---|---|---|
| Participant Pack | `assets/downloads/` | Public. 6 pages, double-sided (flip on long edge), 3 sheets. Page 1 says host numbers are at the check-in desk |
| Participant Pack (print, with host numbers) | SharePoint print pack only | The copy teams get on the day. Same pack, page 1 lists the host phone numbers. Built only when you pass `hosts.json` |
| Check-in Sheet | SharePoint print pack only | Lists organizer cell numbers from `hosts.json` |
| Volunteer and Judge Pack | `assets/downloads/` and the SharePoint print pack | Public. 3 pages: volunteer guide (roles, no names or phone numbers), judge rubric (the same `RUBRIC` as the Participant Pack), score sheet for all teams |

Export each Word file to PDF from Word on a machine with Norwester (TrueType copy) and Open Sans installed, then delete the Word files.

## Participant Pack layout

| Sheet | Front | Back |
|---|---|---|
| 1 | Getting there, getting in, schedule | How the day works, rules, hand-in, demo |
| 2 | Scoring rubric (must stay on one page) | Challenges 1 to 3 |
| 3 | Challenges 4 to 7 | Sketch area (top) and team summary card (bottom half, cut out) |

Cutting out the card only removes the bottom of page 5 (challenges 6 and 7), which teams no longer need at 1:45 PM. If you change the content, check that the PDF is still exactly 6 pages.

The challenges come from `../_data/challenges.yml`, the same file the website uses. The site links to the pack through `pack_pdf` in `_config.yml`.

Internal team documents (event plan, checklist, budget, Judge Form import, slides, meeting notes) live in SharePoint: `CPPUG - Documents/Hackathon/2026-10-10 Hackathon/Team (internal)/`. Do not add them here.
