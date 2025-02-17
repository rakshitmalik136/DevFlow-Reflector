#!/bin/bash

# Define directories to create
directories=(
    "backend"
    "backend/tests"
    "frontend"
    "frontend/public"
    "frontend/public/assets"
    "frontend/src"
    "frontend/src/components"
    "frontend/src/pages"
    "extension"
    "extension/webview"
    "docs"
)

# Define files with their content
declare -A files
files["backend/main.py"]="#!/usr/bin/env python
if __name__ == '__main__':
    print('Starting DevFlow Reflector backend...')
    # TODO: Initialize and start the Flask/FastAPI server
"
files["backend/git_parser.py"]="def parse_git_logs(repo_path):
    # TODO: Implement parsing of git logs from the given repository
    pass
"
files["backend/db_manager.py"]="def init_db():
    # TODO: Initialize the local database (SQLite/JSON)
    pass
"
files["backend/analytics.py"]="def analyze_data(data):
    # TODO: Process and analyze commit data to generate insights
    pass
"
files["backend/requirements.txt"]="Flask==2.0.1
GitPython==3.1.18
"
files["backend/tests/test_sample.py"]="def test_sample():
    # TODO: Write backend tests here
    assert True
"
files["frontend/public/index.html"]="<!DOCTYPE html>
<html>
<head>
    <meta charset='UTF-8'>
    <title>DevFlow Reflector</title>
    <link rel='stylesheet' href='assets/styles.css'>
</head>
<body>
    <div id='root'>Welcome to DevFlow Reflector MVP!</div>
</body>
</html>
"
files["frontend/public/assets/styles.css"]="body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
}
"
files[".gitignore"]="node_modules/
__pycache__/
*.pyc
"
files["LICENSE"]="Apache License
Version 2.0, January 2004
http://www.apache.org/licenses/
"

# Function to create directories
create_directories() {
    for dir in "${directories[@]}"; do
        mkdir -p "$dir"
        echo "Ensured directory exists: $dir"
    done
}

# Function to create files with content
create_files() {
    for file in "${!files[@]}"; do
        if [[ ! -f "$file" ]]; then
            echo -e "${files[$file]}" > "$file"
            echo "Created file: $file"
        else
            echo "File already exists: $file"
        fi
    done
}

# Function to install backend dependencies
install_backend_requirements() {
    local req_file="backend/requirements.txt"
    if [[ -f "$req_file" ]]; then
        echo "Installing backend Python dependencies..."
        pip install -r "$req_file"
    else
        echo "No backend requirements.txt file found."
    fi
}

# Main execution flow
create_directories
create_files
install_backend_requirements

echo "Minimal MVP setup complete. Please run 'npm install' manually in the frontend directory if needed."


echo "DevFlow Reflector setup complete."
