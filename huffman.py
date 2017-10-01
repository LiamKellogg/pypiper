import os
# From the writing and reading of the created binary file
from bitstring import Bits
from bitstring import BitStream

# Import the function from certain classes, making this project inseparable... MWAH HAH HAH HAH HAH... HAHAHAH HAAaa...
from binary_search_tree import Node
from PriorityStack import PriorityStack


# Build the frequency dictionary
def build_freq_table(input_str):
    my_dictionary = {}

    for char in input_str:
        if char not in my_dictionary:
            my_dictionary[char] = 1
        else:
            my_dictionary[char] += 1

    return my_dictionary


# Create the priority queue and the tree
def pQueue(dictionary):

    # Instantiate a PriorityStack object
    pqueue = PriorityStack()

    # Create the nodes for the tree
    for char, freq in dictionary.items():
        node = Node(freq, char, None)   # sorting by keys, so freq is now key
        pqueue.push(node.key, node)

    # Create the tree
    while True:
        # Pop the first two values so that they can become children of a single parent node... or not.
        freq1, value1 = pqueue.pop()
        freq2, value2 = pqueue.pop()

        # Return what tree?
        if value1 is None:
            return None

        # return the whole tree
        elif value2 is None:
            return value1

        else:
            """
            1. create the key of the parent node of the first two values in the priority queue
            2. Create the node, which is empty because it isn't a leaf
            3. Set the left and right children of the parent node
            4. Push value3 to the priority queue because it isn't a root, and needs to attached to another node
                a. Pass the key of the parent node for the sake of the priority stack
                b. Pass the node as the value
            """
            freq3 = freq1 + freq2
            value3 = Node(freq3, None, None)
            value3.left_child = value1
            value3.right_child = value2
            pqueue.push(value3.key, value3)


# Visit all the nodes and create the binary path to each node
def rec_traverse(node, encoding, dict):
    # If node is a leaf
    if node.left_child is None and node.right_child is None:
        dict[node.value] = encoding

    # Visit left_child before right, and add a zero to the binary path
    if node.left_child is not None:
        rec_traverse(node.left_child, encoding + '0', dict)

    if node.right_child is not None:
        rec_traverse(node.right_child, encoding + '1', dict)


# Make the string
def make_string(string, dictionary):
    binary_string = ''
    for i in string:
        binary_string += dictionary[i]
    return binary_string


# Work in progress for decode
def decode_str(string, root, node, counter):
    x = 0;
    decoded_str = None
    while x < len(string):
        c, inc = decodeChar(x, string, root, 0)
        x += inc
        decoded_str += c

# Work in progress for decode
def decodeChar(start, string, node, counter):
    if node.right_child is None and node.left_child is None:
        return node.value, counter

    else:
        if string[start + counter] is 0:
            decodeChar(start, string, node.left_child, counter + 1)
        else:
            decodeChar(start, string, node.right_child, counter + 1)


def main():
    string = input(" > ")
    lookup_table = {} # The dictionary for the values of the string

    """
    1. Build the freq table from the string
    2. Priority queue the returned dictionary
    3. Build the binary string
    """
    root = pQueue(build_freq_table(string))
    rec_traverse(root, '', lookup_table)

    # Write String to binary file
    with open("plznotouchme", 'wb') as file:
        Bits('0b' + make_string(string, lookup_table)).tofile(file)

    # Read data from the created file
    with open("plznotouchme", "rb") as file:
        data = file.read()
        os.remove('plznotouchme')

    decoded_str = BitStream(data).bin
    print(decoded_str)

if __name__ == '__main__':
    main()
