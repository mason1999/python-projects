# Table of contents: 
1. [Introduction](#1)
2. [Line plot](#2)
3. [Figures and Axes ](#3)
4. [Default figures and axes](#4)
5. [Anatomy of a figure ](#5)
6. [Lines and markers](#6)
7. [Legends ](#7)
8. [Axis labels and titles](#8)
9. [Axis labels](#9)
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

- `plt.gca()` : get current axes 
- `plt.gcf()` : get current figure


# Anatomy of a figure <a name = "5"></a>
# Lines and markers <a name = "6"></a>
# Legends <a name = "7"></a>
# Axis labels and titles <a name = "8"></a>
# Axis labels <a name = "9"></a>
# Axis ticks <a name = "10"></a>
# Axis scales <a name = "11"></a>
# Bar charts <a name = "12"></a>
# Pie charts <a name = "13"></a>
# Scatter plots <a name = "14"></a>
# Histograms <a name = "15"></a>
# Subplots <a name = "16"></a>
# 3D plots <a name = "17"></a>
# Contour plots <a name = "18"></a>
# Plotting with Pandas <a name = "19"></a>
