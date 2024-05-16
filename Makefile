.DEFAULT_GOAL := help

launch-env: ## Activate the clearml env (clearml, clearml-agent)

launch-agent: ## Launch one agent on gpu 0 in queue `gpu_dithering`
	CLEARML_WORKER_NAME=clearml-agent-bengio CLEARML_WORKER_ID=clearml-agent-bengio:gpu0 clearml-agent daemon --detached --queue gpu_dithering --create-queue --gpus 0

stop-agent: ## Stop the agent on gpu 0 in queue `gpu_dithering`
	clearml-agent daemon --stop clearml-agent-bengio:gpu0

launch-agents: ## Launch one agent per gpu (4 gpus) in queue `gpu_dithering`
	CLEARML_WORKER_NAME=clearml-agent-bengio CLEARML_WORKER_ID=clearml-agent-bengio:gpu0 clearml-agent daemon --detached --queue gpu_dithering --create-queue --gpus 0
	CLEARML_WORKER_NAME=clearml-agent-bengio CLEARML_WORKER_ID=clearml-agent-bengio:gpu1 clearml-agent daemon --detached --queue gpu_dithering --create-queue --gpus 1
	CLEARML_WORKER_NAME=clearml-agent-bengio CLEARML_WORKER_ID=clearml-agent-bengio:gpu2 clearml-agent daemon --detached --queue gpu_dithering --create-queue --gpus 2
	CLEARML_WORKER_NAME=clearml-agent-bengio CLEARML_WORKER_ID=clearml-agent-bengio:gpu3 clearml-agent daemon --detached --queue gpu_dithering --create-queue --gpus 3

stop-agents: ## Stop the 4 agents in queue `gpu_dithering`
	clearml-agent daemon --stop clearml-agent-bengio:gpu0
	clearml-agent daemon --stop clearml-agent-bengio:gpu1
	clearml-agent daemon --stop clearml-agent-bengio:gpu2
	clearml-agent daemon --stop clearml-agent-bengio:gpu3


exp-from-private-repo: ## Launch an exp from a private repo on `gpu_dithering` queue 
	clearml-task --project Demo --name clearml_test --script clearml/test.py --repo https://github.com/RR5555/Classification_dither.git --branch main --queue gpu_dithering --docker rr5555/dith:cuda12.0-agent

create-tasks-for-pipeline: ## Create the tasks wo exec for pipeline demo
	clearml-task --script step1_dataset_artifact.py --repo https://github.com/RR5555/clearml_demo.git --branch main --docker rr5555/dith:cuda12.0-agent
	clearml-task --script step2_data_processing.py --repo https://github.com/RR5555/clearml_demo.git --branch main --docker rr5555/dith:cuda12.0-agent
	clearml-task --script step3_train_model.py --repo https://github.com/RR5555/clearml_demo.git --branch main --docker rr5555/dith:cuda12.0-agent

pipeline-from-tasks: ## Run pipeline from tasks
	python3 -m pipeline_from_tasks

pipeline-from-functions: ## Run pipeline from functions
	python3 -m pipeline_from_functions

pipeline-from-decorator: ## Run pipeline from decorator
	python3 -m pipeline_from_decorator






# https://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
.PHONY: help

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'


