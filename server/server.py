from flask import Flask, request, jsonify, send_from_directory, Response
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import crawler

RATE_LIMIT = "5/minute"  # requests per minute and IP address

app = Flask(__name__, static_folder='../client')
# Initialize the Limiter object correctly with named arguments
limiter = Limiter(app=app, key_func=get_remote_address)

@app.route('/', methods=['GET'])
def home():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/find_path', methods=['POST'])
@limiter.limit(RATE_LIMIT)
def find_path():
    try:
        data = request.get_json()
        start_page = data['start']
        finish_page = data['finish']

        path, logs, time, discovered = crawler.find_path(start_page, finish_page)

        elapsed_time = logs[-1]  # This seems like a mistake, as 'elapsed_time' is not used later.
        response = jsonify({'path': path, 'logs': logs, 'time': time, 'discovered': discovered})
        print(response)
        return response
    except crawler.TimeoutErrorWithLogs as e:
        app.logger.error(f"Error occurred: {e}")
        return jsonify({'error': str(e), 'logs': e.logs, 'time': e.time, 'discovered': e.discovered}), 500
    except Exception as e:
        # This section might raise a NameError if an exception occurs before 'logs', 'time', or 'discovered' are defined
        app.logger.error(f"Error occurred: {e}")
        return jsonify({'error': 'An error occurred while finding path', 'logs': [], 'time': 0, 'discovered': 0}), 500

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory(app.static_folder, path)

# Ensure 'logs' variable is defined and accessible before using it in 'stream_logs' function
@app.route('/logs', methods=['GET'])
def stream_logs():
    logs = []  # Placeholder for actual log handling logic
    def generate():
        for log in logs:
            yield f"data: {log}\n\n"
    return Response(generate(), mimetype='text/event-stream')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, threaded=True)