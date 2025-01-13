# clearml_demo






https://clear.ml/docs/latest/docs/apps/clearml_task/#pushing-a-script-to-the-server:

|||
|:---|:---|
|`--queue`|Select a task's execution queue. If not provided, a task is created but not launched|


> [!CAUTION]
> When launching a pipeline, the pipeline run itself takes one worker in the queue. Thus, to launch a sequential pipeline with k back-to-back steps in one queue, you have to have at least 2 workers!

> [!WARNING]
> Depending on the definition of the agents, you might have to precise at task level inside the pipeline and the pipeline steps, the corresponding `repo` and `docker`.

> [!WARNING]
> Create task with python will fail if an `import` fails before `execute_remotely(None)`

> [!WARNING]
> Weirdly enough, despite having precised:
> ```python
> task.set_repo(repo="https://github.com/RR5555/clearml_demo.git")
> ```
> The `requirements.txt` was not found it would seem when executing step 2 of the pipeline.\
> A fix is to explicit the dependency on the `requirements.txt`:
> ```python
> task.set_packages(packages="./requirements.txt")
> ```

```bash
docker compose -p clearml-server down
docker compose -f /opt/clearml/docker-compose.yml up -d
```


```bash
make launch-env
make launch-agent
make exp-from-private-repo
make stop-agent
make launch-agents
make pipeline-from-functions
make pipeline-from-decorator

make create-tasks-for-pipeline
make pipeline-from-tasks

make stop-agents
```


### Reports

