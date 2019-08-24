
# Definition for singly-linked list.
class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None
class Node: 
  # Constructor to initialize the node object 
  def __init__(self, data): 
    self.data = data 
    self.next = None
class LinkedList: 
  # Function to initialize head 
  def __init__(self): 
    self.head = None
  # Function to reverse the linked list 
  def reverse(self): 
    prev = None
    current = self.head 
    while(current is not None): 
      next = current.next
      current.next = prev 
      prev = current 
      current = next
    self.head = prev 
  # Function to insert a new node at the beginning 
  def push(self, new_data): 
    new_node = Node(new_data) 
    new_node.next = self.head 
    self.head = new_node 
  
  # Utility function to print the linked LinkedList 
  def printList(self): 
    temp = self.head 
    while(temp): 
      print(temp.data) 
      temp = temp.next

class Solution:
  variable = "Solution"
  def isPalin(self, ll):
    stck = []
    slow = ll

    while (slow != None):
      stck.append(slow.val)
      slow = slow.next

    slow = ll

    while (slow != None):
      if (slow.val == stck[len(stck)-1]):
        stck.pop()
        slow = slow.next
      else:
        return False


    return True
  def mergeTwoLists(self, l1, l2):
    if l1 is None:
      return l2
    elif l2 is None:
      return l1
    elif l1.val < l2.val:
      l1.next = self.mergeTwoLists(l1.next, l2)
      return l1
    else:
      l2.next = self.mergeTwoLists(l1, l2.next)
      return l2
  def mergeTwoListsIterative(self, l1, l2):
    acurrent = None
    aroot = None
    while True:
      if l1 is None:
        aanextNode = l2
      elif l2 is None:
        aanextNode = l1
      elif l1.val < l2.val:
        aanextNode = l1
      else:
        aanextNode = l2

      if aanextNode == l1:
        l1 = l1.next if l1 else None
      if aanextNode == l2:
        l2 = l2.next if l2 else None

      if aanextNode is None:
        break
      if not acurrent:
        acurrent = aanextNode
        aroot = acurrent
      else:
        acurrent.next = aanextNode
      acurrent = aanextNode
    return aroot
  def function(self):
        print("This is a message inside the class.")
  def printList(self, dd):
    while dd:
      print(dd.val)
      dd= dd.next
  def print_backward(self,list):
    if list == None: return
    head = list
    tail = list.next
    self.print_backward(tail)
    print(head.val)
    
  def reverse(self,list):
    current = list
    builder = None
    rev = None
    while (current != None):
      builder = ListNode(current.val)
      builder.next = rev
      rev = builder
      current = current.next
    return rev    
        
  def push(self, l ,new_data): 
    newNode = ListNode(l.val) 
    newNode.next =  l.next
    l.val = new_data
    l.next = newNode

  


# llist = LinkedList() 
# llist.push(20) 
# llist.push(4) 
# llist.push(15) 
# llist.push(85) 
  
# print("Given Linked List")
# llist.printList() 
# llist.reverse() 
# print("\nReversed Linked List")
# llist.printList() 
  

# myobjectx = Solution()
# myobjectx.variable

a = ListNode(12)
a.next = ListNode(14)
a.next.next = ListNode(16)
# b = ListNode(2)
# b.next = ListNode(4)
# b.next.next = ListNode(6)
# c = Solution().mergeTwoLists(a,b)
d = ListNode('AA')

d.next = ListNode('BB')
d.next.next = ListNode('CC')
Solution().push(d,'AA0')
Solution().printList(d)
Solution().print_backward(d)
print("---------------------")
e = Solution().reverse(d)
Solution().printList(e)


#
#e = Solution().reverse(d)
#Solution().printList(d)
#Solution().printList(e)
# print(e.next.val)

# print(d.val)
# print(d.next.val)