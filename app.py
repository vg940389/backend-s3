"""Example of flask main file."""
from flask import Flask, jsonify
import boto3
import os

app = Flask(__name__)

# Set your S3 bucket and file name
S3_BUCKET = os.environ.get('S3_BUCKET', 'kuberocketci-applications-data')
S3_KEY = 'cmtr-74cudwfj/data.txt'
AWS_REGION = os.environ.get('AWS_REGION', 'eu-central-1')  # Change if needed

@app.route('/')
def get_s3_content():
    """Fetches data.txt from S3 and returns its content as JSON."""
    s3 = boto3.client('s3', region_name=AWS_REGION)
    try:
        obj = s3.get_object(Bucket=S3_BUCKET, Key=S3_KEY)
        content = obj['Body'].read().decode('utf-8')
        return jsonify({"content": content})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/hello')
def hello_world():
    """Returns Hello, EDP!"""
    return 'Hello, EDP!'


if __name__ == '__main__':
    app.run()
