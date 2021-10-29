from prefect import Flow
from prefect.tasks.prefect import create_flow_run, wait_for_flow_run
from prefect.run_configs import LocalRun
import prefect
from prefect import task, Flow, Parameter

from prefect import Client
import subprocess


@task
def say_hello(name):
    logger = prefect.context.get("logger")
    logger.info("Hello {}!".format(name))


with Flow("parent-flow", run_config=LocalRun()) as flow:

    people = Parameter("people", default=["Arthur", "Ford", "Marvin"])
    # Map `say_hello` across the list of names
    say_hello.map(people)

try:
    flow.register(project_name="gojob")
except:
    subprocess.run(["prefect", "create", "project", "gojob"])
    flow.register(project_name="gojob")
# client.create_flow_run(flow_id="d7bfb996-b8fe-4055-8d43-2c9f82a1e3c7")
