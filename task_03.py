import sys
from pathlib import Path
from colorama import Fore

def main():
    # check required argument
    try:
        path_string = sys.argv[1]
    except IndexError:
        exit_with_error('Give directory path as argument')

    # create Path object
    path_object = Path(path_string)
    if not path_object.exists():
        exit_with_error('No such directory')
    
    if not path_object.is_dir():
        exit_with_error('Path not for directory')

    # analyze and output structure
    structure_dictionary = build_structure(path_object)
    output_structure(structure_dictionary)

def build_structure(path: Path):
    result = {}
    items = list(path.iterdir())

    for item in items:
        if item.is_dir():
            # recursion if item directory
            inside = build_structure(item)
        else:
            inside = False
        block = {item.name : inside}
        result.update(block)

    return result

def output_structure(structure: dict, indent=''):
    for name in structure:
        prep_name = indent + name
        if type(structure[name]) is dict:
            print_dir(prep_name)
            output_structure(structure[name], indent + '    ')
        else:
            print_file(prep_name)

def print_dir(name: str):
    print(Fore.CYAN + name + '/')

def print_file(name: str):
    print(Fore.GREEN + name)

def exit_with_error(error: str):
    print('Error:', error)
    exit()

if __name__ == '__main__':
    main()
