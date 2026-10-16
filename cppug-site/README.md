# cppug.ca landing page

The main CPPUG site at https://cppug.ca is a Cloudflare Worker named `cppug-site` that serves `index.html`. Its main button links to this hackathon site at https://hackathon.cppug.ca.

- `index.html`: the page. Edit this file.
- The hero logo is the animated `assets/images/logos/cppug-intro.svg` on the hackathon site. It plays once (25 seconds), stops on the logo, and respects reduced-motion settings.
- `build.py`: rebuilds `worker.js` from `index.html` (run `python cppug-site/build.py`).
- `worker.js`: the deployed Worker. It embeds `index.html`, redirects `www.cppug.ca` to `cppug.ca`, and redirects `cppug.ca/hackathon` to `hackathon.cppug.ca`.

To publish a change, run `python cppug-site/build.py` and deploy it with Wrangler (`npx wrangler deploy cppug-site/worker.js --name cppug-site --compatibility-date 2026-10-01`) or paste it into the Worker in the Cloudflare dashboard. The page loads its logo animation, static logo (social image) and Norwester font from hackathon.cppug.ca, so keep those files in this repo.

## DNS (Cloudflare zone cppug.ca)

| Name | Points to | Notes |
|---|---|---|
| `cppug.ca`, `www.cppug.ca` | Worker `cppug-site` (custom domains) | Managed by Cloudflare |
| `hackathon.cppug.ca` | CNAME `ryley-bauer.github.io`, DNS only | GitHub Pages for this repo. When the repo moves to the `cppug` account, change it to `cppug.github.io` |
