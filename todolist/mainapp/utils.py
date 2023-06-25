

menu = [
    {'name': 'Главная страница', 'url': 'home'},
    {'name': 'Добавить заметку', 'url': 'add_note'},
    {'name': 'Мои Заметки', 'url': 'my_notes'},
    {'name': 'Вход', 'url': 'login'},
    {'name': 'Регистрация', 'url': 'registration'},
]

context = {'menu': menu}


class BaseMixin:

    def same_data(self, **kwargs):
        kwargs['menu'] = menu
        return kwargs

