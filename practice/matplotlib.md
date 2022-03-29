# Table of contents: 
1. [Introduction](#1)
2. [Line plot](#2)
3. [Figures and Axes ](#3)
4. [Default figures and axes](#4)
5. [Anatomy of a figure ](#5)
6. [Lines and markers](#6)
7. [Legends ](#7)
8. [Axis labels and titles](#8)
9. [Axis limits](#9)
10. [Axis ticks](#10)
11. [Axis scales](#11)
12. [Bar charts](#12)
13. [Pie charts](#13)
14. [Scatter plots](#14)
15. [Histograms](#15)
16. [Subplots](#16)
17. [3D plots](#17)
18. [Contour plots](#18)
19. [Plotting with Pandas](#19)


# Introduction <a name = "1"></a>
Install: 

    pip3 install matplotlib.pyplot

To begin include this: 

    # from matplotlib import pyplot as plt # will do the same thing
    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd

# Line plot <a name = "2"></a>
- Use `plt.plot([1, 2, 3])` where `[1, 2, 3]` is an example list to be plotted in a line. 
- Use `plt.show()` to display the image
- Use `plt.savefig('my_image')` to save the image


      import matplotlib.pyplot as plt

      # will plot [2, 3, 4] vs [2, 3, 4] by default
      plt.plot([2, 3, 4])
      plt.show()
      plt.savefig('plot.png')

- Specify two parameters to control `x` and `y` values

      import matplotlib.pyplot as plt

      plt.plot([1,2,3,4,5], [5,4,3,2,1])
      plt.savefig('plot.png')

- Plot $x = t\sin t, y = t\cos t$ for $t = 0, 1, ..., 99$

      import matplotlib.pyplot as plt
      import numpy as np

      phi = np.arange(100, dtype=np.float64)
      print(phi)
      plt.plot(phi * np.sin(0.2 * phi), phi * np.cos(0.2 * phi))

      plt.savefig('plot.png')

# Figures and Axes <a name = "3"></a>

- `figure` is whole image
- `axes` are the actual plots. NOT `axis`

      import matplotlib.pyplot as plt
      import numpy as np

      axes = plt.axes()
      print(axes)
      axes.set_title('single axes')

      plt.savefig('plot.png')

# Default figures and axes <a name = "4"></a>

1. When matplotlib is loaded, it automatically creates a `figure`
2. Inside the figure, it contains a default `axes`
3. It is this axes that is drawn on when we use `plt.plot()`.

        import matplotlib.pyplot as plt

        plt.plot([1,2,3,4,5])

        # If `plot` is called again, two lines are drawn on the same plot
        plt.plot([5,4,3,2,1])

        plt.savefig('plot.png')

- `plt.gca()` : get current axes  <-- I haven't used this much
- `plt.gcf()` : get current figure <-- I haven't used this much

**More advanced example: involving styles, legends, titles and tightening layout**
 
- use the `label` parameter in plot so that a name shows up when you use...
- `plt.legend()` plots a legend
- `plt.title('string')` puts a title on figure
- `plt.xlabel('string')` puts an x axis label 
- `plt.ylabel('string')` puts a  y axis label 
- `plt.tight_layout()` puts a tighter layout on figure removing most unecesary whitespace
- `plt.savefig('string')` save the image. 

      import pandas as pd 
      from matplotlib import pyplot as plt

      plt.style.use('seaborn')

      data = pd.read_csv('~/Desktop/python-projects/data/dev_pay.csv')

      # A data frame that looks like this: 
      #    Age  All_Devs  Python  JavaScript
      # 0   18     17784   20046       16446
      # 1   19     16500   17100       16791
      # 2   20     18012   20000       18942
      # 3   21     20628   24744       21780

      ages = data['Age']
      dev_salaries = data['All_Devs']
      py_salaries = data['Python']
      js_salaries = data['JavaScript']

      # python salaries. label is for the legend
      plt.plot(ages, py_salaries, label = 'Python')
      # javascript salaries
      plt.plot(ages, js_salaries, label = 'Javascript')
      # all developer salaries
      plt.plot(ages, dev_salaries, color = '#444444', linestyle = '--', label = 'All Devs')

      # legend
      plt.legend()

      # title
      plt.title('Median salary (AUD) by Age')

      # x and y axis
      plt.xlabel('Ages')
      plt.ylabel('median salary (AUD)')

      # removes some of the whitespace surrounding figure so it's 'nicer'
      plt.tight_layout()

      # shows the plot
      plt.savefig('fig1.png')

**USING THE SUBPLOTS METHOD** 

-  `plt.subplots()` returns a tuple. By defaul it returns `1` axes if no parameters are given. 
- We use the `axes` parameter instead of the `plt` object we had from  before
- All the `plt` becomes `axes` except for things affecting the whole figure. 

  - `.title()` becomes `.set_title()`
  - `.xlabel()` becomes `.set_xlabel()`
  - `.ylabel()` becomes `.set_ylabel()`


        import pandas as pd 
        from matplotlib import pyplot as plt

        plt.style.use('seaborn')

        data = pd.read_csv('~/Desktop/python-projects/data/dev_pay.csv')

        # A data frame that looks like this: 
        #    Age  All_Devs  Python  JavaScript
        # 0   18     17784   20046       16446
        # 1   19     16500   17100       16791
        # 2   20     18012   20000       18942
        # 3   21     20628   24744       21780

        ages = data['Age']
        dev_salaries = data['All_Devs']
        py_salaries = data['Python']
        js_salaries = data['JavaScript']

        # Using the subplots method
        fig, ax = plt.subplots()

        # python salaries. label is for the legend
        ax.plot(ages, py_salaries, label = 'Python')
        # javascript salaries
        ax.plot(ages, js_salaries, label = 'Javascript')
        # all developer salaries
        ax.plot(ages, dev_salaries, color = '#444444', linestyle = '--', label = 'All Devs')

        # legend
        ax.legend()

        # title
        ax.set_title('Median salary (AUD) by Age')
        ax.set_xlabel('Age')
        ax.set_ylabel('Median salary (AUD)')

        # removes some of the whitespace surrounding figure so it's 'nicer'
        plt.tight_layout()

        # shows the plot
        plt.savefig('fig1.png')

**One figure, multiple plots**

To do this we just:

- Input parameters into the `subplots()` function for the `nrows` and `ncols` parameters
- The `subplots()` function will now return a list-- either one dimensional or two dimensional
- To plot, you just decide which one of the `axes` elements to plot into. 
- Everything is still one figure. 

      import pandas as pd 
      from matplotlib import pyplot as plt

      plt.style.use('seaborn')

      data = pd.read_csv('~/Desktop/python-projects/data/dev_pay.csv')

      # A data frame that looks like this: 
      #    Age  All_Devs  Python  JavaScript
      # 0   18     17784   20046       16446
      # 1   19     16500   17100       16791
      # 2   20     18012   20000       18942
      # 3   21     20628   24744       21780

      ages = data['Age']
      dev_salaries = data['All_Devs']
      py_salaries = data['Python']
      js_salaries = data['JavaScript']

      # Using the subplots method. sharex just eliminates all the ticks for 
      # every plot except the lowest one. 
      fig, ax = plt.subplots(nrows = 2, ncols = 1, sharex = True)

      # print(ax) # to see what is printed

      # for the first plot ax[0]
      # python salaries. label is for the legend
      ax[0].plot(ages, py_salaries, label = 'Python')
      # javascript salaries
      ax[0].plot(ages, js_salaries, label = 'Javascript')
      # legend 
      ax[0].legend()
      # title
      ax[0].set_title('Median salary (AUD) by Age')
      #ax[0].set_xlabel('Age')
      ax[0].set_ylabel('Median salary (AUD)')

      # for the second plot ax[1]
      # all developer salaries
      ax[1].plot(ages, dev_salaries, color = '#444444', linestyle = '--', label = 'All Devs')
      ax[1].legend()
      #ax[1].set_title('Median salary (AUD) by Age') 
      ax[1].set_xlabel('Age')
      ax[1].set_ylabel('Median salary (AUD)')

      # removes some of the whitespace surrounding figure so it's 'nicer'
      plt.tight_layout()

      # shows the plot
      plt.savefig('fig1.png')

**Multiple figures**

- With multiple figures, you  just use the `subplots()` function again. 
- Each `figure` owns its own set of axes, so determine which axes to plot on 
- Once you're done with the axes, you deal with the figure with things like:
    - `fig1.tight_layout`
    - `fig1.savefig(...)`

- To show all the figure, you just call `plt.show()`
- The hierachy goes `plt --> figures --> axes` where you can plot multiple plots on axes. 


      import pandas as pd 
      from matplotlib import pyplot as plt

      plt.style.use('seaborn')

      data = pd.read_csv('~/Desktop/python-projects/data/dev_pay.csv')

      # A data frame that looks like this: 
      #    Age  All_Devs  Python  JavaScript
      # 0   18     17784   20046       16446
      # 1   19     16500   17100       16791
      # 2   20     18012   20000       18942
      # 3   21     20628   24744       21780

      ages = data['Age']
      dev_salaries = data['All_Devs']
      py_salaries = data['Python']
      js_salaries = data['JavaScript']

      # Using the subplots method. sharex just eliminates all the ticks for 
      # every plot except the lowest one. 
      fig1, ax1 = plt.subplots()
      fig2, ax2 = plt.subplots()

      # for the first figure
      # python salaries. label is for the legend
      ax1.plot(ages, py_salaries, label = 'Python')
      # javascript salaries
      ax1.plot(ages, js_salaries, label = 'Javascript')

      # additional
      ax1.legend()
      ax1.set_title('Median salary (AUD) by Age')
      ax1.set_xlabel('Age')
      ax1.set_ylabel('Median salary (AUD)')

      # save the first figure
      fig1.tight_layout()
      fig1.savefig('fig1.png')

      # for the second figure
      # all developer salaries
      ax2.plot(ages, dev_salaries, color = '#444444', linestyle = '--', label = 'All Devs')

      # additional
      ax2.legend()
      ax2.set_title('Median salary (AUD) by Age') 
      ax2.set_xlabel('Age')
      ax2.set_ylabel('Median salary (AUD)')

      # save the second figure
      fig2.tight_layout()
      fig2.savefig('fig2.png')

      # plt.show() # uncomment this to show both the figures. 
# Anatomy of a figure <a name = "5"></a>
The anatomy of a figure can be seen in the picture below:

![hello](./fig_anatomy.png)

# Lines and markers <a name = "6"></a>
To plot multiple plots on the same axes: 
1. use the `plt.subplots()` function
2. assign the outputs to variables, `fig` and `ax`
3. Use the `ax.plot(x, y)` to plot each plot on the axes
4. Use `fig.savefig('string')` to save the figure. 
5. optionally use `plt.show()` to show the figure. 


        import matplotlib.pyplot as plt
        import numpy as np

        x = np.array([2, 3, 4, 5])
        y = np.array([5, 2, 20, 25])


        fig, ax = plt.subplots()
        ax.plot(x, y)
        ax.plot(x, y*2)
        ax.plot(x, y*3)
        ax.plot(x, y*4)

        fig.savefig('out.png')

        # plt.show()

To give the lines `linestyle` and `color` enter this as an extra parameter for the `.plot()` function


    import matplotlib.pyplot as plt
    import numpy as np

    x = np.array([2, 3, 4, 5])
    y = np.array([5, 2, 20, 25])


    fig, ax = plt.subplots()
    ax.plot(x, y, color='green', linestyle='solid') # solid green line
    ax.plot(x, y*2, color='pink', linestyle='dotted') # dotted pink line
    ax.plot(x, y*3, color='#FF0000', linestyle='-.') # dash-dot red (hex code) line
    ax.plot(x, y*4, color='#000000', linestyle='--') # dashed black (hex code) line

    fig.savefig('out.png')

    # plt.show()

- To specify a `marker` use the `marker` parameter
- If you don't put in a `linestyle` then the plot will only consist of points. 
- So if you want `marker` and `linestyle` for points and lines you need both. 

      import matplotlib.pyplot as plt
      import numpy as np

      x = np.array([2, 3, 4, 5])
      y = np.array([5, 2, 20, 25])


      fig, ax = plt.subplots()
      # circle markers
      ax.plot(x, y, marker = 'o', color='green', linestyle='solid')
      # pink triangle markers, no line
      ax.plot(x, y*2, marker = '^', color='pink')
      # large red diamond markers
      ax.plot(x, y*3, marker =  'd', color='#FF0000', markersize=12, linestyle='solid')
      # grey '+' markers on a dashed black line
      ax.plot(x, y*4, marker = '+', color='#000000', markerfacecolor='gray', linestyle='--')

      fig.savefig('out.png')

      # plt.show()



# Legends <a name = "7"></a>

To add a legend use a `label = 'string'` in the plot function and `.legend()` function. 

    import matplotlib.pyplot as plt
    import numpy as np

    x = np.array([2, 3, 4, 5])
    y = np.array([5, 2, 20, 25])


    fig, ax = plt.subplots()
    # we use the label = 'string' parameter
    ax.plot(x, y, label = 'a')
    ax.plot(x, y*2, label = 'b')
    ax.plot(x, y*3, label = 'c')
    ax.plot(x, y*4, label = 'd')

    # the .legend() parameter
    ax.legend()

    fig.savefig('out.png')

    # plt.show()
# Axis labels and titles <a name = "8"></a>
To set the axis labels and title...
- If you're accessing directly with the `plt` object then use `.xlabel('string')`, `.ylabel('string')` and `.title('string')`
- If you're accessing via an `axes` object then use `.set_xlabel('string')`, `.set_ylabel('string')` and `.set_title('string')`


      import matplotlib.pyplot as plt
      import numpy as np

      x = np.arange(100, dtype=np.float64) 


      fig, ax = plt.subplots()
      # we use the label = 'string' parameter
      ax.plot(x *  np.sin(0.2 * x), x * np.cos(0.2 * x))

      ax.set_title('spiral')
      ax.set_xlabel('the x axis')
      ax.set_ylabel('the y axis')



      fig.savefig('out.png')

      # plt.show()
# Axis limits <a name = "9"></a>

To set axis limits: 
- use the `xlim()` (for `plt` object) or `set_xlim()` (for `ax` object) same for `y`
- input a tuple to set max and min
- if you only want to set one side: `left = a` or `right = b` parameter for `set_xlim()` 
- similarly `bottom = a` or `top = b` for `set_ylim()`



      import matplotlib.pyplot as plt
      import numpy as np

      x = np.arange(100, dtype=np.float64) 


      fig, ax = plt.subplots()
      ax.plot(x *  np.sin(0.2 * x), x * np.cos(0.2 * x))

      ax.set_title('graphs')
      ax.set_xlabel('the x axis')
      ax.set_ylabel('the y axis')

      # set limits via tuple
      ax.set_xlim((-10, 10))
      ax.set_ylim((-10, 10))


      fig.savefig('out.png')

      # plt.show()
# Axis ticks <a name = "10"></a>
- To change the fontsize of the x axis label and y axis label use the `fontsize = a` parameter in the `.set_xlabel(...)` or `.set_ylabel(...)`
- To change the label size of the ticks, use the `labelsize = a` parameter in the `.tick_params(...)` function. 
- To rotate the label use the `rotation = a` parameter in the `.tick_params(...)` function. 


      import matplotlib.pyplot as plt
      from matplotlib import pyplot as plt
      import numpy as np
      import pandas as pd

      ###################################### this code is to just prepare the data frame #################################
      df = pd.read_csv("../data/temp.csv")
      date = df['date'].copy()
      i = 0
      for str_date in date:
          str_array = str_date.split(sep = '/')
          mmddyy = str_array[1] + '/' + str_array[0] + '/' + str_array[2]
          date[i] = mmddyy
          i += 1

      date = pd.to_datetime(date)
      df = pd.concat([df, date], axis = 1)
      df.columns = ['old date', 'temp', 'date']
      del df['old date']
      ###########################################################################################
      print(df.head())

      fig, ax = plt.subplots()

      ax.plot(df['date'], df['temp'])
      ax.set_title('temperatures across days')
      ax.set_xlabel('days', fontsize = 12)
      ax.set_ylabel('temperature', fontsize = 12)

      # sets tick size and tick rotation for x axis. The tick labels get cut off so we use...
      ax.tick_params(axis = 'x', labelsize = 8, rotation = 40)

      # ... the tick_layout() parameter
      fig.tight_layout()
      fig.savefig('out.png')

# Axis scales <a name = "11"></a>
- We can change the scales of the $X$ and $Y$ axes using the `set_xscale('string')` and `set_yscale('string')`
- Matplotlib accepts `linear`, `log`, `symlog` and `logit` scales. 


      import matplotlib.pyplot as plt
      import numpy as np

      x = np.linspace(0, 200, 200)
      fig, ax = plt.subplots()
      ax.plot(x, x, label='$y = x$')
      ax.plot(x, x ** 2, label='$y = x^2$')
      ax.plot(x, np.exp(x), label='$y = e^x$')

      ax.set_yscale('log')

      ax.set_title('Log chart')
      ax.set_xlabel('x')
      ax.set_ylabel('y')
      ax.set_xlim(left=1)
      ax.set_ylim(bottom=1)

      ax.legend()
      fig.savefig('out.png')

# Bar charts <a name = "12"></a>
We can create a bar chart using the `bar()` function, it takes in two main parameters:
- `x`: A sequence of scalars listing the categories (or if it's not categorical data, it's really just the x values of the chart)
- `height`: A scalar or sequence of scalars listing the heights of the categories. 
# Pie charts <a name = "13"></a>
# Scatter plots <a name = "14"></a>
# Histograms <a name = "15"></a>
# Subplots <a name = "16"></a>
# 3D plots <a name = "17"></a>
# Contour plots <a name = "18"></a>
# Plotting with Pandas <a name = "19"></a>
