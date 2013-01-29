# 61A Homework 10
# Name: Krishna Parashar and Andrea Melendez
# Login: cs61a-wh and cs61a-akz
# TA: Julia Oh
# Section: 11

BRACKETS = {('[', ']'): '+',
    ('(', ')'): '-',
    ('<', '>'): '*',
    ('{', '}'): '/'}
LEFT_RIGHT = {left:right for left, right in BRACKETS.keys()}
ALL_BRACKETS = set(b for bs in BRACKETS for b in bs)

# Q1.

def tokenize(line):
    """Convert a string into a list of tokens.
        
        >>> tokenize('<[2{12.5 6.0}](3 -4 5)>')
        ['<', '[', 2, '{', 12.5, 6.0, '}', ']', '(', 3, -4, 5, ')', '>']
        
        >>> tokenize('2.3.4')
        Traceback (most recent call last):
        ...
        ValueError: invalid token 2.3.4
        
        >>> tokenize('?')
        Traceback (most recent call last):
        ...
        ValueError: invalid token ?
        
        >>> tokenize('hello')
        Traceback (most recent call last):
        ...
        ValueError: invalid token hello
        
        >>> tokenize('<(GO BEARS)>')
        Traceback (most recent call last):
        ...
        ValueError: invalid token GO
        """
    for item in ALL_BRACKETS:
        line = line.replace(item, " " + item + " ")
    line = line.split(" ")
    list_line=[]
    for token in line:
        if token in ALL_BRACKETS:
            list_line.append[token]
        else:
            list_line.append[coerce_to_number(token)]
    return list_line


def coerce_to_number(token):
    """Coerce a string to a number or return None.
        
        >>> coerce_to_number('-2.3')
        -2.3
        >>> print(coerce_to_number('('))
        None
        """
    try:
        return int(token)
    except (TypeError, ValueError):
        try:
            return float(token)
        except (TypeError, ValueError):
            return None

# Q2.

def isvalid(tokens):
    """Return whether some prefix of tokens represent a valid Brackulator
        expression. Tokens in that expression are removed from tokens as a side
        effect.
        
        >>> isvalid(tokenize('([])'))
        True
        >>> isvalid(tokenize('([]')) # Missing right bracket
        False
        >>> isvalid(tokenize('[)]')) # Extra right bracket
        False
        >>> isvalid(tokenize('([)]')) # Improper nesting
        False
        >>> isvalid(tokenize('')) # No expression
        False
        >>> isvalid(tokenize('100'))
        True
        >>> isvalid(tokenize('<(( [{}] [{}] ))>'))
        True
        >>> isvalid(tokenize('<[2{12 6}](3 4 5)>'))
        True
        >>> isvalid(tokenize('()()')) # More than one expression is ok
        True
        >>> isvalid(tokenize('[])')) # Junk after a valid expression is ok
        True
        """
    "*** YOUR CODE HERE ***"
    valid_list=[]
    for t in tokens:
        if t in LEFT_RIGHT:
            valid_list.append[t]
        elif t == LEFT_RIGHT[valid_list[(len(valid_list)-1)]]:
            valid_list.pop[(len(valid_list)-1)]
    if len(valid_list)> 0:
        return False
    return True

# Q3.

