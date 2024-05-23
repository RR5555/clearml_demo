from test import main
from clearml import Task


if __name__ == "__main__":
	task = Task.init(project_name='Demo', task_name='Integrated 2')

	main()



