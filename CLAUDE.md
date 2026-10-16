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
- This repo is the public package. Internal team docs (event plan, checklist, budget, Judge Form import, slides) live in SharePoint: `CPPUG - Documents/Hackathon/2026-10-10 Hackathon/Team (internal)/`. Never add them back here.
- The rubric (criteria, weights, points, anchors) lives in four places: the `RUBRIC` in `docs/build-day-of-docs.py` (page 3 of the Participant Pack and page 2 of the Volunteer and Judge Pack), the Judge Form import file, and `event-plan.md` (SharePoint). It also appears on the site (`index.markdown`, `complete-rules.md`). Change all of them together. Weights are 30, 35, 25, 10. Points are score x 6, 7, 5, 2.
- The rubric must fit on one printed side in both packs. The volunteer guide must stay one page.
- The Judge Form import file stays plain text on purpose (Microsoft Forms Quick import).
- There are two public downloads: the Participant Pack (exactly 6 pages, for duplex printing) and the Volunteer and Judge Pack (3 pages). After you change either one, check the page count and export a new PDF to `assets/downloads/`.

## Saving docs to SharePoint (automatic)

Do not upload files to SharePoint by hand. Merging to `main` does it for you.

- The workflow `.github/workflows/publish-sharepoint.yml` copies `docs/` and `assets/downloads/` to `CPPUG - Documents/Hackathon/Repo sync/` on the CPPUG SharePoint site. It runs on every push to `main` that touches those folders, and by hand from the Actions tab.
- The copy is one way and overwrites every file. Edit the file in the repo. Edits made to the SharePoint copy are lost on the next run.
- It signs in through a federated credential on the Entra app `cppug-hackathon-docs-ci` (CPPUG tenant), so the repo holds no secret. The settings are the repo variables `AZURE_TENANT_ID`, `AZURE_CLIENT_ID`, `SHAREPOINT_HOSTNAME`, `SHAREPOINT_SITE_PATH`, and `SHAREPOINT_DEST_FOLDER`.
- The app can write to the whole CPPUG site, so the workflow only ever writes under `Repo sync/`. Never point `SHAREPOINT_DEST_FOLDER` at `Team (internal)` or `Print pack`. Internal team documents stay in SharePoint and never come back to this repo.
- The credential trusts only this repo (`ryley-bauer/cppug-hackathon`) on the `main` branch. Its subject uses GitHub's numeric IDs: `repo:ryley-bauer@83043124/cppug-hackathon@1412546355:ref:refs/heads/main`. The IDs change if the repo is renamed, moved, or recreated. Then the run fails with `AADSTS700213`. Read the new subject from the failed run's log and update the credential in Entra (app `cppug-hackathon-docs-ci`, Certificates & secrets, Federated credentials).
- Each file must stay under 4 MB. A 403 error on upload means the site grant for the app is missing.

## Writing rules

- Plain language, active voice, short sentences. Define every acronym on first use.
- No em dashes in documents or on the site.
- Do not put attendee names or other non-public details in public material. Organizer phone numbers never go in this repo: the generator reads them from `hosts.json` in the SharePoint print pack.
- Sponsor logos go only in the site's sponsor section. Never place them beside the CPPUG identity.
