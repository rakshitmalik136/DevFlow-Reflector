import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from git_parser import parse_git_logs
from analytics import analyze_data
from db_manager import init_db, get_journal_entries, add_journal_entry

class TestGitParser(unittest.TestCase):
    def test_parse_git_logs(self):
        # Check that we get a list or an error dictionary
        commits = parse_git_logs('.')
        self.assertTrue(isinstance(commits, list) or "error" in commits)

class TestAnalytics(unittest.TestCase):
    def test_analyze_data(self):
        sample_commits = [{
            "hexsha": "dummy",
            "message": "Test commit",
            "author": "Tester",
            "authored_date": 1609459200  # 2021-01-01
        }, {
            "hexsha": "dummy2",
            "message": "Another commit",
            "author": "Tester",
            "authored_date": 1609545600  # 2021-01-02
        }]
        analytics = analyze_data(sample_commits)
        self.assertEqual(analytics["total_commits"], 2)
        self.assertTrue("average_time_between_commits" in analytics)
        self.assertTrue("commit_frequency" in analytics)
        # Verify commit frequency includes both dates
        self.assertIn("2021-01-01", analytics["commit_frequency"])
        self.assertIn("2021-01-02", analytics["commit_frequency"])

class TestDBManager(unittest.TestCase):
    def test_journal_entries(self):
        init_db()
        initial_entries = get_journal_entries()
        entry = {"text": "Test journal entry"}
        add_journal_entry(entry)
        updated_entries = get_journal_entries()
        self.assertEqual(len(updated_entries), len(initial_entries) + 1)

if __name__ == '__main__':
    unittest.main()
