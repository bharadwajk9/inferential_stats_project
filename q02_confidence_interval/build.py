# %load q02_confidence_interval/build.py
# Default imports
import math
import scipy.stats as stats
import pandas as pd
import numpy as np
df = pd.read_csv('data/house_pricing.csv')
sample = df['GrLivArea']


# Write your solution here :
def confidence_interval(sample):
    sample_mean = sample.mean()
    sample_size = sample.count()
    sample_stdev = sample.std()
    z_critical = stats.norm.ppf(q=0.95)
    margin_of_error = z_critical * (sample_stdev/math.sqrt(sample_size))
    confidence_interval = (sample_mean-margin_of_error,
                           sample_mean+margin_of_error)
    return confidence_interval

confidence_interval(sample)




