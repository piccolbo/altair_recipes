import numpy as np
import pandas as pd
import vega_stats as vs

x = np.random.uniform(size=100)
data = pd.DataFrame(dict(x=x, y=np.random.uniform(size=100) + 10 * x))

vs.smoother(data)
