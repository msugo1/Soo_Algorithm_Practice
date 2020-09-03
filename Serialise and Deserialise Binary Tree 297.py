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

        data_list = data.split(" ")

        for i in range(len(data_list)):
            if data_list[i] == 'None':
                data_list[i] = None
            else:
                data_list[i] = int(data_list[i])




