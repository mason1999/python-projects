import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("../data/temp.csv")
df['date'] = pd.to_datetime(df['date'])

