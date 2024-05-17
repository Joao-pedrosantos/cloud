import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError
from flask import Flask, request, jsonify
import logging

app = Flask(__name__)

# Initialize DynamoDB
dynamodb = boto3.resource('dynamodb', region_name='sa-east-1')
table = dynamodb.Table('MyDynamoDBTableName')

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

@app.route('/add_user', methods=['POST'])
def add_user():
    try:
        # Get data from the request
        user_data = request.json
        
        # Validate input
        if not user_data.get('user_id') or not user_data.get('name'):
            return jsonify({'error': 'user_id and name are required fields'}), 400
        
        # Ensure user_id is included in the item
        item = {
            'user_id': user_data['user_id'],
            'name': user_data['name'],
            # Include other attributes as necessary
        }
        
        # Save data to DynamoDB
        response = table.put_item(Item=item)
        
        return jsonify({'message': 'User added successfully', 'response': response}), 200
    except NoCredentialsError:
        logger.error("Credentials not available")
        return jsonify({'error': 'Credentials not available'}), 500
    except PartialCredentialsError:
        logger.error("Incomplete credentials")
        return jsonify({'error': 'Incomplete credentials'}), 500
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/get_user', methods=['GET'])
def get_user():
    try:
        # Get user_id from the request
        user_id = request.args.get('user_id')
        
        # Validate input
        if not user_id:
            return jsonify({'error': 'user_id is a required field'}), 400
        
        # Get user data from DynamoDB
        response = table.get_item(Key={'user_id': user_id})
        
        return jsonify({'message': 'User retrieved successfully', 'user_data': response.get('Item', {})})
    except NoCredentialsError:
        logger.error("Credentials not available")
        return jsonify({'error': 'Credentials not available'}), 500
    except PartialCredentialsError:
        logger.error("Incomplete credentials")
        return jsonify({'error': 'Incomplete credentials'}), 500
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
