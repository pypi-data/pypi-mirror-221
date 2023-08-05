import numpy as np
import matplotlib.pyplot as plt
from plotagain import load_pickle


x_data = load_pickle('x_data.pkl')
y_data = load_pickle('y_data.pkl')
unnamed_arg = load_pickle('unnamed_arg.pkl')

plt.plot(x_data, y_data, c='k', label='sin')
plt.plot(x_data, unnamed_arg, c='b', label='cos')
plt.xlabel('xaxis')
plt.ylabel('yaxis')
plt.title('Title')
plt.legend()
plt.savefig('plot.pdf')
plt.show()