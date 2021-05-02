
class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def print_forward(self):
        if self.head is None:
            print("Linked List is empty")
            return

        linked_list = ''
        itr = self.head
        while itr:
            linked_list += str(itr.data)
            if itr.next:
                linked_list += "<-->"
            else:
                linked_list += "-->"
            itr = itr.next
        print(linked_list)

    def print_backward(self):
        if self.head is None:
            print('Linked List is empty')

        itr = self.head
        while itr.next is not None:
            itr = itr.next

        linked_list = ""

        while itr:
            linked_list += str(itr.data)
            if itr.prev:
                linked_list += "<-->"
            else:
                linked_list += "-->"
            itr = itr.prev
        print(linked_list)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next

        return count

    def insert_at_beginning(self, data):
        new_node = Node(data, self.head)

        if self.head is None:
            self.head = new_node
        else:
            self.head.prev = new_node
            self.head = new_node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data)
            return

        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None, itr)

    def insert_at(self, index, data):

        if index < 0 or index > self.get_length():
            raise Exception("Index out of bounds")
        if index == self.get_length():
            self.insert_at_end(data)
            return
        elif index == 0:
            self.insert_at_beginning(data)
            return
        else:
            itr = self.head
            count = 0
            while itr:
                if count+1 == index:
                    new_node = Node(data, itr.next, itr)
                    itr.next.prev = new_node
                    itr.next = new_node
                    return
                itr = itr.next
                count += 1

    def remove_at(self, index):
        if index < 0 or index > self.get_length():
            raise Exception("Index out of bounds")
        if index == 0:
            self.head = self.head.next
            self.head.prev = None
            return

        itr = self.head
        count = 0
        while itr:
            if count + 1 == index:
                itr.next.next.prev = itr
                itr.next = itr.next.next
                return
            itr = itr.next
            count += 1

    def insert_values(self, data_lists):
        self.head = None

        for data in data_lists:
            self.insert_at_end(data)

    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            return

        itr = self.head
        while itr:
            if itr.data == data_after:
                new_node = Node(data_to_insert, itr.next, itr)
                if itr.next.next:
                    itr.next.next.prev = new_node
                itr.next = new_node

    def remove_by_values(self, value):
        if self.head is None:
            return

        itr = self.head

        if itr.data == value:
            self.head = self.head.next

        while itr:
            if itr.next.data == value:
                if itr.next.next:
                    itr.next = itr.next.next
                    itr.next.next.prev = itr
                    return
                else:
                    itr.next = None
                    return


if __name__ == '__main__':
    ll = DoublyLinkedList()
    ll.insert_values(["banana", "mango", "grapes", "orange"])
    ll.print_forward()
    ll.print_backward()
    ll.insert_at_end("figs")
    ll.print_forward()
    ll.insert_at(0, "jackfruit")
    ll.print_forward()
    ll.insert_at(6, "dates")
    ll.print_forward()
    ll.insert_at(2, "kiwi")
    ll.print_forward()

# Exercise

# Implement doubly linked list.
# The only difference with regulaer linked list is that double linked has prev node reference as well.
# # That way you can iterate in forward and backward direction. Your node class will look this this,
#
# # class Node:
# #     def __init__(self, data=None, next=None, prev=None):
# #         self.data = data
# #         self.next = next
# #         self.prev = prev
# # Add following new methods,
# #
# # def print_forward(self):
# #     # This method prints list in forward dirction. Use node.next
#
# def print_backward(self):
#     # Print linked list in reverse direction. Use node.prev for this.
# Implement all other methods in regular linked list class and make necessary changes for doubly linked list
# (you need to populate node.prev in all those methods)
