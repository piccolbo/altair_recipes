import numpy as np
import pandas as pd
import altair_recipes as ar

data = pd.DataFrame(dict(x=np.random.uniform(size=100)))

ar.autocorrelation(data, "x", max_lag=15)
