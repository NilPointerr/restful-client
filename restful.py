#!/usr/bin/env python3

import argparse
import requests
import sys
import json
import csv

class RestfulClient:
    BASE_URL = "https://jsonplaceholder.typicode.com"

    def __init__(self, method, endpoint, data=None, output=None):
        self.method = method.lower()
        self.endpoint = endpoint
        self.data = data
        self.output = output
        self.url = f"{self.BASE_URL}{self.endpoint}"

    def send_request(self):
        try:
            if self.method == "get":
                response = requests.get(self.url)
            elif self.method == "post":
                headers = {"Content-Type": "application/json"}
                response = requests.post(self.url, headers=headers, json=self.data)
            else:
                raise ValueError("Unsupported HTTP method.")

            self.handle_response(response)

        except requests.RequestException as e:
            print(f"Request failed: {e}")
            sys.exit(1)

    def handle_response(self, response):
        print(f"HTTP Status Code: {response.status_code}")

        if not response.ok:
            print(f"Error: {response.text}")
            sys.exit(1)

        response_data = response.json()
        
        if self.output:
            self.save_output(response_data)
        else:
            print(json.dumps(response_data, indent=4))

    def save_output(self, response_data):
        if self.output.endswith(".json"):
            with open(self.output, "w") as f:
                json.dump(response_data, f, indent=4)
            print(f"Response saved to {self.output}")

        elif self.output.endswith(".csv"):
            if isinstance(response_data, dict):
                response_data = [response_data]  # Convert dict to list

            if isinstance(response_data, list) and response_data:
                keys = response_data[0].keys()
                with open(self.output, "w", newline="") as f:
                    writer = csv.DictWriter(f, fieldnames=keys)
                    writer.writeheader()
                    writer.writerows(response_data)
                print(f"Response saved to {self.output}")

        else:
            print("Unsupported file format. Use .json or .csv")
            sys.exit(1)

def parse_arguments():
    parser = argparse.ArgumentParser(description="Simple REST client for JSONPlaceholder")
    parser.add_argument("method", choices=["get", "post"], help="Request method")
    parser.add_argument("endpoint", help="Request endpoint URI fragment")
    parser.add_argument("-d", "--data", type=json.loads, help="Data to send with request (for POST)")
    parser.add_argument("-o", "--output", help="Output to .json or .csv file (default: dump to stdout)")
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_arguments()
    client = RestfulClient(args.method, args.endpoint, args.data, args.output)
    client.send_request()
