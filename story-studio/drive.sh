#!/bin/bash
# Lädt eine Datei in einen Drive-Ordner: drive.sh <datei> <ordner-id> <mime>. Der Schlüssel kommt aus der Umgebung (nie in diese Datei schreiben).
m=$(mktemp); printf '{"name":"%s","parents":["%s"]}' "$(basename "$1")" "$2" > "$m"
r=$(curl -sS -m 300 -X POST "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart&fields=id,name" -H "Authorization: Bearer proxy-injected" -F "metadata=@$m;type=application/json" -F "file=@$1;type=$3"); rm -f "$m"
echo "$r" | grep -q '"id"' && echo "ok $(basename "$1")" || { echo "FEHLER $(basename "$1") $(echo $r | cut -c1-150)"; exit 1; }
