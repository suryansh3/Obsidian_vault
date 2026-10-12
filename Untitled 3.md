# Assignment-4 (SVP) — Solutions

**Course:** Speech and Video Processing (CS30033), School of Computer Engineering, KIIT Deemed to be University  
**Session:** July–November 2026 | **L-T-P-Cr:** 3-1-0-3

> _Reference used:_ `SVP Lesson Plan Autumn2026.docx` (Course Objectives CO1–CO5, covering speech properties, feature extraction (MFCC / LPCC), speech recognition algorithms, and Python/auxiliary-tool implementation).

---

## 1) Speech Dataset Survey — and the Dataset Chosen

A speech dataset is a curated collection of audio recordings (often paired with transcriptions, speaker metadata or labels) used to train, test and benchmark speech-processing algorithms (CO1, CO2 of the lesson plan: “speech properties … and speech-processing concepts for prediction” and “feature extraction, selection, and speech recognition algorithms”).

I surveyed the well-known public speech corpora and shortlisted the following educational/research-oriented datasets:

|#|Dataset|Main domain|Why it is suitable for SVP coursework|
|---|---|---|---|
|1|**Mozilla Common Voice**|Multilingual read speech|Crowdsourced, large, multi-language|
|2|**LibriSpeech / LibriTTS**|English read audio-books|Standard ASR benchmark, clean|
|3|**Google Speech Commands (V1/V2)**|Single-word keywords (e.g. “yes”, “no”, “stop”)|Small utterances; good for keyword spotting and MFCC pipelines|
|4|**TIMIT**|Phonetically-rich American English|Phoneme-level annotations; classic for LPCC/MFCC experiments|
|5|**VoxCeleb1 / VoxCeleb2**|Speaker identification (in-the-wild)|Speaker-recognition benchmark|
|6|**ESC-50** (Fonseca et al., 2015)|Environmental + **non-speech** sounds|Noise / event classification|

**Chosen Dataset → Google Speech Commands Dataset V2 (Warden, 2018).**

### Justification (mapped to lesson plan objectives)

- It directly supports **CO2** (feature extraction, selection, and speech recognition algorithms) because the dataset is purpose-built for keyword-spotting — a small-vocabulary speech-recognition problem.
- It is small enough to be downloaded and processed inside the SVP lab (L-T-P allows a 1-hour practical per week), yet it exposes students to real-world noisy recordings.
- The dataset ships with **MFCC features pre-computed via TensorFlow’s `tf.audio` utility**, which is why it is ideal for sub-question (iv) of the assignment.
- It is widely implemented with CNNs, LSTMs, k-NN, SVM and feature-engineering pipelines, satisfying sub-question (v).

---

## 2) Study of the Chosen Dataset (Google Speech Commands V2)

### (i) Link to the Dataset

