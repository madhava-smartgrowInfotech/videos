"""Synthesises the sound design (music bed + SFX, no voiceover) for both reels.

Cue times follow transcript/*-transcript.md. Output: audio/<name>-sound.wav
    python audio/make_audio.py
"""
import wave
import numpy as np

SR = 48000
DUR = 10.0
N = int(SR * DUR)
rng = np.random.default_rng(7)


def t_of(d):
    return np.arange(int(SR * d)) / SR


def env_decay(d, tau, attack=0.002):
    t = t_of(d)
    return np.minimum(t / attack, 1.0) * np.exp(-t / tau)


def lowpass(x, cutoff):
    """One-pole low-pass; cutoff may be a scalar or a per-sample array (Hz)."""
    a = 1.0 - np.exp(-2 * np.pi * np.broadcast_to(cutoff, x.shape) / SR)
    y = np.empty_like(x)
    acc = 0.0
    for i in range(len(x)):
        acc += a[i] * (x[i] - acc)
        y[i] = acc
    return y


def sweep(f0, f1, d):
    t = t_of(d)
    f = f0 * (f1 / f0) ** (t / d)
    return np.sin(2 * np.pi * np.cumsum(f) / SR)


# ---- instruments -----------------------------------------------------------
def tick(freq=2000, d=0.06):
    return np.sin(2 * np.pi * freq * t_of(d)) * env_decay(d, 0.012)


def click():
    d = 0.05
    return (rng.standard_normal(int(SR * d)) * env_decay(d, 0.003) * 0.7
            + np.sin(2 * np.pi * 3200 * t_of(d)) * env_decay(d, 0.006))


def pop():
    d = 0.12
    return sweep(620, 220, d) * env_decay(d, 0.035)


def chime(f=880.0, d=0.6):
    t = t_of(d)
    return (np.sin(2 * np.pi * f * t) + 0.6 * np.sin(2 * np.pi * f * 1.5 * t)
            + 0.3 * np.sin(2 * np.pi * f * 2 * t)) * env_decay(d, 0.16) / 1.9


def thud(d=0.35):
    return sweep(95, 38, d) * env_decay(d, 0.09, attack=0.004)


def impact():
    d = 0.7
    noise = lowpass(rng.standard_normal(int(SR * d)), 900) * env_decay(d, 0.08) * 1.5
    return sweep(110, 32, d) * env_decay(d, 0.2, attack=0.004) + noise


def whoosh(d=0.5, f0=400, f1=5000, peak=0.6):
    """Filtered-noise sweep; `peak` is where the loudness crest sits (0..1)."""
    n = int(SR * d)
    t = np.arange(n) / n
    cutoff = f0 * (f1 / f0) ** t
    amp = np.where(t < peak, (t / peak) ** 2, ((1 - t) / (1 - peak)) ** 1.5)
    return lowpass(rng.standard_normal(n), cutoff) * amp * 1.1


def riser(d=0.42):
    t = t_of(d)
    return sweep(280, 1250, d) * (t / d) ** 1.5 * 0.8 + whoosh(d, 600, 6000, 0.95) * 0.5


def ticker(d=0.5, step=0.035):
    out = np.zeros(int(SR * d))
    for k in range(int(d / step)):
        tk = tick(2600 + 40 * k, 0.02) * 0.5
        i = int(k * step * SR)
        out[i:i + len(tk)] += tk[:len(out) - i]
    return out


def bloom(d=0.6):
    t = t_of(d)
    return (np.sin(2 * np.pi * 110 * t) + 0.5 * np.sin(2 * np.pi * 220 * t)) * np.sin(np.pi * t / d) ** 2 * 0.7


def tone(freqs, d, attack=0.03, tau=0.9):
    t = t_of(d)
    s = sum(np.sin(2 * np.pi * f * t) / (1 + 0.35 * i) for i, f in enumerate(freqs))
    return s / len(freqs) * np.minimum(t / attack, 1.0) * np.exp(-t / tau)


def kick():
    d = 0.22
    return sweep(150, 46, d) * env_decay(d, 0.07, attack=0.001)


def hat():
    d = 0.05
    x = rng.standard_normal(int(SR * d))
    return (x - lowpass(x, 6000)) * env_decay(d, 0.012)


def pluck(f, d=0.35):
    t = t_of(d)
    return (np.sin(2 * np.pi * f * t) + 0.4 * np.sin(2 * np.pi * 2 * f * t)) * env_decay(d, 0.09) / 1.4


