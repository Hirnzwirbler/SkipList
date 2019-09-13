import random


class LinkedListNode(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList():
    def __init__(self, head=None):
        self.head = head


class SkipListNode():
    """
    Needed:
    key
    value
    toplayer

    """

    def __init__(self):
        pass


class SkipList():
    def __init__(self):
        pass

    def __next__(self):
        pass

    def search(self):
        pass

    def insert(self):
        pass

    def delete(self):
        pass


def main():
    pass


if __name__ == "__main__":
    main()
