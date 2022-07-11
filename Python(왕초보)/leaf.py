leaf_1 = [0, 0, 2, 4, 7, 7, 9]
leaf_2 = [1, 1, 3, 8]
leaf_3 = [0]

stem_leaf = [leaf_1, leaf_2, leaf_3]

i = 1
for stem in stem_leaf:
    print('{}:'.format(i), stem)
    i += 1