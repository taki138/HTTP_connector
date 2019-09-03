# https://habr.com/ru/post/319164/



my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}

for elm in my_dict:
    # При таком обходе словаря, перебираются только ключи
    # равносильно for elm in my_dict.keys()
    print(elm)

for elm in my_dict.values():
    # При желании можно пройти только по значениям
    print(elm)

for key, value in my_dict.items():
    # Проход по .items() возвращает кортеж (ключ, значение),
    # который присваивается кортежу переменных key, value
    print(key, value)

def dic_vlues_to_string(my_dict: dict) -> str:
    for key, value in my_dict.items():
        # Проход по .items() возвращает кортеж (ключ, значение),
        # который присваивается кортежу переменных key, value
        print(key, value)

