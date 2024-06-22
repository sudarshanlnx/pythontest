from flask import Flask
import boto3

app = Flask(__name__)

def get_public_ip():
    ec2_client = boto3.client('ec2')
    response = ec2_client.describe_instances()
    public_ip = response['Reservations'][0]['Instances'][0]['PublicIpAddress']
    return public_ip

@app.route('/')
def hello():
    return "Hello, World!"

if __name__ == "__main__":
    public_ip = get_public_ip()
    app.run(host=public_ip, port=5000)

