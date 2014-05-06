import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pd.set_option('max_columns', 50)


def group_data( table ):
	groups = []
	for key, group in pd.groupby( table, lambda x: x[1] ):
		total = 0
		for item in group:
			total += int( item[2] )

		groups.append( group[0][1],total )
