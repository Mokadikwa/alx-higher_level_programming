#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - C function that prints some basic info about Python lists
 * @p: pointer to an object of type PyObject
 */

void print_python_list_info(PyObject *p)
{
	Py_ssize_t size = PyList_Size(p);
	Py_ssize_t alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", alloc);

	for (Py_ssize_t i = 0; i < size; ++i)
	{
		PyObject *item = PyList_GetItem(p, i);
		const char *type = Py_TYPE(item)->tp_name;
		printf("Element %ld: %s\n", i, type);
	}
}
