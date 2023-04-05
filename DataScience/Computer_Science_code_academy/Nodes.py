class Node:
    def __init__(self, value, link_node=None):
        self.value = value
        self.link_node = link_node
    def get_value(self):
        return self.value
    def get_link_node(self):
        return self.link_node
    def set_link_node(self,link_node=None):
        self.link_node = link_node
        

A = Node(1,[])
B = Node(2,A)
C = Node(2,[])
A.set_link_node(C)

print('Get A Node')
print(A)

print('Get value and link_node from B Node')
print(B.get_value())
print(B.get_link_node())

print('Get C value from A node')
print(A.get_link_node().get_value())