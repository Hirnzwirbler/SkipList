from random import randint


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


class LinkedList:
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


class SkipListNode:
    def __init__(self, height=0, elem=None):
        self.elem = elem
        self.next = [elem] * (height + 1)


class SkipList:
    def __init__(self):
        self.head = SkipListNode()
        self.len = 0
        self.maxHeight = 0

    def __len__(self):
        return self.len

    def randomHeight(self):
        """
        Basically a simulated coin toss and depending on the outcome the height increments or is returned
        :return: int : Height
        """
        height = 1
        while randint(1, 2) != 1:
            height += 1
        return height

    def find(self, elem, update=None):
        if update is None:
            update = self.updateList(elem)
        if len(update) > 0:
            item = update[0].next[0]
            if item is not None and item.elem == elem:
                return item
        return None

    def updateList(self, elem):
        update = [None] * self.maxHeight
        x = self.head
        for i in reversed(range(self.maxHeight)):
            while x.next[i] is not None and x.next[i].elem < elem:
                x = x.next[i]
            update[i] = x
        return update

    def contains(self, elem, update=None):
        if self.find(elem, update) is None:
            return False
        else:
            return True

    def insert(self, elem):
        node = SkipListNode(self.randomHeight(), elem)

        self.maxHeight = max(self.maxHeight, len(node.next))
        while len(self.head.next) < len(node.next):
            self.head.next.append(None)

        update = self.updateList(elem)
        if self.find(elem, update) is None:
            for i in range(len(node.next)):
                node.next[i] = update[i].next[i]
                update[i].next[i] = node
            self.len += 1

    def displayList(self):
        current = self.head
        while current:
            print('Elem: ' + str(current.elem) + ' : Lvl = ' + str(current.next.__len__()))
            current = current.next[0]


def main():
    sk = SkipList()
    sk.insert(1)
    sk.insert(3)
    sk.insert(6)
    sk.insert(10)
    sk.insert(5)
    sk.insert(26)
    sk.insert(13)
    sk.displayList()


if __name__ == "__main__":
    main()
