import random
class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

class NodeMgmt:
    def __init__(self,head):
        self.head=head

    def insert(self,value):
        self.current_node = self.head
        while True:
            if value<self.current_node.value:
                if self.current_node.left != None:
                    self.current_node=self.current_node.left
                else:
                    self.current_node.left=Node(value)
                    break
            else:
                if self.current_node.right!=None:
                    self.current_node=self.current_node.right
                else:
                    self.current_node.right=Node(value)
                    break
    def search(self,value):
        self.current_node=self.head
        while self.current_node:
            if self.current_node.value==value:
                return True
            elif value<self.current_node.value:
                self.current_node=self.current_node.left
            else:
                self.current_node=self.current_node.right
        return False

    def delete(self,value):
        searched=False
        self.current_node=self.head
        self.parent=self.head
        while self.current_node:
            if self.current_node.value==value:
                searched=True
                break
            elif value<self.current_node.value:
                self.parent=self.current_node
                self.current_node=self.current_node.left
            else:
                self.parent=self.current_node
                self.current_node=self.current_node.right
        if searched==False:
            return False

        #####자식없는경우
        if self.current_node.left==None and self.current_node.right==None:
            if value<self.parent.value:
                self.parent.left=None
            else:
                self.parent.right=None
            del self.current_node
        ####자식있는경우
        if self.current_node.left!=None and self.current_node.right==None:
            if value<self.parent.value:
                self.parent.left=self.current_node.left
            else:
                self.parent.right=self.current_node.left
        elif self.current_node.left==None and self.current_node.right!=None:
            if value<self.parent.value:
                self.parent.left=self.current_node.right
            else:
                self.parent.right=self.current_node.right
        ####
        if self.current_node.left!=None and self.current_node.right!=None:
            if value<self.parent.value:
                self.change_node=self.current_node.right
                self.change_node_parent=self.current_node.right
                while self.change_node.left!=None:
                    self.change_node_parent=self.change_node
                    self.change_node=self.change_node.left
                if self.change_node.right!=None:
                    self.change_node_parent.left=self.change_node.right
                else:
                    self.change_node_parent.left=None
                self.parent_left=self.change_node
                self.change_node.left=self.current_node.left
                self.change_node.right=self.current_node.right
            else:
                self.change_node=self.current_node.right
                self.change_node_parent=self.current_node.right
                while self.change_node.left!=None:
                    self.change_node_parent=self.change_node
                    self.change_node=self.change_node.left
                if self.change_node.right!=None:
                    self.change_node_parent.left=self.change_node.right
                else:
                    self.change_node_parent.left=None
                self.parent.right=self.change_node
                self.change_node.left=self.current_node.left
                self.change_node.right=self.current_node.right
        return True

            
                
    

        
            
        
        

head1=Node(1)
BST=NodeMgmt(head1)
BST.insert(2)
BST.insert(4)
BST.insert(6)
BST.insert(4)
BST.insert(8)
print(BST.search(8))


bst_nums=set()
while len(bst_nums)!=100:
    bst_nums.add(random.randint(0,999))
#print(bst_nums)

#트리에 넣기 100개
head=Node(500)
binary_tree=NodeMgmt(head)
for num in bst_nums:
    binary_tree.insert(num)

#잘 된지 확인
for num in bst_nums:
    if binary_tree.search(num)==False:
        print('search Fail',num)

#10개숫자 랜덤 선택
delete_nums=set()
bst_nums=list(bst_nums)
while len(delete_nums)!=10:
    delete_nums.add(bst_nums[random.randint(0,99)])
#10개 삭제
for del_num in delete_nums:
    if binary_tree.delete(del_num)==False:
        print('delete Failed',num)

