from clearml import Task
import argparse

def define_parser():
	parser = argparse.ArgumentParser(description='Test clearml storage')

	parser.add_argument('--new-task',
						action='store_true',
						help='Provide new id for task')
	parser.add_argument('--change-output-uri',
						action='store_true',
						help='Change output URI')
	return parser

if __name__ == "__main__":
	args = define_parser().parse_args()
	if args.new_task:
		task = Task.init(project_name='Demo', task_name='Storage', reuse_last_task_id=False)
	else:
		task = Task.init(project_name='Demo', task_name='Storage', reuse_last_task_id=True)


	if args.change_output_uri:
		task.output_uri = '/root/clearml_results'

	# add and upload local file artifact
	task.upload_artifact(
		name='dummy_log', 
		artifact_object='a.log'
		)


# TODO: Add a re-use in both cases for output_uri
# TODO: Modify consider a direct access?


