#!/usr/bin/env python
from flask import Flask, jsonify, request
from git_parser import parse_git_logs
from analytics import analyze_data
from db_manager import init_db, get_journal_entries, add_journal_entry

app = Flask(__name__)

# Initialize the journal "database"
init_db()

@app.route('/')
def home():
    return jsonify({"message": "Welcome to DevFlow Reflector API!"})

@app.route('/api/commits', methods=['GET'])
def get_commits():
    repo_path = '.'  # Adjust as needed for your repo path
    commits = parse_git_logs(repo_path)
    return jsonify(commits)

@app.route('/api/analytics', methods=['GET'])
def get_analytics():
    repo_path = '.'
    commits = parse_git_logs(repo_path)
    analytics = analyze_data(commits)
    return jsonify(analytics)

@app.route('/api/journal', methods=['GET', 'POST'])
def journal():
    if request.method == 'POST':
        data = request.json
        result = add_journal_entry(data)
        return jsonify(result)
    else:
        entries = get_journal_entries()
        return jsonify(entries)

if __name__ == '__main__':
    print("Starting DevFlow Reflector backend...")
    try:
        app.run(host='127.0.0.1', port=5000, debug=True)
    except Exception as e:
        logging.exception("An error occurred while running the server:")

#test
