import re
from re import Match

def get_method_docs() -> dict:
    from json import loads
    with open('docs.json', 'r') as f:
        return (loads(f.read())['methods'])

def substitute_method_docs(matches: list[Match[str]], method_docs: dict[str, dict]):
    resources: list[str] = [x.group(1) for x in matches]
    for resource in resources:        
        sub_resource_doc_str = f"<!--m-start {resource} -->\n#### `{resource}`\n**Methods:**\n"
        methods: list[tuple[str, dict]] = method_docs[resource].items()
        for meth, parts in methods:
            meth_doc_string: list[str] = []
            meth_doc_string.append(f'- <details><summary><code>{meth}</code></summary>\n\n')
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
        pattern = re.compile(r'<!--m-start (.+) -->.*<!--m-end \1 -->', re.S)
        matches = list(pattern.finditer(readme))
        return matches

def main():
    method_docs = get_method_docs()
    matches = get_resource_matches()
    sub_method_docs = substitute_method_docs(matches, method_docs)
    with open('README.md', 'r') as f:
        readme: str = f.read()
        for sub, resource in zip(sub_method_docs, matches):
            res = resource.group(1)
            if (sub != f'<!--m-start {res} -->\n#### `{res}`'
                f'\n**Methods:**\n<!--m-end {res} -->'):
                readme = readme.replace(resource.group(0), sub)
            
    with open('README.md', 'w') as f:
        f.write(readme)

if __name__ == '__main__':
    main()
