from clearml import Task


fetched_task = Task.get_task(project_name='Demo', task_name='Storage')
print(fetched_task.artifacts['dummy_log'])
fetched_task_list = Task.get_tasks(project_name='Demo', task_name='Storage')
print(fetched_task_list)

# local_json = fetched_task.artifacts['dummy_log'].get_local_copy()