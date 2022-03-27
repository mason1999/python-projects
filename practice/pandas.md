1. [introduction](#1)
2. [series index](#2)
3. [series dtype](#3)
4. [series functions](#4)
5. [broadcasting](#5)
6. [data frames](#6)
7. [columns and indices](#7)
8. [dataframe construction](#8)
9. [dataframe functions](#9)
10. [csv and excel](#10)
11. [.iloc](#11)
12. [.iloc II](#12)
13. [index selections](#13)
14. [selections, filters and assignments](#14)
15. [missing data](#15)
16. [iterating](#16)
17. [.at and .iat](#17)
18. [group by](#18)
19. [combining and axis](#19)
20. [joining with merge()](#20)
21. [inner join](#21)
22. [outer join](#22)
23. [joining on multiple columns](#23)
24. [category type](#24)
25. [timeseries and resampling](#25)
26. [timeseries indexing](#26)


# introduction

Begin by installing the pandas module

    pip3 install pandas

Series are labelled one-dimensional arrays of data. 

Let's start with a simple `Series` created from a Python list. To create a `Series` we use `pd.Series()`

    import pandas as pd

    data = pd.Series([1,2,3])
    print(data)

This outputs:

    0    1
    1    2
    2    3
    dtype: int64

You'll notice that unlike Numpy arrays, each value (second column) in the `Series` has an associated label (first column). These labels are called the index of the `Series`.

You can think of the index as a name of each row. Since we did not specify an index when we called `pd.Series`, an automatically assigned numerical index was created.

The index allows us to read and write values in the `Series` with the `[]` operator.


    data = pd.Series([7, 8, 9])
    data[1] = 100
    print(data)

    # prints: 
    # 0      1
    # 1    100
    # 2      3
    # dtype: int64

Let's create a Series from a dictionary. The dictionary contains the populations of each of the Australian States/Territories. 

    import pandas as pd

    data = {
        'NSW': 8089526,
        'VIC': 6594804,
        'QLD': 5095100, 
        'WA': 2621680, 
        'SA': 1751693, 
        'ACT': 426709,
        'NT': 245869
    }

    # Create a series from a dictionary,
    # with the keys being the index to each value
    population = pd.Series(data)

    print(population)

    # NSW    8089526
    # VIC    6594804
    # QLD    5095100
    # WA     2621680
    # SA     1751693
    # ACT     426709
    # NT      245869
    # dtype: int64

    print(population["NSW"]) # prints 8089526

# series index

Understanding that each value has an associated label in the form of an index is critical. This is the main difference between Python lists and the Pandas `Series`.

Going back to the first example we've seen, we can explicitly set an index on the values of the `Series` by specifying the `index` keyword argument. 


    import pandas as pd

    data = pd.Series([1,2,3], index=['a', 'b', 'c'])
    print(data)
Here, each of the values `1`, `2`, and `3` has been associated with the index `'a'` , `'b'`, and `'c'`.

We can use the `.index` attribute to get the indices and set them

    import pandas as pd

    data = pd.Series([1,2,3], index=['a', 'b', 'c'])
    print(data.index)

    # Replace the index with a new one.
    data.index = ['x', 'y', 'z']
    print(data)

# series dtype

Every Series also has an associated `dtype`. The `dtype` is the same as in Numpy, and represents the type of data stored in the `Series`.

Pandas will try to automatically detect the `dtype` of the Series based on the input passed into `pd.Series`. If we don't specify an index, an index from `0` to `n-1` will be created for us.


    import pandas as pd
    import numpy as np

    population = pd.Series(np.array([8089526, 6594804, 5095100, 2621680, 1751693, 426709, 245869]))
    print(population)

    # Show this series' dtype
    print(population.dtype)

    # Show this series' index
    print(population.index)
    
    # Fetch the element with index 1
    print(population[1])

`ndarrays` can only hold one kind of data each but not all `Series` need to hold the same kind of data. If there are different kinds of data, Pandas defaults to a catch-all data type called `object`.


    import pandas as pd

    s = pd.Series([1439000000, 331000000.123, 'word'])
    print(s) # dtype is 'object'

Some other commonly seen `dtypes` include `int64`, `float64`, `bool`, `datetime64` and `category`.
# series functions

use `[] operator` to read/write values at specified index

    import pandas as pd

    data = pd.Series([ i**2 for i in range(100) ])
    print(data[10])
    data[2] = 1234
    print(data)

If we pass in a list of booleans, we can use this to choose what rows to return.

    import pandas as pd

    data = pd.Series([1,2,3])
    print(data[[True, False, True]]) # get indices at 0 and 2

If we pass in a list of indices, we can select those specific indices.

    import pandas as pd

    data = pd.Series([1,2,3])
    print(data[[0,2]])

- `.head(n)` returns the first `n` values of the `Series`. If we leave `n` unspecified, then the first `5` rows are returned.
- `.tail(n)` returns the last `n` values of the `Series`. If we leave `n` unspecified, then the last `5` rows are returned.
- `.unique()` returns a list of all the unique values in a series. 

      import pandas as pd

      data = pd.Series([ i**2 for i in range(100) ])
      print(data.head()) # prints first 5 values. 
      print(data.tail()) # prints last 5 values. 

We can iterate through each value of the `Series` using a for loop.


    import pandas as pd

    data = pd.Series([ i**2 for i in range(100) ])
    for x in data:
        print(x)

We can sort using: 

- `.sort_index()` : sort based on indices
- `.sort_values()` : sort based on values

      import pandas as pd

      data = pd.Series(['3', '4', '1', '2'], index=[2,1,4,3])

      # Print the result of the series sorted by the index
      print(data.sort_index())

      # Print the result of the series sorted by the values.
      print(data.sort_values())


# broadcasting
Pandas provide an easy way to apply operations to all values of a `Series`. Like in Numpy, any operations applied to the `Series` itself is "broadcasted" elementwise to all elements.

Example: 

    import pandas as pd

    data = pd.Series([1,2,3])
    data += 2
    print(data)

Comparsion operators are also broadcasted, this is important since we can use a list of boolean values to filter a `Series`.

    import pandas as pd

    data = pd.Series([1,2,3,4,5,6])

    # This returns a Series of Booleans
    print(data > 4)

    # Comparsion operator can also be chained, use & for logical AND and | or logical OR
    print((data < 3) & (data > 5))
    print((data < 3) | (data > 5))

    # Print only the values thare are < 3
    print(data[data < 3])

Sometimes, you may receive the following error with broadcasting comparison operators:

    import pandas as pd

    data = pd.Series([1,2,3,4,5,6])

    print(data < 3 | data > 5) # errors!
    print(data < 3 or data > 5) # errors!
    print((data < 3) | (data > 5)) # works!

If this happens, make sure you are using the `&` and `|` bitwise operators instead of `and` or `or`. Also due to operator precedence, the fix can be simply adding brackets.
# data frames

DataFrames are labelled two-dimensional data. They can be thought of as a list of `Series` with a shared index, they allow us to represent tabular data.

- Note that while `DataFrame` can be created by a list of dictionaries, the  `keys` become the COLUMNS. Previously, the `keys` became the ROWS (indices) for a series. 

Let's create a `DataFrame` from a list of dictionaries:

    import pandas as pd

    df = pd.DataFrame([
        { 'Name': 'Ferrari Dino', 'MPG': 19.7, 'Weight': 2.770 },
        { 'Name': 'Maserati Bora', 'MPG': 15.0, 'Weight': 3.570 },
        { 'Name': 'Volvo 142E', 'MPG': 21.4, 'Weight': 2.580 }
    ])

    print(df)

This outputs:

                Name   MPG  Weight
    0   Ferrari Dino  19.7    2.77
    1  Maserati Bora  15.0    3.57
    2     Volvo 142E  21.4    2.58

Notice again the first column. This is the index of the `DataFrame`. Since we did not specify an index, an automatically generated numerical index has been created for us. Just like in the `Series`, the `DataFrame` index is a label for each row.

# columns and indices

All operations covered here are all commonly used, make sure you know these!


    import pandas as pd

    df = pd.DataFrame([
        { 'Name': 'Ferrari Dino', 'MPG': 19.7, 'Weight': 2.770 },
        { 'Name': 'Maserati Bora', 'MPG': 15.0, 'Weight': 3.570 },
        { 'Name': 'Volvo 142E', 'MPG': 21.4, 'Weight': 2.580 }
    ])

    # Try the functions by uncommenting here

    #df.columns = ['X', 'Y', 'Z']
    #df['Coolness'] = [1,2,3]
    #del df['Coolness']
    #df[['Name', 'Weight']]
    #df.index = df['Name']
    #del df['Name']
    #print(df.loc['Volvo 142E'])
    #df.loc['XYZ'] = [1,2]
    #print(df)
    #df.drop('XYZ', inplace=True)
    #print(df.T)
    print(df)

We can access and update the list of column names of the `DataFrame` by using `.columns`.

    import pandas as pd

    df = pd.DataFrame([
        { 'Name': 'Ferrari Dino', 'MPG': 19.7, 'Weight': 2.770 },
        { 'Name': 'Maserati Bora', 'MPG': 15.0, 'Weight': 3.570 },
        { 'Name': 'Volvo 142E', 'MPG': 21.4, 'Weight': 2.580 }
    ])

    df.columns = ['X', 'Y', 'Z']
    print(df)


In the `DataFrame`, the `[]` operator is used to access and update a particular column.

    import pandas as pd

    df = pd.DataFrame([
        { 'Name': 'Ferrari Dino', 'MPG': 19.7, 'Weight': 2.770 },
        { 'Name': 'Maserati Bora', 'MPG': 15.0, 'Weight': 3.570 },
        { 'Name': 'Volvo 142E', 'MPG': 21.4, 'Weight': 2.580 }
    ])
    print(df['MPG'])

Each column is extracted as a `Series`.

We can also `add` columns with the following operation:


    import pandas as pd

    df = pd.DataFrame([
        { 'Name': 'Ferrari Dino', 'MPG': 19.7, 'Weight': 2.770 },
        { 'Name': 'Maserati Bora', 'MPG': 15.0, 'Weight': 3.570 },
        { 'Name': 'Volvo 142E', 'MPG': 21.4, 'Weight': 2.580 }
    ])
    df['Coolness'] = [2, 5, 6]
    print(df)

To `remove` a column, we can use:

    import pandas as pd

    df = pd.DataFrame([
        { 'Name': 'Ferrari Dino', 'MPG': 19.7, 'Weight': 2.770 },
        { 'Name': 'Maserati Bora', 'MPG': 15.0, 'Weight': 3.570 },
        { 'Name': 'Volvo 142E', 'MPG': 21.4, 'Weight': 2.580 }
    ])

    del df['MPG']
    print(df)

We can select more than one column by passing in an array to the `[]` operator.


    import pandas as pd

    df = pd.DataFrame([
        { 'Name': 'Ferrari Dino', 'MPG': 19.7, 'Weight': 2.770 },
        { 'Name': 'Maserati Bora', 'MPG': 15.0, 'Weight': 3.570 },
        { 'Name': 'Volvo 142E', 'MPG': 21.4, 'Weight': 2.580 }
    ])

    print(df[['Name', 'Weight']])

We can access and update the index of a data frame with the `.index` attribute


    import pandas as pd

    df = pd.DataFrame([
        { 'Name': 'Ferrari Dino', 'MPG': 19.7, 'Weight': 2.770 },
        { 'Name': 'Maserati Bora', 'MPG': 15.0, 'Weight': 3.570 },
        { 'Name': 'Volvo 142E', 'MPG': 21.4, 'Weight': 2.580 }
    ])

    df.index = df['Name'] # set index to name of cars. 
    del df['Name'] # Name is now redundant

We can access a row using the `index`/`row name`

    import pandas as pd

    df = pd.DataFrame([
        { 'Name': 'Ferrari Dino', 'MPG': 19.7, 'Weight': 2.770 },
        { 'Name': 'Maserati Bora', 'MPG': 15.0, 'Weight': 3.570 },
        { 'Name': 'Volvo 142E', 'MPG': 21.4, 'Weight': 2.580 }
    ])

    df.index = df['Name']
    del df['Name'] 

    print(df.loc['Ferrari Dino'])

We can insert rows with the `.loc["name"] = [a, b]`


    import pandas as pd

    df = pd.DataFrame([
        { 'Name': 'Ferrari Dino', 'MPG': 19.7, 'Weight': 2.770 },
        { 'Name': 'Maserati Bora', 'MPG': 15.0, 'Weight': 3.570 },
        { 'Name': 'Volvo 142E', 'MPG': 21.4, 'Weight': 2.580 }
    ])

    df.index = df['Name']
    del df['Name'] 

    df.loc["Toshiba"] = [20.0, 3.8]
    print(df)

We can remove rows with `.drop("index/name", inplace = True/False)`. The `inplace = True` removes the row without returning a new data frame. 



    import pandas as pd

    df = pd.DataFrame([
        { 'Name': 'Ferrari Dino', 'MPG': 19.7, 'Weight': 2.770 },
        { 'Name': 'Maserati Bora', 'MPG': 15.0, 'Weight': 3.570 },
        { 'Name': 'Volvo 142E', 'MPG': 21.4, 'Weight': 2.580 }
    ])

    df.index = df['Name']
    del df['Name'] 

    df.loc["Toshiba"] = [20.0, 3.8]

    df.drop("Toshiba", inplace = True)

We can also return a copy of the data frame transposed with the `.T` attribute. 

    import pandas as pd

    df = pd.DataFrame([
        { 'Name': 'Ferrari Dino', 'MPG': 19.7, 'Weight': 2.770 },
        { 'Name': 'Maserati Bora', 'MPG': 15.0, 'Weight': 3.570 },
        { 'Name': 'Volvo 142E', 'MPG': 21.4, 'Weight': 2.580 }
    ])

    df.index = df['Name']
    del df['Name'] 

    x = df.T
    print(x)


**Creating a dataframe from a list of dictionaries**


    # create data frame from list of dictionaries

    x = pd.DataFrame([
                        {'name': 'mason', 'age': 21, 'mark': 67},
                        {'name': 'jim', 'age': 22, 'mark': 58},
                        {'name': 'adam', 'age': 20, 'mark': 73}
                        
                    ])
    
    # replace the indices with the name column and
    # delete the name column
    x.index = x['name']
    del x['name']
    print(x)

**Creating a dataframe from a dictionary, where the values are lists**

    import pandas as pd

    list_of_names = ['mason', 'bob', 'jake']
    list_of_heights = [168, 170, 172]
    list_of_weights = [65, 63, 64]
    x = pd.DataFrame({
                         'name': list_of_names,
                         'height': list_of_heights,
                         'weight': list_of_weights
                     })

    print(x)

**Creating a dataframe from pandas series**
If the series have a common index, our dataframe will use that common index


    import pandas as pd

    index_to_be_used = ['obs_1', 'obs_2', 'obs_3']

    height = pd.Series([168.5, 175.3, 177.6], index = index_to_be_used)
    weight = pd.Series([65, 63, 68], index = index_to_be_used)

    my_df = pd.DataFrame({'HEIGHT': height, 'WEIGHT': weight})
    print(my_df)

If the series doesn't have an existing index, then the implied index is `0`, `1`,...

    import pandas as pd

    df = pd.DataFrame({'a': [1,2], 'b': [4,5]})
    print(df)

**Creating a dataframe from a numpy array and adding on row/column names after**

We can also use a `numpy` array. We pass it a $2 \times 3$ array (list of lists). 

Each item in the outer list becomes a row. 

    import numpy as np 
    import pandas as pd 

    df = pd.DataFrame(
      np.array([
      [1, 2, 3],
      [4, 5, 6]
      ]),
      columns = ['col1', 'col2', 'col3'], 
      index = ['row1', 'row2']
    )
    print(df)

Another example without `index` parameter (so will just be `0`, `1`, `2`,...)


    import pandas as pd
    import numpy as np

    df = pd.DataFrame(
        [
            ('Alice', 30, 'F'),
            ('Bob', 25, 'M'),
            ('Jack', 27, 'M')
        ],
        columns=['Name', 'Age', 'Gender']
    )

    print(df)

# dataframe functions

    import numpy as np
    import pandas as pd

    # ---- First data frame ----
    list_of_names = ['mason', 'jim', 'bob']
    list_of_ages = [21, 22, 20]
    list_of_heights = [168, 171, 175]
    list_of_sids = ['4765', '3332', '2212']

    df = pd.DataFrame({
                             'name' : list_of_names,
                             'age' : list_of_ages,
                             'height' : list_of_heights,
                             'sid' : list_of_sids 
                         })

    df.index = df['name']
    del df['name']
    print(df)


    # ---- second data frame ----
    df2 = pd.DataFrame({
                           'N': list(range(100)),
                           'powers': [i**2 for i in range(100)]
                       })

    print(df2)

    #print(df.info())
    #print(df.describe()) # gives total, mean, std dev, 5 num summary
    #print(df.head(2)) # gives first 2 observations
    #print(df.tail(2)) # gives last 2 observations
    #print(df.sort_index()) # sorts based off of index. Goes 'bob' -> 'jim' -> 'mason'. alphanumeric.

- `.info()`: prints a summary of the data frame
- `.describe()`: gives total, mean, std dev, and 5 num summary. only works for numerical data
- `.head(n)`: gives first `n` observations
- `.tail(n)`: gives last `n` observations
- `.sort_index()`: sorts the observations by index
- `.sort_values(...)`: we can also sort the observations by value.

We show `.sort_values(...)` in this example. 

    import numpy as np
    import pandas as pd
    
    df = pd.DataFrame(np.array([
    ['jack', 24, 168, 58],
    ['mason', 22, 168, 64],
    ['bob', 25, 178, 73]
    ]),
    columns = ['name', 'age', 'hegiht', 'weight'],
    index = ['obs1', 'obs2', 'obs3'])

    print(df)

    by_name = df.sort_values('name') # sort alphabetically
    by_name = df.sort_values(by = ['name']) # same as first
    by_name_age = df.sort_values(by = ['name', 'age']) # sort first by name then by age
    by_name_age = df.sort_values(by = ['name', 'age']) # sort first by name then by age
    by_name_age_desc = df.sort_values(by = ['name', 'age'], ascending = False) # sort first by name then by age in descending order. 

# csv and excel
Pandas can load and save data from many different formats. Here we highlight the functions for CSV and Excel. The input/output functions are typically named as `pd.read_*` and `pd.to_*` .

**CSV**

A CSV (comma separated file) is a very simple file format - it is a text file data separated by commas. Here is an example:

We store this in a file called "cars.csv"

    Name,MPG,Weight
    Ferrari Dino,19.7,2.770
    Maserati Bora,15.0,3.570
    Volvo 142E,21.4,2.580

We read this in using the `pd.read_csv("<path>")`

    import pandas as pd 
    df = pd.read_csv("~/Desktop/python-projects/data/cars.csv")
    df1 = pd.read_csv("~/Desktop/python-projects/data/cars.csv", header = 0) # same as above
    df2 = pd.read_csv("~/Desktop/python-projects/data/cars.csv", header = 1) # ignores the first line
    df3 = pd.read_csv("~/Desktop/python-projects/data/cars.csv", header = 1, names = ['col1', 'col2', 'col3']) # ignores the first line and replaces it

    print(df)
    print(df1)
    print(df2)
    print(df3)

We can write a data frame back into a csv using the `df.to_csv("<file name>")` function


    import pandas as pd
    import numpy as np

    x = pd.DataFrame(np.array([
                                  [1, 2, 3],
                                  [4, 5, 6],
                                  [7, 8, 9]
                              ]),
                     columns = ['var1', 'var2', 'var3'],
                     index = ['row1', 'row2', 'row3'])

    x.to_csv("file1")
    x.to_csv("file_no_index", index = False)
    x.to_csv("file_no_index_and_header", index = False, header = False)

# .iloc

iloc allows us to index rows in a `DataFrame` much like we would to a Python list. With `iloc()`, we use the implicit numbering of rows and an implicit numbering of columns rather than the indexes and columns.

- If the indexing results in a one-dimensional object, a `Series` is returned.

- If multi-dimensional, then a `DataFrame`.

Given this data of U.S government spending:

          Food/Tobacco  Medical/Health  Private Education
    1940          22.2            3.53              0.341
    1945          44.5            5.76              0.974
    1950          59.6            9.71              1.800
    1955          73.2           14.00              2.600
    1960          86.8           21.10              3.640

Consider the following code: 

    import pandas as pd 

    df = pd.DataFrame({
        'Food/Tobacco': [22.200, 44.500, 59.60, 73.2, 86.80],
        'Medical/Health': [3.530, 5.760, 9.71, 14.0, 21.10],
        'Private Education': [0.341, 0.974, 1.80, 2.6, 3.64]
    }, index=[1940, 1945, 1950, 1955, 1960])

    # Try this code by uncommenting:

    #print(df.iloc[0], "\n") # first row, 1940
    #print(type(df.iloc[0]), "\n") # type series
    #print(df.iloc[1940]) # error!
    #print(df.iloc[0:3], "\n") # rows 0, 1 and 2
    #print(type(df.iloc[0:2]), "\n") # type dataframe

    print(df)

We see that: 

- `df.iloc[0]` : returns us the 0th row. A `Series`
- `df.iloc[0:4]` : returns us rows 0, 1, 2, 3. A `DataFrame`

# .iloc II

More examples of indexing alongside the `column` include: 

    import pandas as pd 

    df = pd.DataFrame({
        'Food/Tobacco': [22.200, 44.500, 59.60, 73.2, 86.80],
        'Medical/Health': [3.530, 5.760, 9.71, 14.0, 21.10],
        'Private Education': [0.341, 0.974, 1.80, 2.6, 3.64]
    }, index=[1940, 1945, 1950, 1955, 1960])

    # column 0
    print(df.iloc[:, 0], '\n')

    # second last column
    print(df.iloc[:, -2], '\n')

    # row 2 onwards, columns 0 to 1
    print(df.iloc[2:, 0:2], '\n')

    # row 0 with only column 0
    print(df.iloc[[0], [0]], '\n')

    # row 0 with columns 0 and 2:
    print(df.iloc[[0], [0, 2]], '\n')
    
    # Rows 0, 3 each with columns 0 and 2:
    print(df.iloc[[0, 3], [0, 2]], '\n')

# index selections using .loc() NOT .iloc()
While `.iloc()` you can access with an absolute index, with `.loc()` you can access with the names index rows or column names. 

Note that with the command `df.loc[a:b]` the RANGES ARE INCLUSIVE. 

    import pandas as pd 

    df = pd.DataFrame({
        'Food/Tobacco': [22.200, 44.500, 59.60, 73.2, 86.80],
        'Medical/Health': [3.530, 5.760, 9.71, 14.0, 21.10],
        'Private Education': [0.341, 0.974, 1.80, 2.6, 3.64]
    }, index=[1940, 1945, 1950, 1955, 1960])

    print(df, "\n")
    # Try this code by uncommenting the following:

    print(df.loc[1940],"\n") # a series
    print(df.loc[1945:1955], "\n") # rows 1945 to 1955
    print(df.loc[1945:1955, ['Food/Tobacco']], "\n") # rows 1945 to 1955, only 'Food/Tobaco' column

# selections, filters and assignments

    import pandas as pd 

    df = pd.DataFrame({
        'Food/Tobacco': [22.200, 44.500, 59.60, 73.2, 86.80],
        'Medical/Health': [3.530, 5.760, 9.71, 14.0, 21.10],
        'Private Education': [0.341, 0.974, 1.80, 2.6, 3.64]
    }, index=[1940, 1945, 1950, 1955, 1960])

    print(df, "\n")
    # Try the examples by uncommenting the following code:

    #print(df.loc[[True, False, True, False, False], [True, True, False]], "\n") # select rows and columns via True and False

    #print(df['Food/Tobacco'] > 50, "\n") # a boolean series giving : [False, False, True, True, True]
    #print(df.loc[df['Food/Tobacco'] > 50], "\n")

    #print(df.loc[(df['Food/Tobacco'] > 50) & (df['Private Education'] < 2)], "\n")

    #print(df.loc[df['Medical/Health'] < 4, 'Private Education'], "\n")

    #print(df.loc[df['Medical/Health'] < 4, ['Private Education', 'Food/Tobacco']], "\n")

    #df.loc[(df['Food/Tobacco'] > 50)] = 0; print(df, "\n") # zero out all obervations with food/tobacco > 50

    #df.loc[df['Medical/Health'] < 4, 'Private Education'] = 100; print(df, "\n") # make all the rows with medical/health < 4 have private education be 100

    #df['Medical/Health'] = 0; print(df, "\n") # make all observations in the medical/health column zero. 

**SELECTIONS**

Similar to the `Series`, the `DataFrame` allows us to index by boolean arrays of values, where `True` means to take the value, and `False` means to skip the value. The first array indicates what rows to index, and the second array indicates what columns to index.

For example with the above data: 

          Food/Tobacco  Medical/Health  Private Education
    1940          22.2            3.53              0.341
    1945          44.5            5.76              0.974
    1950          59.6            9.71              1.800
    1955          73.2           14.00              2.600
    1960          86.8           21.10              3.640

Calling `df` with `df.loc[[True, False, True, False, False], [True, True, False]]` will result in a DataFrame containing the `1940` and `1950` rows, each with the `Food/Tobacco` and `Medical/Health` column.

          Food/Tobacco  Medical/Health  Private Education
    1940          22.2            3.53              0.341
    1945          44.5            5.76              0.974
    1950          59.6            9.71              1.800
    1955          73.2           14.00              2.600
    1960          86.8           21.10              3.640

    >>> df.loc[[True, False, True, False, False], [True, True, False]]
          Food/Tobacco  Medical/Health
    1940          22.2            3.53
    1950          59.6            9.71

We can create our own `pd.Series` of booleans by simply applying a boolean comparison operator to it. The expression `df['Food/Tobacco'] > 50` will create a series with `True` for the years that `Food/Tobacco` expenditure was greater than 50 billion, and `False` otherwise.

    >>> df['Food/Tobacco'] > 50
    1940    False
    1945    False
    1950     True
    1955     True
    1960     True
    Name: Food/Tobacco, dtype: bool


Giving the resulting `Series` to `[]` returns the rows where `Food/Tobacco` expenditure was greater than 50 billion.

    >>> df.loc[df['Food/Tobacco'] > 50]
          Food/Tobacco  Medical/Health  Private Education
    1950          59.6            9.71               1.80
    1955          73.2           14.00               2.60
    1960          86.8           21.10               3.64

We can chain multiple conditions together using the single ampersand `&` operator. For example, if we were looking for years where `Food/Tobacco` spending was greater than 50 billion, and `Private Education` spending was less than 2 billion we can chain those conditions together like this:

    >>> df.loc[(df['Food/Tobacco'] > 50) & (df['Private Education'] < 2)]
          Food/Tobacco  Medical/Health  Private Education
    1950          59.6            9.71                1.8

`.loc` can also be used to target specific columns with the next argument to the function. 

    >>> df.loc[df['Medical/Health'] < 4, 'Private Education']
    1940    0.341
    Name: Private Education, dtype: float64

Note that we can specify multiple columns by specifying a list.

    >>> df.loc[df['Medical/Health'] < 4, ['Private Education', 'Food/Tobacco']]
          Private Education  Food/Tobacco
    1940              0.341          22.2

**ASSIGNMENTS**

Furthermore, we can use the filtering capabilities to assign values into the `DataFrame`.

    >>> df.loc[(df['Food/Tobacco'] > 50)] = 0
          Food/Tobacco  Medical/Health  Private Education
    1940          22.2            3.53              0.341
    1945          44.5            5.76              0.974
    1950           0.0            0.00              0.000
    1955           0.0            0.00              0.000
    1960           0.0            0.00              0.000

By assigning to 0, we've zeroed out the selected rows.

Just as we can target cells using `.loc`, we can assign to those specific cells.

    >>> df.loc[df['Medical/Health'] < 4, 'Private Education'] = 100
    >>> df
          Food/Tobacco  Medical/Health  Private Education
    1940          22.2            3.53            100.000
    1945          44.5            5.76              0.974
    1950           0.0            0.00            100.000
    1955           0.0            0.00            100.000
    1960           0.0            0.00            100.000

We can assign columns using the `[]` to select the column:


    >>> df['Medical/Health'] = 0
          Food/Tobacco  Medical/Health  Private Education
    1940          22.2               0            100.000
    1945          44.5               0              0.974
    1950           0.0               0            100.000
    1955           0.0               0            100.000
    1960           0.0               0            100.000

**SUMMARY**

- `df.loc[<logical vector>]` : obtain rows with *all* columns
  
  - `df.loc[[True, True, False, False, True]]` : get 0th, 1st and 5th row
  - `df.loc[df['var1'] > 50]` : get all rows where `var1` is greater than 50

- `df.loc[<logical vector>, <list of variables>]` : obtain rows with *some* columns
  
  - `df.loc[[True, True, False, False, True], [True, False, True]` : get 0th, 1st and 5th row alongside 0th and 2nd column 
  - `df.loc[(df['var1'] > 50) & (df['var2'] < 2), ['var1', 'var2']]`: Get the rows where `var1` is greater than 50 and the rows where `var2` is less than 2. Only select the `var1` and `var2` columns. 

- Note that `df['var1'] = df.loc[:, 'var1']` so you could just use `df.loc[]` for subsetting rows and columns!

Example: 

    # select 'Food/Tobacco column' 
    print(df['Food/Tobacco'], "\n") 
    # select 'Food/Tobacco column' using df.loc
    print(df.loc[:, 'Food/Tobacco'], "\n") 
    # select the 1940 row
    print(df.loc[1940]) 
    # select the 1940 and 1950 row
    print(df.loc[[1940, 1950]]) 
    # select 1955 and 1960 rows and 'Food/Tobacco' and 'Medical/Health' colums
    print(df.loc[[1955, 1960], ['Food/Tobacco', 'Medical/Health']]) 

    # get all observations which have 'Food/Tobacco' > 50
    print(df.loc[df['Food/Tobacco'] > 50], "\n")
    print(df.loc[df.loc[:, 'Food/Tobacco'] > 50], "\n")
    
    # get all observations which have 
    #'Food/Tobacco' > 50 OR  'Medical/Health' > 5
    print(df.loc[(df['Food/Tobacco'] > 50) | (df['Medical/Health'] > 5) ], "\n")
    print(df.loc[(df.loc[:,'Food/Tobacco'] > 50) | (df.loc[:,'Medical/Health'] > 5) ], "\n")

    # get all observations which have 
    # 'Medical/Health' > 10 and select 
    # 'Food/Tobacco', 'Medical/Health' columns
    print(df.loc[df['Medical/Health'] > 10, ['Food/Tobacco', 'Medical/Health']])
# missing data


**NaN for missing numerical data**

In Pandas, missing data values are represented using `np.nan`

    import pandas as pd
    import numpy as np

    df = pd.DataFrame({
        'Food/Tobacco': [22.200, np.nan, 59.60, 73.2, 86.80],
        'Medical/Health': [3.530, 5.760, 9.71, 14.0, 21.10],
        'Private Education': [0.341, 0.974, 1.80, np.nan, 3.64]
    }, index=[1940, 1945, 1950, 1955, 1960])

    print(df,"\n")
    print(df.dropna(), "\n") # drop all rows with an NaN present
    print(df.fillna(0), "\n") # replaces all occurences of NaN with zero
    print(df.isna(), "\n") # return a dataframe of booleans telling where the NaN's are

- `.dropna()`: We can remove all rows containing missing values with the `.dropna()` function. This returns a new `DataFrame` with those rows removed. We can optionally choose to drop columns instead of rows if we desire.
- `.fillna()`: We can also fill the missing values with a specified value. Here we use `.fillna(0)` to fill all missing values with 0.
- `np.isna()`: `isnan` is a function provided by NumPy to check if a value is a NaN.

      >>> np.isnan(np.nan)
      True
      >>> np.isnan(0)
      False

- `.isna()`: Pandas also provides `.isna()` which returns a mask of missing values in the DataFrame.

**None for missing non-numerical data**

    import pandas as pd
    import numpy as np

    df = pd.DataFrame(
        [
            ('Alice', 30, 'F'),
            ('Bob', 25, 'M'),
            ('Eve', 99, None)
        ],
        columns=['Name', 'Age', 'Gender']
    )

    print(df)
    print(pd.isnull(df))

- `pd.isnull(df)`: Return a mask dataframe checking whether a value is `None` or not. 

      >>> pd.isnull(df)
            Food/Tobacco  Medical/Health  Private Education
      1940         False           False              False
      1945          True           False              False
      1950         False           False              False
      1955         False           False              True
      1960         False           False              False

- `ps.notnull(df)`: Return the logical inverse of above. 


      >>> pd.notnull(df)
            Food/Tobacco  Medical/Health  Private Education
      1940         True           True              True
      1945         False          True              True
      1950         True           True              True
      1955         True           True              False
      1960         True           True              True



# iterating
We can interate through the variables in a dataframe with a `for` loop

    import pandas as pd

    df = pd.DataFrame(
        [
            ('Alice', 30, 'F'),
            ('Bob', 25, 'M'),
        ],
        columns=['Name', 'Age', 'Gender']
    )

    print(df, "\n")

    for x in df: # x takes the value of the variable/columns
        print(x) # prints 'Name', 'Age', then 'Gender'

We can iterate through every row in the `DataFrame` using `.iterrows()`


    import pandas as pd

    df = pd.DataFrame(
        [
            ('Alice', 30, 'F'),
            ('Bob', 25, 'M'),
        ],
        columns=['Name', 'Age', 'Gender']
    )

    print(df, "\n")

    for index, row in df.iterrows():
        print(type(row))

        # see the indices of the series
        print(row.index) 
        # change the indices
        row.index = ['NAME', 'AGE', 'GENDER']
        # get the type ==> should be 'object'
        print(row.dtype) 
        # print out the name and gender of each row. 
        # should also print out 'Name: 1, dtype: object'
        print(row[['NAME', 'AGE']]) 
        for x in row: # print out the values of our row
            print(x) # prints Bob, 25, M (e.g)
        print(row.sort_index()) # sort by index
        print("---------------")

Note: since every row returned is a `Series` created anew, you should not modify the `DataFrame` by changing the row that is returned. Depending on the data type contained within the `DataFrame`, it may or may not work.
# .at and .iat
While the `df.loc[]` and `df.iloc[]` target rows and columns, we can get indivudal cells with `df.at[<index name>, <column name>]` and `df.iat[index, column]`. The difference is betwen using the actual names or the indicies.

    import pandas as pd

    df = pd.DataFrame({
        'Food': [22.200, 44.500, 59.60, 73.2, 86.80],
        'Med': [3.530, 5.760, 9.71, 14.0, 21.10],
        'School': [0.341, 0.974, 1.80, 2.6, 3.64]
    }, index=[1940, 1945, 1950, 1955, 1960])

    # Try the functions below by uncommenting them

    # print the data frame out 
    print(df, "\n")

    # print the cell at index 1940 in the 'Food' column
    print(df.at[1940, 'Food'], "\n")

    # change the cell value to 0
    df.at[1940, 'Food'] = 0

    # use indices to get the value
    print(df.iat[3, 2], "\n")

    # use indices to change the value
    df.iat[3, 2] = 1234

    # print out the data frame again. 
    print(df, "\n")
# group by

Remember: 

- That `df['var1']` is the same as `df.loc[:, 'var 1']` and that it returns a series. 
- We can use methods like `.mean()`, `.max()`, `.sum()`, `.min()` on these series

  - `df['var1'].mean()` for example

- We can access multiple columns with a list **AND THEN** apply the method `.mean()` on it (for example)

  - `df[['var1', 'var2']].mean()` : returns mean of `var1` and `var2`

- We can use `.groupby('var1')` or `.groupby(['var1', 'var2'])` to group by a single or multiple variables
- We can then select the column or columns in which we want to find something about

  - `df.groupby('var1')['var2'].mean()` : group by `var1` and find the mean across the `var2` column
  - `df.groupby(['var1', 'var2'])[['var2', 'var3']].mean()` : group by `var1` and `var2`and find the mean across the `var2` and `var3` columns

# combining and axis
In summary: 

- use the `pd.concat([x, y])` to join two series or data frames together
- you can use the `axis` parameter to know which axis to joing along. 

  - `axis = 0` means to join along the horizontal axis (--)
  - `axis = 1` means to join along the vertical axis (|)

Example: joining series

    import pandas as pd

    # can join two series together with pd.concat([series_1, series_2])
    x = pd.Series([1, 2])
    y = pd.Series([3, 4])

    # the indices will be repeated. We show this by printing out the 
    # value(s) at index 1. It will yield 2 values. 
    z = pd.concat([x, y])
    print(z, "\n")
    print(z[1])

Example: joining data frames: 

    import pandas as pd

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

Example: Using the `axis` parameter

    import pandas as pd

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

    df3 = pd.concat([df1, df2])

    print(df3.mean(axis = 0), "\n") # take mean along horizontal axis (--)
    print(df3.mean(axis = 1), "\n") # take mean along vertical axis (|)

    x = pd.concat([df1, df2], axis = 1) # add along the vertical axis (|)
    print(df3, "\n")
    print(x, "\n")

# joining with merge()
Recall that to join two data frames together you can use: 

- `pd.concat()`


      import pandas as pd 

      # using `pd.concat()` to make a data frame. 
      index = [0, 1, 2, 3]

      df1 = pd.DataFrame(['a', 'b', 'c', 'd'], 
                         index = index,
                         columns = ['X'])
      print(df1, '\n')

      df2 = pd.DataFrame(['e', 'f', 'g', 'h'],
                         index = index,
                         columns = ['Y'])

      print(df2, '\n')

      print(pd.concat([df1, df2], axis = 1), '\n')

- `[]` to add a column for a data frmae

      df1 = pd.DataFrame(['a', 'b', 'c', 'd'], 
                         index = index,
                         columns = ['X'])

      df2 = pd.DataFrame(['e', 'f', 'g', 'h'],
                         index = index,
                         columns = ['Y'])

      df1['Y'] = df2['Y']
      print(df1, '\n')

This is actually a join/merge operation, where we combine two different DataFrames using a column as a key (we're using the index as the key). There is a more general way to combine two DataFrames and that is by using the `pd.merge()` function.

- Note that `pd.merge(df1, df2, on = 'var1')` joins `df2` to the right of `df1` where a common column between `df1` and `df2` is given to the `on` parameter. 


      import pandas as pd

      customers = pd.DataFrame([
          (1, 'Alice', '1 ABC Street'),
          (2, 'Bob', '2 ABC Street'),
          (3, 'Eve', '3 ABC Street'),
      ], columns=['Customer_ID', 'Name', 'Address'])
      print(customers, '\n')

      orders = pd.DataFrame([
          (1, 1, 'TV', 100),
          (2, 1, 'Radio', 50),
          (3, 3, 'TV', 100),
      ], columns=['Order_ID', 'Customer_ID', 'Product', 'Quantity'])
      print(orders, '\n')

      print(pd.merge(orders, customers, on='Customer_ID'))

If we didn't have the same column in `df1` and `df2` we could specify the `left_on` and `right_on` parameters. 

- `left_on` and `right_on` must be the same data type 
- It'll combine the rows by matching the values from the `left_on` and `right_on` rows.
- The resultant dataframe will always be smaller (or same size) than the ones which make it up. 

Example 1: 

    import pandas as pd

    df1 = pd.DataFrame({
                           'name':  ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'], 
                           'age' : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 
                           'weight': [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
                       })

    df2 = pd.DataFrame([
                           ('D', 6, 'M'),
                           ('F', 1, 'F'),
                           ('C', 10, 'M'),
                           ('J', 3, 'F'),
                           ('A', 4, 'M'), 
                           ('H', 8, 'M')
                       ], columns = ['label', 'time', 'sex'])

    df3 = pd.DataFrame([
                           ('D', 34, 'M'), 
                           ('X', 5, 'F'),
                       ], columns = ['letter', 'num', 'sex'])
    print(df1, '\n')
    print(df2, '\n')

    print(pd.merge(left = df1, right = df2, left_on = 'name', right_on = 'label'), '\n')
    print(pd.merge(left = df1, right = df2, left_on = 'age', right_on = 'time'), '\n')
    print(pd.merge(left = df2, right = df3, left_on = 'label', right_on = 'letter'),'\n')
    print(pd.merge(left = df2, right = df3, left_on = 'time', right_on = 'num'),'\n')

Example 2: 


    import pandas as pd


    orders = pd.DataFrame([
        (1, 1, 3, 'TV', 100),
        (2, 1, 1, 'Radio', 50),
        (3, 3, 3, 'TV', 100),
    ], columns=['Order_ID', 'Customer_ID', 'Referrer_ID', 'Product', 'Quantity'])
    print('orders')
    print(orders, '\n')

    customers = pd.DataFrame([
        (1, 'Alice', '1 ABC Street'),
        (2, 'Bob', '2 ABC Street'),
        (3, 'Eve', '3 ABC Street'),
    ], columns=['Customer_ID', 'Name', 'Address'])

    print('cusomters')
    print(customers, '\n')


    print(pd.merge(orders, customers, left_on='Order_ID', right_on='Customer_ID'), '\n')
    print(pd.merge(orders, customers, left_on='Referrer_ID', right_on='Customer_ID'), '\n')

Example 3: Joining on an index 

- To use the index as the column to join on you either have to set the `left_index = True` or `right_index = True` or both. 
- If we put `left_index = True` then the resultant data frame gets it's indices from the **other** data frame. 


      import pandas as pd

      df1 = pd.DataFrame([
                             ('A', 'a', 1), 
                             ('B', 'b', 4),
                             ('C', 'c', 9), 
                             ('D', 'd', 5), 
                             ('E', 'e', 2)
                         ], columns = ['cap', 'low', 'num'])

      df1.index = df1['cap']
      del df1['cap']
      print(df1, '\n')


      df2 = pd.DataFrame([
                             ('A', 'aa', 1), 
                             ('B', 'bb', 4),
                             ('C', 'cc', 9), 
                             ('D', 'dd', 5), 
                             ('E', 'ee', 2)
                         ], columns = ['capital letter', 'lowercase letter', 'number'])

      print(df2, '\n')

      df3 = pd.DataFrame({
                             'name': ['mason', 'jason', 'blason'], 
                             'age' : [34, 35, 36],
                             'cap' : ['A', 'D', 'F']
                         }, index = ['A', 'D', 'F'])

      df3.index = df3['cap']

      # indices got taken from the right data frame (df2)
      print(pd.merge(left = df1, right = df2, left_index = True, right_on = 'capital letter'))

      # indices get taken from the the left data frame (df1)
      print(pd.merge(left = df1, right = df2, left_on = 'num', right_index = True))

      # indices get taken from both because they're the same!
      print(pd.merge(left = df1, right = df3, left_index = True, right_index = True))

# inner join
- If we wanted to `merge` on a column, an inner merge means that the result will only have the rows which BOTH data frames have. 
- It's like an AND case

      import pandas as pd

      colours = pd.DataFrame([
          (1, 'Brown'),
          (2, 'White'),
          (3, 'Green'),
          #(4, 'Orange'),  #uncomment this to get the 4th observation too
      ], columns=['Product_ID', 'Colour'])

      print(colours, '\n')

      types = pd.DataFrame([
          (1, 'Basketball'),
          (2, 'Baseball'),
          (3, 'Tennis Ball'),
          (4, 'Squash Ball'), 
      ], columns=['Product_ID', 'Type'])

      print(types, '\n')

      print(pd.merge(colours, types, on='Product_ID'))

# outer join
The outer join is like an OR. It can be specified into 3 categories:

- Left outer join: keeps all the data from the left data frame, possibly introducing `NaN` or `None`. Does an inner join for the right data frame


      import pandas as pd

      colours = pd.DataFrame([
          (1, 'Brown'),
          (2, 'White'),
          (3, 'Green'),
          (4, 'Orange'),
      ], columns=['Product_ID', 'Colour'])

      print(colours, '\n')

      types = pd.DataFrame([
          (1, 'Basketball'),
          (2, 'Baseball'),
          (3, 'Tennis Ball'),
          (7, 'Soccer') # Not included in final dataframe.  
      ], columns=['Product_ID', 'Type'])

      print(types, '\n')

      # colours is the left and types is the right
      print(pd.merge(left = colours, right = types, on='Product_ID', how='left'))

- Right outer join: Keeps all the data from the right data frame, possibly introducing `NaN` or `None`. Does an innjer join for the left data frame 


      import pandas as pd

      colours = pd.DataFrame([
          (1, 'Brown'),
          (2, 'White'),
          (3, 'Green'),
          (7, 'Yellow') # Not included in final data frame. 
      ], columns=['Product_ID', 'Colour'])

      print(colours, '\n')

      types = pd.DataFrame([
          (1, 'Basketball'),
          (2, 'Baseball'),
          (3, 'Tennis Ball'),
          (4, 'Squash Ball')
      ], columns=['Product_ID', 'Type'])

      print(types, '\n')

      # colours is the left and types is the right
      print(pd.merge(colours, types, on='Product_ID', how='right'))

- Full outer join: Keeps all the data from **both** data frames, possibly introducing `NaN` or `None`

      import pandas as pd

      colours = pd.DataFrame([
          (1, 'Brown'),
          (2, 'White'),
          (3, 'Green'),
          (4, 'Orange'),
      ], columns=['Product_ID', 'Colour'])

      types = pd.DataFrame([
          (1, 'Basketball'),
          (2, 'Baseball'),
          (3, 'Tennis Ball'),
          (5, 'Hockey Puck')
      ], columns=['Product_ID', 'Type'])

      # colours is the left and types is the right
      print(pd.merge(colours, types, on='Product_ID', how='outer'))

# joining on multiple columns
To join on multiple columns, for the `on = 'var1'` parameter, include a list instead. That is `on = ['var1', 'var2']`

    import pandas as pd

    df1 = pd.DataFrame([
        ('Square', 'Red', 0),
        ('Round', 'Green', 20),
        ('Hexagonal', 'Blue', 1000),
    ], columns=['Shape', 'Colour', 'Likes'])

    print(df1, '\n')

    df2 = pd.DataFrame([
        ('Square', 'Red', 0),
        ('Round', 'Green', 100),
        ('Hexagonal', 'Blue', 1000),
    ], columns=['Shape', 'Colour', 'Sales'])

    print(df2, '\n')

    # specify a list instead
    print(pd.merge(df1, df2, on=['Shape', 'Colour']))

# category type

`Category` is a data type in pandas that isn't in NumPy. A column with dtype `category` can only take on one of a set of values. It's analogous to Excel's enum. We can save memory and prevent invalid values from being set by converting object columns into `category` columns.

Let's convert the "Gender" column to a `Category` type, using the `astype` function and assigning it back to the column. When we run the `info()` function, we notice that the dtype of this column is now `category` rather than `object`.


    import pandas as pd

    income = pd.DataFrame({
        'Gender': ['Female', 'Male', 'Male', 'Male', 'Male', 'Male', 'Male', 'Female', 'Male', 'Female', 'Male', 'Male', 'Female', 'Male', 'Male'],
        'Income level': ['lower middle', 'low', 'middle', 'higher middle', 'higher middle', 'middle', 'middle', 'higher middle', 'I prefer not to answer', 'middle', 'high', 'lower middle', 'I prefer not to answer', 'higher middle', 'middle']
    })

    income['Gender'] = income['Gender'].astype('category')
    print(income.info())


# timeseries and resampling
- To make a timeseries we can use the `pd.date_range(starting date, period = n, freq = <S|H|D|W|M|Y|>)` function. 
- `starting date` is a string for time. E.g `2020-01-01`
- `period` is how many dates you wanna make. 
- `freq` is either `S`, `H`, `D`, `W`, `M` or `Y` denoting the time. 

      import pandas as pd

      index = pd.date_range('2020-01-01', periods=6, freq='H')
      print(index, '\n')
      print(pd.Series([0,1,2,3, 4, 5], index=index), '\n')

- We can also do ranges of dates by putting in two dates and a specified for `freq`


      import pandas as pd
      import numpy as np

      print(pd.date_range('2020-01-01', '2020-02-01', freq='D'))

- 

# timeseries indexing
