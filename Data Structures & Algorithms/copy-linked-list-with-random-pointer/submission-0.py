class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if not head:
            return None

        old_to_copy = {None: None}

        curr = head

        while curr:
            copy = Node(curr.val)
            old_to_copy[curr] = copy
            curr = curr.next

        curr = head

        while curr:

            copy = old_to_copy[curr]

            copy.next = old_to_copy[curr.next]
            copy.random = old_to_copy[curr.random]

            curr = curr.next

        return old_to_copy[head]