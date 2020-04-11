Problem 5: Linked lists union / intersection

union() - Returns union of two LinkedLists. This solution assumes we are not allowed to use any more complex datastructures than Linked lists.
            Assuming n = len(llist_1) + len(llist_2)
            Runtime complexity is O(n^2) as while inserting each value O(n) time is spent in checking if it's present in union and not duplicate.
            Space complexity is O(n)

intersection() - Returns intersection of two LinkedLists. This solution assumes we are not allowed to use any more complex datastructures than Linked lists.
            Assuming n = len(llist_1) + len(llist_2)
            Runtime complexity O(n^2) as while inserting each value time complexity is O(n)
            Space complexity is O(n); alternatively with minor modification of picking smaller llist while comparing it is O(min(len(llist_1), len(llist_2))); in either case it's linear.


union_set() - Returns union of two LinkedLists. This solution assumes we are not allowed to use hashable data structures like sets or dictionaries.
            Assuming n = len(llist_1) + len(llist_2)
            Runtime complexity is O(n) as
                1. Conversion to set is O(n)
                2. Union set operator is O(n)
            Space complexity is O(n)

intersection_set() - Returns union of two LinkedLists. This solution assumes we are not allowed to use hashable data structures like sets or dictionaries.
            Assuming n = len(llist_1) + len(llist_2)
            Runtime complexity is O(n) as
                1. Conversion to set is O(n)
                2. Intersection set operator is O(n)
            Space complexity is O(n); alternatively with minor modification of picking smaller llist while comparing it is O(min(len(llist_1), len(llist_2))); in either case it's linear.

        This is assuming ammortized average case for intersection. Worst case will be O(k*t) where k = len(llist_1) and t = len(llist_2). This is vaild assumption for hash based datastructures like Sets.