from datetime import datetime

def analyze_data(commits):
    """
    Analyze commit data and return useful metrics.
    
    Expected commit format:
      {
         "hexsha": str,
         "message": str,
         "author": str,
         "authored_date": int (Unix timestamp)
      }
    
    Returns a dictionary containing:
      - total_commits: int
      - average_time_between_commits: float (in seconds)
      - commit_frequency: dict mapping date (YYYY-MM-DD) to count
    """
    if not commits or not isinstance(commits, list):
        return {"total_commits": 0}

    total_commits = len(commits)
    
    # Sort commits by authored_date (oldest first)
    sorted_commits = sorted(commits, key=lambda c: c['authored_date'])
    
    # Calculate differences between consecutive commits
    diffs = []
    for i in range(1, len(sorted_commits)):
        diff = sorted_commits[i]['authored_date'] - sorted_commits[i-1]['authored_date']
        diffs.append(diff)
    average_diff = sum(diffs)/len(diffs) if diffs else 0
    
    # Calculate commit frequency per day
    frequency = {}
    for commit in commits:
        date_str = datetime.fromtimestamp(commit['authored_date']).strftime("%Y-%m-%d")
        frequency[date_str] = frequency.get(date_str, 0) + 1

    return {
        "total_commits": total_commits,
        "average_time_between_commits": average_diff,
        "commit_frequency": frequency
    }
