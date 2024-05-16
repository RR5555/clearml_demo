# clearml_demo





https://clear.ml/docs/latest/docs/apps/clearml_task/#pushing-a-script-to-the-server:

|||
|:---|:---|
|`--queue`|Select a task's execution queue. If not provided, a task is created but not launched|



clearml-task --project examples --name no_execute --script keras_mnist.py --branch master --requirements requirements.txt --args epochs=1