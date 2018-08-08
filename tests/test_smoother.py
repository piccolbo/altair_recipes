import numpy as np
import pandas as pd
import altair_recipes as ar

x = np.random.uniform(size=100)
data = pd.DataFrame(dict(x=x, y=np.random.uniform(size=100) + 10 * x))

ar.smoother(data)
