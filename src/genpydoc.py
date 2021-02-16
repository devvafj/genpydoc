from itertools import chain
import sys


path_to_file = "sample.py"
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
    """
    Iterates over a list of strings and returns all elements in a single-line string.

    Parameters:
    ----------
    lst: list
        The list that will be iterated.

    Returns:
    ----------
    A string with all elements from the list joined without separators.
    """
    return ''.join(chain.from_iterable(lst))


def write_docs(path_to_file, doc):
    """
    Create Docstrings template to each function in a file.

    Parameters:
    ----------
    path_to_file: str
        A string representing the path where the file is located,
        including the filename and extension.
    """
    with open(path_to_file, 'r+') as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            if line.startswith('def'):
                lines[i] = lines[i].strip() + chain_list(doc)
        f.seek(0)
        for line in lines:
            f.write(line)
    f.close()


def run_script():
    """
    It's the entrypoint function when the script will run.

    To run this script, navigate to its location and execute with command line:
    python genpydoc.py <path>/<file>.<extension>

    E.g.
    python genpydoc.py C:/Users/Vafj/Documents/sample.py OR
    python genpydoc.py /home/Documents/sample.py

    Note: The function checks if the second argument was passed and if only 2 arguments were passed.
    Otherwise the script report an invalid syntax. If the path/file doesn't exists, no such file report.
    """
    if len(sys.argv) > 2 or len(sys.argv) == 1:
        print("[ERROR]: The syntax used to call this script was wrong:")
        print("Right Sintax: python genpydoc.py <path>/<file>.<extension>")
    else:
        try:
            write_docs(sys.argv[1], numpydoc)
            print(f"[SUCCESS] Awesome! Docstrings were added to script!")
        except FileNotFoundError:
            print(f"[ERROR] Sorry, the file or directory used doesn't exist -> {sys.argv[1]}")


if __name__ == '__main__':
    run_script()
