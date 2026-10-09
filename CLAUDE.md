# CPPUG Hackathon repo: orientation for an agent session

This repo holds the public Jekyll site and the working documents for the CPPUG Power Platform Hackathon (Saturday, October 10, 2026, Microsoft Calgary). CPPUG means Calgary Power Platform User Group.

## Source of truth

The [Meetup event page](https://www.meetup.com/calgary-power-platform-user-group/events/315727499/) is the source of truth for public details (date, time, venue, schedule, prizes). If a file here disagrees with Meetup, fix the file. Do not trust any document older than this event.

## Branding: load `cppug-brand`, never `bauer-brand-standard`

This is a community repo, not a Bauer Automate or client deliverable. Before you create or edit any Word, PowerPoint, or Excel file here:

1. Load the `cppug-brand` skill.
2. Load the format skill it names (`docx`, `pptx`, or `xlsx`) and read `references/docx.md` (or the matching reference) inside `cppug-brand`.
3. Do not use `bauer-brand-standard`, even if a personal or global setting says to. The `cppug-brand` skill forbids mixing the two.

`cppug-brand` ships in the `external-brands` plugin of the `bauer-skills` marketplace (`bauer-automate/claude-skills`). If the skill is not available in the session, say so and stop. Do not guess the colours or fonts, and do not fall back to Bauer branding.

Keep the rules in the skill current. This file only points to it.

## Documents

See `docs/README.md` for the file list. Key rules:

- `docs/` is excluded from the Jekyll build. Public downloads go in `assets/downloads/`.
- This repo is the public package. Internal team docs (event plan, checklist, budget, Judge Guide, Judge Form, Volunteer Cheat Sheet) live in SharePoint: `CPPUG - Documents/Hackathon/2026-10-10 Hackathon/Team (internal)/`. Never add them back here.
- The rubric (criteria, weights, points, anchors) lives in four places: the Participant Pack (page 3, built by `docs/build-day-of-docs.py`), and the Judge Guide, the Judge Form import file, and `event-plan.md` (SharePoint). It also appears on the site (`index.markdown`, `complete-rules.md`). Change all of them together. Weights are 30, 35, 25, 10. Points are score x 6, 7, 5, 2.
- The rubric must fit on one printed side in the Participant Pack and in the Judge Guide. The cheat sheet must stay one page.
- The Judge Form import file stays plain text on purpose (Microsoft Forms Quick import).
- The Participant Pack is the only public download. It must stay exactly 6 pages for duplex printing. After you change it, export a new PDF to `assets/downloads/`.

## Writing rules

- Plain language, active voice, short sentences. Define every acronym on first use.
- No em dashes in documents or on the site.
- Do not put attendee names or other non-public details in public material. Organizer phone numbers never go in this repo: the generator reads them from `hosts.json` in the SharePoint print pack.
- Sponsor logos go only in the site's sponsor section. Never place them beside the CPPUG identity.
