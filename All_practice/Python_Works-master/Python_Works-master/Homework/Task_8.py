import re

def parse_data_string(data_string):
    parsed_data = {}

    # Используем регулярное выражение для поиска всех блоков с объявлениями данных
    regex = r"do declare (\w+) <\| \{(.*?)\} \. done;"
    matches = re.findall(regex, data_string)

    # Обходим все найденные совпадения
    for match in matches:
        key = match[0]  # ключ - первая группа с именем переменной
        values_str = match[1]  # вторая группа с данными в строковом формате

        # Используем регулярное выражение для разбора множества значений
        values = re.findall(r"'(.*?)'", values_str)
        parsed_data[key] = values

    return parsed_data


# Пример использования
data_string = "<data> do declare usre <| { 'enadi_149' , 'onla_457' , 'dige_657' ,'quesaza' }. done; do declare soce <| {'xeer' , 'ribe_997' ,'aten_645' ,'atbice_564' }. done; </data>"
parsed_data = parse_data_string(data_string)
print(parsed_data)
