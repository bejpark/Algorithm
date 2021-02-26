class Node:
    def __init__(self,data,prev=None,next=None):
        self.prev=prev
        self.next=next
        self.data=data

class NodeMgmt:
    def __init__(self,data):
        self.head=Node(data)
        self.tail=self.head

    def insert(self,data):
        if self.head==None:
            self.head=Node(data)
            self.tail=self.head
        else:
            node=self.head
            while node.next:
                node=node.next
            new=Node(data)
            node.next=new
            new.prev=node
            self.tail=new

    def desc(self):
        node=self.head
        while node:
            print(node.data)
            node=node.next

    def search_from_head(self,data):
        if self.head==None:
            return False
        node=self.head
        while node:
            if node.data==data:
                return node
            else:
                node=node.next
        return False

    def insert_before(self,data,before_data):
        if self.head==None:
            self.head=Node(data)
            return True
        else:
            node=self.tail
            while node.data!=before_data:
                node=node.prev
                if node==None:
                    return False
            new = Node(data)
            before_new=node.prev
            before_new.next=new
            new.prev=before_new
            new.next=node
            node.prev=new

double_link=NodeMgmt(0)
for data in range(1,10):
    double_link.insert(data)
double_link.desc()


node_1=double_link.search_from_head(4)
print(node_1.data)

double_link.insert_before(1.5, 2)
double_link.desc()
