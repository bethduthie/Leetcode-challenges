# need to find how many levels in tree from beginning to end
# go along each branch until it reaches the end/until all inputs are null
# if left + right values are not null, add 1 to depth
# else return depth
# need to get if statement to end of tree

def maxDepth(node):
    depth = 0
    while node.left.val !=None and node.right.val !=None:
        depth +=1
        node = node.right
    return depth