# ---- mixer -----------------------------------------------------------------
PITCH = 1.0    # voiceover pitch factor: 1 keeps the voice natural; below 1 deepens and slows it


def load_vo(path):
    """Reads a mono 16-bit WAV, trims silence, deepens the pitch and resamples to SR."""
    with wave.open(path, 'rb') as w:
        sr = w.getframerate()
        x = np.frombuffer(w.readframes(w.getnframes()), dtype='<i2').astype(np.float64) / 32768
    loud = np.where(np.abs(x) > 0.01)[0]
    x = x[max(loud[0] - int(0.01 * sr), 0):loud[-1] + int(0.05 * sr)]
    n_out = int(len(x) / sr * SR / PITCH)
    y = np.interp(np.linspace(0, len(x) - 1, n_out), np.arange(len(x)), x)
    return y / np.max(np.abs(y))


class Mix:
    def __init__(self):
        self.l = np.zeros(N)
        self.r = np.zeros(N)
        self.vo = np.zeros(N)

    def say(self, at, path, gain=0.9):
        sig = load_vo(path)
        i = int(at * SR)
        sig = sig[:N - i] * gain
        self.vo[i:i + len(sig)] += sig
        print(f'  {path}: {at:.2f} -> {at + len(sig) / SR:.2f}s')

    def add(self, at, sig, gain=1.0, pan=0.0):
        """pan: -1 left .. +1 right (equal power)."""
        i = int(at * SR)
        if i >= N:
            return
        sig = sig[:N - i] * gain
        ang = (pan + 1) * np.pi / 4
        self.l[i:i + len(sig)] += sig * np.cos(ang) * 1.414
        self.r[i:i + len(sig)] += sig * np.sin(ang) * 1.414

    def write(self, path):
        # duck the bed under the voiceover
        active = (np.abs(self.vo) > 0.02).astype(np.float64)
        win = int(0.12 * SR)
        duck = 1.0 - 0.5 * np.minimum(np.convolve(active, np.ones(win), 'same') / (win * 0.25), 1.0)
        st = np.stack([self.l * duck + self.vo, self.r * duck + self.vo], axis=1)
        fade = int(0.2 * SR)
        st[-fade:] *= np.linspace(1, 0, fade)[:, None]      # clean tail for looping
        st = np.tanh(st * 1.1)                              # soft limiter
        st = st / np.max(np.abs(st)) * 0.7                  # about -3 dBFS peak, headroom for AAC
        with wave.open(path, 'wb') as w:
            w.setnchannels(2)
            w.setsampwidth(2)
            w.setframerate(SR)
            w.writeframes((st * 32767).astype('<i2').tobytes())


A3, C4, E4, G4, A4, C5, D5, E5, G5 = 220.0, 261.63, 329.63, 392.0, 440.0, 523.25, 587.33, 659.25, 783.99


def music(m):
    """120 BPM bed: pulse from 0, kick + hats from 2.0, pad from 5.0, duck at 7.2, chord at 7.5."""
    seq = [A4, E5, C5, E5, A4, G5, E5, C5]
    for k in range(29):                                    # eighth notes, 0.0 .. 7.0
        at = k * 0.25
        m.add(at, pluck(seq[k % 8]), 0.16 if k % 2 == 0 else 0.10, pan=0.35 if k % 2 else -0.35)
    for b in range(15):                                    # beats, 0.0 .. 7.0
        at = b * 0.5
        m.add(at, tone([55.0], 0.3, attack=0.005, tau=0.1), 0.45)
        if at >= 2.0:
            m.add(at, kick(), 0.55)
            m.add(at + 0.25, hat(), 0.16, pan=0.2)
    pad = tone([A3, C4, E4, G4], 2.4, attack=0.25, tau=3.0)
    pad[-int(0.3 * SR):] *= np.linspace(1, 0, int(0.3 * SR))
    m.add(5.0, pad, 0.22)
    for b in range(5):                                     # bass under the peak section
        m.add(5.0 + b * 0.5, tone([110.0, 220.0], 0.4, attack=0.005, tau=0.18), 0.3)
    m.add(7.5, tone([130.81, 196.0, C4, E4, G4, D5], 2.5, attack=0.02, tau=2.2), 0.6)


