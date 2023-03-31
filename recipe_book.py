from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class MyKivyApp(App):
    def build(self):
        # Создаем главный контейнер, используя BoxLayout
        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Создаем контейнер для поля ввода и кнопки
        input_layout = BoxLayout(
            orientation='horizontal', 
            size_hint=(1, None), 
            height=70, 
            spacing=10, 
            pos_hint={'center_x': 0.5, 'top': 1})

        # Создаем поле для ввода текста
        text_input = TextInput(multiline=True)

        # Создаем кнопку
        button = Button(text='Нажми меня', size_hint=(.4, 1))

        # Добавляем поле ввода текста и кнопку в контейнер
        input_layout.add_widget(text_input)
        input_layout.add_widget(button)

        # Добавляем контейнер для поля ввода и кнопки в верхнюю часть главного контейнера
        main_layout.add_widget(input_layout)




        # Создаем контейнер для вывода
        result_layout = BoxLayout(
            orientation='horizontal',
            size_hint=(1, None),
            spacing=10,
            pos_hint={'center_x': 0.5})

       

        # Добавляем контейнер для вывода в главный контейнер
        main_layout.add_widget(result_layout)



        # Создаем контейнер для кнопок навигации
        nav_layout = BoxLayout(
            orientation='horizontal',
            size_hint=(1, 0.01),
            height=30,
            spacing=10,
            pos_hint={'center_x': 0.5, 'bottom': 1})

        # Создаем кнопки навигации
        home_button = Button(text='Домой', size_hint=(0.3, 1))
        fav_button = Button(text='Избранное', size_hint=(0.3, 1))
        profile_button = Button(text='Личный кабинет', size_hint=(0.4, 1))

        # Добавляем кнопки навигации в контейнер
        nav_layout.add_widget(home_button)
        nav_layout.add_widget(fav_button)
        nav_layout.add_widget(profile_button)

        # Добавляем контейнер с кнопками навигации в нижнюю часть главного контейнера
        main_layout.add_widget(nav_layout)

        return main_layout


if __name__ == '__main__':
    MyKivyApp().run()