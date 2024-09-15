import requests

def run_throughput_test(use_mock=False):
    if use_mock:
        # Simulated response for testing
        return {
            "status": "success",
            "throughput": "1000 Mbps"
        }
    
    # Actual request to the Viavi MTS5800 device
    response = requests.post('http://mts5800/api/start_test', json={'type': 'throughput'})
    return response.json()

def run_latency_test(target, use_mock=False):
    if use_mock:
        # Simulated response for testing
        return {
            "result": "PING 8.8.8.8 (8.8.8.8): 56 data bytes\n64 bytes from 8.8.8.8: icmp_seq=0 ttl=118 time=10.3 ms\n..."
        }
    
    # Actual request to the Viavi MTS5800 device
    response = requests.post('http://mts5800/latency_test', json={'target': target})
    return response.json()

def run_fault_test(target, use_mock=False):
    if use_mock:
        # Simulated response for testing
        return {
            "status": "connected"
        }
    
    # Actual request to the Viavi MTS5800 device
    response = requests.post('http://mts5800/fault_test', json={'target': target})
    return response.json()

def run_speed_test(use_mock=False):
    if use_mock:
        # Simulated response for testing
        return {
            "download_speed_mbps": 100.5,
            "upload_speed_mbps": 50.2
        }
    
    # Actual request to the Viavi MTS5800 device
    response = requests.post('http://mts5800/speed_test', json={})
    return response.json()

if __name__ == "__main__":
    # Example usage
    print("Running throughput test...")
    print(run_throughput_test())

    print("Running latency test...")
    print(run_latency_test('8.8.8.8'))

    print("Running fault test...")
    print(run_fault_test('8.8.8.8'))

    print("Running speed test...")
    print(run_speed_test())
