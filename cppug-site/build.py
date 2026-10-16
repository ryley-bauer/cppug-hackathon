"""Rebuild worker.js from index.html. Run: python cppug-site/build.py"""
import json
import pathlib

d = pathlib.Path(__file__).parent
tail = (d / "worker.js").read_text(encoding="utf8")
tail = tail[tail.index("export default"):]
tail = "\n".join(line for line in tail.split("\n") if "cppug-intro-16x9.svg" not in line or "<iframe" in line)
head = "const HTML = " + json.dumps((d / "index.html").read_text(encoding="utf8")) + ";\n\n"
(d / "worker.js").write_text(head + tail, encoding="utf8", newline="\n")
