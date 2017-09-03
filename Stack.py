class Stack:
    def __init__(self) -> None:
        self.head = None

    def push(self, value):
        # Do something
        link_to_add = Link(value)           # add link
        link_to_add.next = self.head        # Add link to the next head
        self.head = link_to_add             # Change the head point

    def pop(self):
        # Return something
        link_to_pass = self.head            # ???
        if link_to_pass is None:            # Check if the head is none, return nothing
            return None
        self.head = link_to_pass.next       # Change the head point

        return link_to_pass.value           # Return the value of the popped value


class Link:
    def __init__(self, value):
        self.next = None
        self.value = value


def main():
    stack = Stack()

    for i in range(5):
        stack.push(abs(i - 5))
        print(stack.pop())
    print(stack.pop())

if __name__ == '__main__':
    main()