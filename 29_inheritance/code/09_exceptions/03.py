

try:
    path = input()
    file = open(path, 'r')
    file.close()
except OSError:
    print('OSError')
except FileNotFoundError:
    print('FileNotFoundError')
except PermissionError:
    print('PermissionError')
except Exception as e:
    print(e)

"""
not_exist.txt     ==> OSError
/boot/efi/        ==> OSError
"""