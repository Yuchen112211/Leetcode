'''

138. Copy List with Random Pointer
Medium

A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.

 

Example 1:

Input:
{"$id":"1","next":{"$id":"2","next":null,"random":{"$ref":"2"},"val":2},"random":{"$ref":"2"},"val":1}

Explanation:
Node 1's value is 1, both of its next and random pointer points to Node 2.
Node 2's value is 2, its next pointer points to null and its random pointer points to itself.

Solution:
The idea is clone all nodes first using DFS. Each time add val and new node to a dictionary. Then get random node by head.random.val
Read the code, very simple but brilliant.

'''

def copyRandomList(self, head):  
	return self.helper(head, {})

def helper(self, head, dict):
	"""
	The idea is clone all nodes first using DFS. Each time add val and new node to a dictionary. Then get random node by head.random.val
	"""
	if head:
		# Generate new node and add it to dictionary
		new_head = Node(head.val, None, None)
		dict[head.val] = new_head

		# Process next node
		new_next_node = self.helper(head.next, dict)
		new_head.next = new_next_node

		# Process random node
		random_val = head.random.val if head.random else None
		new_head.random = dict[random_val] if random_val in dict else None

		return new_head

	return None
