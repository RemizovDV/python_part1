import easy as my_lib 
def menu(): 
    print('�������� �������� (1-4):') 
    print('1.������� ����������') 
    print('2.����������� ������� ����������') 
    print('3.������� ����������') 
    print('4.������� ����������') 
    print('��� ������ �������"q"') 
    action = input() 
    return action 
def option(action): 
    if action == 'q': 
        print('�����') 
        return 
    action_item = { 
        '1': my_lib.ChangeDirectory, 
        '2': my_lib.DirListing, 
        '3': my_lib.DeleteDirectory, 
        '4': my_lib.MakeDirectory 
        } 
    item = None 
    try: 
        item = int(action) 
        if item in range(1, 5): 
            for item, key in action_item.items(): 
                if item == action: 
                    key() 
        else: 
            print('"{}" - ������������ �������!'.format(action)) 
    except IndexError: 
        print('"{}" - ������������ �������!'.format(action)) 
    answer = input('���������� ������ � ����������?\n"y" - ��: ') 
    option(menu()) if answer == 'y' else option('q') 

option(menu()) 
