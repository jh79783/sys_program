import numpy as np

foo = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
bar = np.array([[3, 4, 5], [6, 7, 8], [9, 10, 11]])

# print(foo)
print("sum", np.concatenate((foo, bar), axis=None))
# print( np.concatenate((foo, bar), axis=0))
# print("sum", np.concatenate((foo, bar), axis=1))
