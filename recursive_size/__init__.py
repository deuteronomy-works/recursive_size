# This module recursively gets the size of a folder
import os


def looper(path_name):
    try:
        _ = os.listdir(path_name)

    except FileNotFoundError:
        # Probably file path is too long
        # will attempt to read anyway
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

    except:
        return os.stat(path_name).st_size

    return get_size(path_name)


def get_size(folder_name):
    total = 0

    try:
        conts = os.listdir(folder_name)

    except:
        try:
            return os.stat(folder_name).st_size

        except Exception as exc:
            # Send early error back to user
            raise RuntimeError(f'Unable to read {folder_name}') from exc

    for x in conts:
        y = os.path.join(folder_name, x)
        total += looper(y)

    return total

