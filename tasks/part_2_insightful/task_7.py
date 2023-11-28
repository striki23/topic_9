# Программа проверки правильности создания пароля
while True:
    password = input('Введите пароль:')
    if len(password) < 8:
        print('Пароль должен содержать не менее 8 символов.')
    elif len(password) > 255:
        print('Пароль не может быть больше 255 символов')
    elif password[0].isdigit():
        print('Пароль не может начинаться с цифры')
    elif not password[-1].isalnum():
        print('Пароль должен заканчиваться буквой или цифрой')
    elif password.isdigit():
        print('Пароль не должен состоять только из цифр')
    elif password.isalpha():
        print('Пароль не должен состоять только из буквенных символов')
    elif password.isalnum():
        print('ПРЕДУПРЕЖДЕНИЕ: Ваш пароль состоит только из букв и цифр')
        warning = input('Хотите добавить специальные символы?(y/N):')
        if warning == 'N':
            print('\nПароль принят!')
            break
    else:
        print('\nПароль принят!')
        break
