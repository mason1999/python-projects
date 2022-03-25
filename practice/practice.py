import pandas as pd

# can join two series together with pd.concat([series_1, series_2])
x = pd.Series([1, 2])
y = pd.Series([3, 4])

# the indices will be repeated. We show this by printing out the 
# value(s) at index 1. It will yield 2 values. 
z = pd.concat([x, y])
print(z, "\n")
print(z[1])

# using pd.concat([df1, df2]) : joins df2 along rows of df1
df1 = pd.DataFrame({
                       'eating' : [22.200, 44.500, 59.60],
                       'medicine': [3.530, 5.760, 9.71],
                       'study': [0.341, 0.974, 1.80]
                   },
                   index = [1940, 1945, 1950])

print(df1, "\n")


df2 = pd.DataFrame({
                       'eating' : [73.2, 86.80],
                       'medicine': [14.0, 21.10],
                       'study': [2.6, 3.64]                   },
                   index = [1955, 1960])

print(df2, "\n")

df3 = pd.concat([df1, df2])
print(df3, "\n")

# using the axis parameter
df1 = pd.DataFrame({
                       'eating' : [22.200, 44.500, 59.60],
                       'medicine': [3.530, 5.760, 9.71],
                       'study': [0.341, 0.974, 1.80]
                   },
                   index = [1940, 1945, 1950])
df2 = pd.DataFrame({
                       'eating' : [73.2, 86.80],
                       'medicine': [14.0, 21.10],
                       'study': [2.6, 3.64]                   },
                   index = [1955, 1960])
df3 = pd.concat([df1, df2])

print(df3.mean(axis = 0), "\n") # take mean along horizontal axis (--)
print(df3.mean(axis = 1), "\n") # take mean along vertical axis (|)

x = pd.concat([df1, df2], axis = 1) # add along the vertical axis (|)
print(df3, "\n")
print(x, "\n")
