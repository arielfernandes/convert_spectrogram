#!/usr/bin/env python3

# Author: Ariel Fernandes <0.arielfernandes.0@gmail.com>
# Created at <2023-06-12 seg 12:09>
from audio_image.main import list_dirnames, audio_to_imagem
def test_return_list_dirnames_true():
    assert list_dirnames('Animal-Sound-Dataset-master/')

def test_return_dict_audio_to_imagem_true():
    assert audio_to_imagem("Animal-Sound-Dataset-master/")

def test_return_dict_audio_to_imagem():
    list_dir = list_dirnames('Animal-Sound-Dataset-master/')
    assert (type(list_dir) == list) and list_dir != None
