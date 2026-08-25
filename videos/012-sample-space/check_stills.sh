#!/usr/bin/env bash
set -e
cd ~/math/notebooks/probability/manim/012-sample-space
D=media/videos/script/480p15
S=media/videos/stills
rm -f $S/*.png

extract() {  # extract <video> <name> <frac>
  local dur
  dur=$(ffprobe -v error -show_entries format=duration -of csv=p=0 $D/$1.mp4)
  local ts
  ts=$(python3 -c "print(max(0, float('$dur') * $3))")
  ffmpeg -y -v error -ss "$ts" -i $D/$1.mp4 -frames:v 1 $S/$2.png
}

extract Scene1_DartboardAnalogy s1_title 0.25
extract Scene1_DartboardAnalogy s1_end  0.93
extract Scene2_FormalDefinition s2_dots 0.30
extract Scene3_DieExample       s3_omega 0.45
extract Scene3_DieExample       s3_event 0.90
extract Scene4_CoinFlipEvents   s4_allH 0.52
extract Scene4_CoinFlipEvents   s4_map 0.95
extract Scene5_TraderScaleUp    s5_omega 0.55

for f in s1_title s1_end s2_dots s3_omega s3_event s4_allH s4_map s5_omega; do
  printf '%s: ' "$f"
  ffprobe -v error -f lavfi "movie=$S/$f.png,signalstats" \
    -show_entries frame_tags=lavfi.signalstats.YAVG,lavfi.signalstats.YMAX \
    -of csv=p=0 -read_intervals '%+#1'
done

total=0
for v in Scene1_DartboardAnalogy Scene2_FormalDefinition Scene3_DieExample Scene4_CoinFlipEvents Scene5_TraderScaleUp; do
  d=$(ffprobe -v error -show_entries format=duration -of csv=p=0 $D/$v.mp4)
  printf '%s: %ss\n' "$v" "$d"
  total=$(python3 -c "print($total + $d)")
done
printf 'TOTAL: %ss\n' "$total"
