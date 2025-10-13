import os

def list_directory_contents(path='/'):
    try:
        entries = os.listdir(path)
        print(f'Contents of "{path}":')
        for entry in entries:
            print(entry)
    except FileNotFoundError:
        print(f'Error: The directory "{path}" does not exist.')
    except PermissionError:
        print(f'Error: Permission denied to access "{path}".')
    except Exception as e:
        print(f'An unexpected error occurred: {e}')

# Example usage
list_directory_contents()  # Lists contents of the current directory
# list_directory_contents('/path/to/directory')  # Lists contents of a specified directory
