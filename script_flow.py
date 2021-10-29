from prefect import Client

client = Client()
client.create_flow_run(flow_id="89d74474-5922-4b51-bc1f-26e3256c5c60")