[Clearml Docs -- Reports](https://clear.ml/docs/latest/docs/webapp/webapp_reports/)


### Datasets

[Clearml Docs -- Clearml Data](https://clear.ml/docs/latest/docs/clearml_data/)

```bash
curl -o Affairs.csv https://vincentarelbundock.github.io/Rdatasets/csv/AER/Affairs.csv
clearml-data create --project DatasetProject --name HelloDataset
clearml-data add --files Affairs.csv
clearml-data close
clearml-data create --project DatasetProject --name HelloDataset2 --parents 479a1e15b44e44daa4e27efa97811246
clearml-data close
```


## Integrated


Launch `clearml-test-integrated-exp_container-1`?

docker compose -p clearml-agent down
docker compose -p clearml-launcher down

See repo `clearml-agent`: `clearml-agent/integrated`: `README`, `Makefile`


* `integrated_test.py`:
  * Desc.:\
  	Create a task with:
	|||
	|:---|:---|
	|Project|`Demo`|
	|Task|`Integrated 1`|
	The computational load is inside the file declaring the task. (The load register a scatter plot and scalars (i:i*2 for i in range(100)))
  * Not found (`EXECUTION`):
    * Repo
    * Container
    * Destination
  * Hostname (`INFO`): `5df405395f17` (the `CONTAINER ID`)
  * Description (`INFO`): ''Auto-generated at 2024-05-21 07:00:10 UTC by root@5df405395f17''
* `integrated_test2.py`:
  * Desc.:
	Create a Task with:
	|||
	|:---|:---|
	|Project|`Demo`|
	|Task|`Integrated 2`|
	With an argument parser:
	||||
	|:---|:---|:---|
	|`repo`|bool|`task.set_repo(repo="https://github.com/RR5555/clearml_demo.git", branch="main", commit=None)`|
	|`docker`|bool|`task.set_base_docker(docker_image="rr5555/clearml_test:integrated", docker_arguments=None, docker_setup_bash_script=None)`|
	|`new_task`|bool|`reuse_last_task_id=False`|

	`Task.force_requirements_env_freeze(force=True, requirements_file=None)`:
	TODO: Attempt to use local pkgs?

	https://clear.ml/docs/latest/docs/configs/clearml_conf
	''

	`agent.package_manager.system_site_packages` (bool)

    * Indicates whether Python packages for virtual environments are inherited from the system when building a virtual environment for an experiment.

    	The values are:
        * `true` - Inherit
        * `false` - Do not inherit (load Python packages)
	''

	''
	`sdk.development.default_output_uri` (string)

    The default output destination for model checkpoints (snapshots) and artifacts. If the `output_uri` parameter is not provided when calling `Task.init()`, then use the destination in `default_output_uri`.

	''

	''
	`sdk.development.worker.log_stdout` (bool)

    * For development mode workers, indicates whether all stdout and stderr messages are logged.

    	The values are:
        * `true` - Log all
        * `false` - Do not log all
	''

	''

	`sdk.storage.direct_access.url` (string)

    * Specify a list of direct access objects using glob patterns which matches sets of files using wildcards. Direct access objects are not downloaded or cached, and any download request will return a direct reference.

	''



	**Computational load**: imported from `test.py`; `main()`

	`test.py`: `logging` and `SummaryWritter`:\
	TODO: Check out how results are stored: are there duplicates? (log is captured, but log stdout or all streams?)



```bash
cd /root/code
python integrated_test.py
python integrated_test2.py
python integrated_test2.py --docker
python integrated_test2.py --repo
python integrated_test2.py --docker --repo
python integrated_test2.py --docker --repo --force-reqs
python integrated_test2.py --docker --repo --force-reqs --new-task
```


https://clear.ml/docs/latest/docs/webapp/webapp_exp_track_visual#custom-parameter-groups

https://clear.ml/docs/latest/docs/webapp/webapp_exp_track_visual/#general-information



[Task.ignore_requirements](https://clear.ml/docs/latest/docs/references/sdk/task/#taskignore_requirements): ''Ignore a specific package when auto generating the requirements list. Example: Task.ignore_requirements(‘pywin32’)''


[ClearML Agent CLI](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_ref/#parameters):
''`--install-globally`:	Install the required Python packages before creating the virtual environment. Use `agent.package_manager.system_site_packages` to control the installation of the system packages. When `--docker` is used, `--install-globally` is always true.''


TODO: Look at `ClearML-Docs.md`\#`Re-use Artifcats`
TODO: https://clear.ml/docs/latest/docs/model_registry#querying-models


https://ibrahimhkoyuncu.medium.com/clearml-complete-guide-to-manage-datasets-and-create-pipeline-to-train-ml-model-ef06f93bca7b
''
```python
task = Task.init(project_name=project_name, task_name="step_2")
args = {
    'dataset_name': '',
    'random_state': 42,
    'test_size': 0.2,
}

# store arguments, later we will be able to change them from outside the code
task.connect(args)
print('Arguments: {}'.format(args))

# only create the task, we will actually execute it later
task.execute_remotely()
```
''

TODO: Preview for text artifacts


https://www.google.com/search?client=ubuntu-sn&channel=fs&q=clearml+text+file+artifact+preview

https://clear.ml/docs/latest/docs/guides/reporting/using_artifacts/

https://github.com/allegroai/clearml/issues/333


# Re-use artifacts

```bash
root@5df405395f17:~/code# python -m reuse_artifact
{'name': 'dummy_log', 'size': 13, 'type': 'custom', 'mode': <ArtifactModeEnum.output: 'output'>, 'url': 'file:///root/results/Demo/Storage.a62c2407ebb54c9a89ef307b51dee753/artifacts/dummy_log/a.log', 'hash': '0ba904eae8773b70c75333db4de2f3ac45a8ad4ddba1b242f0b3cfc199391dd8', 'timestamp': datetime.datetime(2024, 7, 6, 9, 25, 37), 'metadata': {}, 'preview': 'a.log - 13 bytes\n'}
{'name': 'dummy_log', 'size': 13, 'type': 'custom', 'mode': <ArtifactModeEnum.output: 'output'>, 'url': 'file:///root/results/Demo/Storage.a62c2407ebb54c9a89ef307b51dee753/artifacts/dummy_log/a.log', 'hash': '0ba904eae8773b70c75333db4de2f3ac45a8ad4ddba1b242f0b3cfc199391dd8', 'timestamp': datetime.datetime(2024, 7, 6, 9, 25, 37), 'metadata': {}, 'preview': 'a.log - 13 bytes\n'}
file:///root/results/Demo/Storage.a62c2407ebb54c9a89ef307b51dee753/artifacts/dummy_log/a.log
/root/results/Demo/Storage.a62c2407ebb54c9a89ef307b51dee753/artifacts/dummy_log/a.log
['Hello world!\n']
```


