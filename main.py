
# Сохранение в json. name - это meaning, а file принимает переменную-словарь,
# path - относительный путь к файлу, но не более одной папки
def save(name, file, path='jsonComLab/'):
    from json import dump
    import os
    try:
        os.mkdir(path)
    except FileExistsError:
        pass
    with open(path + name + '.json', 'w') as add_info_file:
        dump(file, add_info_file)


# сборка файла
def creator(meaning, request, response):
    dct = {
        meaning: {
            "request": request,
            "response": response,
        }
    }
    save(meaning, dct)


# заполнение листов, где _type - это "запрос", или "ответ". _type влияет только на текст
def smart_input(_type):

    result = []
    key = True
    print('Для продолжения, введите "$$next". Для того, чтобы узнать все команды - введите "$$help".')
    while key:
        input_text = input(f"Введите {_type}, или команду: ")
        # проверка на рабочие команды
        if "$$" in input_text:
            match input_text:
                case "$$next":
                    key = False
                    break
                case "$$del":
                    try:
                        result.pop()
                    except:
                        print(f"Данный {_type}-лист пуст.")
                case "$$clear":
                    result = []
                case "$$show":
                    print(f"{_type}-лист: {result}")
                case "$$help":
                    print("$$del - удаляет последний добавленный элемент;\n"
                          "$$clear - очищает лист;\n"
                          "$$show - показывает лист добавленных значений;\n"
                          "$$next - заканчивает набор и переводит к следующему этапу;\n")
                case _:
                    print("Команда написана неверно, либо отсутствует.")
        else:
            result.append(input_text)

    return result


def inputs():

    meaning = input('Название meaning: ')
    request = smart_input("запрос")
    response = smart_input("ответ")

    return meaning, request, response


def main():
    meaning, request, response = inputs()
    creator(meaning, request, response)


if __name__ == "__main__":
    main()