# -*- coding: utf-8 -*-
"""python project 1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13aPSwocmHRsYlRaV23YlXbxYIuCS4bsf
"""

import librosa
import numpy as np
def extract_features(audio_path):
    y, sr = librosa.load(audio_path, sr=None)
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    chroma = librosa.feature.chroma_stft(y=y, sr=sr)
    mel = librosa.feature.melspectrogram(y=y, sr=sr)
    spectral_centroid = librosa.feature.spectral_centroid(y=y, sr=sr)

    features = np.concatenate([mfccs.mean(axis=1), chroma.mean(axis=1), mel.mean(axis=1), np.mean(spectral_centroid, axis=1)])
    return features

def detect_scream(features):

    threshold = 0.5
    scream_probability = sum(features) / len(features)

    if scream_probability > threshold:
        return True
    else:
        return False

def analyze_scream(scream_detected):
    if scream_detected:
        print("Potential scream detected. Crime analysis and intervention required.")
    else:
        print("No scream detected. No immediate action required.")

if __name__ == "__main__":
    audio_path ="/content/man-scream-121085.mp3"
    audio_features = extract_features(audio_path)
    scream_detected = detect_scream(audio_features)
    analyze_scream(scream_detected)

"""# New Section"""