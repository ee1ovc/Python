# 1) Создать переменную типа String
name: str = 'Ivan'
print('name =',name, type(name))

# 2) Создать переменную типа Integer
age = 33
print('age = ',age, type(age))

# 3) Создать переменную типа Float
height = 176.7
print('height =',height, type(height))

# 4) Создать переменную типа Bytes
# brain_memory = bytes(4)
# brain_memory = bytes(b'\xff\xff')
brain_memory = bytes([25, 75, 150,255])
print('brain_memory =',brain_memory, type(brain_memory))

# 5) Создать переменную типа List
Vadim_courses = ['Linux, Bash, Postman,Charles, Fiddler,SQL, Postgres, Redis, Jmeter']
print('Vadim_courses =',Vadim_courses, type(Vadim_courses))

# 6) Создать переменную типа Tuple
Vadim_schelude_group_26 = ('Basic Course Monday 20:45','Python Tuesday 21:00','Wednesday English Lesson 19:00','Thursday Basic Course 20:45','Python Friday 21:00','Job Interview Saturday 9:30','Presentations,Python Sunday 10:00')
print('Vadim_schelude_group_26 =',Vadim_schelude_group_26,type(Vadim_schelude_group_26))

# 7) Создать переменную типа Set
Ivan_daily_schelude = {'Eat','Work','Sleep','Study'}
print('Ivan_daily_schelude =',Ivan_daily_schelude,type(Ivan_daily_schelude))

# 8) Создать переменную типа Frozen set
# Nosleep = set('Rest')
# Nofood = frozenset('Eat')
# print(Nosleep == Nofood,type(Nosleep),type(Nofood))
Frozen_Ivan_daily_schelude = frozenset({'Eat','Work','Sleep','Study'})
print('Frozen_Ivan_daily_schelude =',Frozen_Ivan_daily_schelude,type(Frozen_Ivan_daily_schelude))


# 9) Создать переменную типа Dict
Goals = {1: 'Get Wealthy', 2:'Get Healthy'}
print(Goals,type(Goals))

# 10) Вывести в консоль все выше перечисленные переменные с добавлением типа данных.
print ((name, type(name)), (age, type(age)), (height, type(height)), (brain_memory, type(brain_memory)), (Vadim_courses, type(Vadim_courses)), (Vadim_schelude_group_26,type(Vadim_schelude_group_26)), (Ivan_daily_schelude,type(Ivan_daily_schelude)), (Frozen_Ivan_daily_schelude,type(Frozen_Ivan_daily_schelude)), (Goals,type(Goals)))
# Cltr(Cmd Linux) + shift + F10 RMB or "Run Filename"

# 11) Создать 2 переменные String, создать переменную в которой суммируете эти переменные. Вывести в консоль
a = 'Python'
b = 'Rocks'
c = a + b
print('c =',c,type(c))
# Cltr(Cmd Linux) + shift + F10 or RMB "Run Filename"

# 12) Создать 2 переменные Integer, создать переменную в которой суммируете эти переменные. Вывести в консоль.
a = 7
b = 2
c = a + b
print('c =',c,type(c))
# Cltr(Cmd Linux) + shift + F10 or RMB "Run Filename"

# 13) Создать переменную в которой Разделите эти переменные Int. Вывести в консоль.
c = a / b
print('c =',c,type(c))
# Cltr(Cmd Linux) + shift + F10 or RMB "Run Filename"

# 14) Создать переменную в которой Умножите эти переменные Int. Вывести в консоль.
c = a * b
print('c =', c,type(c))
# Cltr(Cmd Linux) + shift + F10 or RMB "Run Filename"

# 15) Создать переменную в которой Разделите без остатка эти переменные Int. Вывести в консоль.
c = a // b
print('c =',c,type(c))
# Cltr(Cmd Linux) + shift + F10 or RMB "Run Filename"

# 16) Создать переменную в которой надо присвоить остаток от деления этих переменных Int. Вывести в консоль.
c = a % b
print('c =',c,type(c))
# Cltr(Cmd Linux) + shift + F10 or RMB "Run Filename"

# 17) Вывести в одну строку переменные типа String и Integer используя “,” (Запятую)
# c = name, age
# print(c)
print(name,age, sep= ",")

# 18) Вывести в одну строку переменные типа String и Integer используя “+” (Плюс)
# print(name + age) - can only concatenate str (not "int") to str

print(name + str(age), sep= "+")

# Выгрузить файл в Git репозиторий.


# VCS > Git Remotes > https://github.com/ee1ovc/Python.git
# Git > pull
# Git > commit push