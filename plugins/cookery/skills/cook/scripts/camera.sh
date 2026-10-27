#!/bin/sh
set -eu

# First open the top-down iPhone preview in QuickTime.
folder=${1:-${TMPDIR:-/tmp}/cookery}
mkdir -p "$folder"

window_id=$(osascript -l JavaScript <<'JXA'
ObjC.import('CoreGraphics');
var windows = ObjC.deepUnwrap(ObjC.castRefToObject($.CGWindowListCopyWindowInfo($.kCGWindowListOptionAll, $.kCGNullWindowID)));
var camera = windows.filter(function(w) {
  return w.kCGWindowOwnerName === 'QuickTime Player' && w.kCGWindowName === 'Movie Recording';
});
if (camera.length !== 1) throw new Error('Open exactly one QuickTime Movie Recording preview.');
String(camera[0].kCGWindowNumber);
JXA
)

echo "Saving pictures to $folder every five seconds. Stop with Ctrl+C."
while true; do
  picture="$folder/$(date -u +%Y%m%dT%H%M%SZ).jpg"
  screencapture -x -o -l "$window_id" -t jpg "$picture"
  cp "$picture" "$folder/.latest.jpg"
  mv -f "$folder/.latest.jpg" "$folder/latest.jpg"
  sleep 5
done
