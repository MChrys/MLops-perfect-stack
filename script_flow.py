from prefect import Client

client = Client()
client.create_flow_run(flow_id="1f289ef3-7246-4c6c-9460-414c5adc5121")
