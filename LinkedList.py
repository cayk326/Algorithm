class Node():
    '''
    This class define basic structure of Single Linked List.
    Also this class have some methods to do basic operation of linked list
    which are Set Data to Node, Get Data from Node, Set Next Node, Get Next Node
    '''

    # Node for Single Linked List
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
    # set the data to node
    def set_data(self, data):
        self.data = data
    # get the data from node
    def get_data(self, data):
        return self.data
    # set the next node
    def set_next(self, next):
        self.next = next
    # get the next node
    def get_next(self):
        return self.next

class SingleLinkedList():
    # Define head of single linked list
    def __init__(self):
        self.head = None
        self.length = 0
    # count single list length
    def list_length(self):
        temp = self.head
        count = 0
        while temp is not None:
            count += 1
            temp = temp.get_next()
        return count
    # print data of single linked list's node
    def print_single_linked_list(self):
        temp = self.head
        # print data while temp is not None
        while temp:
            print(temp.data, end=' ')
            temp = temp.next

    # Add node to leading linked list
    def insert_node_to_start(self,data):
    # get length of current linked list
        length = self.list_length() # get length of current linked list
        new_node = Node(data) # Create new node
        if self.head == None: # first time to insert node
            self.head = new_node # first node will be a head. next is none
        else:
            new_node.set_next(self.head)
            self.head = new_node
        self.length = length + 1


    # Add node to last linked list
    def insert_node_to_end(self,data):
        length = self.list_length()
        new_node = Node(data)
        temp = self.head

        # move to last node
        while temp.get_next is not None:
            temp = temp.get_next()
        temp.next = new_node # add new node to last position of list
        self.length = length + 1

    def insert_position(self, position, data):
        if position < 0 or position > self.length:
            raise ValueError
        else:
            if position == 0:
                self.insert_at_start(data)
            else:
                if position == self.length:
                    self.insert_at_end(data)
                else:
                    length = self.list_length()
                    new_node = Node(data)
                    count = 0
                    temp = self.head
                    while count < position - 1:
                        count += 1
                        temp = temp.get_next()
                    new_node.set_next(temp.get_next())
                    temp.set_next(new_node)
                    self.length = length + 1

    def delete(self, data):
        length = self.list_length()
        temp = self.head
        # target is head
        if (temp.next is not None):
            if (temp.data == data):
                self.head = temp.get_next()
                temp = None
                self.length = length - 1
                return
            else:
                #  search node
                while temp.next is not None:
                    if temp.data == data:
                        break
                    # save node as previous one and move to next
                    prev = temp
                    temp = temp.get_next()
                # if target will not find
                if temp is None:
                    return

                self.length = length - 1
                prev.next = temp.get_next()
                return

    def search(self, node, data):
        if node is None:
            return False
        if node.data == data:
            return True
        return self.search(node.get_next(), data)


if __name__ == '__main__':
    List = SingleLinkedList()
    # Node1
    List.insert_at_start(1)
    # Node1 -> Node2
    List.insert_at_end(2)
    # Node1 -> Node2 -> Node3
    List.insert_at_end(3)
    # Node4 -> Node1 -> Node2 -> Node3
    List.insert_at_start(4)
    # Node4 -> Node1 -> Node2 -> Node5 -> Node3
    List.insert_position(3, 5)
    # Node4 -> Node1 -> Node2 -> Node5 -> Node3 -> Node6
    List.insert_at_end(6)
    List.print_linked_list()
    print()
    # Node4 -> Node1 -> Node2 -> Node5 -> Node6
    List.delete(3)
    List.print_linked_list()
    print()