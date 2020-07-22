######   1
print("Qs 1 ans.")
a = {
    "key1": 1,
    "key2": {
            "key3": 1,
            "key4": {
                    "key5": 4
            }
    }
}


def print_depth(a):
    d = 1
    # testList = [] #uncomment this line for testing test_bongo.py

    def depth(a, d):
        for key in a:
            if type(a[key]) == dict:
                print(key + " " + str(d))
                # testList.append(str(d)) #uncomment this line for testing test_bongo.py
                depth(a[key], d+1)
            else:
                print(key + " " + str(d))
                # testList.append(str(d)) #uncomment this line for testing test_bongo.py
    depth(a, d)
    # return testList #uncomment this line for testing test_bongo.py
print_depth(a)


######   2
print("\nQs 2 ans.")


class Person(object):
    def __init__(self, first_name, last_name, father):
        self.first_name = first_name
        self.last_name = last_name
        self.father = father

    def dic(self):
        d = {}
        d = {
            "first_name:": self.first_name,
            "last_name:": self.last_name,
            "father:": self.father
        }
        return d


person_a = Person(" User ", " 1 ", None)
person_b = Person(" User1 ", " 2 ", person_a.dic())

a = {
    "key1": 1,
    "key2": {
            "key3": 1,
            "key4": {
                    "key5": 4,
                    "user:": person_b.dic(),
            },
    },
}


def print_depth(a):
    d = 1
    testList = []

    def depth(a, d):
        for key in a:
            if type(a[key]) == dict:
                print(key + " " + str(d))
                testList.append(str(d))
                # d += 1
                depth(a[key], d+1)
            else:
                print(key + " " + str(d))
                testList.append(str(d))
    depth(a, d)
    return testList


print_depth(a)

####   3
print("\nQs 3 ans.")


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def findPath(root, path, node):
    if root is None:
        return False

    path.append(root.value)

    if root.value == node:
        return True

    if findPath(root.left, path, node) or findPath(root.right, path, node):
        return True

    path.pop()
    return False


def lca(node1, node2):
    path1 = []
    path2 = []

    if (not findPath(root, path1, node1)) or not (findPath(root, path2, node2)):
        return "Invalid node."

    p = 0
    while p < len(path1) and p < len(path1):
        if path1[p] != path2[p]:
            break
        p += 1

    return path1[p - 1]


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(8)
root.left.left.right = Node(9)
root.right.left = Node(6)
root.right.right = Node(7)
print(lca(5, 7))

