import tkinter as tk
from timeit import default_timer as timer


def identity(x):
    '''Identity function'''
    return x


f = identity
# for attribute in (f.__name__,
#                   f.__doc__,
#                   f.__module__,
#                   f.__class__):
#     print(attribute)

######### lambda  #########
add_l = lambda x, y: x + y


# print(add_l(1, 120))

def under_lambda(x, y):
    return add_l(x, y)


# print(under_lambda(8, 3))

colors = ["Goldenrod", "Purple", "Salmon", "Turquoise", "Cyan"]


def normalize_case(string):
    return string.casefold()


# normalized_colors = map(normalize_case, colors)
normalized_colors = map(lambda s: s.casefold(), colors)
# print(lambda s: s.casefold(), colors)


recent_presidents = ['Борис Ельцин', 'Владимир Путин', 'Дмитрий Медведев']


# print('Последними президентами были %s.' % ', '.join(recent_presidents))

######### decorators #########
def makeitalic(str='Test'):
    def wrapped():
        return "<i>" + str + "</i>"

    return wrapped


def funct_excecution_timer(funct):
    start = timer()
    funct
    end = timer()
    print(f'Function {funct.__name__} excecuted time: {end - start}')
    return funct


funct_excecution_timer(makeitalic(str='Test'))


@funct_excecution_timer
def makeitalic(str='Test'):
    def wrapped():
        return "<i>" + str + "</i>"

    return wrapped


def shout(word="да"):
    return word.capitalize() + "!"


print(shout())
scream = shout
print(scream())
del shout
try:
    print(shout())
except NameError as e:
    print(e)

print(scream())


def talk():
    # Внутри определения функции "talk" мы можем определить другую...
    def whisper(word="да"):
        return word.lower() + "...";

    # ... и сразу же её использовать!
    print(whisper())


# Теперь, КАЖДЫЙ РАЗ при вызове "talk", внутри неё определяется а затем
# и вызывается функция "whisper".
talk()
# выведет: "да..."
# Но вне функции "talk" НЕ существует никакой функции "whisper":
try:
    print(whisper())
except NameError as e:
    print(e)
    # выведет : "name 'whisper' is not defined"


def getTalk(type="shout"):
    # Мы определяем функции прямо здесь
    def shout(word="да"):
        return word.capitalize() + "!"

    def whisper(word="да"):
        return word.lower() + "...";

    # Затем возвращаем необходимую
    if type == "shout":
        # Заметьте, что мы НЕ используем "()", нам нужно не вызвать функцию,
        # а вернуть объект функции
        return shout
    else:
        return whisper


# Как использовать это непонятное нечто?
# Возьмём функцию и свяжем её с переменной
talk = getTalk()


# Как мы можем видеть, "talk" теперь - объект "function":
# print(talk)
# Который можно вызывать, как и функцию, определённую "обычным образом":
# print(talk())
# Если нам захочется - можно вызвать её напрямую из возвращаемого значения:
# print(getTalk("whisper")())

def doSomethingBefore(func):
    print("Я делаю что-то ещё, перед тем как вызвать функцию, которую ты мне передал")
    print(func())


doSomethingBefore(scream)

######### memoization #########
# https://habr.com/ru/post/335866/
# https://habr.com/ru/post/426341/
# https://habr.com/ru/post/190850/
# https://habr.com/ru/post/423679/
# https://habr.com/ru/post/121162/
