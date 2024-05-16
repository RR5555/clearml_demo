# clearml_demo





https://clear.ml/docs/latest/docs/apps/clearml_task/#pushing-a-script-to-the-server:

|||
|:---|:---|
|`--queue`|Select a task's execution queue. If not provided, a task is created but not launched|



> [!CAUTION]
> I had to regenerate the PAT after extending it to this repo before the PAT could work again for the new one (or for both, will ahve to check again) 


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
launch-env
launch-agent
exp-from-private-repo
stop-agent
launch-agents
pipeline-from-functions
pipeline-from-decorator

create-tasks-for-pipeline
pipeline-from-tasks

stop-agents
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


