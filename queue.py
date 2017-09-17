from Stack import Link


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, value):
        add_link = Link(value)
        if self.head is None:
            self.head = add_link

        if self.tail is not None:
            self.tail.next = add_link
        self.tail = add_link

    def dequeue(self):
        dequeue_link = self.head
        if dequeue_link is None:
            return None

        self.head = dequeue_link.next

        if self.head is None:
            self.tail = None

        return dequeue_link.value


def main():
    q = Queue()

    for i in range(5):
        q.enqueue(i)

    print(q.dequeue())

if __name__ == '__main__':
    main()
