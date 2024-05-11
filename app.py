from flask import Flask, request, jsonify
import boto3

app = Flask(__name__)

# Initialize DynamoDB and S3 clients
dynamodb = boto3.resource('dynamodb')
s3 = boto3.client('s3')
table = dynamodb.Table('MyDynamoDBTable')

@app.route('/create_user', methods=['POST'])
def create_user():
    data = request.json
    response = table.put_item(Item=data)
    return jsonify(response), 201

@app.route('/upload_file', methods=['POST'])
def upload_file():
    file = request.files['file']
    s3.upload_fileobj(file, 'my-s3-bucket-unique-name', file.filename)
    return jsonify({"message": "File uploaded"}), 200

@app.route('/download_file/<filename>', methods=['GET'])
def download_file(filename):
    s3.download_file('my-s3-bucket-unique-name', filename, f'/tmp/{filename}')
    return jsonify({"message": "File downloaded"}), 200

if __name__ == '__main__':
    app.run(debug=True)
