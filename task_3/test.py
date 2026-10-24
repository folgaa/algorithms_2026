from rb_tree import RB_Tree


tree = RB_Tree()
test_values = [20, 15, 25, 10, 5, 30, 35, 18, 22]
for value in test_values:
    tree.insert(value)
    tree.print_tree_rec_wide()
