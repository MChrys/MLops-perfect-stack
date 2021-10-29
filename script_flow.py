from prefect import Client

client = Client()
client.create_flow_run(flow_id="7296e6fd-1f01-422e-b298-c127637e0e14")
