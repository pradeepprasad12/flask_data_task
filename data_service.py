def fetch_data():
    # Mock data simulating an external service response
    return ["sample data one", "sample data two", "sample data three"]

def process_data(data):
    # Process the data by converting all text to uppercase
    return [item.upper() for item in data]
