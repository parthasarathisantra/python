import os

def list_directory_contents(path="/Users"):
    """
    Print the files and subdirectories in the given path.
    If path is not provided, it lists the current directory.
    """
    try:
        entries = os.listdir(path)
    except FileNotFoundError:
        print(f"Error: The directory '{path}' does not exist.")
        return
    except PermissionError:
        print(f"Error: Permission denied for directory '{path}'.")
        return
    except OSError as e:
        print(f"Error reading directory '{path}': {e}")
        return

    print(f"Contents of directory: {path}")
    for entry in entries:
        print(entry)


if __name__ == "__main__":
    # Example usage:
    # To list the current directory:
    list_directory_contents()

    # Or to list a specific directory, e.g.:
    # list_directory_contents("C:/Users/parth/OneDrive/skill/python/chapter 1")
