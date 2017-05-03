import sys
import os
import pandas as pd
import numpy as np
from pandas import DataFrame, Series
from datetime import datetime


frame = pd.read_csv(sys.argv[1], index_col=2,parse_dates = True)
# print frame





print frame.ix['2015-01-09 21:30:00']
