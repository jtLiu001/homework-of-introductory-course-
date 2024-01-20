import os
import librosa
import matplotlib.pyplot as plt
import numpy as np


def extract_vocal_features(audio_path):
    y, sr = librosa.load(audio_path, sr=None)

    # 提取人声特征
    mfccs = librosa.feature.mfcc(y=y, sr=sr).mean(axis=1)
    chroma = librosa.feature.chroma_stft(y=y, sr=sr).mean(axis=1)
    spectral_centroid = librosa.feature.spectral_centroid(y=y, sr=sr)[0].mean()
    zero_crossing_rate = librosa.feature.zero_crossing_rate(y)[0].mean()

    return {
        "mfccs": mfccs,
        "chroma": chroma,
        "spectral_centroid": spectral_centroid,
        "zero_crossing_rate": zero_crossing_rate,
    }


def extract_accompaniment_features(audio_path):
    y, sr = librosa.load(audio_path, sr=None)

    # 提取伴奏特征
    spectral_centroid = librosa.feature.spectral_centroid(y=y, sr=sr)[0].mean()
    spectral_bandwidth = librosa.feature.spectral_bandwidth(y=y, sr=sr)[0].mean()
    tempo, _ = librosa.beat.beat_track(y=y, sr=sr)
    harmonics, percussive = librosa.effects.hpss(y)
    harmonics_mean = harmonics.mean()
    percussive_mean = percussive.mean()

    return {
        "spectral_centroid": spectral_centroid,
        "spectral_bandwidth": spectral_bandwidth,
        "tempo": tempo,
        "harmonics_mean": harmonics_mean,
        "percussive_mean": percussive_mean,
    }


def process_audio_folder(folder_path):
    """处理一个音乐风格文件夹中的所有音频文件"""
    genre_features = {"vocals": [], "accompaniment": []}
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        if file_name.endswith("_vocals.mp3"):
            features = extract_vocal_features(file_path)
            genre_features["vocals"].append(features)
        elif file_name.endswith("_accompaniment.mp3"):
            features = extract_accompaniment_features(file_path)
            genre_features["accompaniment"].append(features)
    return genre_features


def plot_feature_across_genres(all_genres_features, feature_name, feature_type):
    """为特定特征绘制不同风格的图表"""
    plt.figure(figsize=(10, 6))
    for genre, features in all_genres_features.items():
        # 根据特征类型（人声或伴奏）提取特定特征的所有值
        feature_values = [song[feature_name] for song in features[feature_type] if feature_name in song]

        # 绘制每首歌的特征值
        plt.plot(feature_values, label=f'{genre} {feature_name}')

        # 计算并绘制平均值
        if feature_values:
            avg_value = np.mean(feature_values)
            plt.axhline(avg_value, color='grey', linestyle='--', linewidth=0.8)

    plt.title(f'{feature_type.capitalize()} Feature: {feature_name}')
    plt.xlabel('Songs')
    plt.ylabel(f'{feature_name} value')
    plt.legend()
    plt.show()


def main():
    root_folder = r"D:\music_type_analyse\separated"
    all_genres_features = {}
    for genre_folder in os.listdir(root_folder):
        genre_folder_path = os.path.join(root_folder, genre_folder)
        if os.path.isdir(genre_folder_path):
            all_genres_features[genre_folder] = process_audio_folder(genre_folder_path)

    # 绘制图表
    feature_names = ['mfccs', 'chroma', 'spectral_centroid', 'zero_crossing_rate',
                     'spectral_bandwidth', 'tempo', 'harmonics_mean', 'percussive_mean']
    for feature_name in feature_names:
        plot_feature_across_genres(all_genres_features, feature_name)


if __name__ == "__main__":
    main()
