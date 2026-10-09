# CPPUG Power Platform Hackathon

The public package for the Calgary Power Platform User Group (CPPUG) hackathon at Microsoft Calgary on Saturday, October 10, 2026.

- **Website:** https://ryley-bauer.github.io/cppug-hackathon/
- **RSVP and updates:** [Meetup event page](https://www.meetup.com/calgary-power-platform-user-group/events/315727499/). Meetup is the source of truth for date, time, venue, and prizes.
- **Contact:** communityleader@cppug.onmicrosoft.com, or message us in the Meetup event chat.

## Download

[**Participant Pack (PDF, 6 pages)**](assets/downloads/CPPUG%20Hackathon%20-%20Participant%20Pack.pdf): everything for the day in one document. Getting there and getting in, the schedule, rules, the scoring rubric, the seven challenges, a sketch area, and the team summary card to cut out. It prints on 3 sheets, double-sided.

## What is in this repo

- The Jekyll site (`index.markdown`, `challenges.md`, `complete-rules.md`, `project-ideas.md`, `_data/`, `_layouts/`, `_includes/`, `_sass/`), published with GitHub Pages.
- `assets/downloads/`: the Participant Pack PDF.
- `docs/`: the script that builds the pack. See `docs/README.md`.

Organizer working documents live in the CPPUG SharePoint site, not here.

## Run the site locally

```bash
bundle install
bundle exec jekyll serve
```

Then open http://localhost:4000/cppug-hackathon/.
