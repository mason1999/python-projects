import matplotlib.pyplot as plt

data = {
    'China': 1402625480,
    'India': 1362187627,
    'US': 329680233,
    'Indonesia': 268074600,
    'Pakistan': 220312891,
}
# data.items() : returns a list of tuples [(key1, val1), (key2, val2), ...]
# *data.items(): returns a vararg structure: (k1, v1), (k2, v2), ...
# zip(*data.items()): returns (k1, k2, k3, ...), (v1, v2, v3,...)
labels, values = zip(*data.items())
plt.bar(labels, values)
plt.savefig('out.png')
