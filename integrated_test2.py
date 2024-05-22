from clearml import Task
import argparse

from .test import main


def define_parser():
	parser = argparse.ArgumentParser(description='Test clearml Task integration')
	# parser.add_argument('integers', metavar='N', type=int, nargs='+',
	# 					help='an integer for the accumulator')
	# parser.add_argument('--sum', dest='accumulate', action='store_const',
	# 					const=sum, default=max,
	# 					help='sum the integers (default: find the max)')
	parser.add_argument('--docker',
						action='store_true')
	parser.add_argument('--repo',
						action='store_true')
	return parser




if __name__ == "__main__":
	args = define_parser().parse_args()
	task = Task.init(project_name='Demo', task_name='Integrated 2')
	if args.docker:
		# https://clear.ml/docs/latest/docs/references/sdk/task/#set_base_docker
		task.set_base_docker(docker_image="rr5555/clearml_test:integrated", docker_arguments=None, docker_setup_bash_script=None)
	if args.repo:
		# https://clear.ml/docs/latest/docs/references/sdk/task/#set_repo
		task.set_repo(repo="https://github.com/RR5555/clearml_demo.git", branch="main", commit=None)
	main()


