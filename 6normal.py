# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе
from sys import getsizeof
class School:
    def __init__(self, school_name, school_adress, teachers, students):
        self._school_name = school_name
        self._school_adress = school_adress
        self._teachers = teachers
        self._students = students
    def get_all_classes(self):
        classes = set([student.get_class_room for student in self._students])
        return list(sorted(classes, key=lambda x: int(x[:-1])))
    def get_students(self, class_room):
        return [student.get_short_name for student in self._students if
                class_room == student.get_class_room]
    def get_teachers(self, class_room):
        return [teacher.get_short_name for teacher in self._teachers if
                class_room in teacher.get_classes]
    def find_student(self, student_full_name):
        for person in self._students:
            if student_full_name == person.get_full_name:
                teachers = [teachers.get_short_name for teachers in
                            self._teachers if person.get_class_room in
                            teachers.get_classes]
                lessons = [teachers.get_courses for teachers in
                           self._teachers if person.get_class_room in
                           teachers.get_classes]
                parents = person.get_parents
                return {
                    'full_name': student_full_name,
                    'class_room': person.get_class_room,
                    'teachers': teachers,
                    'lessons': lessons,
                    'parents': parents
                    }
    @property
    def name(self):
        return 'МБОУ ' \
               '"{}"'.format(self._school_name)
    @property
    def adress(self):
        return '{}'.format(self._school_adress)
class People:
    def __init__(self, last_name, first_name, middle_name):
        self._last_name = last_name
        self._first_name = first_name
        self._middle_name = middle_name
    @property
    def get_full_name(self):
        return '{0} {1} {2}'.format(self._last_name,
                                    self._first_name,
                                    self._middle_name)
    @property
    def get_short_name(self):
        return '{0} {1}.{2}.'.format(self._last_name,
                                     self._first_name[:1],
                                     self._middle_name[:1])
class Student(People):
    def __init__(self, last_name, first_name, middle_name,
                 class_room, mather, father):
        People.__init__(self, last_name, first_name, middle_name)
        self._class_room = class_room
        self._parents = {
            'mather': mather,
            'father': father
            }
    @property
    def get_class_room(self):
        return self._class_room
    @property
    def get_parents(self):
        return self._parents
class Teacher(People):
    def __init__(self, last_name, first_name, middle_name,
                 courses, classes):
        People.__init__(self, last_name, first_name, middle_name)
        self._courses = courses
        self._classes = classes
    @property
    def get_courses(self):
        return self._courses
    @property
    def get_classes(self):
        return self._classes
teachers = [
    Teacher('Иванов', 'Иван', 'Иванович', 'Русский язык',
            ['5А', '5Б', '6А', '6Б', '6В', '7Б', '9А', '9Б', '10А', '10Б']),
    Teacher('Сыроежкин', 'Вячеслав', 'Валерьевич', 'Право',
            ['10А', '10Б', '9А', '9Б']),
    Teacher('Ляпкин', 'Ля', 'Си', 'Философия',
            ['5А', '5Б', '6А', '6Б', '6В', '7Б', '9А', '9Б', '10А', '10Б']),
    Teacher('Тяпкин', 'Алексей', 'Игорьевич', 'Иностранный язык',
            ['5А', '5Б', '6А', '6Б', '6В', '7Б', '9А', '9Б', '10А', '10Б']),
    Teacher('Рожкин', 'Николай', 'Иванович', 'Психология',
            ['6А', '6Б', '6В', '7Б', '9А', '9Б'])
    ]
students = [
    Student('Юдин', 'Артем', 'Алексеевич', '10Б','Юрина О. А.', 'Юрин А. В.'),
    Student('Александров', 'Михаил', 'Андреевич', '5А', 'Александров А.А.', 'Александрова А.А.'),
    Student('Багликов', 'Сергей', 'Владимирович', '5Б', 'Багликов А.В.', 'Багликова Б.Б.'),
    Student('Белкин', 'Михаил', 'Павлович', '5А', 'Белкин А.П.', 'Белкина В.В.'),
    Student('Власов', 'Андрей', 'Александрович', '6Б', 'Власов А.А.', 'Власова Г.Г.'),
    Student('Галкин', 'Кирилл', 'Олегович', '6А', 'Галкин А.О.', 'Галкина Д.Д.'),
    Student('Голубев', 'Филипп', 'Игоревич', '7Б', 'Голубев А.И.', 'Голубева Е.Е.'),
    Student('Гущин', 'Никита', 'Иванович', '9А', 'Гущин П.И.', 'Гущина Ж.Ж.'),
    Student('Дербугова', 'Ольга', 'Викторовна', '9Б', 'Дербугов А.В.', 'Дербугова З.З'),
    Student('Дзодзиков', 'Муслим', 'Тамерланович', '10А', 'Дзодзиков Б.Т.', 'Дзодзикова И.И.'),
    Student('Киселева', 'Ирина', 'Владимировна', '10Б', 'Киселев Т.В.', 'Киселева К.К.'),
    Student('Корбовская', 'Мария', 'Дмитриевна', '5А', 'Корбовский П.Д.', 'Корбовская Л.Л.'),
    Student('Лисаев', 'Кирилл', 'Александрович', '5Б', 'Лисаев О.А.', 'Лисаева М.М.'),
    Student('Лындов-Фомин', 'Артём', 'Михайлович', '5А', 'Лындов-Фомин О.М.', 'Лындов-Фомина Н.Н.'),
    Student('Панков', 'Евгений', 'Сергеевич', '6Б', 'Панков А.С.', 'Панкова О.О.'),
    Student('Плотникова', 'Дарья', 'Витальевна', '6А', 'Плотников', 'Плотникова П. П.'),
    Student('Победённый', 'Вячеслав', 'Андреевич', '7Б', 'Победённый А.А.', 'Победённая Р.Р.'),
    Student('Поваляев', 'Алексей', 'Владиславович', '9А', 'Поваляев В.В.', 'Поваляева С.С.'),
    Student('Потапова', 'Анна', 'Юрьевна', '9Б', 'Потапова А.Ю.', 'Потапова Т.Т.'),
    Student('Терехов', 'Иван', 'Евгеньевич', '10А', 'Терехов К.Е.', 'Терехова У.У.'),
    Student('Чекалин', 'Сергей', 'Алексеевич', '10Б', 'Чекалин П.Б.', 'Чекалина Ф.Ф.'),
    Student('Чекмарев', 'Олег', 'Александрович', '5А', 'Чекмарев А.А.', 'Чекмарева Х.Х.'),
    Student('Шаймарданов', 'Дамир', 'Рифович', '5Б', 'Шаймарданов Н.Р.', 'Шаймарданова Ч.Ч.')
    ]
school = School('Школа №2', 'Верхняя Пышма'
                'Кривоусова, 48', teachers, students)
print(school.name)
print(school.adress)
print('\nСписок классов школы:')
print(', '.join(school.get_all_classes()))
print('\nСписок "10Б" класса:')
print('\n'.join(school.get_students('10Б')))
try:
    student = school.find_student('Юдин Артем Александр')
    #print(getsizeof(student))
    print('\nУченик: {0}\nКласс: "{1}"\n'
          'Учителя: {2}\nПредметы: {3}'.format(student['full_name'],
                                            student['class_room'],
                                        ', '.join(student['teachers']),
                                        ', '.join(student['lessons'])))
    print('Родители: {0}, {1}'.format(student['parents']['mather'],
                                      student['parents']['father']))
except TypeError:
    print('Юдин Артем Александр не учится')
print('\nКласс: "5А"\nПреподаватели: '
      '{0}'.format(', '.join(school.get_teachers('5А'))))