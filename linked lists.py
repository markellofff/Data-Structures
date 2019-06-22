"""
Properties of linked list:
1. Successive elements are connected by pointers
2. The last node points to NULL
3. Can grow or sink in size during execution of the program
4. Does not waste memory space (But takes extra memory space for pointers). it allocates memory as list grows.
"""
"""SINGLY LINKED LIST"""


# Node of singly linked list

class Node:
    # Constructor
    def __init__(self, data):
        self.data = data
        self.next = None


class Linked_list:

    def __init__(self):
        self.head = None

    # Method for printing all the elements of the list
    def elements(self):
        temp = self.head
        elems = []
        while temp:
            elems.append(temp.data)
            temp = temp.next
        return elems

    def length_list(self):
        temp = self.head
        count = 0
        while temp.next != None:
            temp = temp.next
            count += 1
        return count

    # Method for the traversal of the list by its index no
    def index(self, data):
        index = 0
        cur = self.head
        while (cur):
            if cur.data == data:
                print(f"{data} is at the index {index}")
            cur = cur.next
            index += 1

    def search_index(self, index_no):
        cur = self.head
        if index_no == 0:
            return self.head.data
        index = 0
        while True:
            if index == index_no:
                return (f"Data at index no {index_no} is {cur.data}")
            cur = cur.next
            index += 1

    # Method for inserting an object or data in beginning of the list
    def insert_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Method for inserting the node at last
    def insert_end(self, data):
        new_node = Node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node

    # Method for inserting the data after the given index
    def insert_after_index(self, prev_index, new_data):
        if prev_index < 0 or prev_index > self.length_list():
            print("Index Out Of range")
            return
        if prev_index == 0:
            return self.insert_beginning(new_data)
        else:
            new_node = Node(new_data)
            cur_index = 0
            cur = self.head
            while cur_index < prev_index:
                cur_index += 1
                cur = cur.next
            new_node.next = cur.next
            cur.next = new_node

    # Method for deleting the Node from start
    def delete_start(self):
        if self.length_list() == 0:
            print("Empty list")
            return
        else:
            self.head = self.head.next

    # Method for deleting Node from the End
    def delete_end(self):
        if self.length_list() == 0:
            print("Empty list")
            return
        else:
            cur_node = self.head
            prev_node = self.head
            while cur_node.next != None:
                prev_node = cur_node
                cur_node = cur_node.next
            prev_node.next = None
            return
    # Method for deleting the intermediate Node by its Index No
    def del_intermediate(self,index):
        if index > self.length_list():
            print( "Index Out of Range")
            return
        if index == self.length_list():
            self.delete_end()
            return
        if index == 0:
            self.delete_start()
            return
        cur_node = self.head
        prev_node = self.head
        cur_index = 0
        while cur_index != index:
            prev_node = cur_node
            cur_node = cur_node.next
            cur_index+=1
        prev_node.next = cur_node.next
        return

    
# Driver Code
# Following comments are the output of that particular line
my_list = Linked_list()
first = my_list.head = Node(12)
second = first.next = Node(15)
third = second.next = Node(20)
print(my_list.elements()) # [12, 15, 20]
print(my_list.length_list()) # 2
my_list.insert_beginning(101)  # [101, 12, 15, 20]
print(my_list.elements()) # [101, 12, 15, 20]
my_list.insert_end(10000)  # [101, 12, 15, 20, 10000]
my_list.insert_after_index(2, 5100)  # [101, 12, 15, 5100, 20, 10000]
print(my_list.elements())
my_list.delete_start()  # [12, 15, 5100, 20, 10000]
print(my_list.elements())
my_list.delete_end()  # [12, 15, 5100, 20]
print(my_list.elements())
my_list.del_intermediate(2) # [12, 15, 20]
print(my_list.elements())
