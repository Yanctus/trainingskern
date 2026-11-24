"""Erzeugt die Instagram-Stories (3 pro Tag) aus den Reel-Videos.

Aufruf: python3 make_stories.py <videos_dir> <out_dir>
Erwartet <videos_dir>/01.mp4 … 11.mp4 (Nummer = Kampagnen-Nummer).
"""
import subprocess
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

W, H = 1080, 1920
BG = (13, 13, 10)
CREAM = (245, 241, 231)
NEON = (212, 255, 0)
ORANGE = (255, 87, 34)
GREY = (150, 150, 140)
FONT_BLACK = "/usr/share/fonts/opentype/inter/InterDisplay-Black.otf"
FONT_BOLD = "/usr/share/fonts/opentype/inter/Inter-Bold.otf"
FONT_SEMI = "/usr/share/fonts/opentype/inter/Inter-SemiBold.otf"

# Tag -> (Video-Nr, Typ, Titel, Label Mittag, Text Mittag, Unterzeile Mittag)
DAYS = [
    (1, "01", "V", "Kein Plan?", "FRAGE AN DICH",
     "Wie lange brauchst du für deine Trainings­planung?", "Schreib uns deine Zeit. Wir sind gespannt."),
    (2, "05", "U", "Fangduell im Diamanten", "FRAGE AN DICH",
     "Wie startet dein Training?", "Runden laufen oder direkt mit Ball? Antworte per Nachricht."),
    (3, "03", "U", "Pressing-Rondo 4 gegen 2", "KURZ ERKLÄRT",
     "Zwei Kontakte. Acht Pässe. Ein Punkt.", "Die Rondo-Regel für heute. Das Reel kommt um 18:30."),
    (4, "04", "U", "3 gegen 2 zum Abschluss", "FRAGE AN DICH",
     "Spielt dein Team Überzahl sauber aus?", "Oder wird’s am Ende doch ein Solo? Schreib uns."),
    (5, "07", "V", "So läuft’s woanders", "FRAGE AN DICH",
     "Was nervt dich bei der Übungs­suche am meisten?", "Antworte per Nachricht. Wir lesen alles."),
    (6, "06", "U", "Pyramiden-Staffel", "FÜR DIE KLEINEN",
     "Wettkampf schlägt Warte­schlange.", "Staffeln mit Ball halten alle in Bewegung. Heute 18:30 im Reel."),
    (7, "09", "U", "Dritter Mann zum Abschluss", "COACHING-PUNKT",
     "Pass und Start im selben Moment.", "Das Timing macht den dritten Mann gefährlich. Heute 18:30 im Reel."),
    (8, "02", "U", "Pressing-Rondo: Aufbau", "SERIE · TEIL 2",
     "Pressing-Rondo in 20 Sekunden aufgebaut.", "Teil 1 verpasst? Schau auf unser Profil. Teil 2 kommt um 18:30."),
    (9, "08", "V", "Zeit für was Neues", "FRAGE AN DICH",
     "Wie oft machst du die gleichen Übungen?", "Ehrlich sein ist erlaubt. Schreib uns."),
    (10, "10", "U", "Dribbel-Dreieck mit Ablage", "COACHING-PUNKT",
     "Offen stehen. Erster Kontakt nach vorn.", "Der Schlüssel im Dribbel-Dreieck. Heute 18:30 im Reel."),
    (11, "11", "U", "Pressing-Rondo: Finale", "SERIE · TEIL 3",
     "Pressing-Rondo: Coaching und Steigerung.", "Das Finale der Serie. Heute 18:30."),
]


HOOK_T = {"01": 2.4, "07": 2.4, "08": 2.4}


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    """Umbruch an Leerzeichen, weichen Trennstellen (­) und Bindestrichen."""
    parts = []  # (text, space_before, soft_break_after)
    for w in text.split(" "):
        first = True
        for chunk in w.replace("-", "-\u0001").split("\u0001"):  # harte Bindestriche
            subs = chunk.split("­")                             # weiche Trennstellen
            for j, s in enumerate(subs):
                if s:
                    parts.append((s, first, j < len(subs) - 1))
                    first = False
    lines, cur, cur_soft = [], "", False
    for p, space, soft in parts:
        test = cur + (" " if space and cur else "") + p
        if not cur or draw.textlength(test + ("-" if soft else ""), font=fnt) <= max_w:
            cur, cur_soft = test, soft
        else:
            lines.append(cur + ("-" if cur_soft else ""))
            cur, cur_soft = p, soft
    lines.append(cur)
    return lines


def fit_lines(draw, text, path, size, max_w, min_size=72):
    while size > min_size:
        fnt = font(path, size)
        lines = wrap(draw, text, fnt, max_w)
        if all(draw.textlength(l, font=fnt) <= max_w for l in lines) and len(lines) <= 5:
            return fnt, lines, size
        size -= 6
    fnt = font(path, size)
    return fnt, wrap(draw, text, fnt, max_w), size


def ffprobe_duration(path):
    out = subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                                   "-of", "csv=p=0", str(path)])
    return float(out)


def grab(video, t, out):
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", f"{t:.2f}", "-i", str(video),
                    "-frames:v", "1", str(out)], check=True)
    return Image.open(out).convert("RGB")


