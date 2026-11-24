#!/usr/bin/env python3
# Prüft, ob die Aufnahmen einer Übung noch zum aktuellen Text passen (alte Aufnahmen sagen z. B. „Neon vier“ oder „Rot acht“).
# Aufruf im Ordner story-studio:  python3 tonpruefung.py [UE-123 ...]   (ohne Angabe: alle)
# Liest den Katalog aus out/cache/einheiten.json (frisch holen: node studio.mjs ... --neu, oder curl wie in studio.mjs).
import json, re, sys
d = json.load(open("out/cache/einheiten.json"))
ALT = re.compile(r"(?<!Team )\b(Neon|Rot|Orange) (eins|zwei|drei|vier|fünf|sechs|sieben|acht|neun|zehn|elf|\d+)\b")
def sagt(b): return [(s.get("say") or s.get("label") or "").strip() for s in (b or {}).get("steps") or []]
codes = set(sys.argv[1:]); schlecht = 0
for e in sorted(d, key=lambda e: e.get("code") or ""):
    if codes and e.get("code") not in codes: continue
    ch = (e.get("audio") or {}).get("chapters") or []
    soll = [sagt(e.get("board"))] + [sagt(v.get("board")) for v in e.get("versions") or []]
    abw = sum(1 for i, c in enumerate(ch) if i < len(soll) for x, y in zip(c.get("steps_text") or [], soll[i]) if x.strip() != y)
    alt = bool(ALT.search(" ".join(t for c in ch for t in c.get("steps_text") or [])))
    springer = "Springer" in json.dumps(e, ensure_ascii=False)
    if abw or alt or springer or e.get("wartet_auf_ton"):
        schlecht += 1
        print(f"NICHT VERFILMEN {e.get('code')} {e.get('title')}: " + ", ".join(x for x in [
            f"{abw} Aufnahmen passen nicht zum Text" if abw else "", "alte Namen (Neon/Rot + Nummer) im Ton" if alt else "",
            "sagt Springer" if springer else "", "wartet auf Ton" if e.get("wartet_auf_ton") else ""] if x))
    elif codes: print(f"ok {e.get('code')} {e.get('title')}")
print(f"{schlecht} Übungen mit Ton-Problem")
