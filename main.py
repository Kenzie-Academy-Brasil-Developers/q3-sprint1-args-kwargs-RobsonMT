def sum_numbers(*args: list[int]) -> int:
    return(sum(args))


def get_multiplied_amount(multiplier: int, *args: list[int]) -> int:
    return(multiplier * sum(args))
 

def word_concatenator(*args: list[str]) -> str:
    return(' '.join(args))


def inverted_word_factory(*args: tuple) -> str:
    output = (' '.join([x[::-1] for x in list(args[::-1])]))
    return output


def dictionary_separator(**kwargs: dict) -> tuple:
    keys = [x for x in kwargs.keys()]
    values = [x for x in kwargs.values()]
    return(tuple([keys] + [values],))


def dictionary_creator(*args, **kwargs):
    if len(args) < len(kwargs):
        return None
    
    dict_values = []
    
    output = {}

    for value in kwargs.values():
        dict_values.append(value)

    for i, value in enumerate(dict_values):
        output[args[i]] = value
    
    return output


def purchase_logger(**kwargs):
    product = f'Product {str(kwargs["name"])}'
    coast = f'costs {str(kwargs["price"])}'
    quantity = f'and was bought {str(kwargs["quantity"])}'

    return f'{product} {coast} {quantity}'


def world_cup_logger(country, *args):
    sorted_list = sorted([str(x) for x in args])
    output = f'{country} - '

    for year in sorted_list:
        if year == sorted_list[-2]:
            output += f'{year} e '
        elif year == sorted_list[-1]:
            output += year
        else:
             output += f'{year}, '

    return output