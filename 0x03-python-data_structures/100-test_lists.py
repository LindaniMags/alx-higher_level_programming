import ctypes

library = ctypes.CDLL('./libPyList.so')
library.print_python_list_info.argtypes = [ctypes.py_object]
lists = ['hello', 'World']
library.print_python_list_info(lists)
del lists[1]
library.print_python_list_info(lists)
lists = lists + [4, 5, 6.0, (9, 8), [9, 8, 1024], "Holberton"]
library.print_python_list_info(lists)
lists = []
library.print_python_list_info(lists)
lists.append(0)
library.print_python_list_info(lists)
lists.append(1)
lists.append(2)
lists.append(3)
lists.append(4)
library.print_python_list_info(lists)
lists.pop()
library.print_python_list_info(lists)
