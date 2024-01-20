from spleeter.separator import Separator
import librosa
import soundfile as sf
import os
import gc


def preprocess_and_save(audio_path, output_folder):
    """音频预处理：降低采样率，截取中间两分钟"""
    y, sr = librosa.load(audio_path, sr=None)
    duration = librosa.get_duration(y=y, sr=sr)
    start = (duration / 2) - 60
    end = (duration / 2) + 60
    start_sample = int(start * sr)
    end_sample = int(end * sr)
    y_middle = y[start_sample:end_sample]
    y_resampled = librosa.resample(y_middle, orig_sr=sr, target_sr=8000)

    # 保存预处理后的音频
    processed_audio_path = os.path.join(output_folder, os.path.basename(audio_path).replace(".mp3", "_processed.mp3"))
    sf.write(processed_audio_path, y_resampled, 8000)
    return processed_audio_path


def separate_tracks(separator,processed_audio_path, output_folder):
    """使用Spleeter分离人声和伴奏"""
    # 获取原始文件名（不含扩展名）
    base_name = os.path.basename(processed_audio_path)
    file_name = os.path.splitext(base_name)[0]

    # 指定输出的人声和伴奏音轨文件名
    vocals_output = os.path.join(output_folder, file_name + "_vocals")
    accompaniment_output = os.path.join(output_folder, file_name + "_accompaniment")

    # 分离音轨
    separator.separate_to_file(processed_audio_path, output_folder, codec='mp3',
                               filename_format="{filename}_{instrument}.{codec}")

    # 返回人声和伴奏的文件路径
    return vocals_output + ".mp3", accompaniment_output + ".mp3"


def process_folder(separator,folder_path, output_folder):
    all_features = []
    for file in os.listdir(folder_path):
        if file.endswith(".mp3"):
            file_path = os.path.join(folder_path, file)
            processed_audio_path = preprocess_and_save(file_path, r"D:\music_type_analyse\lower_sampling_rate")
            separate_tracks(separator,processed_audio_path, output_folder)
            del processed_audio_path,
            gc.collect()  # 显式触发垃圾回收
    return all_features


def main():
    separator = Separator('spleeter:2stems')
    input_folder = r"D:\music_type_analyse\material\Chinese style"
    output_folder = r"D:\music_type_analyse\separated\Chinese style"
    process_folder(separator,input_folder, output_folder)


if __name__ == "__main__":
    main()
