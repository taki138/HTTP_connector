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


######### memoization #########