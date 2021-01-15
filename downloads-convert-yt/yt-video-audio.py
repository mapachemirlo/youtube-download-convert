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
from os import path


# -- Crear path de descargas
sis_op = sys.platform
sis_op = sis_op[:3]

if sis_op == 'lin':

    os.system('clear')
    print('* Creando directorio de descarga...')
    os.system('mkdir DownloadYoutube')
    path_folder_video = './DownloadYoutube'
    path_folder_song = './DownloadYoutube'
    name_video = './DownloadYoutube'

elif sis_op == 'win':

    os.system('cls')
    print('* Creando directorio de descarga en ... ''\t')
    os.system('pwd')
    os.system('mkdir DownloadYoutube')
    path_folder_video = '.\\DownloadYoutube\\'
    path_folder_song = '.\\DownloadYoutube\\'
    name_video = '.\\DownloadYoutube\\'

else:
    os.system('cls')

    print('No se pudo identificar el Sistema Operativo, se asumirá que es Windows')
    print('* Creando directorios ...')
    os.system('mkdir DownloadYoutube')
    path_folder_video = '.\\DownloadYoutube\\'
    path_folder_song = '.\\DownloadYoutube\\'
    name = '.\\DownloadYoutube\\'

print('===================================================')
print('')
print("         PROCYON YOUTUBE DOWNLOAD-CONVERT         ")
print('')
print(' Author: Claudio Herrera - Procyon desarrollo 2021 ')
print('===================================================')
print(' Ejecutar con Python 3.*')
print(' Para salir presiones Ctrl + c ''\n')


def main():
    
    try:
        url = input(' ==> Ingrese URL para descarga: ')
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
        print(f'-- Descargando el video: "{stream.title}"...''\n')
        title = stream.title

        stream.download(output_path=path_folder_video, filename=title)
        name = name_video + title + '.mp4'

        try:
            clip = mp.VideoFileClip(name)
            print(f'-- Convirtiendo a MP3: "{stream.title}"...')
            clip.audio.write_audiofile(path_folder_song + title + '.mp3', bitrate="320k")
            print('\n''** Descarga y conversión EXITOSA!! **' '\n')
            print('-Desea descargar otro link? - Ingrese la opción deseada: ''\n' 'SI(1) / SALIR(2)')   
            op = int(input('Ingrese opción: '))
            if op == 1:
                main()
            elif op == 2:
                print('Saliendo..')
            else:
                print('Opción inválida, saliendo del programa.')
            
        except:
            print('** Video descargado exitosamente! pero ERROR en codec para la conversión a MP3 **' '\n')
            print('-Desea volver a intentarlo con otro link? - Ingrese la opción deseada: ''\n' 'SI(1) / SALIR(2)')   
            op = int(input('Ingrese opción: '))
            if op == 1:
                main()
            elif op == 2:
                print('Saliendo..')
            else:
                print('Opción inválida, saliendo, chau...')

    except:
        print('ERROR RE FATAL!! Saliendo!')
  

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Saliendo...")

