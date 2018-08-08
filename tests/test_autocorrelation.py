import numpy as np
import pandas as pd
import vega_stats as vs

data = pd.DataFrame(dict(x=np.random.uniform(size=100)))

vs.autocorrelation(data, "x", max_lag=15)
