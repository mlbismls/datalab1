import matplotlib.pyplot as plt

def is_in_interval(x, minimum, maximum):
    return minimum <= x <= maximum

x = range(0, 10)
y = [2 * value for value in x]
# plt.plot(x, y)
# plt.show()
#
# plt.scatter(x, y)
# plt.show()
#
# plt.plot(x, y)
# where = [is_in_interval(value, 2, 6) for value in x]
# plt.fill_between(x, y, where=where)
# plt.show()

plt.scatter(x, y)
plt.xlabel('Values between zero and ten')
plt.ylabel('Twice the values of x')
where = [is_in_interval(value, 2, 6) for value in x]
plt.fill_between(x, y, where=where)
plt.show()
