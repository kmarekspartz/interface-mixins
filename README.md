# interface-mixins

To create an Interface, pass it an interface name and a list of method names:

~~~ python
AnInterface = Interface('AnInterface', [
    'some',
    'methods',
    'the',
    'interface',
    'should',
    'have'
])
~~~


We also provide a way to create abstract test cases to help test objects
against the interface:

~~~ python
AbstractTestAnInterface = AbstractInterfaceTest('AbstractTestAnInterface', [
    'some',
    'methods',
    'the',
    'interface',
    'should',
    'have'
])
~~~


These tests can be used by creating TestCases which inherit from from the
abstract test. This makes sure each method is implemented in AClass:

~~~ python
from unittest import TestCase

class TestAClass(AbstractTestAnInterface, TestCase):
    def setUp(self):
        self.obj = AClass()
~~~


It is also possible to create both the Interface and the AbstractInterfaceTest at the same time. Also, you can create multiple interfaces using the following idiom[^1]:

~~~ python
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
~~~

[^1]: This isn't very idiomatic Python. The use `globals` is ugly. This is just an idiom for using this library. I'm not sure I like it.
