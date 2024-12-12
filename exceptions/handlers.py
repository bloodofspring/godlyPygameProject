from collections.abc import Callable
from typing import Any, Optional

import colorama


def handle_broad_exception(exception: Any, **custom_exceptions: tuple[type[Exception], str, Optional[str]]) -> bool:
    """
    Обрабатывает кастомные исключения

    Т. Е. При совпадении с указанным пользователем типом исключений будет отображаться заданное сообщение
    :param exception: Тип возникшего исключения
    :param custom_exceptions: Пользовательские исключения
    :return: true если ни одно из пользовательских исключений не было возбуждено, иначе false
    """
    for cust in custom_exceptions.values():
        exception_, message, color = cust
        if color is None:
            color = colorama.Fore.LIGHTRED_EX

        if not isinstance(exception_(), type(exception)):
            continue

        print(color + message)

        return False

    return True


def exception_handler(
        ignore_broad_exceptions: bool = False,
        default_message: str | None = None,
        **custom_exceptions: tuple[type[Exception], str, Optional[str]]
):
    """
    Декоратор для универсальной обработки исключений
    :param ignore_broad_exceptions: Если задан параметр default_message при незаданном пользователем кастомном исключении будет отображено оно (default_message) иначе - ничего
    :param default_message: Сообщение по умолчанию (будет отображено при возникновении непредусмотренного исключения, только если ignore_broad_exceptions=true)
    :param custom_exceptions: Исключения, которые необходимо обработать отдельно (<Тип исключения>, <Сообщение при возникновении данного исключения>, <Цвет сообщения (если none - будет выставлен красный)>)
    """
    colorama.init(autoreset=True)

    def decorator(func: Callable):
        def inner(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as error:
                if not handle_broad_exception(exception=error, **custom_exceptions):
                    return False

                if ignore_broad_exceptions:
                    if default_message:
                        print(default_message)
                else:
                    print(colorama.Fore.LIGHTRED_EX + f"{type(error)}: {error}")

                return False

        return inner

    return decorator
