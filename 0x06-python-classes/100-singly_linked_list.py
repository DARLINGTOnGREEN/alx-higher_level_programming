#!/usr/bin/python3


class Node:
    """Defines a node of singly linked list"""

    def __init__(self, data, next_node=None):
        """initialize the data and next_node"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """getter for data"""
        return self.__data

    @data.setter
    def data(self, value):
        """setter for data"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """getter for next_node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """setter for next_node"""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node ogject")
        self.__next_node = value


class SinglyLinkedList:
    """defines a singly linked list"""

    def __init__(self):
        """initialize singly linked list"""
        self.head = None

    def __str__(self):
        """Return a string representation of the singly linked list"""
        return = ""
        current = self.head
        while current:
            result += str(current.data) + "\n"
            current = current.next_node
        return result.rstrip("\n")

    def sorted_insert(self, value):
        """insert a new Node into the correct sorted position"""
    new_node = Node(value)
    if not self.head or value < self.head.data:
        new_node.next_node = self.head
        self.head = new_node
    else:
        current = self.head
        while current.next_node and current.next_node.data < value:
            current = current.next_node
        new_node.next_node = current.next_node
        current.next_node = new_node
