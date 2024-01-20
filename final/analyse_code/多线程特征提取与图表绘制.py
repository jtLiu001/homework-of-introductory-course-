from concurrent.futures import ProcessPoolExecutor
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


def process_single_file(file_path):
    """处理单个文件并返回其特征"""
    if file_path.endswith("_vocals.mp3"):
        return "vocals", extract_vocal_features(file_path)
    elif file_path.endswith("_accompaniment.mp3"):
        return "accompaniment", extract_accompaniment_features(file_path)


def process_audio_folder_parallel(folder_path):
    """并行处理音乐风格文件夹中的所有音频文件"""
    genre_features = {"vocals": [], "accompaniment": []}
    file_paths = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith(".mp3")]

    with ProcessPoolExecutor() as executor:
        for file_type, features in executor.map(process_single_file, file_paths):
            genre_features[file_type].append(features)

    return genre_features


def plot_feature_across_genres(all_genres_features, feature_name, feature_type):
    """为特定特征绘制不同风格的图表"""
    plt.figure(figsize=(10, 6))

    # 设置不同风格的颜色
    colors = ['red', 'green', 'blue']
    genre_color = {genre: color for genre, color in zip(all_genres_features.keys(), colors)}

    # 绘制每种风格的线条和平均值线
    for genre, features_dict in all_genres_features.items():
        features = features_dict[feature_type]
        feature_values = [feature[feature_name] for feature in features if feature_name in feature]

        # 确保此特征对于此类型存在
        if not feature_values:
            continue

        # 生成每首歌曲的 x 值
        x_values = list(range(len(feature_values)))

        # 绘制特征值折线
        plt.plot(x_values, feature_values, '-o', label=genre, color=genre_color[genre])

        # 计算并绘制每种风格的平均特征值直线
        avg_value = np.mean(feature_values)
        plt.axhline(avg_value, color=genre_color[genre], linestyle='--', linewidth=2, label=f"{genre} average")

    plt.title(f'{feature_type.capitalize()} Feature: {feature_name}')
    plt.xlabel('Song Number')
    plt.ylabel(f'{feature_name} Value')
    plt.legend()
    plt.show()


def main():
    root_folder = r"D:\music_type_analyse\separated"
    all_genres_features = {}
    for genre_folder in os.listdir(root_folder):
        genre_folder_path = os.path.join(root_folder, genre_folder)
        if os.path.isdir(genre_folder_path):
            all_genres_features[genre_folder] = process_audio_folder_parallel(genre_folder_path)

    # 定义两种类型的特征集
    vocal_features = ['mfccs', 'chroma', 'spectral_centroid', 'zero_crossing_rate']
    accompaniment_features = ['spectral_centroid', 'spectral_bandwidth', 'tempo', 'harmonics_mean', 'percussive_mean']

    # 为人声和伴奏的每个特征绘制图表
    for feature_name in set(vocal_features) | set(accompaniment_features):
        plot_feature_across_genres(all_genres_features, feature_name,
                                   'vocals' if feature_name in vocal_features else 'accompaniment')


if __name__ == "__main__":
    main()

