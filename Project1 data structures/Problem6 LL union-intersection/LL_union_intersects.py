'''
Union and Intersection of Two Linked Lists

Your task for this problem is to fill out the union and intersection functions. The union of two sets A and B is the set of elements which are in A, in B, or in both A and B. The intersection of two sets A and B, denoted by A ∩ B, is the set of all objects that are members of both the sets A and B.

You will take in two linked lists and return a linked list that is composed of either the union or intersection, respectively. Once you have completed the problem you will create your own test cases and perform your own run time analysis on the code.

We have provided a code template below, you are not required to use it:
'''

from typing import Any, Set


class Node:
    def __init__(self, value: Any) -> None:
        self.value = value
        self.next = None

    def __repr__(self) -> str:
        return str(self.value)


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def __str__(self) -> str:
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value: Any) -> None:

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size


def is_present(llist: LinkedList, val: Any) -> bool:
    ''' Checks if `val` is present in `llist`

        Worst Case runtime: O(n) where n is length of `llist`
    '''
    assert val is not None, 'Presence of None should not be checked'

    head = llist.head
    while head:
        if head.value == val:
            return True
        head = head.next
    return False


def union(llist_1: LinkedList, llist_2: LinkedList) -> LinkedList:
    ''' Returns union of two LinkedLists. This solution assumes we are not allowed
        to use any more complex datastructures than Linked lists.

        Assuming n = len(llist_1) + len(llist_2)
        Runtime complexity is O(n^2) as while inserting each value O(n) time is spent in checking if it's present in union and not duplicate.
    '''
    union_ll = LinkedList()

    head = llist_1.head
    while head:
        # if present in list 2 and not duplicate -> append it to intersection
        val = head.value
        if not is_present(union_ll, val):
            union_ll.append(val)
        head = head.next

    head = llist_2.head
    while head:
        # if present in list 2 and not duplicate -> append it to intersection
        val = head.value
        if not is_present(union_ll, val):
            union_ll.append(val)
        head = head.next

    return union_ll


def intersection(llist_1: LinkedList, llist_2: LinkedList) -> LinkedList:
    ''' Returns intersection of two LinkedLists. This solution assumes we are not allowed
        to use any more complex datastructures than Linked lists.

        Assuming n = len(llist_1) + len(llist_2)
        Runtime complexity O(n^2) as while inserting each value O(n) time is spent in checking if it's present in intersection and not duplicate.
    '''
    intersect_ll = LinkedList()

    # since overall program runs in more than O(n) time, picking small linkedlist will provide a small optimization.
    if llist_1.size() > llist_2.size():
        head = llist_2.head
        bigger_llist = llist_1
    else:
        head = llist_1.head
        bigger_llist = llist_2

    while head:
        # if present in list 2 and not duplicate -> append it to intersection
        val = head.value
        if is_present(bigger_llist, val) and not is_present(intersect_ll, val):
            intersect_ll.append(val)
        head = head.next
    return intersect_ll



# Convert linked list to set.
def LL_to_set(LList: LinkedList) -> Set:
    ''' Returns set of all values in linkedlist'''

    lset = set()
    head = LList.head
    while head:
        lset.add(head.value)
        head = head.next
    return lset


def set_to_LL(list_set: set) -> LinkedList:
    ''' Returns linkedlist of all items in set'''
    ll = LinkedList()
    for value in list_set:
        ll.append(value)
    return ll



def union_set(llist_1: LinkedList, llist_2: LinkedList) -> LinkedList:
    ''' Returns union of two LinkedLists. This solution assumes we are not allowed
        to use hashable data structures like sets or dictionaries.

        Assuming n = len(llist_1) + len(llist_2)
        Runtime complexity is O(n) as
            1. Conversion to set is O(n)
            2. Union set operator is O(n)
    '''

    result_set = LL_to_set(llist_1).union(LL_to_set(llist_2))
    return set_to_LL(result_set)

def intersection_set(llist_1: LinkedList, llist_2: LinkedList) -> LinkedList:
    ''' Returns union of two LinkedLists. This solution assumes we are not allowed
        to use hashable data structures like sets or dictionaries.

        Assuming n = len(llist_1) + len(llist_2)
        Runtime complexity is O(n) as
            1. Conversion to set is O(n)
            2. Intersection set operator is O(n)

            This is assuming ammortized average case for intersection. Worst case will be O(k*t) where k = len(llist_1) and t = len(llist_2).
    '''

    result_set = LL_to_set(llist_1).intersection(LL_to_set(llist_2))
    return set_to_LL(result_set)




print(' -- Test case 1 - Using slower pure linkedlist implementation --')

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

# better way to test is to use inbuilt set operations instead of visually comparing if output is correct
print('Union:', 'passed' if LL_to_set(union(linked_list_1,linked_list_2)) == set(element_1).union(set(element_2)) else 'failed')
print('Intersection:', 'passed' if LL_to_set(intersection(linked_list_1,linked_list_2)) == set(element_1).intersection(set(element_2)) else 'failed')


print(' -- Test case 2 - using faster function utilizing set functions --')


linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)


print('Union using sets:', 'passed' if LL_to_set(union_set(linked_list_1,linked_list_2)) == set(element_1).union(set(element_2)) else 'failed')
print('Intersection using sets:', 'passed' if LL_to_set(intersection(linked_list_1,linked_list_2)) == set(element_1).intersection(set(element_2)) else 'failed')



print(' -- Test case 3 - One linked list empty --')

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = []

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)


print('Union:', 'passed' if LL_to_set(union_set(linked_list_1,linked_list_2)) == set(element_1).union(set(element_2)) else 'failed')
print('Intersection:', 'passed' if LL_to_set(intersection(linked_list_1,linked_list_2)) == set(element_1).intersection(set(element_2)) else 'failed')
print('Union using sets:', 'passed' if LL_to_set(union_set(linked_list_1,linked_list_2)) == set(element_1).union(set(element_2)) else 'failed')
print('Intersection using sets:', 'passed' if LL_to_set(intersection(linked_list_1,linked_list_2)) == set(element_1).intersection(set(element_2)) else 'failed')

print(' -- Test case 4 - mixed types --')

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,'aa',65,'b',4,3,23]
element_2 = [5, 6, 'aa']

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)


print('Union:', 'passed' if LL_to_set(union_set(linked_list_1,linked_list_2)) == set(element_1).union(set(element_2)) else 'failed')
print('Intersection:', 'passed' if LL_to_set(intersection(linked_list_1,linked_list_2)) == set(element_1).intersection(set(element_2)) else 'failed')
print('Union using sets:', 'passed' if LL_to_set(union_set(linked_list_1,linked_list_2)) == set(element_1).union(set(element_2)) else 'failed')
print('Intersection using sets:', 'passed' if LL_to_set(intersection(linked_list_1,linked_list_2)) == set(element_1).intersection(set(element_2)) else 'failed')