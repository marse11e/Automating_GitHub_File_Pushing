# Вот улучшенная версия функции, которая включает обработку ошибок и логирование:

import os
import subprocess
import datetime
import logging

logging.basicConfig(filename='push_to_github.log', level=logging.DEBUG)

def отправить_на_github(file_or_folder, repo_url):
    try:
        # Проверяем, существует ли файл или папка
        if not os.path.exists(file_or_folder):
            raise ValueError(f'{file_or_folder} не существует.')
        # Указываем сообщение коммита
        commit_message = 'Автоматический коммит на ' + str(datetime.datetime.now())
        # Добавляем файл или папку в репозиторий
        subprocess.run(['git', 'add', file_or_folder], check=True)
        # Совершаем коммит с сообщением коммита
        subprocess.run(['git', 'commit', '-m', commit_message], check=True)
        # Отправляем изменения в репозиторий GitHub
        subprocess.run(['git', 'push', '-u', repo_url, 'master'], check=True)
    except subprocess.CalledProcessError as e:
        logging.error(e)
        print(e)
    except Exception as e:
        logging.error(e)
        print(e)
        
        
#     Эта версия проверяет существование указанного файла или папки перед попыткой добавить его в репозиторий. 
#     Он также использует параметр check в методе subprocess.run(), 
#     чтобы в случае неудачного завершения команды git выбрасывалось исключение, 
#     что делает обработку и отладку любых возникающих проблем проще. 
#     Также используется модуль логирования python для записи любых ошибок, которые могут произойти во время выполнения функции.
  
#     Пожалуйста, обратите внимание, что этот код все еще предполагает, что git установлен и git репозиторий уже настроен и настроен.