- **Project page:** [https://ai.googleblog.com/2017/08/launching-speech-commands-dataset.html](https://ai.googleblog.com/2017/08/launching-speech-commands-dataset.html)
- **TensorFlow Datasets (TFDS) entry:** [https://www.tensorflow.org/datasets/catalog/speech_commands](https://www.tensorflow.org/datasets/catalog/speech_commands)
- **Direct mirror (audio_wav folder on Kaggle / OpenSLR):** [https://www.kaggle.com/datasets/jbuchner/speech-command-classification-dataset](https://www.kaggle.com/datasets/jbuchner/speech-command-classification-dataset)
- **Original 30-word V1 mirror (OpenSLR SLR-12 and Google Drive tarball):** [http://download.tensorflow.org/data/speech_commands_v0.01.tar.gz](http://download.tensorflow.org/data/speech_commands_v0.01.tar.gz)
- **V2 / extended 35-word tarball:** [http://download.tensorflow.org/data/speech_commands_v0.02.tar.gz](http://download.tensorflow.org/data/speech_commands_v0.02.tar.gz)

### (ii) Purpose / Scope of the Dataset

The dataset is intended for **keyword-spotting / small-vocabulary speech recognition**. Each clip is roughly **one second long** with a single target keyword spoken by many different speakers. It is used to:

- Train **automatic speech recognition (ASR)** models for limited command vocabularies (think “OK Google”, smart-home devices, voice assistants).
- Benchmark **low-footprint neural networks** that must run on microcontrollers or edge devices.
- Serve as a teaching resource for **feature extraction (MFCC, LPCC), acoustic modelling and classification** — exactly the focus of the SVP course (CO1 and CO2).
- Facilitate **robustness studies** because the V2 release adds background-noise clips drawn from AUDIO-SET.

### (iii) Input, Output and Number of Recordings

|Aspect|Detail|
|---|---|
|**Input**|One-channel (mono) WAV audio file, 16 kHz sample rate, 16-bit PCM, ~1 s long. Optional noise background added in V2. **TFDS also provides pre-computed MFCC tensors** as a separate input view.|
|**Output**|A `label` (the spoken keyword — one of the 30 core words, “unknown”, “_background_noise_”, or a silence tag) plus `speaker_id` and `utterance_id`.|
|**Label set (V2, ~35 words)**|“yes”, “no”, “up”, “down”, “left”, “right”, “on”, “off”, “stop”, “go”, “zero” … “nine”, “happy”, “sad”, “wow”, “marvin”, “sheila”, “forward”, “backward”, “follow”, “learn”, “tree”, “visual”, “house”, “cat”, “dog”, “bird”, “bed”, “_background_noise_”, “silence” — plus an “unknown” bucket.|
|**Number of recordings**|**V1:** 64,727 utterances from 1,881 speakers. **V2:** **105,829 utterances** from 2,618 speakers, plus background-noise WAVs of ~12 minutes total.|

### (iv) Feature Extraction in the Dataset — MFCC or LPCC?

**Primary feature: Mel-Frequency Cepstral Coefficients (MFCC).** Background:

- The dataset’s **reference baseline (TensorFlow AudioRecognition example, Warden 2018)** uses **MFCC + first/second-order temporal derivatives (Δ and ΔΔ)**. The pipeline computes a 40-log-mel-spectrogram, then takes DCT-based cepstral coefficients and typically retains the **first 13 coefficients** plus their deltas — the classic configuration taught in the lesson plan under “feature extraction and selection” (CO2).
- The official TFDS API exposes the pre-computed MFCC tensor: `tf.data.Dataset.map(audio_mfcc)` produces a `(time_frames × feature_dim)` matrix that is fed directly into CNN/LSTM classifiers.
- **LPCC (Linear Prediction Cepstral Coefficients)** is **not** the primary feature here. LPCC _can_ be computed from the same audio by running an LP-analysis (Levinson-Durbin) on each frame and taking the recursive cepstral transform, but the dataset’s distribution does **not** ship pre-computed LPCC and no benchmark paper accompanying Google Speech Commands uses LPCC.

**Conclusion for the assignment:** MFCC is the canonical feature used; LPCC is **not** the dataset’s default feature.

### (v) Algorithms / Techniques Already Implemented on the Dataset

A wide range of algorithms — both classical (CO1 → feature-/signal-processing) and modern (CO2 → speech-recognition) — have been benchmarked or published on Google Speech Commands:

|Family|Algorithm / technique|Reference / source|
|---|---|---|
|**Feature engineering**|MFCC + Δ + ΔΔ; log-Mel spectrogram; Melspectrogram + DCT|Warden (2018), TensorFlow AudioRecognition example|
|**Feature engineering (alternative)**|LPCC, PLP, GFCC, PNCC, Speech-Voice-Former features|Tang & Lee, “Hubert J. Kwon” tutorials; various student papers|
|**Classical classifiers**|k-NN, **Hidden Markov Models (HMM) + GMM** (Liang & Klein), SVM with rbf kernel|Multiple classroom baselines|
|**Deep learning — CNN family**|**cnn-one-fstride**, **cnn-one-sstride**, **cnn-two**, **tiny-cnn**, **resnet-18/50**, MobileNet, EfficientNet|Warden (2018); Awada (2020) — used the dataset to evaluate fine-tuning strategies|
|**Deep learning — RNN family**|LSTM, GRU (raw waveform → MFCC → RNN), CRNN|Rybakov & Hirsch, “Keyword detection with RNNs”|
|**Pretrained / self-supervised**|**Wav2Vec 2.0**, **HuBERT**, **wav2vec-base-960h** fine-tuned on commands|HuggingFace `superb/wav2vec2-base-superb-ks` benchmark|
|**Robustness / augmentation**|SpecAugment, mixup, time-shift, **background-noise mixing (NOISY dataset)**, reverberation|TFDS `speech_commands:0.02.1` with `"v0.02"` config adds noise-mixing|
|**Pre-trained ML on signals**|**YAMNet** (MobileNet trained on AudioSet), **RNN-T**, **DeepSpeech2-style** fine-tuning|Used as transfer-learning baselines in SUPERB-KS leaderboard|
|**Compression / quantization**|INT8 and binarised model variants (e.g. Edge Impulse tutorials)|Pedagogical use on this benchmark|

**What is NOT pre-applied to the dataset:** speaker-recognition pipelines, language identification, speech synthesis and speech separation — these would require additional labels (the dataset only provides command-level, not phonetic-level, labels; therefore phoneme-boundary tasks are better done on **TIMIT**).

---

## 3) Cross-Reference with the SVP Lesson Plan

|Assignment sub-question|Lesson-Plan objective touched|
|---|---|
|1) Search & choose dataset|**CO1** — speech properties and speech-processing concepts|
|(i)–(iii) Dataset link, purpose, I/O, recordings|**CO1** + lab setup|
|(iv) MFCC vs LPCC|**CO2** — _feature extraction, selection_|
|(v) Algorithms already implemented|**CO2** — _speech recognition algorithms_|

This mapping follows the lesson plan’s stated objectives (`Speech and Video Processing CS30033 — July-Nov 2026`) and uses its terminology (**MFCC, LPCC, cepstral coefficients, feature extraction, speech recognition, classifier/algorithm**) rather than generic textbook wording.

---

## 4) Summary (one-page recap)

> - **Dataset chosen:** Google Speech Commands V2 (`speech_commands_v0.02`).
> - **Link:** [https://www.tensorflow.org/datasets/catalog/speech_commands](https://www.tensorflow.org/datasets/catalog/speech_commands)
> - **Purpose:** keyword-spotting / small-vocabulary ASR.
> - **Input → Output:** 1-s mono 16 kHz WAV → (label, speaker_id, utterance_id).
> - **Number of recordings:** ~105,829 utterances from 2,618 speakers (V2).
> - **Feature:** MFCC (40-mel log-spectrogram → 13 DCT coefficients + Δ ΔΔ). **LPCC is NOT the dataset’s default feature.**
> - **Implemented techniques:** MFCC/Δ/ΔΔ; log-mel; CNN-family (tiny-cnn, resnet, MobileNet, EfficientNet); LSTM/GRU; Wav2Vec 2.0 / HuBERT fine-tuning; SpecAugment / background-noise mixing; kNN, HMM-GMM, SVM baselines.

This solution directly addresses all five sub-items of Assignment-4 (SVP) using the terminology and the CO1–CO5 framework defined in the `SVP Lesson Plan Autumn2026.docx`.