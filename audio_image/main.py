import shutil
from pathlib import Path

import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np


def audio_to_image(dir_name: str):
    base_dir = Path(__file__).parent / dir_name

    if not base_dir.exists() or not base_dir.is_dir():
        print(f'Error: Directory not found in {base_dir}')
        return

    for sub_dir in base_dir.iterdir():
        if sub_dir.is_dir():
            audio_files = list(sub_dir.glob('*.wav'))

            if audio_files:
                create_image_spectogram(audio_files, sub_dir.name)


def create_image_spectogram(list_filename: list[Path], category_name: str):
    base_path = Path(__file__).parent
    new_path_dir = base_path / 'dataset' / category_name

    if new_path_dir.exists():
        shutil.rmtree(new_path_dir)

    new_path_dir.mkdir(parents=True, exist_ok=True)

    for file_path in list_filename:
        file_stem = file_path.stem

        clip, sample_rate = librosa.load(file_path, sr=None)

        fig = plt.figure(figsize=[0.72, 0.72])
        S = librosa.feature.melspectrogram(y=clip, sr=sample_rate)
        librosa.display.specshow(librosa.power_to_db(S, ref=np.max))

        save_path = new_path_dir / f'{file_stem}.jpg'
        plt.savefig(save_path, dpi=400, bbox_inches='tight', pad_inches=0)

        plt.close(fig)
        plt.close('all')


if __name__ == '__main__':
    audio_to_image('audios')
