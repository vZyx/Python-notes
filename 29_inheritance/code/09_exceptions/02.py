

try:
    path = input()
    file = open(path, 'r')
    file.close()
except FileNotFoundError:
    print('FileNotFoundError')
except PermissionError:
    print('PermissionError')
except OSError:
    print('Interrupted or Timeout errors')
except Exception as e:
    print(e)

"""
not_exist.txt     ==> FileNotFoundError
/boot/efi/        ==> PermissionError
"""