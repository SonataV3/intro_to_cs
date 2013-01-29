 # 61A Homework 7
# Name: Krishna Parashar and Andrea Melendez
# Login: cs61a-wh and cs61a-akz
# TA: Julia Oh
# Section: 11

def num_splits(s, d):
    """Return the number of ways in which s can be partitioned into two
        sublists that have sums within d of each other.
        
        >>> num_splits({1, 5, 4}, 0)  # splits to {1, 4} and {5}
        1
        >>> num_splits({6, 1, 3}, 1)  # no split possible
        0
        >>> num_splits({-2, 1, 3}, 2) # {-2, 3} {1} and {-2, 1, 3} {}
        2
        >>> num_splits({1, 4, 6, 8, 2, 9, 5}, 3)
        12
        
        Hint: You can split a set s into one arbitrary element and the rest with:
        
        k = s.pop()
        rest = set(s)
        s.add(k)
        
        After which s is unchanged, and {k}.union(rest) == s
        
    my_list = []
    list_of_sets = [[]]
    number_of_sums = []
    counter, i, j = 0, 0, 0
    while len(s) > 0:
        counter = 0
        k = s.pop()
        my_list.append(k)
    for element in my_list:
        list_of_sets.extend([subset + [element] for subset in list_of_sets])
    while i <= (len(list_of_sets) + 1):
        number_of_sums.append(abs(sum(list_of_sets[i]), list_of_sets[(len(list_of_sets + 1) - i]))
        i += 1
    while j <= (number_of_sums + 1):
        if number_of_sums[i] <= d:
            counter += 1
        j += 1
    print(list_of_sets)
    print(len(list_of_sets))
""" 
# Q2.

def num_trees(n):
    """How many full binary trees have exactly n leaves? E.g.,
        
        1   2        3       3    ...
        *   *        *       *
        / \      / \     / \
        *   *    *   *   *   *
        / \         / \
        *   *       *   *
        
        >>> num_trees(1)
        1
        >>> num_trees(2)
        1
        >>> num_trees(3)
        2
        >>> num_trees(8)
        429
        
        """
    # Base Case
    if n == 1:
        return 1
    total_trees = 0
    for i in range(1, n):
        # Factorial Recursion
        total_trees += num_trees(i) * num_trees(n-i)
    return total_trees


# Q3.

def mario_number(level):
    """Return the number of ways that Mario can perform a sequence of steps
        or jumps to reach the end of the level without ever landing in a Piranha
        plant. Assume that every level begins and ends with a space.
        
        >>> mario_number(' P P ')   # jump, jump
        1
        >>> mario_number(' P P  ')   # jump, jump, step
        1
        >>> mario_number('  P P ')  # step, jump, jump
        1
        >>> mario_number('   P P ') # step, step, jump, jump or jump, jump, jump
        2
        >>> mario_number(' P PP ')  # Mario cannot jump two plants
        0
        >>> mario_number('    ')    # step, jump ; jump, step ; step, step, step
        3
        >>> mario_number('    P    ')
        9
        >>> mario_number('   P    P P   P  P P    P     P ')
        180
        """
    """Base Cases"""
    if level == '': #if beginning or end
        return 0
    if level == ' ': #if space or step
        return 1
    if level[0] == 'P': #if plant
        return 0
    return mario_number(level[1:]) + mario_number(level[2:])

# Q4.

maze1 = """
    ******** *
    * *      *
    * * ******
    * *   *  *
    * *** *  *
    *   * *  *
    *** * *  *
    *        *
    * ********
    """

maze2 = """
    ********** *
    *      *   *
    *** **** * *
    *      * * *
    * **** * * *
    *      *** *
    ****** *   *
    *        * *
    * **********
    """

def print_path(maze):
    """Print a path through a maze.
        
        >>> print_path(maze1)
        ********.*
        * *......*
        * *.******
        * *...*  *
        * ***.*  *
        *   *.*  *
        *** *.*  *
        *.....   *
        *.********
        
        >>> print_path(maze2)
        **********.*
        *      *  .*
        *** **** *.*
        *      * *.*
        * **** * *.*
        *      ***.*
        ****** *...*
        *........* *
        *.**********
        """
    "*** YOUR CODE HERE ***"


class Leaf(object):
    def __init__(self, letter, weight):
        self.letter = letter
        self.weight = weight

class Tree(object):
    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.weight = left.weight + right.weight

A = Leaf('a', 8)
BCD = Tree(Leaf('b', 3), Tree(Leaf('c', 1), Leaf('d', 1)))
EFGH = Tree(Tree(Leaf('e', 1), Leaf('f', 1)),
            Tree(Leaf('g', 1), Leaf('h', 1)))
AH = Tree(A, Tree(BCD, EFGH))

# Q5.

def decode(tree, code):
    """Decode a list of 0's and 1's using the Huffman encoding tree.
        
        >>> decode(AH, [1, 0, 0, 0, 1, 0, 1, 0])
        'bac'
        """
    word = ''
    while code != []:
        word += decode_one(tree, code)
    return word

def decode_one(tree, code):
    """Decode and remove the first letter in code, using tree.
        
        >>> code = [1, 0, 0, 0, 1, 0, 1, 0]
        >>> decode_one(AH, code)
        'b'
        >>> code
        [0, 1, 0, 1, 0]
        """
    "*** YOUR CODE HERE ***"

# Q6.

def encodings(tree):
    """Return all encodings in a tree as a dict from letters to bit lists.
        
        >>> e = encodings(AH)
        >>> e['a']
        [0]
        >>> e['c']
        [1, 0, 1, 0]
        >>> e['h']
        [1, 1, 1, 1]
        """
    "*** YOUR CODE HERE ***"

# Q7.

def huffman(elements):
    """Return an optimal Huffman encoding tree of elements, a sorted lists.
        
        >>> h = huffman([Leaf('c', 1), Leaf('d', 1), Leaf('b', 3), Leaf('a', 8)])
        >>> for letter, code in sorted(encodings(h).items()): print(letter + ':', code)
        a: [1]
        b: [0, 1]
        c: [0, 0, 0]
        d: [0, 0, 1]
        """
    "*** YOUR CODE HERE ***"
'''
if __name__ == "__main__":
    import doctest
    doctest.testmod()
'''
