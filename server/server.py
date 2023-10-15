from flask import Flask, request, jsonify, send_from_directory
import crawler

app = Flask(__name__, static_folder='../client')

@app.route('/', methods=['GET'])
def home():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/find_path', methods=['POST'])
def find_path():
    try:
        data = request.get_json()
        start_page = data['start']
        finish_page = data['finish']

        path = crawler.find_path(start_page, finish_page)

        return jsonify({'path': path})
    except Exception as e:
        app.logger.error(f"Error occurred: {e}")
        return jsonify({'error': 'An error occurred while finding path'}), 500

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory(app.static_folder, path)

if __name__ == '__main__':
    app.run(port=5000)
