from binary_search_tree import Node
from PriorityStack import PriorityStack


def build_freq_table(input_str):
    my_dictionary = {}

    for char in input_str:
        if char not in my_dictionary:
            my_dictionary[char] = 1
        else:
            my_dictionary[char] += 1

    return my_dictionary


def pQueue(dictionary):

    pqueue = PriorityStack()

    for char, freq in dictionary.items():
        node = Node(freq, char, None)   # sorting by keys, so freq is now key
        pqueue.push(node.key, node)

    while True:
        freq1, value1 = pqueue.pop()
        freq2, value2 = pqueue.pop()

        if value1 is None:
            return None

        elif value2 is None:
            return value1

        else:
            freq3 = freq1 + freq2
            value3 = Node()
            value3.left_child = freq1
            value3.right_child = freq2
            pqueue.push(value3)


def main():
    string = input(" > ")

    build_freq_table(string)

if __name__ == '__main__':
    main()
