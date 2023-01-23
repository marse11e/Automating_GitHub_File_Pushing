import os
import subprocess
import datetime

# Укажите путь к файлу или папке, которые вы хотите отправить на GitHub
file_or_folder = '/path/to/file_or_folder'

# Укажите URL репозитория GitHub
repo_url = 'https://github.com/username/repository.git'

# Укажите сообщение коммита
commit_message = 'Автоматический коммит на ' + str(datetime.datetime.now())

# Добавьте файл или папку в репозиторий
subprocess.run(['git', 'add', file_or_folder])

# Сделайте коммит с сообщением коммита
subprocess.run(['git', 'commit', '-m', commit_message])

# Отправьте изменения в репозиторий GitHub
subprocess.run(['git', 'push', '-u', 'origin', 'master'])
