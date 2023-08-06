import xmltodict

def dict_from_xmlfile(filename):
    '''
        Get dictionary from filename.
        Args:
            filename : (str) path to the XML file to be read;
        Return:
            (dict) with data;
    '''
    f = open(filename, "rb")
    data_dict = xmltodict.parse(f.read())
    f.close()
    return data_dict


def recursive_dict_reader(my_dict, prev_pef_names = []):
    '''
        Recursive deployer of nested dictionaries 
        dictionaries into a single-level dictionary.
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
        A decorator that checks if the searched key 
        is in the dictionary. Dictionary, if not, the 
        exception is triggered - an empty dictionary 
        is returned.
    '''
    def wrapper(dict):
        try:
            return func(dict)
        except KeyError:
            return {}
    
    return wrapper

def dict_reader_wrapper(my_dict, key_name):
    '''
        In order to quickly call
        recursive_dict_reader for those cases
        where the first level of the key is the same as
        key of the expanded subdictionary.

        Args:
            my_dict - top-level dictionary;
            key_name - sub-dictionary key in the top-level dictionary.
    '''
    return (
        recursive_dict_reader(my_dict[key_name], [key_name])
        if key_name in my_dict.keys() else {}
    )