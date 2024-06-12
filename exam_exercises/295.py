import random


class Node:
    def __init__(self,k):
        self.key = k
        self.parent = None
        self.left = None
        self.right = None


def bst_insert(t, k):
    if t == None:
        return Node(k)
    x = t
    while True:
        if k <= x.key:
            if x.left == None:
                x.left = Node(k)
                x.left.parent = x
                return t
            x = x.left
        else:
            if x.right == None:
                x.right = Node(k)
                x.right.parent = x
                return t
            x = x.right


class Canvas:
    def __init__(self,width):
        self.line_width = width
        self.canvas = []

    def put_char(self,x,y,c):
        if x < self.line_width:
            pos = y*self.line_width + x
            l = len(self.canvas)
            if pos < l:
                self.canvas[pos] = c
            else:
                self.canvas[l:] = [' ']*(pos - l)
                self.canvas.append(c)

    def print_out(self):
        i = 0
        sp = 0
        for c in self.canvas:
            if c != ' ':
                print(' '*sp, end='')
                print(c, end='')
                sp = 0
            else:
                sp += 1
            i = i + 1
            if i % self.line_width == 0:
                print('\n', end='')
                sp = 0
        if i % self.line_width != 0:
            print('\n', end='')


def print_binary_tree_r(t,x,y,canvas):
    max_y = y
    if t.left != None:
        x, max_y, lx, rx = print_binary_tree_r(t.left,x,y+2,canvas)
        x = x + 1
        for i in range(rx,x):
            canvas.put_char(i, y+1, '/')

    middle_l = x
    for c in str(t.key):
        canvas.put_char(x, y, c)
        x = x + 1
    middle_r = x

    if t.right != None:
        canvas.put_char(x, y+1, '\\')
        x = x + 1
        x0, max_y2, lx, rx = print_binary_tree_r(t.right,x,y+2,canvas)
        if max_y2 > max_y:
            max_y = max_y2
        for i in range(x,lx):
            canvas.put_char(i, y+1, '\\')
        x = x0

    return (x,max_y,middle_l,middle_r)


def print_tree_w(t,width):
    canvas = Canvas(width)
    print_binary_tree_r(t,0,0,canvas)
    canvas.print_out()


def print_tree(t):
    print_tree_w(t,20000)


# --------- DEBUGGING --------------


def random_bst_n(n):
    """Return a random BST of size n, consisting of values between 1 and 100 inclusive"""
    T = None
    for _ in range(n):
        T = bst_insert(T, random.randint(1,100))
    return T


# --------- 295 ---------------

def bst_root_change(t, x):
    if t.left is None and t.right is None:
        t.key = x
        return t
    elif t.left is None:
        new_root = t.right
        t.right = None
        new_root.parent = None
    elif t.right is None:
        new_root = t.left
        t.left = None
        new_root.parent = None
    else:
        new_root = t
        t = t.right
        while t.left is not None:
            t = t.left
        if t == t.parent.left:
            t.parent.left = t.right
            if t.right is not None:
                t.right.parent = t.parent
        else:
            # KNOW: t == t.parent.right
            t.parent.right = t.right
            if t.right is not None:
                t.right.parent = t.parent
        t.parent = None
        t.right = None
    new_root.key = t.key
    t.key = x
    bst_insert_node(new_root, t)
    return new_root


def bst_insert_node(t,x):
    """Insert the singular node 'x' into binary search tree 't'. Returns nothing."""
    while True:
        if x.key < t.key:
            if t.left is None:
                t.left = x
                x.parent = t
                return
            t = t.left
        else:
            if t.right is None:
                t.right = x
                x.parent = t
                return
            t = t.right

