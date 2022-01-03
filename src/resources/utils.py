import re

def camel_snake_converter(string: str, snake_to_camel: bool = False):
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
