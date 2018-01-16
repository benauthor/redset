from unittest import TestCase

from redset.interfaces import Serializer


class Py3kCompatibilityTestCase(TestCase):
    def test_cant_instantiate_abstract(self):
        with self.assertRaises(TypeError):
            ser = Serializer()
