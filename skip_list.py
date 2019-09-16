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

    def insert(self, data):
        new_node = LinkedListNode(data)
        new_node.set_next(self.head)
        self.head = new_node

    def size(self):
        current = self.head
        counter = 0
        while current:
            counter += 1
            current = current.get_next()
        return counter

    def find(self, data):
        current = self.head
        found = False
        while current and not found:
            if current.get_data == data:
                return current
            else:
                current = current.get_next()
        if current is None:
            raise ValueError("Data not found!")

    def delete(self, data):
        current = self.head
        previous = None
        found = False
        while current and not found:
            if current.get_data == data:
                found = True
            else:
                current = current.get_next()
                previous = current
        if current is None:
            raise ValueError("Data not found!")
        if previous is None:
            raise ValueError("Data not found!")
        else:
            previous.set_Next(current.get_next())


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
