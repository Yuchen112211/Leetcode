'''

388. Longest Absolute File Path
Medium

Suppose we abstract our file system by a string in the following manner:

The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:

dir
    subdir1
    subdir2
        file.ext

The directory dir contains an empty sub-directory subdir1 and a sub-directory subdir2 containing a file file.ext.

The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" represents:

dir
    subdir1
        file1.ext
        subsubdir1
    subdir2
        subsubdir2
            file2.ext

The directory dir contains two sub-directories subdir1 and subdir2. subdir1 contains a file file1.ext and an empty second-level sub-directory subsubdir1. subdir2 contains a second-level sub-directory subsubdir2 containing a file file2.ext.

We are interested in finding the longest (number of characters) absolute path to a file within our file system. For example, in the second example above, the longest absolute path is "dir/subdir2/subsubdir2/file2.ext", and its length is 32 (not including the double quotes).

Given a string representing the file system in the above format, return the length of the longest absolute path to file in the abstracted file system. If there is no file in the system, return 0.

Note:

    The name of a file contains at least a . and an extension.
    The name of a directory or sub-directory will not contain a ..

Time complexity required: O(n) where n is the size of the input string.

Notice that a/aa/aaa/file1.txt is not the longest file path, if there is another path aaaaaaaaaaaaaaaaaaaaa/sth.png.

Solution:

We can actually see this as a tree problem.

Since the directory path is strictly specified by the \n and \t, we can split the original path by the \n character,
because each line represents a single file, then we can seperately consider each path.

Then we can see each line of file path contains several \t characters, and this character can actually represents
the level of the file, for example, dir has no \t, so it's the first level, \t\subdir has one \t, which is in the second level.
So then we can split each line of the file path by \t, the length of the corresbonding list is the level the path is in.

We can construct the length of the path and the level into a tuple for future usage, also we need to define if it is a 
file or not, since we only need to compute the path length of a file. So here's an example:

"dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" has list of tuple:
(3, 1, False) #dir
(7, 2, False) #\tsubdir1
(9, 3, True)  #\t\tfile1.ext
(10, 3, False)
(7, 2, False)
(10, 3, False)
(9, 4, True)
The first value is the length of the file path, the second is the level of the file, the third represents whether the
path is a file or not.

Then we can simply consider this to be a pre-order traverse of a n-ary tree. Maintain a dictionary to record all the 
corresbonding degree and value.

Even if the degree is already inside the dictionary, we can simply update the degree's value since this is a preorder
traversal.

If the path is a file, update the max value if necessary.

'''
class Solution(object):
	def lengthLongestPath(self, input):
		"""
		:type input: str
		:rtype: int
		"""
		inputs = input.split('\n')
		for i in range(len(inputs)):
			inputs[i] = inputs[i].split('\t')
		treeDegree = []
		for i in inputs:
			treeDegree.append((len(i[-1]), len(i), '.' in i[-1]))

		nodeValue = {}
		nodeValue[0] = -1
		maxLength = 0
		for value, degree, isFile in treeDegree:
			nodeValue[degree] = nodeValue[degree - 1] + value + 1
			if isFile:
				maxLength = max(nodeValue[degree], maxLength)
		return maxLength

input1 = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"

s = Solution()

print s.lengthLongestPath(input1)