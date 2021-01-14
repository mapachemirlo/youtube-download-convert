#!/usr/bin/env python
#_*_coding: utf8 _*_
# ProcyonYouTube Download - Version 1.0.0
# +++ Pequeño script para descarga y conversión a mp3 de videos de YouTube +++
# Author: Claudio Herrera - Procyon desarrollo
# Ejecutar con Python 3.*
# Año 2021

import pytube
import sys
import os
import moviepy.editor as mp


# -- Crear path de descargas
sis_op = sys.platform
sis_op = sis_op[:3]

if sis_op == 'lin':
    os.system('clear')
    print('* Creando directorios ...')

    path_folder_video = '/DownloadYoutube/Video/'
    path_folder_song = '/DownloadYoutube/Song/'
    os.mkdir(path_folder_video)
    os.mkdir(path_folder_song)
    name_video = './DownloadYoutube/Video/'
elif sis_op == 'win':
    os.system('cls')
    print('* Creando directorios ...')
    os.system('mkdir DownloadYoutube\Video')
    os.system('mkdir DownloadYoutube\Song')
    path_folder_video = '.\\DownloadYoutube\\Video\\'
    path_folder_song = '.\\DownloadYoutube\\Song\\'
    name_video = '.\\DownloadYoutube\\Video\\'
else:
    os.system('cls')
    print('No se pudo identificar el Sistema Operativo, se asumirá que es Windows')
    print('* Creando directorios ...')
    os.system('mkdir DownloadYoutube\Video')
    os.system('mkdir DownloadYoutube\Song')
    path_folder_video = '.\\DownloadYoutube\\Video\\'
    path_folder_song = '.\\DownloadYoutube\\Song\\'
    name = '.\\DownloadYoutube\\Video\\'

print('')
print("         PROCYON YOUTUBE DOWNLOAD      ")
print('')
print(' Autor: Procyon desarrollo - 2021 ')
print('------------------------------------------------------')
print(' Ejecutar con Python 3.*\n')


def main():
    
    try:
        url = input('==> Ingresa URL para descarga: ')
        url = url.split('&')

        url.pop(2)
        url.pop(1)
        url_yt = url[0]

        try:
            yt = pytube.YouTube(url_yt)
        except pytube.exceptions.RegexMatchError:
            print(f'La URL especificada no es válida: {url_yt}')
            exit()

        prog_steam_list = yt.streams.filter(progressive=True)
        stream = prog_steam_list.order_by('resolution').first()
        print(f'-- Descargando el video: "{stream.title}"...')
        title = stream.title


        stream.download(output_path=path_folder_video, filename=title)
        name = name_video + title + '.mp4'
        clip = mp.VideoFileClip(name)
        clip.audio.write_audiofile(path_folder_song + title + '.mp3', bitrate="320k")

    except:
        print('Error muy fatal...')
  

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Saliendo...")

