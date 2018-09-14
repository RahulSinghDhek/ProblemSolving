def has_loop(head):
    temp=head
    if temp and temp.next==temp:
        return 1
    if temp and not temp.next:
        return 0
    if temp and temp.next:
        node_1 = temp
        node_2 = temp.next
        while node_1 and node_2:
            if node_1 == node_2:
                return 1
            node_1 = node_1.next
            node_2 = node_2.next.next
    return 0                    
