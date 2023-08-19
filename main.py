import sys
import fileinput


class Guide:
    """Объект справочник.

    выполняет команды взаимодействующие с txt файлом/бд:
    add_contact(self.params) - добавляет запись о кнтакте в бд;
    get_contact - возвращает список контактов;
    edit_contact(self.params) - находит контакт, который нужно изменить
        по id и меняет значения у параметров переданых в params;
    find_contact(self.params) - находит контакт по указанным параметрам и
        выводит его в консоль;
    сохраняются данные вследующем виде:
        id/surname/name/company/privat_phone/work_phone
    """
    def __init__(self, input_data):
        self.params = input_data

    def add_contact(self) -> None:
        """Функция сохранения контакта в справочник.

        принимает на вход данные контакта и сохраняет их в бд
        """
        with open('./contact_base.txt', 'r+') as file:
            index = len(file.readlines())
            file.write(
                f'{index}/{self.params["surname"]}/{self.params["name"]}/'
                f'{self.params["middle_name"]}/{self.params["company"]}/'
                f'{self.params["privat_phone"]}/{self.params["work_phone"]}\n'
            )
        return 'Контакт успешно сохранен!'

    def get_contact(self):
        """Метод возвращающий все данные из справочника."""
        with open('./contact_base.txt', 'r') as file:
            data = file.read()
        return data

    def edit_contact(self) -> None:
        """Функция редактирования для справочника.

        принимает на вход словарь вида: параметр-значение,
        меняет все выбранные поля и выводит сообщение об успешном
        выполнении команды.
        """
        param_indexes = {
            'surname': 1,
            'name': 2,
            'middle_name': 3,
            'company': 4,
            'private_phone': 5,
            'work_phone': 6
        }
        if len(self.params) > 1:
            item_id = self.params.pop('id')
            for line in fileinput.input('./contact_base.txt', inplace=1):
                line = line.split('/')
                if line[0] == item_id:
                    for param, new_value in self.params.items():
                        line[param_indexes[param]] = new_value
                sys.stdout.write('/'.join(line))
            return 'Данные успешно обновлены'
        else:
            return 'Никаких изменений применено не было.'

    def find_contact(self):
        """Метод поиска контактов по параметрам."""
        with open('./contact_base.txt', 'r') as file:
            for line in file.readlines():
                if set(self.params).issubset(line.split('/')):
                    return line
            else:
                return 'Данные с указанными значениями не найдены'


def command_manager(command, values={}):
    try:
        print(getattr(Guide(values), command)())
    except KeyError as exception:
        print(f'Данное/ые значение/я отсутствует: {exception}')
    except AttributeError:
        print('Эта комманда не поддерживается.')


if __name__ == '__main__':
    while True:
        command, *values = input().split(' ')
        if command == 'exit':
            break
        try:
            dict_values = dict(value.split('=') for value in values)
            command_manager(command, dict_values)
        except ValueError:
            print(
                'Данные указаны неверно, тестовый пример:'
                'add_contact name=value surname=value middle_name=value'
                'company=value privat_phone=value work_phone=value'
            )
