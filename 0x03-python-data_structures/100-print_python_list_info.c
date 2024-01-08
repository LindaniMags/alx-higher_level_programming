#include <Python.h>
#include <object.h>
#include <listobject.h>

void print_python_list_info(PyObject *p)
{
	long int length = PyList_Size(p);
	int count;
	PyListObject *object = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", length);
	printf("[*] Allocated = %li\n", object->allocated);
	for (count = 0; count < length; count++)
		printf("Element %count: %s\n", count, Py_TYPE(object->val[count])->name_);
}
