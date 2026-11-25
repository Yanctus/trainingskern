#!/bin/bash
# Lädt die Videos der Runde vom 25.11.2026 in den Drive (braucht einen gültigen Google-Schlüssel für www.googleapis.com).
cd "$(dirname "$0")"
U=1adLAJwAyhhvE9BT5b6Uj2wfLqGVvbrHA; SP=1NrOtcLDP6ixXSlpTuyB7GY0CKoi_4BvT
for f in out/kampagne-{48..55}-*.mp4; do case $f in *story*) ;; *) ./drive.sh "$f" $U video/mp4;; esac; done
for f in out/spielsystem-0{1,2}-*.mp4; do ./drive.sh "$f" $SP video/mp4; done
