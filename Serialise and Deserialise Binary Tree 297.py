# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
# it's a hard-leveled one, so don't let the fact I might not be able to solve this discourage me
# well let's rather enjoy the process of finding ways to reach the answer

# to begin with, I tried to make the tree an array with queue but it didn't work

""" how my thought process went
Q = deque()
ser = []

1. put root in Q

while queue:

2. popleft()
    node = Q.popleft()

3. if node is None:
	ser.append(node)
	continue

4. else:
	ser.append(node)
	Q.append(node.left)
	Q.append(node.right)
"""

import collections

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        queue = collections.deque()
        queue.append(root)
        ser = []

        while queue:
            node = queue.popleft()

            if node is None:
                ser.append(node)
                continue
            else:
                ser.append(node.val)
                queue.append(node.left)
                queue.append(node.right)

        # above is the one that's been only coded from my thought process
        # Nones within numbers mean they don't have child nodes but still other nodes exist after them
        # ,whereas Nodes after all of the numbers are an indication of no more nodes from the last number
        # so delete them till number pops at the end of the list
        while ser[-1]:
            ser.pop()

        # ser (a short for om serialise) returns [1, 2, 3, None, None, 4, 5] itself, which is the answer I was looking for
        # but it says that rtype is str so, looked up how to turn elements in the list into string
        list_to_str = ' '.join(map(str, ser))

        # returns '1 2 3 None None 4 5' now
        return list_to_str

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        # str -> list
        # how to turn numbers that are str into into properly without any intervention by 'None'
        # I was annoyed at how int(element) was not working despite an exception being set (if element is None, continue)
        # then I realised actually it's not None but 'None'

        # data_list = data.split(" ")
        #
        # for i in range(len(data_list)):
        #     if data_list[i] == 'None':
        #         data_list[i] = None
        #     else:
        #         data_list[i] = int(data_list[i])

        # first try
class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


# get_child_index to turn a data_list to tree
def get_left_child_index(data_list, index):
    if 0 < 2 * index < len(data_list):
        return 2 * index


def get_right_child_index(data_list, index):
    if 0 < 2 * index + 1 < len(data_list):
        return 2 * index + 1


data = [None, 1, 2, 3, None, None, 4, 5, None, None, None, None]


def deserialise(data_list):
    for ind, val in enumerate(data_list):
        data_list[ind] = (ind, val)

    queue = collections.deque()
    queue.append(data_list[1])
    left_index = 0
    right_index = 0

    root = iterate = TreeNode(data_list[1][1])

    while queue:
        index_and_value = queue.popleft()

        left_index = get_left_child_index(data_list, index_and_value[0])
        right_index = get_right_child_index(data_list, index_and_value[0])

# I tried to get indices to move onto the next (left, and right child) and value for tree nodes
# then, realised it is not as simple as a linked_list
# it can't be like node = node.next ... should think about it more how to move next branches in trees

# 5 Sep 2020
# get started again

# tried to put right and left child indices in queue and create nodes with them
def deserialise(data_list):
    start_index = 1

    queue = collections.deque()
    queue.append(start_index)

    root = node = TreeNode(data_list[queue[0]])

    while queue:
        node_index = queue.popleft()

        left_index = get_left_child_index(data_list, node_index)
        right_index = get_right_child_index(data_list, node_index)

        node.left = TreeNode(data_list[left_index])
        node.right = TreeNode(data_list[right_index])

        queue.append(left_index)
        queue.append(right_index)

    return root

# what if nodes themselves are put in the queue instead of indices?
# 1. create root node and put it in queue
# 2. take it out of the queue and add left and right child nodes from index 2
# 2-1. whenever a child node adds to its parent, increase the index by 1
# 2-2. None -> I guess it can be passed on because a node itself already has two Nones for its left and right - cool
# 3. only if a node is not None, run an append operation into a queue
# 4. repeat till the index reach the end of the given list
# 5. return root

# 4. should be till queue comes in empty! because the list will be like [ ~ num, None, None, None, None]
# so those Nones won't be added into a queue

    def deserialise(data):
        data_list = data.split(" ")

        # str to list
        # split turns every element into string in a list
        # so note that None will be 'None'  not(None)
        for i in range(len(data_list)):
            if data_list[i] == 'None':
                data_list[i] = None
            else:
                data_list[i] = int(data_list[i])

        queue = collections.deque()
        root = TreeNode(data_list[1])

        queue.append(root)
        index = 2

        while queue:
            node = queue.popleft()

            if data_list[index] is not None:
                node.left = TreeNode(data_list[index])
                queue.append(node.left)
            index += 1

            if data_list[index] is not None:
                node.right = TreeNode(data_list[index])
                queue.append(node.right)
            index += 1

        return root

# pass the test case but it returned IndexError(list index out of range) when submitted
# I'll have a look later

# deleted this line

#         for i in range(len(data_list)):
#             if data_list[i] == 'None':
#                 data_list[i] = None
#             else:
#                 data_list[i] = int(data_list[i])

# it's not necessary because

# if data_list[index] != 'None':
# node.left / .right = TreeNode(int(data_list[index]))
# will do the job itself
# also added this to the first line of serialise

#         if not root:
#             return ""

# by referring to Leetcode discussions / maybe the error had kept appearing due to the case there's no root for serialise
# that's probably why it solved the problem

def deserialize(self, data):
    """Decodes your encoded data to tree.

    :type data: str
    :rtype: TreeNode
        """
    # str -> list
    # how to turn numbers that are str into into properly without any intervention by 'None'
    if not data:
        return None

    data_list = data.split(" ")

    root = TreeNode(data_list[0])
    queue = collections.deque([root])
    index = 1

    while queue:
        node = queue.popleft()

        if data_list[index] != 'None':
            node.left = TreeNode(int(data_list[index]))
            queue.append(node.left)
        index += 1

        if data_list[index] != 'None':
            node.right = TreeNode(int(data_list[index]))
            queue.append(node.right)
        index += 1

    return root