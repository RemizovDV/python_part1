import easy as my_lib 
def menu(): 
    print('Выберете действие (1-4):') 
    print('1.Сменить Директорию') 
    print('2.Просмотреть текущую Директории') 
    print('3.Удалить Директорию') 
    print('4.Создать Директорию') 
    print('Для Выхода нажмите"q"') 
    action = input() 
    return action 
def option(action): 
    if action == 'q': 
        print('Выход') 
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
            print('"{}" - некорректная команда!'.format(action)) 
    except IndexError: 
        print('"{}" - некорректная команда!'.format(action)) 
    answer = input('Продолжить работу с программой?\n"y" - Да: ') 
    option(menu()) if answer == 'y' else option('q') 

option(menu()) 
