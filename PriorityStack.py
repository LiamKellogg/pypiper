class Link:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class PriorityStack:

    def __init__(self):
        self.head = None

    def push(self, key, value):
        link = Link(key, value)

        if self.head is None:
            self.head = link

        elif link.key < self.head.key:
            link.next = self.head
            self.head = link

        else:
            recursive_push(self.head, link)

    def pop(self):
        if self.head is None:
            return None, None

        link_pop = self.head
        self.head = link_pop.next
        return link_pop.key, link_pop.value


def recursive_push(before, link_add):
    next_link = before.next

    if next_link is None:
        before.next = link_add

    elif link_add.key < next_link.key:
        link_add.next = before.next
        before.next = link_add

    else:
        recursive_push(before.next, link_add)


def main():
    pstack = PriorityStack()
    pstack.push(5, 5)
    pstack.push(7, 7)
    pstack.push(6, 6)

    for i in range(3):
        print(pstack.pop())

if __name__ == '__main__':
    main()
