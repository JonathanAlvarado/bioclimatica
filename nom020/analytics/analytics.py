import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from nom.models import results

pd.set_option('max_columns', 50)

def read_data():
	query_set = results.objects.all()
	data = qs.values('estado', 'ciudad', 'pisos', 'materiales', 'nom')
	data_frame = pd.DataFrame.from_records( data )

	return data_frame

def discretized_data( data ):
	efficiency = [ 0, 25, 35, 50, 75, 100 ]
	group_names = ['0-25%', '25-35%', '35-50%', '50-75%', '75-100%']
	cats = pd.cut( data, efficiency, group_names )
	freq = pd.value_counts( cats )
	return freq

def group_data( table ):
	groups = []
	for key, group in pd.groupby( table, lambda x: x[1] ):
		total = 0
		for item in group:
			total += int( item[2] )

		groups.append( group[0][1],total )

