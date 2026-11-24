#!/usr/bin/env python3
# Erzeugt VIDEOS.md: Übersicht aller Kampagnen-Videos, damit keine Übung doppelt verfilmt wird.
# Aufruf im Ordner story-studio:  python3 videoliste.py
import json, glob, os, re, subprocess
namen = {}
try: namen = {e["code"]: e["title"] for e in json.load(open("out/cache/einheiten.json"))}
except Exception: pass
alt = {}  # Namen aus der vorigen VIDEOS.md behalten, falls der Katalog-Cache fehlt
if os.path.exists("VIDEOS.md"):
    for c, n in re.findall(r"\| (UE-\d+) \| ([^|]+?) \|", open("VIDEOS.md").read()): alt[c] = n
def name(c): return namen.get(c) or alt.get(c) or ""
def laenge(n):
    f = f"out/{n}.mp4"
    if not os.path.exists(f): return ""
    try: return f"{float(subprocess.run(['ffprobe','-v','0','-show_entries','format=duration','-of','csv=p=0',f],capture_output=True,text=True).stdout):.0f} s"
    except Exception: return ""
altlaenge = {}
if os.path.exists("VIDEOS.md"):
    for n, l in re.findall(r"\| `(kampagne-[^`]+)` \|[^\n]*?\| (\d+ s) \|", open("VIDEOS.md").read()): altlaenge[n] = l
zeilen, eigen, kurz = [], {}, {}
for p in sorted(glob.glob("stories/kampagne-*.json")) + sorted(glob.glob("stories/spielsystem-*.json")):
    n = os.path.basename(p)[:-5]
    if n == "kampagne-01-kein-plan": continue  # alte Zeichentrick-Fassung, ersetzt durch -comic
    s = json.load(open(p)); nr = int(n.split("-")[1]) + (100 if n.startswith("spielsystem") else 0)
    sz = s["szenen"]; hook = next((z for z in sz if z["typ"] == "hook" and z.get("film")), {})
    text = " / ".join(z.replace("*", "") for z in hook.get("zeilen", [])) or hook.get("text", "").replace("*", "")
    codes = list(dict.fromkeys(z["code"] for z in sz if z.get("code")))
    # Marketing: Story-Block mit "art": "marketing"; die alten Videos ohne Story-Bilder fest
    uebung = not (s.get("storys", {}).get("art") == "marketing" or nr in (1, 7, 8))
    art = "Spielsystem" if nr > 100 else ("Übung" if uebung else "Marketing")
    for c in codes: (eigen if uebung or nr > 100 else kurz).setdefault(c, []).append(('S' + str(nr - 100).zfill(2)) if nr > 100 else f"{nr:02d}")
    st = s.get("storys", {}); frage = " ".join(st.get("frage", []))
    if st.get("art") == "marketing": frage = " ".join(st.get("problem", [])) + " → " + frage
    zeilen.append(f"| {('S' + str(nr - 100).zfill(2)) if nr > 100 else f'{nr:02d}'} | `{n}` | {art} | {', '.join(f'{c} {name(c)}'.strip() for c in codes)} | {hook.get('film','')} | {text} | {laenge(n) or altlaenge.get(n,'')} | {frage} |")
out = ["# Alle Kampagnen-Videos", "",
 "Automatisch erzeugt mit `python3 videoliste.py` (im Ordner `story-studio`). Nach jeder neuen Runde neu erzeugen.",
 "Zweck: Keine Übung doppelt verfilmen, Intros und Story-Fragen abwechseln.", "",
 "Alle Videos liegen im Drive „Trainingskern Videos“ (Übung → „Übungen“, Marketing → „Vermarktung“), Story-Bilder ab Nr. 12 in „Storys“.",
 "Was schon auf Instagram ist, zeigt der Drive-Ordner „Bereits geposted“.", "",
 "## Übungen mit eigenem Video (nicht noch einmal verfilmen)", "",
 "| Code | Übung | Video |", "|---|---|---|"]
out += [f"| {c} | {name(c)} | {', '.join(v)} |" for c, v in sorted(eigen.items())]
out += ["", "## Nur kurz angerissen (in Marketing-Videos, dürfen noch ein eigenes Video bekommen)", "", "| Code | Übung | Video |", "|---|---|---|"]
out += [f"| {c} | {name(c)} | {', '.join(v)} |" for c, v in sorted(kurz.items()) if c not in eigen]
out += ["", "## Alle Videos", "", "| Nr | Datei | Art | Übung(en) | Intro | Text im Intro | Länge | Story-Frage |", "|---|---|---|---|---|---|---|---|"] + zeilen
open("VIDEOS.md", "w").write("\n".join(out) + "\n")
print(f"VIDEOS.md: {len(zeilen)} Videos, {len(eigen)} Übungen mit eigenem Video, {len([c for c in kurz if c not in eigen])} nur angerissen")
