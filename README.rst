interface-mixins
================

To create an Interface, pass it an interface name and a list of method
names. A class will be created which raises NotImplementedError for each
of the specified method names:

.. code:: python

    AnInterface = Interface('AnInterface', [
        'some',
        'methods',
        'the',
        'interface',
        'should',
        'have'
    ])

To use this interface, simply inherit from it:

.. code:: python

    class AClass(AnInterface):
        pass

We also provide a way to create abstract test cases to help test objects
against the interface:

.. code:: python

    AbstractTestAnInterface = AbstractInterfaceTest('AbstractTestAnInterface', [
        'some',
        'methods',
        'the',
        'interface',
        'should',
        'have'
    ])

These tests can be used by creating TestCases which inherit from from
the abstract test. This makes sure each method is implemented in AClass:

.. code:: python

    from unittest import TestCase

    class TestAClass(AbstractTestAnInterface, TestCase):
        def setUp(self):
            self.obj = AClass()

It is also possible to create both the Interface and the
AbstractInterfaceTest at the same time. Also, you can create multiple
interfaces using the following idiom [1]_:

.. code:: python

    interfaces = {
        'AnInterface': [
            'some',
            'methods',
            'the',
            'interface',
            'should',
            'have'
        ],
        'AnotherInterface': [
            'different',
            'methods'
        ]
    }

    for interface_name, methods in interfaces.iteritems():
        interface_name += 'Interface'
        globals()[interface_name] = Interface(interface_name, methods)
        test_name = 'AbstractTest' + interface_name
        globals()[test_name] = AbstractInterfaceTest(test_name, methods)

.. [1]
   This isn't very idiomatic Python. The use ``globals`` is ugly. This
   is just an idiom for using this library. I'm not sure I like it.
