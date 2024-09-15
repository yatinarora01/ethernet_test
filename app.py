from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import subprocess
import speedtest

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_test', methods=['POST'])
def start_test():
    if request.content_type != 'application/json':
        return jsonify({'error': 'Unsupported Media Type'}), 415

    data = request.get_json()
    test_type = data.get('type')

    if test_type == 'throughput':
        # Your existing throughput test logic here
        return jsonify({'status': 'throughput test started'}), 200
    else:
        return jsonify({'error': 'Invalid test type'}), 400

@app.route('/latency_test', methods=['POST'])
def latency_test():
    if request.content_type != 'application/json':
        return jsonify({'error': 'Unsupported Media Type'}), 415

    target = request.json.get('target', '8.8.8.8')  # Default to Google's public DNS
    try:
        result = subprocess.run(['ping', '-c', '4', target], capture_output=True, text=True)
        output = result.stdout
        return jsonify({'result': output}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/fault_test', methods=['POST'])
def fault_test():
    if request.content_type != 'application/json':
        return jsonify({'error': 'Unsupported Media Type'}), 415

    target = request.json.get('target', '8.8.8.8')
    try:
        result = subprocess.run(['ping', '-c', '1', target], capture_output=True, text=True)
        if result.returncode == 0:
            return jsonify({'status': 'connected'}), 200
        else:
            return jsonify({'status': 'faulty'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/speed_test', methods=['POST'])
def speed_test():
    if request.content_type != 'application/json':
        return jsonify({'error': 'Unsupported Media Type'}), 415

    try:
        st = speedtest.Speedtest()
        st.get_best_server()
        download_speed = st.download() / 1_000_000  # Convert to Mbps
        upload_speed = st.upload() / 1_000_000  # Convert to Mbps
        return jsonify({
            'download_speed_mbps': download_speed,
            'upload_speed_mbps': upload_speed
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
