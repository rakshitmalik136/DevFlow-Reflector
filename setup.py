import os
import subprocess
from setuptools import setup, find_packages

# Dictionary mapping file paths to their stub content.
sample_files = {
    # ===== Backend Files =====
    os.path.join("backend", "main.py"):
        """#!/usr/bin/env python
if __name__ == '__main__':
    print('Starting DevFlow Reflector backend...')
    # TODO: Initialize and start the Flask/FastAPI server
""",
    os.path.join("backend", "git_parser.py"):
        """def parse_git_logs(repo_path):
    # TODO: Implement parsing of git logs from the given repository
    pass
""",
    os.path.join("backend", "db_manager.py"):
        """def init_db():
    # TODO: Initialize the local database (SQLite/JSON)
    pass
""",
    os.path.join("backend", "analytics.py"):
        """def analyze_data(data):
    # TODO: Process and analyze commit data to generate insights
    pass
""",
    os.path.join("backend", "requirements.txt"):
        """Flask==2.0.1
GitPython==3.1.18
""",
    os.path.join("backend", "tests", "test_sample.py"):
        """def test_sample():
    # TODO: Write backend tests here
    assert True
""",
    # ===== Frontend Files =====
    os.path.join("frontend", "public", "index.html"):
        """<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>DevFlow Reflector</title>
    <link rel="stylesheet" href="assets/styles.css">
</head>
<body>
    <div id="root">Welcome to DevFlow Reflector MVP!</div>
</body>
</html>
""",
    os.path.join("frontend", "public", "assets", "styles.css"):
        """body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
}
""",
    os.path.join("frontend", "src", "components", "ChartComponent.js"):
        """export default function ChartComponent() {
    return <div>Chart Component</div>;
}
""",
    os.path.join("frontend", "src", "components", "JournalForm.js"):
        """export default function JournalForm() {
    return <div>Journal Form</div>;
}
""",
    os.path.join("frontend", "src", "components", "Dashboard.js"):
        """export default function Dashboard() {
    return <div>Dashboard Component</div>;
}
""",
    os.path.join("frontend", "src", "pages", "DashboardPage.js"):
        """export default function DashboardPage() {
    return <div>Dashboard Page</div>;
}
""",
    os.path.join("frontend", "src", "pages", "JournalPage.js"):
        """export default function JournalPage() {
    return <div>Journal Page</div>;
}
""",
    os.path.join("frontend", "src", "pages", "SettingsPage.js"):
        """export default function SettingsPage() {
    return <div>Settings Page</div>;
}
""",
    os.path.join("frontend", "src", "App.js"):
        """import React from 'react';

function App() {
    return (
        <div>
            <h1>DevFlow Reflector</h1>
            <p>Welcome to the MVP!</p>
        </div>
    );
}

export default App;
""",
    os.path.join("frontend", "src", "index.js"):
        """import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';

ReactDOM.render(<App />, document.getElementById('root'));
""",
    os.path.join("frontend", "src", "api.js"):
        """export function fetchData() {
    // TODO: Implement API calls to backend
    return fetch('/api/data').then(response => response.json());
}
""",
    os.path.join("frontend", "package.json"):
        """{
  "name": "devflow-reflector-frontend",
  "version": "0.1.0",
  "private": true,
  "dependencies": {
    "react": "^18.0.0",
    "react-dom": "^18.0.0"
  },
  "scripts": {
    "start": "echo 'Run frontend manually'",
    "build": "echo 'Build frontend manually'"
  }
}
""",
    os.path.join("frontend", "README.md"):
        """# DevFlow Reflector Frontend

This folder contains the React-based frontend for DevFlow Reflector.
""",
    # ===== Extension Files =====
    os.path.join("extension", "manifest.json"):
        """{
  "name": "devflow-reflector",
  "version": "0.1.0",
  "description": "Future VS Code/GitHub extension for DevFlow Reflector.",
  "main": "extension.js",
  "author": "Your Name",
  "license": "Apache-2.0"
}
""",
    os.path.join("extension", "extension.js"):
        """console.log('DevFlow Reflector extension logic goes here.');
""",
    os.path.join("extension", "webview", "WebviewComponent.js"):
        """export default function WebviewComponent() {
    return <div>Extension Webview Component</div>;
}
""",
    # ===== Documentation Files =====
    os.path.join("docs", "architecture.md"):
        """# Architecture and Roadmap

This document describes the architecture and future roadmap for DevFlow Reflector.
""",
    # ===== Root-Level Files =====
    ".gitignore":
        """node_modules/
__pycache__/
*.pyc
""",
    "LICENSE":
        """Apache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/

TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION
... (full license text here)
""",
    "setup.sh":
        """#!/bin/bash
echo "DevFlow Reflector setup complete."
"""
}


def create_directories():
    """Ensure all required directories exist."""
    directories = [
        "backend",
        os.path.join("backend", "tests"),
        "frontend",
        os.path.join("frontend", "public"),
        os.path.join("frontend", "public", "assets"),
        os.path.join("frontend", "src"),
        os.path.join("frontend", "src", "components"),
        os.path.join("frontend", "src", "pages"),
        "extension",
        os.path.join("extension", "webview"),
        "docs"
    ]
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        print(f"Ensured directory exists: {directory}")


def create_sample_files():
    """Create sample files with stub content if they do not exist."""
    for file_path, content in sample_files.items():
        parent_dir = os.path.dirname(file_path)
        if parent_dir and not os.path.exists(parent_dir):
            os.makedirs(parent_dir, exist_ok=True)
            print(f"Created parent directory for file: {parent_dir}")
        if not os.path.exists(file_path):
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Created file: {file_path}")
        else:
            print(f"File already exists: {file_path}")


def install_backend_requirements():
    """Install backend Python dependencies from requirements.txt."""
    req_file = os.path.join("backend", "requirements.txt")
    if os.path.exists(req_file):
        print("Installing backend Python dependencies...")
        subprocess.check_call(["pip", "install", "-r", req_file])
    else:
        print("No backend requirements.txt file found.")


if __name__ == '__main__':
    # Step 1: Create the full directory structure.
    create_directories()

    # Step 2: Create sample files with minimal content.
    create_sample_files()

    # Step 3: Optionally install backend dependencies.
    install_backend_requirements()

    print("Minimal MVP setup complete. Please run 'npm install' manually in the frontend directory if needed.")

    # Step 4: Setup the backend package (if desired)
    setup(
        name="devflow-reflector",
        version="0.1.0",
        description="DevFlow Reflector: A tool to visualize Git history and track developer productivity via journaling.",
        author="Your Name",
        license="Apache License 2.0",
        packages=find_packages(where="backend"),
        package_dir={"": "backend"},
        include_package_data=True,
        entry_points={
            "console_scripts": [
                "devflow-backend=main:main",  # Adjust this as necessary for your entry point
            ],
        },
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: Apache Software License",
            "Operating System :: OS Independent",
        ],
        python_requires=">=3.8",
    )
