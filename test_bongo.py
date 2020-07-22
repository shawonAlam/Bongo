import unittest
import bongoBD


class TestBongoBD(unittest.TestCase):

    def test_lca(self):
        self.assertEqual(bongoBD.lca(3, 7), 3)
        self.assertEqual(bongoBD.lca(6, 7), 3)
        self.assertEqual(bongoBD.lca(9, 6), 1)
        self.assertEqual(bongoBD.lca(0, 6), "Invalid node.")

    def test_print_depth(self):
        a = {"key1": 1, "kwy2": {"key3": 1, "key4": {"key5": 4}}}
        b = ['1', '1', '2', '2', '3']
        self.assertEqual(bongoBD.print_depth(a), b)

        a = {"key1": 1, "kwy2": {"key3": 1, "key4": {"key5": 4}, "test1": 10}}
        b = ['1', '1', '2', '2', '3', '2']
        self.assertEqual(bongoBD.print_depth(a), b)

        a = {"key1": 1, "key2": {"key3": 1, "key4": {"key5": 4}}, "test2": 10}
        b = ['1', '1', '2', '2', '3', '1']
        self.assertEqual(bongoBD.print_depth(a), b)

    def test_print_depth_2(self):
        a = {
            "key1": 1,
            "key2": {
                "key3": 1,
                "key4": {
                    "key5": 4,
                    "user:": bongoBD.person_b.dic(),
                },
            },
        }
        b = ['1', '1', '2', '2', '3', '3', '4', '4', '4', '5', '5', '5']
        self.assertEqual(bongoBD.print_depth(a), b)

        a = {
            "key1": 1,
            "key2": {
                "key3": 1,
                "key4": {
                    "key5": 4,
                    "user:": bongoBD.person_b.dic(),
                }, "test1": 11
            },
        }
        b = ['1', '1', '2', '2', '3', '3', '4', '4', '4', '5', '5', '5', '2']
        self.assertEqual(bongoBD.print_depth(a), b)

        a = {
            "key1": 1,
            "key2": {
                "key3": 1,
                "key4": {
                    "key5": 4,
                    "user:": bongoBD.person_b.dic(),
                },
            }, "test2": 22
        }
        b = ['1', '1', '2', '2', '3', '3', '4', '4', '4', '5', '5', '5', '1']
        self.assertEqual(bongoBD.print_depth(a), b)



if __name__ == '__main__':
    unittest.main()