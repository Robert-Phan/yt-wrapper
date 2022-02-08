import re
from re import Match

def get_method_docs() -> dict:
    from json import loads
    with open('docs.json', 'r') as f:
        return (loads(f.read())['methods'])

def get_method_matches():
    with open('README.md', 'r') as f:
        readme: str = f.read()
        pattern = re.compile(r'<!--m-start (.+) -->.*<!--m-end \1 -->', re.S)
        matches = list(pattern.finditer(readme))
        return matches

def substitute_method_docs(matches: list[Match[str]], method_docs: dict[str, dict]):
    resources: list[str] = [x.group(1) for x in matches]
    for resource in resources:        
        sub_resource_doc_str = f"<!--m-start {resource} -->\n#### `{resource}`\n**Methods:**\n"
        methods: list[tuple[str, dict]] = method_docs[resource].items()
        for meth, parts in methods:
            meth_doc_string: list[str] = []
            meth_doc_string.append(f'- <details><summary><code>{meth}</code></summary>\n    <br>\n\n')
            part_items: list[tuple[str, any]] = parts.items()
            for part, under in part_items:
                if part == 'def':
                    meth_doc_string.append(f'    {under}  \n')
                elif part == 'ref':
                    meth_doc_string.append(f'    [Reference]({under})')
                else:
                    params: dict[str, list[str]] = under
                    meth_doc_string.append(f'    {part}:\n')
                    for param, param_doc in params.items():
                        meth_doc_string.append(f'    - `{param}`\n\n')
                        param_doc_str = ''.join([f'        {x}\n' for x in param_doc])
                        meth_doc_string.append(param_doc_str)
                    meth_doc_string.append('\n')
            meth_doc_string.append('\n</details>\n\n')
            sub_resource_doc_str += ''.join(meth_doc_string)
        sub_resource_doc_str += f'<!--m-end {resource} -->'
        yield (sub_resource_doc_str)

def get_resource_matches():
    with open('README.md', 'r') as f:
        readme: str = f.read()
        pattern = re.compile(r'<!--r-start (.+) -->.*<!--r-end \1 -->', re.S)
        matches = list(pattern.finditer(readme))
        return matches

def get_resource_docs() -> dict:
    from json import loads
    with open('docs.json', 'r') as f:
        return (loads(f.read())['resources'])

def substitute_resource_docs(matches: list[Match[str]], resource_docs: dict[str, dict]):
    def resource_dict_to_docs(resource: dict[str, str | dict], indent: int = 0):
        res: list[str] = []
        for key, value in resource.items():
            if key == 'def':
                res.append("")
                res.append("    "*indent + value)
            else:
                res.append(f"{'    '*indent}- `{key}`")
                if type(value) == str:
                    res.append("")
                    res.append('    '*(indent+1) + value)
                else:
                    cum = (resource_dict_to_docs(value, indent+1))
                    res += cum
        return res

    resources: list[str] = [x.group(1) for x in matches]
    for resource in resources:    
        resource_doc_list  = resource_dict_to_docs(resource_docs[resource])
        definition = resource_doc_list.pop(1) if resource_doc_list else ""
        resource_doc_list = ["    " + x for x in resource_doc_list]
        resource_doc = f"<!--r-start {resource} -->\n"\
        + f"#### `{resource}`\n" \
        + f"{definition}\n"\
        + f"- <details><summary><code>{resource}</code></summary>\n" \
        + '\n'.join(resource_doc_list) \
        + "\n</details>\n"\
        + f"<!--r-end {resource} -->"
        yield resource_doc


def main():
    with open('README.md', 'r') as f:
        readme: str = f.read()
        
        method_docs = get_method_docs()
        method_matches = get_method_matches()
        sub_method_docs = substitute_method_docs(method_matches, method_docs)
        for sub, resource in zip(sub_method_docs, method_matches):
            readme = readme.replace(resource.group(0), sub)
            
        resource_docs = get_resource_docs()
        resource_matches = get_resource_matches()
        sub_resource_docs = substitute_resource_docs(resource_matches, resource_docs)
        for sub, resource in zip(sub_resource_docs, resource_matches):
            readme = readme.replace(resource.group(0), sub)

    with open('README.md', 'w') as f:
        f.write(readme)

if __name__ == '__main__':
    main()
