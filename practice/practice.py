import matplotlib.pyplot as plt

# plt.plot([1,2,3,4,5])
# 
# # If `plot` is called again, two lines are drawn on the same plot
# plt.plot([5,4,3,2,1])
# 
# plt.show()

# plt.plot([1, 2, 3], [2, 4, 6])
# plt.show()


f1 = plt.figure()
a1 = f1.gca()
a1.plot([1, 2, 3, 4])
f1.savefig('f1.png')


f2 = plt.figure()
a2 = f2.gca()
a2.plot([1, 1, 1, 1])
f2.savefig('f2.png')

f3 = plt.gcf()
a3 = f3.gca()
a3.plot([1, 2, 3], [4, 5, 6])
f3.show()
