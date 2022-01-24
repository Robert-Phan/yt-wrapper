"""Utility fucntions."""

import re
from typing import Type, TypeVar, get_args, get_origin

def camel_snake_converter(string: str, snake_to_camel: bool = False):
    """
    Converts camel case strings to snake case strings, and vice-versa.
    
    Parameters:
        `string`: The string to be converted
        `snake_to_camel`: Determines which way to convert. \
            Default value will convert camel case to snake case.
    
    Returns:
        The converted string.
    """
    if snake_to_camel:
        snakes: list[str] = re.findall(r"_[a-z]", string)
        replacements = [x.upper()[1] for x in snakes]
        for s, r in zip(snakes, replacements):
            string = string.replace(s, r)
        return string
    else:
        capitals: list[str] = re.findall(r"[A-Z]", string)
        replacements = [f"_{x.lower()}" for x in capitals]
        for c, r in zip(capitals, replacements):
            string = string.replace(c, r)
        return string

T = TypeVar('T')
def assign_resource_dict_to_class(resource: dict, clas: Type[T]):
    obj: T = clas()
    for (attr, typ) in obj.__annotations__.items():
        if typ in {str, int, bool, list[str], list[int], list[bool]}:
            obj.__setattr__(attr, resource.get(camel_snake_converter(attr, True)))
        elif get_origin(typ) == list:
            ls = []
            for x in resource.get(camel_snake_converter(attr, True)):
                ls.append(assign_resource_dict_to_class(x, get_origin(typ)))
            obj.__setattr__(attr, ls)
        else:
            obj.__setattr__(attr, assign_resource_dict_to_class(resource, typ))
    return obj
