#!/usr/bin/env python3

'''
Given the root to a binary tree, implement serialize(root), which serializes
the tree into a string, and deserialize(s), which deserializes
the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

The following test should pass:

node = Node('root', Node('left', Node('left.left')),
            Node('right', Node('right.left'), Node('right.right')))

assert deserialize(serialize(node)).left.left.val == 'left.left'


The tree looks like
                        
                        [root]
                         /   \
                        /     \
                       /       \
                      /         \
                     /           \
                    /             \
                left              right
                /                /     \
               /                /       \
        left.left       right.left      right.right

'''


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(root):
    container = []

    def encode(node):
        if node is None:                    # condition when parent node has no children
            # use "x" as a flag to show None --> useful when deserealising back to tree
            container.append(Node('x'))
            return None
        container.append(node)
        encode(node.left)
        encode(node.right)

    encode(root)

    return ' '.join(str(node.val) for node in container)


def deserialize(serialised):

    def decode(arr_iterable):
        node_value = next(arr_iterable)     # get the next item from the array
        if node_value == "x":               # reading the None flag
            return None
        node = Node(node_value)
        node.left = decode(arr_iterable)
        node.right = decode(arr_iterable)

        return node

    # creating a generator to get each of the node value
    def node_val_generator(array):
        for node_value in array:
            yield node_value

    arr_iterable = node_val_generator(serialised.split(' '))
    return decode(arr_iterable)


if __name__ == "__main__":
    node = Node('root', Node('left', Node('left.left')),
                Node('right', Node('right.left'), Node('right.right')))
    print(serialize(node))
    print(deserialize(serialize(node)).left.left.val == 'left.left')
