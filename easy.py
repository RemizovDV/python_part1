# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py
import os 
import sys 
import shutil 

# 0 Копирование файла
def CopyFile(): 
    FileName=sys.argv[0] 
    while FileName in os.listdir(os.getcwd()): 
        FileName = file_name.split('.py').pop(0) + '_copy.py' 
        CurrentFile= os.path.join(os.getcwd(), sys.argv[0]) 
        NewFile=os.path.join(os.getcwd(),FileName) 
    try: 
        shutil.copy(CurrentFile,NewFile) 
    except: 
        print('Error')

#Смена директории

def ChangeDirectory(): 
    TargetDirectory=input('Введите название директории или символ "*"\n' \ 
                          'если хотите перейти в родительский каталог: ') 
    if TargetDirectory == '*': 
        to_dir=(os.getcwd().split('\\') if os.name=='nt' else 
                os.getcwd().split('/')) 
        to_dir.pop() 
        to_dir = ('\\'.join(to_dir) if os.name=='nt' else 
                '/'.join(to_dir))         
    else: 
        to_dir = os.path.join(os.getcwd(), TargetDirectory) 
    try: 
        os.chdir(to_dir) 
        print('Переход выполнен') 
    except FileExistsError: 
        print('Переход не выполнен') 

# 2. Список директории
def DirListing():
    CurrentPath=os.getcwd() 
    ListDirectory=os.listdir(CurrentPath) 
    return ListDirectory 


def MakeDirectory(): 
    NameDirectory=input('Введите название новой Директории:\n') 
    CurrentPath=os.path.join(os.getcwd(),NameDirectory) 
    try: 
        os.mkdir(CurrentPath) 
        print('Директория {} успешно создана'.format(NameDirectory)) 
    except FileExistsError: 
        print('Директория с таким именем уже существует')
        
def DeleteDirectory(): 
    NameDirectory = input('Введите название Директории для удаления:\n') 
    CurrentPath = os.path.join(os.getcwd(), NameDirectory) 
    try: 
        os.rmdir(CurrentPath) 
        print('Директория {} успешно удалена'.format(CurrentPath)) 
    except FileExistsError: 
    print('Не удаётся найти путь') 
