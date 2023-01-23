# суть действий

import datetime
import os 
from subprocess import check_output

class GitUpload:
    def __init__(self, dir_name, file_name):
        self.dir_name = dir_name
        self.file_name = file_name

    def upload(self):
        # Установим текущую дату
        current_date = datetime.datetime.now().strftime("%d-%m-%Y")

        # Запустить процесс git add
        check_output(f'git add {self.file_name}', cwd=self.dir_name, shell=True)

        # Запустить процесс git commit
        check_output(f'git commit -m "Auto commit {current_date}"', cwd=self.dir_name, shell=True)

        # Запустить процесс git push
        check_output('git push', cwd=self.dir_name, shell=True)


# Класс GitUpload инициализирует атрибуты для директории и имени файла, 
# а также содержит метод upload, который предназначен для автоматической отправки указанного файла в GitHub каждый день. 
# На практике это может использоваться, например, для сохранения обновлений данных.
