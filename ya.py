import requests
import os
import PySimpleGUI as sg
import time


class Yandex:

    def __init__(self, ya_token):
        with open('ya_token.txt', 'r') as file:
            self.ya_token = file.read().strip()
        self.url = 'https://cloud-api.yandex.net/v1/disk/resources'

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': f'OAuth {self.ya_token}'
        }

    def create_folder(self, path):
        headers = self.get_headers()
        requests.put(f'{self.url}?path={path}', headers=headers)

    def upload_file(self, loadfile, savefile, replace=False):
        headers = self.get_headers()
        res = requests.get(f'{self.url}/upload?'
                           f'path={savefile}&overwrite={replace}',
                           headers=headers).json()
        with open(loadfile, 'rb') as f:
            try:
                requests.put(res['href'], files={'file': f})
            except KeyError:
                print(res)

    def backup(self, savepath, loadpath):
        self.create_folder(savepath)
        for address, dirs, files in os.walk(loadpath):
            for i, file in enumerate(files):
                self.upload_file(f'{address}/{file}', f'{savepath}/{file}')
                sg.one_line_progress_meter('Процесс загрузки файлов '
                                           'на ЯндексДиск', i + 1, len(files),
                                           '-key-')
                time.sleep(1)
