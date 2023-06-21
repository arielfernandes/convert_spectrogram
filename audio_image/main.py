#!/usr/bin/env python3

# Author: Ariel Fernandes <0.arielfernandes.0@gmail.com>
# Created at <2023-06-21 qua 15:47>
#!/usr/bin/env python3

import librosa
import librosa.display
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pydash
import os
import shutil
import pathlib
import re


# get the directories with the audio files
def audio_to_image(dir_name: str):
    """create path audio from source"""
    files: dict = {}
    regex = f'{dir_name}(.?\w+.*)'

    if not(list_dir := list_dirnames(dir_name)):
        return
    if isinstance(list_dir, list):
        for d in list_dir:
            DIRNAME = re.findall(regex, d, re.MULTILINE)[0]
            list_filenames = os.listdir(d)
            path_files = [f'{d}/{i}' for i in list_filenames]

            files[DIRNAME] = path_files

    create_spectogram(files)


# Generate source list to files audio
def list_dirnames(dir_name: str) -> list | None:
    """create list with source files"""

    dir_path = os.path.dirname(os.path.realpath(__file__))
    DIR = f"{dir_path}/{dir_name}"

    if not(path_audios := os.listdir(DIR)):
        return

    if isinstance(path_audios, list):
        return [f"{dir_path}/{dir_name}{i}" for i in path_audios]

def create_spectogram(dict_filename: dict):
    for x in dict_filename:
        dir_file = dict_filename.get(x)
        if isinstance(dir_file, list):
            create_image_spectogram(dir_file, x)


def create_image_spectogram(list_filename: list, dir_name: str):
    """generate image from audios
        Takes the paths of the .wav convert to image
    """
    regex = f'{dir_name}(.?\w+.*)'

    PATHDIR = os.path.dirname(os.path.realpath(__file__))
    DIRECTORY =  f'/dataset/{dir_name}'
    NEW_PATHDIR = f'{PATHDIR}{DIRECTORY}/'

    if os.path.exists(NEW_PATHDIR):
        shutil.rmtree(NEW_PATHDIR)

    os.mkdir(NEW_PATHDIR)

    for filename in list_filename:
        NAME = re.findall(regex, filename, re.MULTILINE)[0].replace('/','')

        plt.interactive(False)
        clip, sample_rate = librosa.load(filename, sr=None)
        fig = plt.figure(figsize=[0.72,0.72])
        S = librosa.feature.melspectrogram(y=clip, sr=sample_rate)
        librosa.display.specshow(librosa.power_to_db(S, ref=np.max))
        filename  = pathlib.Path(f"{NEW_PATHDIR}/{NAME.replace('.wav', '')}.jpg")
        plt.savefig(filename, dpi=400, bbox_inches='tight',pad_inches=0)
        plt.close()
        #fig.clf()
        plt.close(fig)
        plt.close('all')
        del filename,NAME,clip,sample_rate,fig,S

if __name__ == '__main__':
   audio_to_image('Animal-Sound-Dataset-master/')
