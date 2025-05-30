from flask import Flask, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app) 

@app.route('/api/posts', methods=['GET'])
def get_posts():
    try:
        response = requests.get('https://jsonplaceholder.typicode.com/posts')
        response.raise_for_status()
        return jsonify({
            'success': True,
            'data': response.json(),
            'message': 'Posts fetched successfully'
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Failed to fetch posts: {str(e)}'
        }), 500

@app.route('/api/posts/<int:post_id>', methods=['GET'])
def get_post(post_id):
    try:
        response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{post_id}')
        response.raise_for_status()
        return jsonify({
            'success': True,
            'data': response.json(),
            'message': 'Post fetched successfully'
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Failed to fetch post: {str(e)}'
        }), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)