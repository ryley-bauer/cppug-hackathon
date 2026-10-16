# CPPUG logo intro

The Calgary Power Platform User Group (CPPUG) logo intro: a 25 second drive down a valley road into Calgary. Six Power Platform icons climb the Calgary Tower, and then the name appears.

| File | What it is | Use it for |
|---|---|---|
| `cppug-logo.svg` | The logo as one static vector (white shapes, official icon colours, transparent background) | Slides, docs, web, print on dark colours |
| `cppug-intro-4x3.svg` | The animated intro, 4:3 frame | A web page (see below) |
| `cppug-intro-16x9.svg` | The animated intro, 16:9 frame | A web page (see below) |
| `cppug-intro-16x9.webm` | The intro as video, 1920 by 1080, 30 frames per second | Web pages and slides that play video |
| `cppug-intro-16x9.gif` | The intro as a looping image, 960 by 540, 15 frames per second | Places that only take an image (about 10 MB) |

## The animated SVG files

- They run on a script inside the file. Open one directly in a browser, or embed it with `<object>`, `<iframe>` or inline.
- An `<img>` tag does not run scripts, so it shows a blank first frame. Use the GIF or the WebM there.
- They play on their own, pause 3 seconds on the logo, and loop. Add `?loop=0` to the file address to play once and stay on the logo. If the viewer asks for reduced motion, they show the final logo.
- They make no network requests.

## Icons

The Power Apps, Power Automate, Power Pages, Dataverse and Copilot Studio icons are Microsoft's official vectors from the Power Platform icon pack. The Power BI icon is from the archived `microsoft/PowerBI-Icons` repository (CC BY 4.0). The shapes of the tower, buildings and name are traced from the original CPPUG logo image.
