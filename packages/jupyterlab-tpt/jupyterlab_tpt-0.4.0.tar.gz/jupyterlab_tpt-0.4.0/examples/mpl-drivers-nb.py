# %%
import numpy as np

X = np.linspace(-10, 10)
Y = X ** 3

# %%
import matplotlib.pyplot as plt
#%matplotlib notebook
#%matplotlib widget
%matplotlib ipympl

# %%
plt.figure()
plt.plot(X, Y);

# %%
