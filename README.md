# CPPUG Power Platform Hackathon

The public package for the Calgary Power Platform User Group (CPPUG) hackathon at Microsoft Calgary on Saturday, October 10, 2026.

- **Website:** https://ryley-bauer.github.io/cppug-hackathon/
- **RSVP and updates:** [Meetup event page](https://www.meetup.com/calgary-power-platform-user-group/events/315727499/). Meetup is the source of truth for date, time, venue, and prizes.
- **Contact:** communityleader@cppug.onmicrosoft.com, or message us in the Meetup event chat.

## Downloads

| Document | What it covers |
|---|---|
| [Know Before You Go](assets/downloads/CPPUG%20Hackathon%20-%20Know%20Before%20You%20Go.pdf) | Getting there, getting in, parking, what to bring |
| [Participant Handout](assets/downloads/CPPUG%20Hackathon%20-%20Participant%20Handout.pdf) | Schedule, rules, and the scoring rubric |
| [Challenge Case Studies](assets/downloads/CPPUG%20Hackathon%20-%20Challenge%20Case%20Studies.pdf) | The seven prepared challenges |
| [Team Summary Card](assets/downloads/CPPUG%20Hackathon%20-%20Team%20Summary%20Card.pdf) | What each team hands in by 1:45 PM |

## What is in this repo

- The Jekyll site (`index.markdown`, `challenges.md`, `complete-rules.md`, `project-ideas.md`, `_data/`, `_layouts/`, `_includes/`, `_sass/`), published with GitHub Pages.
- `assets/downloads/`: the PDFs above.
- `docs/`: the Word sources for those PDFs and the script that generates most of them. See `docs/README.md`.

Organizer working documents live in the CPPUG SharePoint site, not here.

## Run the site locally

```bash
bundle install
bundle exec jekyll serve
```

Then open http://localhost:4000/cppug-hackathon/.
