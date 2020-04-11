import os
from typing import List


def find_files(suffix: str, path: str) -> List[str]:
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    # check inputs
    if not isinstance(suffix, str): raise ValueError('suffix must be a string')
    if not os.path.isdir(path): raise FileNotFoundError(f'No such directory found: {path}')

    child_items = os.listdir(path)
    found_files = list()

    for item in child_items:
        item_path = os.path.join(path, item)

        # if item is a file and matches suffix, add it in list
        if os.path.isfile(item_path) and item_path.endswith(suffix):
            found_files.append(item_path)

        # if item is a directory, recursively search it for matching files.
        elif os.path.isdir(item_path):
            found_files.extend(find_files(suffix, item_path))

    return found_files



if __name__ == "__main__":
    c_files = find_files('.c', './testdir')
    print(*c_files, sep='\n')

    # search python files. There are none so this shouldn  print empty list
    print('Python files: ', end='')
    print(find_files('.py', './testdir'), sep='\n')

    # Python file in current directory includes this file itself
    print('Python in current folder: ', end='')
    print(find_files('.py', './'))

    # Specifying no suffix will return all the files
    print('No suffix filter: ', end='')
    print(find_files('', './testdir'))

    # Find deeply nested file
    print('Find deeply hideen haskell file: ', end='')
    print(find_files('.hs', './testdeepdir'))

    # Directory doesn't exist
    print('Check on directory that doesn\'t exist: ', end='')
    print(find_files('.hs', './whereisthisdir'))  # this should raise FileNotFoundError
