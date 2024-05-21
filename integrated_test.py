import numpy as np
import matplotlib.pyplot as plt

# Add the following two lines to your code, to have ClearML automatically log your experiment
from clearml import Task
task = Task.init(project_name='Demo', task_name='Integrated 1')

# Create a plot using matplotlib, or you can also use plotly
plt.scatter(np.random.rand(50), np.random.rand(50), c=np.random.rand(50), alpha=0.5)
# Plot will be reported automatically to clearml
plt.show()

# Report some scalars
for i in range(100):
	task.get_logger().report_scalar(title="graph title", series="linear", value=i*2, iteration=i)



