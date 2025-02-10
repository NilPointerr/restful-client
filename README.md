# RESTful Client

## Description
A simple command-line REST client for JSONPlaceholder using Python 3 and the `requests` library.

## Installation
```bash
git clone <repo-url>
cd restful-client
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
chmod +x restful.py
```

## Usage

### Get all posts
```bash
./restful.py get /posts
```

### Get a single post
```bash
./restful.py get /posts/1
```

### Post data
```bash
./restful.py post /posts -d '{"title": "The Future of AI", "body": "Artificial Intelligence is transforming the world, enabling automation, data-driven insights, and innovative solutions across industries.", "userId": 1}'
```

### Save response to JSON file
```bash
./restful.py get /posts -o output.json
```

### Save response to CSV file
```bash
./restful.py get /posts -o output.csv
```