def brack_read(tokens):
    """Return an expression tree for the first well-formed Brackulator
        expression in tokens. Tokens in that expression are removed from tokens as
        a side effect.
        
        >>> brack_read(tokenize('100'))
        100
        >>> brack_read(tokenize('([])'))
        Pair('-', Pair(Pair('+', nil), nil))
        >>> print(brack_read(tokenize('<[2{12 6}](3 4 5)>')))
        (* (+ 2 (/ 12 6)) (- 3 4 5))
        >>> brack_read(tokenize('(1)(1)')) # More than one expression is ok
        Pair('-', Pair(1, nil))
        >>> brack_read(tokenize('[])')) # Junk after a valid expression is ok
        Pair('+', nil)
        
        >>> brack_read(tokenize('([]')) # Missing right bracket
        Traceback (most recent call last):
        ...
        SyntaxError: unexpected end of line
        
        >>> brack_read(tokenize('[)]')) # Extra right bracket
        Traceback (most recent call last):
        ...
        SyntaxError: unexpected )
        
        >>> brack_read(tokenize('([)]')) # Improper nesting
        Traceback (most recent call last):
        ...
        SyntaxError: unexpected )
        
        >>> brack_read(tokenize('')) # No expression
        Traceback (most recent call last):
        ...
        SyntaxError: unexpected end of line
        """
    if tokens == []:
        raise(SyntaxError('Unexpected End of Line'))

    def is_number(token): #Checks if arg is int or float
        return (type(token) is int or type(token) is float)

    def list_to_pair(list):
        if list == []:
            return nil
        return Pair(l[0], list_to_pair(l[1:]))

    def action(tokens, first = False):
        expressions = []
        buffer = []
        previous = []
        while tokens != []:
            token = tokens.pop(0)
            if is_number(token) and buffer == []:
                #Check is token is valid and nothing is in buffer
                expressions.append([t]) #Append token ot expression
                continue #Does not return yet
            buffer.append(token)
            if token in left_brackets:
                previous.append(token)
            elif token in right_brackets:
                if token != LEFT_RIGHT[previous.pop()]:
                    raise(SyntaxError('unexpected ' + token))
                if previous == []:
                    if first == True:
                        first = tokens[0]
                        if is_number(first):
                            expressions.append(buffer)
                            buffer = []
                            return first
                        else: # It's a bracket!
                            expression = left_to_symbol[first]
                            expressions.append(buffer)
                            buffer = []
                            return Pair(exp, read(tokens[1:-1]))
        if (previous != []):
            raise(SyntaxError('Unexpected End of Line'))
        if first:
            first = tokens[0]
                if is_number(first):
                    return first
                else: # It's a bracket!
                    expression = left_to_symbol[first]
                    return Pair(exp, read(tokens[1:-1]))
        return list_to_pair(expressions)

    left_brackets = LEFT_RIGHT.keys()
    right_brackets = LEFT_RIGHT.values()
    left_to_symbol = {key[0]:BRACKETS[key] for key in BRACKETS.keys()}
    return read(tokens, True)

# Q4.

from urllib.request import urlopen

def puzzle_4():
    """Return the soluton to puzzle 4."""
    "*** YOUR CODE HERE ***"


class Pair(object):
    """A pair has two instance attributes: first and second.  For a Pair to be
        a well-formed list, second is either a well-formed list or nil.  Some
        methods only apply to well-formed lists.
        
        >>> s = Pair(1, Pair(2, nil))
        >>> s
        Pair(1, Pair(2, nil))
        >>> print(s)
        (1 2)
        >>> len(s)
        2
        >>> s[1]
        2
        >>> print(s.map(lambda x: x+4))
        (5 6)
        """
    def __init__(self, first, second):
        self.first = first
        self.second = second
    
    def __repr__(self):
        return "Pair({0}, {1})".format(repr(self.first), repr(self.second))
    
    def __str__(self):
        s = "(" + str(self.first)
        second = self.second
        while isinstance(second, Pair):
            s += " " + str(second.first)
            second = second.second
        if second is not nil:
            s += " . " + str(second)
        return s + ")"
    
    def __len__(self):
        n, second = 1, self.second
        while isinstance(second, Pair):
            n += 1
            second = second.second
        if second is not nil:
            raise TypeError("length attempted on improper list")
        return n
    
    def __getitem__(self, k):
        if k < 0:
            raise IndexError("negative index into list")
        y = self
        for _ in range(k):
            if y.second is nil:
                raise IndexError("list index out of bounds")
            elif not isinstance(y.second, Pair):
                raise TypeError("ill-formed list")
            y = y.second
        return y.first
    
    def map(self, fn):
        """Return a Scheme list after mapping Python function FN to SELF."""
        mapped = fn(self.first)
        if self.second is nil or isinstance(self.second, Pair):
            return Pair(mapped, self.second.map(fn))
        else:
            raise TypeError("ill-formed list")

class nil(object):
    """The empty list"""
    
    def __repr__(self):
        return "nil"
    
    def __str__(self):
        return "()"
    
    def __len__(self):
        return 0
    
    def __getitem__(self, k):
        if k < 0:
            raise IndexError("negative index into list")
        raise IndexError("list index out of bounds")
    
    def map(self, fn):
        return self

nil = nil() # Assignment hides the nil class; there is only one instance


def read_eval_print_loop():
    """Run a read-eval-print loop for the Brackulator language."""
    global Pair, nil
    from scheme_reader import Pair, nil
    from scalc import calc_eval
    
    while True:
        try:
            src = tokenize(input('> '))
            while len(src) > 0:
                expression = brack_read(src)
                print(calc_eval(expression))
        except (SyntaxError, ValueError, TypeError, ZeroDivisionError) as err:
            print(type(err).__name__ + ':', err)
        except (KeyboardInterrupt, EOFError):  # <Control>-D, etc.
            return

if __name__ == "__main__":
    import doctest
    doctest.testmod()

