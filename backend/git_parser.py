import git

def parse_git_logs(repo_path):
    """
    Parse the Git logs for the repository at 'repo_path'.
    Returns a list of dictionaries containing commit data.
    """
    try:
        repo = git.Repo(repo_path)
    except Exception as e:
        return {"error": str(e)}
    
    commits = []
    for commit in repo.iter_commits():
        commits.append({
            "hexsha": commit.hexsha,
            "message": commit.message.strip(),
            "author": commit.author.name,
            "authored_date": commit.authored_date,  # Unix timestamp
        })
    return commits
