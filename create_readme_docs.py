def get_method_docs():
    from json import loads
    with open('docs.json', 'r') as f:
        return (loads(f.read())['methods'])

def get_replaceables():
    import re
    with open('README.md', 'r') as f:
        readme: str = f.read()
        pattern = re.compile('<!--m .+ -->')
        replaceables: list[str] = pattern.findall(readme)
        return replaceables

def generate_method_docs(replaceables: list[str], method_docs: dict):
    replaceables = [x[6:-4] for x in replaceables]
    for resource in replaceables:
        methods: list[tuple[str, dict]] = method_docs[resource].items()
        final_resource_string = f"#### `{resource}`\n**Methods:**\n"
        for meth, parts in methods:
            final_meth_string: list[str] = []
            final_meth_string.append(f'- <details><summary><code>{meth}</code></summary>\n\n')
            
            part_items: list[tuple[str, any]] = parts.items()
            for part, under in part_items:
                if part == 'def':
                    final_meth_string.append(f'    {under}  \n')
                elif part == 'ref':
                    final_meth_string.append(f'    [Reference]({under})')
                else:
                    params: dict[str, list[str]] = under
                    final_meth_string.append(f'    {part}:\n')
                    for param, param_doc in params.items():
                        final_meth_string.append(f'    - `{param}`\n\n')
                        param_doc_str = ''.join([f'        {x}\n' for x in param_doc])
                        final_meth_string.append(param_doc_str)
                    final_meth_string.append('\n')
            final_meth_string.append('\n</details>\n\n')
            final_resource_string += ''.join(final_meth_string)
        yield (final_resource_string)

if __name__ == '__main__':
    method_docs = get_method_docs()
    replaceables = get_replaceables()
    with open('README.md', 'r') as f:
        readme: str = f.read()
        for replaced, original in zip(generate_method_docs(replaceables,
                                                           method_docs), replaceables):
            if replaced != f'#### `{original[6:-4]}`\n**Methods:**\n':
                print(f'Writing docs for {original[6:-4]}...')
                readme = readme.replace(original, replaced)
    
    with open('README.md', 'w') as f:
        f.write(readme)