# This module recursively gets the size of a folder
# The maximum file path length it can read is 263 characters
import os
import sys


MAXIMUM_FILE_PATH_LENGTH = 263


def handle_single_or_except(path_name, except_value):

    except_type = sys.exc_info()[0]

    if except_type == NotADirectoryError:
        try:
            return os.stat(path_name).st_size

        except Exception as exc:
            # Still couldn't read, still send error to user
            raise RuntimeError(f'Unable to read {path_name}') from exc

    elif except_type == FileNotFoundError:
        if len(path_name) > MAXIMUM_FILE_PATH_LENGTH:
            # won't be able to read
            print(f'ERROR - FILE NAME TOO LONG: {path_name}')
            return 0

        else:
            try:
                with open(path_name, 'rb') as long_file:
                    # successful read
                    return len(long_file.read())

            except FileNotFoundError:
                # Fix this Errno 2
                # File could not be read, skipping
                return 0

            except:
                # File could not be read, skipping
                return 0

    else:
        # Send early error back to user
        raise RuntimeError(f'Unable to read {path_name}') from except_value


def looper(path_name):
    try:
        _ = os.listdir(path_name)

    except Exception as exc:
        handle_single_or_except(path_name, exc)

    return get_size(path_name)


def get_size(folder_name):
    total = 0

    try:
        conts = os.listdir(folder_name)

    except Exception as exc:
        return handle_single_or_except(folder_name, exc)

    for x in conts:
        y = os.path.join(folder_name, x)
        total += looper(y)

    return total