def logo_from(video, tmp):
    """Schneidet das TRAININGSKERN-Badge aus einem Übungs-Frame aus."""
    im = grab(video, 14, tmp / "logo_src.png")
    return im.crop((60, 255, 482, 348))


def banner(draw, y, top, bottom, top_fill=NEON, top_color=BG):
    f1, f2 = font(FONT_BLACK, 96), font(FONT_BOLD, 42)
    pad = 28
    tw = draw.textlength(top, font=f1)
    draw.rectangle((72 + 14, y + 14, 72 + tw + 2 * pad + 14, y + 130 + 14), fill=ORANGE)
    draw.rectangle((72, y, 72 + tw + 2 * pad, y + 130), fill=top_fill)
    draw.text((72 + pad, y + 10), top, font=f1, fill=top_color)
    size = 42
    while draw.textlength(bottom, font=f2) > W - 150 and size > 28:
        size -= 2
        f2 = font(FONT_BOLD, size)
    draw.text((76, y + 168), bottom, font=f2, fill=CREAM)


def story_morgen(day, vid, typ, title, video, out, tmp):
    dur = ffprobe_duration(video)
    if typ == "V":
        im = grab(video, HOOK_T[vid], tmp / "m.png")  # Hook-Frame, wenn der Text steht
    else:
        # Komplett-Videos starten direkt mit dem Feld, Übungs-Videos haben vorne einen Hook
        t = dur * 0.22 if vid in ("09", "10", "11") else dur * 0.45
        im = grab(video, t, tmp / "m.png")
    ov = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    od = ImageDraw.Draw(ov)
    od.rectangle((0, 1440, W, 1720), fill=(13, 13, 10, 235))
    im = Image.alpha_composite(im.convert("RGBA"), ov).convert("RGB")
    d = ImageDraw.Draw(im)
    sub = "Neues Reel: " + title if typ == "U" else "Neu bei Trainingskern. Nicht verpassen."
    banner(d, 1468, "HEUTE 18:30", sub)
    im.save(out, quality=92)


def story_mittag(label, text, sub, logo, out):
    im = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(im)
    # dezentes Raster wie im Video-Look
    for yy in range(0, H, 36):
        for xx in range(0, W, 36):
            d.point((xx, yy), fill=(30, 30, 26))
    im.paste(logo, (60, 300))
    fl = font(FONT_BOLD, 40)
    lw = d.textlength(label, font=fl)
    d.rectangle((72, 470, 72 + lw + 36, 532), fill=NEON)
    d.text((90, 476), label, font=fl, fill=BG)
    fq, lines, size = fit_lines(d, text.upper(), FONT_BLACK, 112, W - 150)
    y = 580
    for i, line in enumerate(lines):
        col = NEON if i == len(lines) - 1 else CREAM
        d.text((72, y), line, font=fq, fill=col)
        y += int(size * 1.1)
    d.rectangle((72, y + 30, 222, y + 42), fill=ORANGE)
    fs = font(FONT_SEMI, 46)
    y += 80
    for line in wrap(d, sub, fs, W - 150):
        d.text((72, y), line, font=fs, fill=CREAM)
        y += 62
    fa = font(FONT_BOLD, 40)
    d.text((72, 1560), "trainingskern.de  ·  Link in Bio", font=fa, fill=GREY)
    im.save(out, quality=92)


# Zeitpunkte (Sekunden) für das Abend-Bild der Vermarktungs-Videos: Produkt-Szene statt Hook
EVENING_V_T = {"01": 10.3, "07": 21.2, "08": 21.0}


def story_abend(typ, vid, video, out, tmp):
    """Abend-Story als Bild: andere Szene aus dem Reel als morgens + JETZT NEU.

    (Video-Ausschnitte wurden verworfen: die Sprache läuft im Reel durch, jeder Schnitt klingt falsch.)
    """
    dur = ffprobe_duration(video)
    if typ == "V":
        t = EVENING_V_T[vid]
    elif vid in ("09", "10", "11"):
        t = dur * 0.60   # Komplett-Videos: Coaching-Punkt / Steigerung
    else:
        t = dur * 0.72   # späterer Schritt als morgens (45 %)
    im = grab(video, t, tmp / "a.png")
    ov = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(ov).rectangle((0, 1440, W, 1720), fill=(13, 13, 10, 235))
    im = Image.alpha_composite(im.convert("RGBA"), ov).convert("RGB")
    d = ImageDraw.Draw(im)
    sub = "Jetzt auf dem Profil. Link in Bio." if typ == "V" else "Ganzes Reel auf dem Profil."
    banner(d, 1468, "JETZT NEU", sub)
    im.save(out, quality=92)


def main(videos_dir, out_dir):
    videos_dir, out_dir = Path(videos_dir), Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    tmp = out_dir / "_tmp"
    tmp.mkdir(exist_ok=True)
    logo = logo_from(videos_dir / "05.mp4", tmp)
    for day, vid, typ, title, label, text, sub in DAYS:
        v = videos_dir / f"{vid}.mp4"
        p = f"tag{day:02d}"
        story_morgen(day, vid, typ, title, v, out_dir / f"{p}_1_morgen_0900.jpg", tmp)
        story_mittag(label, text, sub, logo, out_dir / f"{p}_2_mittag_1230.jpg")
        story_abend(typ, vid, v, out_dir / f"{p}_3_abend_1845.jpg", tmp)
        print("fertig", p)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
