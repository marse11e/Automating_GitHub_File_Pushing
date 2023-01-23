# Вот предыдущий код в виде функции:

import os
import subprocess
import datetime

def отправить_на_github(file_or_folder, repo_url):
    # Укажите сообщение коммита
    commit_message = 'Автоматический коммит на ' + str(datetime.datetime.now())

    # Добавьте файл или папку в репозиторий
    subprocess.run(['git', 'add', file_or_folder])

    # Сделайте коммит с сообщением коммита
    subprocess.run(['git', 'commit', '-m', commit_message])

    # Отправьте изменения в репозиторий GitHub
    subprocess.run(['git', 'push', '-u', repo_url, 'master'])
    
# Вы можете использовать эту функцию, вызвав ее и передав путь файла или папки и URL репозитория в качестве аргументов:
file_or_folder = '/path/to/file_or_folder'
repo_url = 'https://github.com/username/repository.git'
отправить_на_github(file_or_folder, repo_url)

# Вы можете настроить запуск этой функции каждый день с помощью инструмента, такого как cron на Linux или Task Scheduler на Windows.
# Обратите внимание, что этот код предполагает, что git установлен и git репозиторий уже настроен и настроен.
