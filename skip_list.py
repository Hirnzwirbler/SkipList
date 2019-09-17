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
    """
    The very basic structure of a single node for a skip list.
    Stores the element and the "tower" for the skipping with the given height.
    """

    def __init__(self, height=0, elem=None):
        self.elem = elem
        self.next = [elem] * (height + 1)

    def display_node(self):
        """
        Just to display the single node with the element and the max height level.
        Right now it is more a method to make it easier to check if everything is working.
        """
        print('Elem: ' + str(self.elem) + ' : Lvl = ' + str(self.next.__len__()))


class SkipList:
    """
    The class for the skip list. Always has the head as a basic Node, a length and a max height.
    The skip list is basically a linked list with shortcuts for faster access
    For the basic functionality:
     - https://en.wikipedia.org/wiki/Skip_list
     - https://brilliant.org/wiki/skip-lists/
     - https://azrael.digipen.edu/~mmead/www/Courses/CS280/SkipLists.html
    Otherwise every function is documented for more insight
    """

    def __init__(self):
        self.head = SkipListNode()
        self.len = 0
        self.maxHeight = 0

    def __len__(self):
        """
        Simple len method. Nothing special
        :return: length of list
        """
        return self.len

    def random_height(self):
        """
        Basically a simulated coin toss and depending on the outcome the height increments or is returned
        However the height needs at least to be 1
        :return: int : Height
        """
        height = 1
        while randint(1, 2) != 1:
            height += 1
        return height

    def find(self, elem, update=None):
        """
        Searches the skip list for an element (data type should not matter)
        If no update is given it will generate one
        :param elem: The element to search for
        :param update: the update list, None if not provided
        :return: item or None
        """
        if update is None:
            update = self.update_list(elem)
        if len(update) > 0:
            item = update[0].next[0]
            if item is not None and item.elem == elem:
                return item
        return None

    def update_list(self, elem):
        """
        The update list is basically the search path
        Builds the update list by checking the current items next list (top to bottom)
        If it is not None and the element is not too small. The current is set with the next one and stored in the
        update list at the height level it was found.
        :param elem: the element you search for
        :return: update list
        """
        update = [None] * self.maxHeight
        current = self.head
        for i in reversed(range(self.maxHeight)):
            while current.next[i] is not None and current.next[i].elem < elem:
                current = current.next[i]
            update[i] = current
        return update

    def contains(self, elem, update=None):
        """
        Simply utilizes the find method to check if an element exists in the list
        :param elem: the element to search for
        :param update: update list
        :return: True or False
        """
        if self.find(elem, update) is None:
            return False
        else:
            return True

    def insert(self, elem):
        """
        Adds a new element at the right place, so the whole list stays ordered.
        Creates a node first with the given element and a random height.

        :param elem: The new element for the list
        """
        node = SkipListNode(self.random_height(), elem)

        self.maxHeight = max(self.maxHeight, len(node.next))
        while len(self.head.next) < len(node.next):
            self.head.next.append(None)

        update = self.update_list(elem)
        if self.find(elem, update) is None:
            for i in range(len(node.next)):
                node.next[i] = update[i].next[i]
                update[i].next[i] = node
            self.len += 1

    def delete(self, elem):
        """
        Deletes the given element.
        Basically works similar to insert but in reverse
        :param elem: the element to delete
        """
        update = self.update_list(elem)
        foundElem = self.find(elem, update)
        if foundElem is not None:
            for i in range(len(foundElem.next)):
                update[i].next[i] = foundElem.next[i]

    def display_list(self):
        """
        Simply displays the complete skip list, including their height levels
        """
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
    print('Displaying the whole list with height levels:')
    print('The None Element basically tells the max level for the whole list.')
    print('')
    sk.display_list()
    print('')
    print('Finding a Node:')
    print('')
    sk.find(10).display_node()
    print('')
    print('Deleting a Node:')
    print('')
    sk.delete(10)
    sk.display_list()


if __name__ == "__main__":
    main()
