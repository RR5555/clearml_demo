from clearml import Task, StorageManager

# create an dataset experiment
task = Task.init(project_name="Demo", task_name="step1_dataset_artifact")

task.set_base_docker(docker_image="ubuntu:jammy")
task.set_repo(repo="https://github.com/RR5555/clearml_demo.git")


# only create the task, we will actually execute it later
task.execute_remotely()

# simulate local dataset, download one, so we have something local
local_iris_pkl = StorageManager.get_local_copy(
    remote_url='https://github.com/allegroai/events/raw/master/odsc20-east/generic/iris_dataset.pkl')

# add and upload local file containing our toy dataset
task.upload_artifact('dataset', artifact_object=local_iris_pkl)

print('uploading artifacts in the background')

# we are done
print('Done')
