import turtle

def build_tree(t, branch_length, shorten_by, angle, minimum_branch_length):
    if branch_length  > minimum_branch_length:
        t.forward(branch_length)
        new_length = branch_length - shorten_by
        
        t.left(angle)
        build_tree(t, new_length, shorten_by, angle)
        
        t.right(angle *2)
        build_tree(t, new_length, shorten_by, angle)
        
        t.left(angle)
        t.backward(branch_length)
        