def sfx_common(m):
    """Cues shared by both reels (same animation timeline)."""
    m.add(0.00, bloom(), 0.5)
    m.add(0.22, whoosh(0.45, 500, 6000, 0.5), 0.30)
    m.add(0.86, pop(), 0.35)
    m.add(1.50, click(), 0.5, pan=-0.2)
    m.add(1.53, chime(1046.5, 0.4), 0.22, pan=-0.2)
    m.add(1.70, whoosh(0.6, 300, 7000, 0.45), 0.45, pan=0.3)
    m.add(3.20, whoosh(0.6, 5000, 250, 0.4), 0.40)
    m.add(3.52, riser(), 0.35)
    m.add(4.00, impact(), 0.35)
    m.add(4.02, chime(783.99, 0.7), 0.16)
    for i, at in enumerate([3.47, 3.55, 3.63]):
        m.add(at, whoosh(0.22, 2500, 9000, 0.5), 0.12, pan=[-0.6, 0.6, 0.0][i])
    m.add(4.76, whoosh(0.5, 250, 8000, 0.85), 0.5)
    for i in range(6):
        m.add(5.02 + i * 0.035, pop(), 0.2, pan=[-0.1, 0.0, -0.6, 0.6, -0.3, 0.5][i])
    m.add(5.36, ticker(0.5), 0.22)
    m.add(5.50, thud(), 0.6)
    m.add(5.98, tick(1500, 0.08), 0.25)
    m.add(7.10, whoosh(0.5, 200, 6000, 0.8), 0.6)
    m.add(7.16, whoosh(0.45, 400, 9000, 0.8), 0.3, pan=0.3)
    m.add(7.50, impact(), 0.7)
    m.add(7.84, pop(), 0.3)
    m.add(9.00, tick(1800, 0.04), 0.08)


def inboxtales():
    m = Mix()
    music(m)
    sfx_common(m)
    for i in range(3):                                     # three headline lines
        m.add(0.60 + i * 0.05, tick(1700 + 150 * i), 0.14)
    for i, at in enumerate([2.20, 2.35, 2.50]):            # checklist ticks
        m.add(at, tick(1900 + 260 * i, 0.08), 0.35, pan=-0.3)
    m.add(2.60, chime(1318.5, 0.5), 0.25)
    scan = whoosh(0.75, 1500, 3500, 0.5)
    m.add(2.20, scan, 0.07, pan=0.2)
    for at, k in [(0.2, 1), (2.2, 2), (3.7, 3), (5.3, 4), (7.25, 5)]:
        m.say(at, f'audio/vo/inboxtales-{k}.wav')
    m.write('audio/inboxtales-sound.wav')


def smartgrow():
    m = Mix()
    music(m)
    sfx_common(m)
    for i in range(4):                                     # four headline lines
        m.add(0.60 + i * 0.05, tick(1700 + 130 * i), 0.14)
    for i in range(3):                                     # tech-stack pills
        m.add(2.05 + i * 0.06, whoosh(0.16, 2000, 7000, 0.5), 0.10, pan=0.4)
    for i, at in enumerate([2.20, 2.32, 2.44, 2.56]):      # checklist ticks
        m.add(at, tick(1900 + 220 * i, 0.08), 0.35, pan=-0.3)
    m.add(2.68, chime(1318.5, 0.5), 0.25)
    for i in range(3):                                     # service pills
        m.add(5.50 + i * 0.06, pop(), 0.14, pan=-0.4 + 0.4 * i)
    for at, k in [(0.2, 1), (2.45, 2), (5.3, 3), (7.8, 4)]:
        m.say(at, f'audio/vo/smartgrow-{k}.wav')
    m.write('audio/smartgrow-sound.wav')


def schoolgrads():
    m = Mix()
    music(m)
    sfx_common(m)
    for i in range(4):                                     # four headline lines
        m.add(0.60 + i * 0.05, tick(1700 + 130 * i), 0.14)
    for i, at in enumerate([2.20, 2.32, 2.44, 2.56]):      # checklist ticks
        m.add(at, tick(1900 + 220 * i, 0.08), 0.35, pan=-0.3)
    m.add(2.68, chime(1318.5, 0.5), 0.25)
    for i in range(3):                                     # partner logo pills
        m.add(5.50 + i * 0.06, pop(), 0.14, pan=-0.4 + 0.4 * i)
    for at, k in [(0.2, 1), (2.3, 2), (3.8, 3), (5.3, 4), (7.3, 5)]:
        m.say(at, f'audio/vo/schoolgrads-{k}.wav')
    m.write('audio/schoolgrads-sound.wav')


if __name__ == '__main__':
    inboxtales()
    smartgrow()
    schoolgrads()
    print('wrote audio/inboxtales-sound.wav, audio/smartgrow-sound.wav, audio/schoolgrads-sound.wav')
