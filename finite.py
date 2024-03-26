from llist import LList, Node, append
import random


def llength(lst):
    """return the length of a finite linked list"""
    count = 0
    cnode = lst.head
    while cnode:
        count += 1
        cnode = cnode.next
    return count

def llprint(lst):
    """print a finite linked list"""
    cnode = lst.head
    while cnode:
        print(cnode.val, end=" ")
        cnode = cnode.next
    

if __name__ == "__main__":
    llist = LList()
    for i in range(10):
        append(llist,(Node(random.randint(0,100))))

from genfinite import lst
print(llength(lst))
