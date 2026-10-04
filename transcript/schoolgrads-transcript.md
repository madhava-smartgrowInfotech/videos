# School Grads intro reel: transcript, sound design and SFX

- **Video:** `concepts/Schoolgrads/SchoolGrads-Reel-Intro-10s-with-sound.mp4` (1080×1920, 30fps, 10.00s). The silent version is `SchoolGrads-Reel-Intro-10s.mp4` in the same folder.
- **Audio status:** music bed and SFX are synthesised in code; the voice is the built-in Windows male voice at its natural pitch, as a placeholder.
- **Tempo:** 120 BPM (one beat every 0.5s).

## 1. Voiceover transcript

Total: 21 words. These are the timings used in the video. Tone to aim for with a better voice: warm and assured.

| Time | Line |
|---|---|
| 0.20–1.67s | "Building global learning institutions." |
| 2.30–3.23s | "Seven key dimensions." |
| 3.80–4.75s | "Forty plus countries." |
| 5.30–6.18s | "One million students." |
| 7.30–9.73s | "School Grads. Put your school in the front row." |

## 2. On-screen text transcript

| Time | Text on screen |
|---|---|
| 0.0–0.5s | School Grads (logo) |
| 0.5–2.0s | schoolgrads.ai · School Grads · Partnering with Schools to Build Global Learning Institutions · Transforming Indian education with global excellence. · Partner With Us |
| 2.0–3.5s | 7 key dimensions · Partnering with Schools · Curriculum · Teacher Training · Digital Tools · Leadership · 4/4 |
| 3.5–5.0s | Proven impact · 40+ · Countries |
| 5.0–7.5s | Our expertise areas. · Pedagogy · Digital · Training · Curriculum · Assessment · Analytics · 10+ Global Products · 1M+ Students · Code School Finland, GraphoGame, Kindiedays (logos) |
| 7.5–10.0s | School Grads (logo) · Put your school in the front row · Partner With Us · schoolgrads.ai |

## 3. Music and sound design

| Time | Layer | Direction |
|---|---|---|
| 0.0–2.0s | Music in | Starts on frame 0 with a soft sub pulse and a light plucked synth on the beat. No long intro; the logo is already on screen. |
| 2.0–5.0s | Build | Add a tight kick on every beat and a closed hi-hat on the off-beats. Keep it clean and minimal, modern tech feel. |
| 5.0–7.2s | Peak | Fullest section: add a bass note and a bright pad under the services and stats. |
| 7.2–7.5s | Drop-out | Music ducks or filters down under the wipe so the wipe SFX reads clearly. |
| 7.5–10.0s | Resolve | One sustained warm chord on the 7.5 beat, with a soft tail to 10.0. No new rhythmic elements; the end card is a hold. |

Overall mix: music sits about 10–12 dB under the voiceover; SFX sit between the two. Keep everything short and dry so it survives phone speakers.

## 4. SFX cue sheet

| Time | Picture event | SFX |
|---|---|---|
| 0.00s | Logo pill breathes out | Soft low "bloom" or sub swell |
| 0.22s | Pill unfolds into browser window | Quick airy whoosh, rising |
| 0.60s | Headline lines rise through masks | Four light ticks, staggered |
| 0.86s | Buttons pop in | Small soft pop |
| 1.50s | Cursor clicks "Partner With Us" | Crisp mouse click, then a short bright "confirm" tone as the button changes colour |
| 1.70s | Whip-pan to the checklist scene | Fast whoosh, left to right |
| 2.20s | Checklist tick 1 (Curriculum) | Short tick |
| 2.32s | Checklist tick 2 (Teacher Training) | Short tick, slightly higher |
| 2.44s | Checklist tick 3 (Digital Tools) | Short tick, higher again |
| 2.56s | Checklist tick 4 (Leadership) | Short tick, highest |
| 2.68s | "4/4" chip changes colour | Small success chime |
| 3.20s | Camera dollies down to the gauge | Low whoosh, downward |
| 3.52–3.94s | Ring fills while the counter runs to 40+ | Rising riser or pitch sweep, ending on the beat |
| 4.00s | Gauge pulse ring | Soft impact with a short ring-out |
| 3.45–3.95s | Speed streaks cross the frame | Two or three thin fast swishes |
| 4.76s | Fly-through of the gauge ring | Accelerating whoosh into a short "suck" |
| 5.02–5.20s | Six service tiles fly in | Rapid flutter of six soft taps |
| 5.50s | Stats card lands | Solid low thud |
| 5.36–5.86s | Counters run up to 10+ and 1M+ | Fast number ticker |
| 5.50–5.70s | Three partner logo pills rise in | Three soft pops |
| 5.98s | Numbers bump | Light accent hit |
| 7.14s | Navy then lime wipe rises | Big upward whoosh, two layers |
| 7.50s | Frame fully lime | Deep impact on the beat |
| 7.80s | Logo settles on the end card | Warm "arrival" tone |
| 7.84s | CTA pill pops in | Soft pop |
| 9.00s | Arrow nudges on the CTA | Very quiet tick (optional) |

## 5. Notes for whoever produces the audio

- All times are measured from the animation timeline, so they are frame-accurate at 30fps.
- The reel does not loop seamlessly. If it will loop on Instagram, end the music tail by about 9.8s so the restart is clean.
- To replace the voice, save new files over `audio/vo/schoolgrads-1.wav` to `schoolgrads-5.wav` and run `python audio/make_audio.py`.
