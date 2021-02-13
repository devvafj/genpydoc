from itertools import chain


path_to_file = "own_script.py"
numpydoc = [
            """\n    \"""\n""",
            "    Write a description here.\n"
            "\n    Parameters:\n",
            "    ----------\n",
            "    param1: type\n",
            "        Description of param1.\n",
            "    paramN: type\n",
            "        Description of paramN.\n\n",
            "    Returns:\n",
            "    ----------\n",
            "    return_var: type\n",
            "        Description of return var.\n",
            """    \"""\n""",
            ]


def chain_list(lst):
    return ''.join(chain.from_iterable(lst))


def write_docs(path_to_file, doc):
    with open(path_to_file, 'r+') as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            if line.startswith('def'):
                lines[i] = lines[i].strip() + chain_list(doc)
        f.seek(0)
        for line in lines:
            f.write(line)


def run_script():
    write_docs(path_to_file, numpydoc)


if __name__ == "__main__":
    run_script()
