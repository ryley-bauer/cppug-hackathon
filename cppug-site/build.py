"""Rebuild worker.js from index.html and cppug-intro.svg. Run: python cppug-site/build.py"""
import json
import pathlib

d = pathlib.Path(__file__).parent
tail = (d / "worker.js").read_text(encoding="utf8")
tail = tail[tail.index("export default"):]
route = ("    if (url.pathname === '/cppug-intro.svg') { return new Response(SVG, { headers: "
         "{ 'content-type': 'image/svg+xml', 'cache-control': 'public, max-age=86400' } }); }\n")
if "SVG" not in tail:
    tail = tail.replace("    return new Response(HTML,", route + "    return new Response(HTML,")
head = ("const HTML = " + json.dumps((d / "index.html").read_text(encoding="utf8")) + ";\n"
        "const SVG = " + json.dumps((d / "cppug-intro.svg").read_text(encoding="utf8")) + ";\n\n")
(d / "worker.js").write_text(head + tail, encoding="utf8", newline="\n")
