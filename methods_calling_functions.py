def send_email(message, recipient,
               sender="university.help@gmail.com"):

    if (".com" or ".ru" or ".net") not in (recipient or sender) or "@" not in (recipient or sender):
        print(f'Невозможно отправить письмо '
              f'с адреса {sender} на адрес {recipient}.')

    elif sender == recipient:
        print(f'Невозможно отправить письмо самому себе.')

    elif sender == "university.help@gmail.com":
        print(f'Письмо успешно отправлено '
              f'с адреса {sender} на адрес {recipient}.')

    else: print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ!'
                f' Письмо отправлено с адреса {sender} на адрес {recipient}.')



send_email("Привет", "vasyok1337@gmail.com")
send_email("Привет", "vasyok1337@gmail")
send_email("Привет", "vasyok1337gmail.com")

send_email("Привет", "vasyok1337@gmail.com", "vasyok1337@gmail.com")

send_email("Привет", "vasyok@gmail.com", "vasyok1337@gmail.com")