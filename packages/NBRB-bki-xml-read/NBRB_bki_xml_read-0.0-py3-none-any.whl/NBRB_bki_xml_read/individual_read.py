@dict_reading_decorator
def read_client(client_dict):
    '''
        Read bki information starting from the "client" field
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
        Read the response from bki starting from the "result" field.
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