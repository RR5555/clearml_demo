from clearml import Task


fetched_task = Task.get_task(task_name='Demo', project_name='Storage')
print(fetched_task.artifacts['dummy_log'])
# local_json = fetched_task.artifacts['dummy_log'].get_local_copy()