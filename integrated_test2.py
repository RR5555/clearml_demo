from clearml import Task
import argparse

from test import main


def define_parser():
	parser = argparse.ArgumentParser(description='Test clearml Task integration')
	# parser.add_argument('integers', metavar='N', type=int, nargs='+',
	# 					help='an integer for the accumulator')
	# parser.add_argument('--sum', dest='accumulate', action='store_const',
	# 					const=sum, default=max,
	# 					help='sum the integers (default: find the max)')
	parser.add_argument('--docker',
						action='store_true',
						help='Set base docker for task')
	parser.add_argument('--repo',
						action='store_true',
						help='Set repo for task')
	parser.add_argument('--new-task',
						action='store_true',
						help='Provide new id for task')
	parser.add_argument('--force-reqs',
						action='store_true',
						help='Force pip freeze usage for task reqs capture')
	return parser

if __name__ == "__main__":
	args = define_parser().parse_args()
	if args.force_reqs:
		Task.force_requirements_env_freeze(force=True, requirements_file=None)
	if args.new_task:
		task = Task.init(project_name='Demo', task_name='Integrated 2', reuse_last_task_id=False)
	else:
		task = Task.init(project_name='Demo', task_name='Integrated 2', reuse_last_task_id=True)
	if args.docker:
		# https://clear.ml/docs/latest/docs/references/sdk/task/#set_base_docker
		task.set_base_docker(docker_image="rr5555/clearml_test:integrated", docker_arguments=None, docker_setup_bash_script=None)
	if args.repo:
		# https://clear.ml/docs/latest/docs/references/sdk/task/#set_repo
		task.set_repo(repo="https://github.com/RR5555/clearml_demo.git", branch="main", commit=None)
	main()


