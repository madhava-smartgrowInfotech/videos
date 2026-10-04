# Intro reels: InboxTales, SmartGrow Infotech and School Grads

10-second Instagram Reel intros (9:16, 1080×1920, 30fps, H.264, exactly 10.00s). Each reel is an HTML/GSAP animation rendered frame by frame in headless Chrome and encoded with ffmpeg.

Project root: `C:\Users\Admin\Documents\ibt`

All paths below are full paths.

## 1. Videos

### InboxTales (inboxtales.com)

| Version | Path |
|---|---|
| Final, with sound and voice | `C:\Users\Admin\Documents\ibt\InboxTales-Reel-Intro-10s-with-sound.mp4` |
| Final, silent | `C:\Users\Admin\Documents\ibt\InboxTales-Reel-Intro-10s.mp4` |
| Final, silent (renderer's copy, identical) | `C:\Users\Admin\Documents\ibt\out\final.mp4` |
| Alternate concept: product (unpolished original of the winner) | `C:\Users\Admin\Documents\ibt\out\product.mp4` |
| Alternate concept: kinetic type | `C:\Users\Admin\Documents\ibt\out\kinetic.mp4` |
| Alternate concept: dark-to-light contrast | `C:\Users\Admin\Documents\ibt\out\contrast.mp4` |

The three alternate concepts are silent, first-pass versions.

### SmartGrow Infotech (smartgrowinfotech.com)

| Version | Path |
|---|---|
| With sound and voice | `C:\Users\Admin\Documents\ibt\concepts\smartgrow\SmartGrow-Reel-Intro-10s-with-sound.mp4` |
| Silent | `C:\Users\Admin\Documents\ibt\concepts\smartgrow\SmartGrow-Reel-Intro-10s.mp4` |
| Silent (renderer's copy, identical) | `C:\Users\Admin\Documents\ibt\out\smartgrow.mp4` |

### School Grads (schoolgrads.ai)

| Version | Path |
|---|---|
| With sound and voice | `C:\Users\Admin\Documents\ibt\concepts\Schoolgrads\SchoolGrads-Reel-Intro-10s-with-sound.mp4` |
| Silent | `C:\Users\Admin\Documents\ibt\concepts\Schoolgrads\SchoolGrads-Reel-Intro-10s.mp4` |
| Silent (renderer's copy, identical) | `C:\Users\Admin\Documents\ibt\out\Schoolgrads.mp4` |

## 2. Transcripts

Each file has the same five sections: voiceover transcript, on-screen text transcript, music and sound design, SFX cue sheet, production notes.

| Brand | Path |
|---|---|
| InboxTales | `C:\Users\Admin\Documents\ibt\transcript\inboxtales-transcript.md` |
| SmartGrow Infotech | `C:\Users\Admin\Documents\ibt\transcript\smartgrow-transcript.md` |
| School Grads | `C:\Users\Admin\Documents\ibt\transcript\schoolgrads-transcript.md` |

### Voiceover as recorded

**InboxTales**

| Time | Line |
|---|---|
| 0.20–1.69s | "Digital excellence, redefined." |
| 2.20–3.11s | "Built by bug hunters." |
| 3.70–4.38s | "Lightning fast." |
| 5.30–6.51s | "Not just another web agency." |
| 7.25–9.64s | "InboxTales. Let's build the extraordinary." |

**SmartGrow Infotech**

| Time | Line |
|---|---|
| 0.20–2.19s | "We engineer products for companies that mean business." |
| 2.45–4.13s | "End to end. One standard." |
| 5.30–6.67s | "Nine services, one team." |
| 7.80–9.56s | "SmartGrow. Ready when you are." |

**School Grads**

| Time | Line |
|---|---|
| 0.20–1.67s | "Building global learning institutions." |
| 2.30–3.23s | "Seven key dimensions." |
| 3.80–4.75s | "Forty plus countries." |
| 5.30–6.18s | "One million students." |
| 7.30–9.73s | "School Grads. Put your school in the front row." |

## 3. Audio

### Mixed sound files (music bed, SFX and voice)

| Brand | Path |
|---|---|
| InboxTales | `C:\Users\Admin\Documents\ibt\audio\inboxtales-sound.wav` |
| SmartGrow Infotech | `C:\Users\Admin\Documents\ibt\audio\smartgrow-sound.wav` |
| School Grads | `C:\Users\Admin\Documents\ibt\audio\schoolgrads-sound.wav` |

### Voiceover lines

Folder: `C:\Users\Admin\Documents\ibt\audio\vo`

| Brand | Files |
|---|---|
| InboxTales | `inboxtales-1.wav` to `inboxtales-5.wav` |
| SmartGrow Infotech | `smartgrow-1.wav` to `smartgrow-4.wav` |
| School Grads | `schoolgrads-1.wav` to `schoolgrads-5.wav` |

The voice is the built-in Windows male voice (Microsoft David) at its natural pitch. It is a placeholder: to use a better voice, save new files over these with the same names and run the audio script.

### Audio script

`C:\Users\Admin\Documents\ibt\audio\make_audio.py` synthesises the music bed and SFX in code, mixes in the voiceover lines, and writes the three sound files.

## 4. Source files

### Animation pages

| Reel | Path |
|---|---|
| InboxTales final | `C:\Users\Admin\Documents\ibt\concepts\final\index.html` |
| SmartGrow Infotech | `C:\Users\Admin\Documents\ibt\concepts\smartgrow\index.html` |
| School Grads | `C:\Users\Admin\Documents\ibt\concepts\Schoolgrads\index.html` |
| InboxTales concept: product | `C:\Users\Admin\Documents\ibt\concepts\product\index.html` |
| InboxTales concept: kinetic | `C:\Users\Admin\Documents\ibt\concepts\kinetic\index.html` |
| InboxTales concept: contrast | `C:\Users\Admin\Documents\ibt\concepts\contrast\index.html` |
| Minimal template | `C:\Users\Admin\Documents\ibt\concepts\_template\index.html` |

### Brand assets

| Brand | Path | Contents |
|---|---|---|
| InboxTales | `C:\Users\Admin\Documents\ibt\assets` | `logo-mark.png` and seven site photos |
| SmartGrow Infotech | `C:\Users\Admin\Documents\ibt\concepts\smartgrow\assets` | `logo-horizontal.png`, `logo-mark.png`, `office.jpg` |
| SmartGrow Infotech fonts | `C:\Users\Admin\Documents\ibt\concepts\smartgrow\fonts` | Satoshi 500, 700, 900 |
| School Grads | `C:\Users\Admin\Documents\ibt\concepts\Schoolgrads\assets` | `logos`, `gallery`, `images`, `partners`, `team` |

### Pipeline

| File | Path |
|---|---|
| Renderer | `C:\Users\Admin\Documents\ibt\render.mjs` |
| Shared fonts and brand tokens | `C:\Users\Admin\Documents\ibt\shared\base.css` |
| Seek harness | `C:\Users\Admin\Documents\ibt\shared\reel.js` |
| Dependencies | `C:\Users\Admin\Documents\ibt\package.json` |

## 5. Review images

Contact sheets show one frame every 0.5s. The `contact-safe.png` versions overlay the Instagram UI zones.

| Reel | Contact sheet | Individual stills |
|---|---|---|
| InboxTales final | `C:\Users\Admin\Documents\ibt\out\final\contact.png` | `C:\Users\Admin\Documents\ibt\out\final\stills` |
| SmartGrow Infotech | `C:\Users\Admin\Documents\ibt\out\smartgrow\contact.png` | `C:\Users\Admin\Documents\ibt\out\smartgrow\stills` |
| School Grads | `C:\Users\Admin\Documents\ibt\out\Schoolgrads\contact.png` | `C:\Users\Admin\Documents\ibt\out\Schoolgrads\stills` |

## 6. Commands

Run from the project root. Replace `Schoolgrads` with `final` (InboxTales) or `smartgrow` as needed.

Preview in a browser (space pauses, `s` shows the Instagram safe zones):

```bash
node render.mjs --serve
```

Render a contact sheet of stills:

```bash
node render.mjs Schoolgrads --stills
```

Render the silent MP4 to `out/<name>.mp4`:

```bash
node render.mjs Schoolgrads --video
```

Rebuild all three sound files:

```bash
python audio/make_audio.py
```

Merge sound into a video (School Grads shown):

```bash
./node_modules/ffmpeg-static/ffmpeg.exe -y -i out/Schoolgrads.mp4 -i audio/schoolgrads-sound.wav -map 0:v -map 1:a -c:v copy -c:a aac -b:a 192k -t 10 -movflags +faststart concepts/Schoolgrads/SchoolGrads-Reel-Intro-10s-with-sound.mp4
```

| Reel | Silent input | Sound file | Output |
|---|---|---|---|
| InboxTales | `out/final.mp4` | `audio/inboxtales-sound.wav` | `InboxTales-Reel-Intro-10s-with-sound.mp4` |
| SmartGrow Infotech | `out/smartgrow.mp4` | `audio/smartgrow-sound.wav` | `concepts/smartgrow/SmartGrow-Reel-Intro-10s-with-sound.mp4` |
| School Grads | `out/Schoolgrads.mp4` | `audio/schoolgrads-sound.wav` | `concepts/Schoolgrads/SchoolGrads-Reel-Intro-10s-with-sound.mp4` |

## 7. Known limits

- None of the reels loops seamlessly.
- Around 5.0s the frame is nearly empty for about a quarter second during the ring fly-through.
- The sound was checked by level measurements only, not by ear. The music and SFX are synthesised and simple; the voice is synthetic.
- Only the InboxTales final went through independent QA. SmartGrow and School Grads were checked on rendered stills.
- The SmartGrow office photo comes from their site and appears to be a stock image.
- The School Grads photos are named as classroom shots but show signing ceremonies and a stage event, so the six tiles look repetitive and don't match their labels well.
