/* Descriptors */
#ifndef Py_DESCROBJECT_H
#define Py_DESCROBJECT_H
#ifdef __cplusplus
extern "C" {
#endif

typedef PyObject *(*getter)(PyObject *, void *);
typedef int (*setter)(PyObject *, PyObject *, void *);

struct PyGetSetDef {
    const char *name;
    getter get;
    setter set;
    const char *doc;
    void *closure;
};

PyAPI_DATA(PyTypeObject) PyClassMethodDescr_Type;
PyAPI_DATA(PyTypeObject) PyGetSetDescr_Type;
PyAPI_DATA(PyTypeObject) PyMemberDescr_Type;
PyAPI_DATA(PyTypeObject) PyMethodDescr_Type;
PyAPI_DATA(PyTypeObject) PyWrapperDescr_Type;
PyAPI_DATA(PyTypeObject) PyDictProxy_Type;
PyAPI_DATA(PyTypeObject) PyProperty_Type;

PyAPI_FUNC(uint64_t) PyDescr_NewMethod(PyTypeObject *, PyMethodDef *);
PyAPI_FUNC(uint64_t) PyDescr_NewClassMethod(PyTypeObject *, PyMethodDef *);
PyAPI_FUNC(uint64_t) PyDescr_NewMember(PyTypeObject *, PyMemberDef *);
PyAPI_FUNC(uint64_t) PyDescr_NewGetSet(PyTypeObject *, PyGetSetDef *);

PyAPI_FUNC(uint64_t) PyDictProxy_New(PyObject *);
PyAPI_FUNC(uint64_t) PyWrapper_New(PyObject *, PyObject *);

#ifndef Py_LIMITED_API
#  define Py_CPYTHON_DESCROBJECT_H
#  include "cpython/descrobject.h"
#  undef Py_CPYTHON_DESCROBJECT_H
#endif

#ifdef __cplusplus
}
#endif
#endif /* !Py_DESCROBJECT_H */
