# -*- coding: utf-8 -*-
# Parte C — Listas Enlazadas

# Nodo para lista simple
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# TODO 5: Lista enlazada simple
class LinkedList:
    def __init__(self):
        self.head = None

    def insert_front(self, data):
        nuevo = Node(data)
        nuevo.next = self.head
        self.head = nuevo

    def insert_end(self, data):
        nuevo = Node(data)
        if self.head is None:
            self.head = nuevo
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = nuevo

    def traverse(self):
        actual = self.head
        print("Elementos de la lista:")
        if actual is None:
            print("Es una lista vacia :'(")
            return
        while actual:
            print(actual.data, end=" -> ")
            actual = actual.next
        print("None")

# Nodo para lista doblemente enlazada
class DNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

# TODO 6: Lista doblemente enlazada
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None 

    def insert_front(self, data):
        nuevo = DNode(data)

        if self.head is None:
            self.head = nuevo
            self.tail = nuevo
        else:
            nuevo.next = self.head
            self.head.prev = nuevo
            self.head = nuevo

    def insert_end(self, data):
        new_node = DNode(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def traverse_forward(self):
        current = self.head
        print("\nRecorrido  hacia adelante:")
        if current is None:
            print("Es una lista vacia.")
            return

        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

    def traverse_backward(self):
        current = self.tail
        print("\nRecorrido hacia atrás:")
        if current is None:
            print("Es una lista vacia.")
            return

        while current:
            print(current.data, end=" <-> ")
            current = current.prev
        print("None")

if __name__ == "__main__":
    print("== Listas Enlazadas ==")

    print("\nLista simple:")
    l = LinkedList()
    l.insert_front(10)
    l.insert_end(20)
    l.traverse()

    print("\nLista doblemente enlazada:")
    dl = DoublyLinkedList()
    dl.insert_front(1)
    dl.insert_end(2)
    dl.insert_end(3)
    dl.traverse_forward()
    dl.traverse_backward()