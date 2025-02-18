import json
import os
import time

# Ensure the path is relative to this file
JOURNAL_FILE = os.path.join(os.path.dirname(__file__), 'journal.json')

def init_db():
    """
    Initialize the journal database by creating an empty JSON file if it doesn't exist.
    """
    if not os.path.exists(JOURNAL_FILE):
        with open(JOURNAL_FILE, 'w') as f:
            json.dump([], f)

def get_journal_entries():
    """
    Retrieve all journal entries.
    """
    with open(JOURNAL_FILE, 'r') as f:
        return json.load(f)

def add_journal_entry(entry):
    """
    Add a new journal entry.
    If 'timestamp' is not provided, it adds the current time.
    """
    if "timestamp" not in entry:
        entry["timestamp"] = int(time.time())
    entries = get_journal_entries()
    entries.append(entry)
    with open(JOURNAL_FILE, 'w') as f:
        json.dump(entries, f)
    return entry
