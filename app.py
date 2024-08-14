from flask import Flask, jsonify
from data_service import fetch_data, process_data

app = Flask(__name__)

# In-memory storage for processed data
processed_data_storage = {}

@app.route('/fetch-data', methods=['GET'])
def fetch_data_endpoint():
    # Simulate fetching data from an external service
    raw_data = fetch_data()
    
    # Process the fetched data
    processed_data = process_data(raw_data)
    
    # Store processed data in memory
    processed_data_storage['data'] = processed_data
    
    return jsonify({"message": "Data fetched and processed successfully", "processed_data": processed_data})

@app.route('/get-processed-data', methods=['GET'])
def get_processed_data():
    # Return the processed data stored in memory
    if 'data' in processed_data_storage:
        return jsonify({"processed_data": processed_data_storage['data']})
    else:
        return jsonify({"error": "No processed data available"}), 404

if __name__ == '__main__':
    app.run(debug=True)
