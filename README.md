# clearml_demo





https://clear.ml/docs/latest/docs/apps/clearml_task/#pushing-a-script-to-the-server:

|||
|:---|:---|
|`--queue`|Select a task's execution queue. If not provided, a task is created but not launched|



clearml-task --project examples --name no_execute --script keras_mnist.py --branch master --requirements requirements.txt --args epochs=1


> [!CAUTION]
> When launching a pipeline, the pipeline run itself takes one worker in the queue. Thus, to launch a sequential pipeline with k back-to-back steps in one queue, you have to have at least 2 workers!

> [!WARNING]
> Depending on the definition of the agents, you might have to precise at task level inside the pipeline and the pipeline steps, the corresponding `repo` and `docker`.

