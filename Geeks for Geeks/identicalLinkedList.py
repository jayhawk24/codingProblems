def areIdentical(head1, head2):
    while head1 and head2:
        if head1.data == head2.data:
            head1 = head1.next
            head2 = head2.next
        else:
            return 0
    if head1 and not head2:
        return 0
    if not head1 and head2:
        return 0
    return 1


# {
#  Driver Code Starts
# Node Class
class node:
    def __init__(self, val):
        self.data = val
        self.next = None


# Linked List Class
class Linked_List:
    def __init__(self):
        self.head = None

    def insert(self, val):
        new_node = node(val)
        new_node.data = val
        new_node.next = self.head
        self.head = new_node


def printList(head):
    while head:
        print(head.data, end=" ")
        head = head.next
    print()


def createList(arr, n):
    lis = Linked_List()
    for i in range(n):
        lis.insert(arr[i])
    return lis.head


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        head1 = createList(arr, n)
        n = int(input())
        arr = list(map(int, input().strip().split()))
        head2 = createList(arr, n)
        if areIdentical(head1, head2):
            print("Identical")
        else:
            print("Not identical")
# Contributed by: Harshit Sidhwa
# } Driver Code Ends