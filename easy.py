# ������-1:
# �������� ��������� ���������� �������,
# ����������� �������� � ������� ������� ����������.
# ������� ������ ����� ���� ������ ��������, � ������� ����� ������:
# 1. ������� � �����
# 2. ����������� ���������� ������� �����
# 3. ������� �����
# 4. ������� �����
# ��� ������ ������� 1, 3, 4 ��������� ����������� �������� �����
# � ������� ��������� ��������: "������� �������/�������/�������",
# "���������� �������/�������/�������"

# ��� ������� ������ ������ ����������� ��������� �� ������� easy,
# ����������� � ���� ��������������� �������,
# � ��������������� � ������ ���� �� easy.py
import os 
import sys 
import shutil 

# 0 ����������� �����
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

#����� ����������

def ChangeDirectory(): 
    TargetDirectory=input('������� �������� ���������� ��� ������ "*"\n' \ 
                          '���� ������ ������� � ������������ �������: ') 
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
        print('������� ��������') 
    except FileExistsError: 
        print('������� �� ��������') 

# 2. ������ ����������
def DirListing():
    CurrentPath=os.getcwd() 
    ListDirectory=os.listdir(CurrentPath) 
    return ListDirectory 


def MakeDirectory(): 
    NameDirectory=input('������� �������� ����� ����������:\n') 
    CurrentPath=os.path.join(os.getcwd(),NameDirectory) 
    try: 
        os.mkdir(CurrentPath) 
        print('���������� {} ������� �������'.format(NameDirectory)) 
    except FileExistsError: 
        print('���������� � ����� ������ ��� ����������')
        
def DeleteDirectory(): 
    NameDirectory = input('������� �������� ���������� ��� ��������:\n') 
    CurrentPath = os.path.join(os.getcwd(), NameDirectory) 
    try: 
        os.rmdir(CurrentPath) 
        print('���������� {} ������� �������'.format(CurrentPath)) 
    except FileExistsError: 
    print('�� ������ ����� ����') 
