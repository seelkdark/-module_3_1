# Инициализация переменной calls
calls = 0
def count_calls():
    global calls  # Указываем, что мы будем использовать глобальную переменную
    calls += 1   # Увеличиваем счетчик вызовов на 1
def string_info(string):
    count_calls()  # Увеличиваем счетчик вызовов
    length = len(string)  # Длина строки
    return (len(string), string.upper(), string.lower())
def is_contains(string, list_to_search):
    count_calls()  # Увеличиваем счетчик вызовов
    # Приведение строки к нижнему регистру для поиска
    normalized_string = string.lower()
    return normalized_string in (item.lower() for item in list_to_search)  # Поиск в списке с учетом регистра
# Вызовы функций с произвольными данными
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBan
print(is_contains('cycle', ['recycle', 'cyclic'])) # No matches
print(calls)