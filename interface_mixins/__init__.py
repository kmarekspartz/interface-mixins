"""
Interfaces for Python.
"""

def Interface(interface_name, method_names, parent=None):
    """
    Create an interface with the the name and method names given.
    """
    if parent is None:
        parent = (object, )

    def interface_helper(*args, **kwargs):
        """
        The default implementation of a method for an interface.
        """
        raise NotImplementedError
    methods = {
        method_name: interface_helper
        for method_name
        in method_names
    }
    return type(interface_name, parent, methods)


def AbstractInterfaceTest(test_name, method_names, parent=None):
    """
    Create an abstract tests with the test name which makes sure the methods
    with the names given are implemented.
    """
    if parent is None:
        parent = (object, )

    def abstract_interface_test_helper(method_name):
        """
        Creates a closure to test a method with the given method_name.
        """
        def test_method(self):
            """
            Closure to test for the existence of a method on self.obj given
            by method_name.
            """
            try:
                getattr(self.obj, method_name)()
            except NotImplementedError:
                self.fail(
                    type(self.obj).__name__ +
                    ' does not implement ' +
                    method_name
                )
        return test_method
    methods = {
        'test_' + method_name: abstract_interface_test_helper(method_name)
        for method_name
        in method_names
    }
    return type(test_name, parent, methods)
