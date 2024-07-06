from clearml import Task


fetched_task = Task.get_task(project_name='Demo', task_name='Storage')
print(fetched_task.artifacts['dummy_log'])
fetched_task_list = Task.get_tasks(project_name='Demo', task_name='Storage', task_filter={'status':('completed',)})
for _task in fetched_task_list:
    print(_task.artifacts['dummy_log'])

print(fetched_task.artifacts['dummy_log'].url)
print(fetched_task.artifacts['dummy_log'].url[7:])


with open(fetched_task.artifacts['dummy_log'].url[7:],'r') as _file:
    print(_file.readlines())



# local_json = fetched_task.artifacts['dummy_log'].get_local_copy()
# local_json = fetched_task.artifacts['dummy_log'].get()
