def recursive_dict_reader(my_dict, prev_pef_names = []):
    '''
        Рекурсивный развертыватель вложеных
        словарей в одноуровневый словарь
    '''
    res = {}
    
    for key, val in my_dict.items():
        curr_key_dict = prev_pef_names + [key]
        if type(val) == dict:
            res = {
                **res,
                **recursive_dict_reader(
                    val, curr_key_dict
                )
            }
        else:
            res["/".join(curr_key_dict)] = val
    return res


def dict_reading_decorator(func):
    '''
        Декоратор который проверяет находится ли искомый ключ в
        словаре, если нет то срабатывает ислючение - возврящается
        пустой словарь
    '''
    def wrapper(dict):
        try:
            return func(dict)
        except KeyError:
            return {}
    
    return wrapper

def dict_reader_wrapper(my_dict, key_name):
    '''
        Для того, чтобы быстро вызывать
        recursive_dict_reader для тех случаев
        где первый уровень ключа такой-же как
        ключ разворачивоемого подсловаря
        
        my_dict - словарь верхнего уровня;
        key_name - ключ подсловаря в словаре верхнего уровня.
    '''
    return (
        recursive_dict_reader(my_dict[key_name], [key_name])
        if key_name in my_dict.keys() else {}
    )

@dict_reading_decorator
def read_client(client_dict):
    '''
        Прочитать инфомрацию bki начиная от поля "client"
    '''
    res = {
        **dict_reader_wrapper(client_dict, "titul"),
        **dict_reader_wrapper(client_dict, "registrationplace"),
        **dict_reader_wrapper(client_dict, "range"),
        **dict_reader_wrapper(client_dict, "scoring"),
    }
    
    return res

@dict_reading_decorator
def read_result(result_dict):
    '''
        Прочитать ответ от bki начиная от поля "result"
    '''

    # информация о клиенте
    res = {
        **dict_reader_wrapper(result_dict, "completecode"),
        **(
            read_client(result_dict["client"])
            if "client" in result_dict.keys() else {}
        )
    }

    return res