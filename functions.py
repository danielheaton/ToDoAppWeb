# Constants used in the functions module
FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """ Read a text file of the todo list. """
    # Open file with context manager. This will automatically close the file with an error or completion
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg,filepath=FILEPATH):
    """ Write the to-do items list in the text file."""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    print("Hello")
    print(get_todos())