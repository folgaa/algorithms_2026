from linked_list import LinkedList


def reverse_linked_list(ll : LinkedList):
    prev_node = None
    curnode = ll.head
    while curnode:
        next_cur = curnode.next
        curnode.next = prev_node
        prev_node = curnode
        curnode = next_cur
    ll.head = prev_node
    return ll


ll_test = LinkedList()
ll_test.append_list([1, 2, 3, 4, 5])

print("Original: ")
ll_test.print_list_in_line()

ll_test = reverse_linked_list(ll_test)

print("Final: ")
ll_test.print_list_in_line()
