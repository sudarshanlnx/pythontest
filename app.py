from flask import Flask
import boto3

app = Flask(__name__)

def get_public_ip():
    try:
        ec2_client = boto3.client('ec2')
        response = ec2_client.describe_instances()
        public_ip = response['Reservations'][0]['Instances'][0]['PublicIpAddress']
        return public_ip
    except Exception as e:
        print(f"Error retrieving public IP address: {e}")
        return None

@app.route('/')
def hello():
    return "Hello, World!"

if __name__ == "__main__":
    public_ip = get_public_ip()
    if public_ip:
        app.run(host=public_ip, port=5000)
    else:
        print("Failed to retrieve public IP address. Exiting.")
