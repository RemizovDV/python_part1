import os 
import sys 
import shutil 

#Модуль shutil содержит набор функций высокого уровня 
#для обработки файлов, групп файлов, и папок. В частности, 
#доступные здесь функции позволяют копировать, перемещать и удалять файлы и папки. 

# Вывод списка файлов 
def DirListing():
    CurrentPath=os.getcwd() 
    ListDirectory=os.listdir(CurrentPath) 
    return ListDirectory 
#Создание директории
def MakeDirectiry(NameDirectoty): 
    CurrentPath=os.path.join(os.getcwd(),NameDirectoty) 
    try: 
        os.mkdir(CurrentPath) 
        print('Директория {} успешно создана'.format(NameDirectoty)) 
    except FileExistsError: 
        print('Директория с таким именем уже есть')
#Удаление директории
def DeleteDirectory(NameDirectoty): 
    CurrentPath=os.path.join(os.getcwd(), NameDirectoty) 
    try: 
        os.rmdir(CurrentPath) 
        print('Директория {} успешно удалена'.format(NameDirectoty)) 
    except FileExistsError: 
        print('Не удаётся найти путь') 
#Копирование файла
def CopyFile(): 
    FileName = sys.argv[0] 
    while FileName in os.listdir(os.getcwd()): 
        FileName=FileName.split('.py').pop(0) + '_copy.py' 
        CurrentFile=os.path.join(os.getcwd(), sys.argv[0]) 
        NewFile=os.path.join(os.getcwd(),FileName) 
    try: 
        shutil.copy(CurrentFile,NewFile) 
    except: 
        print('Ошибка Копирования') 
