# DevFlow Reflector

DevFlow Reflector is a developer productivity tool that combines dynamic visualization of your git repository history with a personal productivity journal. It transforms raw git logs into interactive visualizations and correlates them with developer reflections, enabling you to gain actionable insights into your workflow, track progress over time, and identify areas for improvement.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Demo](#demo)
- [Codebase Structure](#codebase-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License & Dual Licensing Terms](#license--dual-licensing-terms)
- [Contact](#contact)

## Overview

Traditional git logs provide a wealth of raw data about commit history, but they can be overwhelming and lack context. DevFlow Reflector goes further by:
- **Visualizing your Git History:** Interactive graphs and charts show commit trends, branch activity, and key milestones.
- **Integrating a Productivity Journal:** Attach notes or reflections to specific commits or time periods, adding context to your coding activity.
- **Correlating Data & Reflections:** Identify patterns (e.g., how productivity relates to work habits) through combined analytics.

This holistic view helps developers, teams, and project managers understand not only what was done, but also why it happened and how to improve future workflows.

## Features

- **GitFlow Visualization:**
  - Parse local git logs to extract commit metadata.
  - Display commit frequency, branch merges, and timelines using interactive charts.
  - Highlight key commits with additional contextual notes.

- **Productivity Journal:**
  - Create, edit, and attach journal entries to specific commits or date ranges.
  - View daily/weekly summaries that combine commit statistics with personal insights.
  - Export or archive journal data for retrospectives.

- **Local Data Handling:**
  - All data is processed locally using in‑house logic and stored in local files (JSON/SQLite) to remain independent of external APIs.
  - Provides a self‑hosted solution that emphasizes privacy and full control over your data.

- **Extensibility & Customization:**
  - Modular architecture makes it easy to add new visualization components or analytics modules.
  - Designed as a FOSS project to foster community contributions and further innovation.

## Demo

*Include screenshots or a link to a demo video here.*

## Codebase Structure

Below is a suggested codebase structure:

```
/DevFlowReflector
├── /src
│   ├── /components
│   │   ├── GitVisualizer.js        # Component for interactive git history visualization
│   │   ├── ProductivityDashboard.js # UI for displaying productivity analytics and journal entries
│   │   └── JournalEntryForm.js      # Form for adding/editing journal entries
│   │
│   ├── /services
│   │   ├── GitParser.js             # Module to parse local git logs and extract metadata
│   │   └── JournalManager.js        # Module to handle CRUD operations for journal entries
│   │
│   ├── /assets
│   │   └── styles.css               # Custom styles for the application
│   │
│   ├── app.js                     # Main application entry point
│   └── index.html                 # HTML file to load the application
│
├── /docs
│   ├── README.md                  # This README file
│   └── LICENSE.md                 # License file (see below)
│
├── /tests
│   ├── testGitParser.js           # Unit tests for GitParser module
│   └── testJournalManager.js      # Unit tests for JournalManager module
│
├── package.json                   # Project metadata and dependencies (if using Node.js)
└── .gitignore                     # Files and directories to ignore in git
```

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/DevFlowReflector.git
   cd DevFlowReflector
   ```

2. **Install dependencies:**

   If using Node.js (or similar):

   ```bash
   npm install
   ```

3. **Build/Run the Application:**

   For a web‑based version, open `index.html` in your browser or run a local web server:

   ```bash
   npm start
   ```

## Usage

- **Visualizing Git History:**  
  Run the GitParser to load your repository’s commit data. The GitVisualizer component will render interactive graphs.
  
- **Using the Journal:**  
  Add new journal entries via the JournalEntryForm. Link entries to specific commits or date ranges for contextual insights.

- **Analyzing Productivity:**  
  View the ProductivityDashboard for daily and weekly summaries that correlate your commit data with your journal entries.

## Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](docs/CONTRIBUTING.md) for guidelines on how to report issues, suggest features, or submit pull requests.

## License & Dual Licensing Terms

DevFlow Reflector is provided as open source for non-commercial use under the [Business Source License (BSL) 1.1](https://mariadb.com/bsl-faq-adopting-the-business-source-license/) (or a similar source‑available license of your choice). **For any commercial use—including products or services whose value is derived substantially from the functionality of DevFlow Reflector—a separate commercial license is required, which includes royalty payments.**

### In summary:
- **Non-Commercial Use:** Free to use, modify, and distribute under the BSL for personal and academic purposes.
- **Commercial Use:** If you plan to commercialize DevFlow Reflector or its derivatives, please contact [your-email@example.com] for licensing terms and royalty arrangements.

*Please refer to the full license text in [LICENSE.md](docs/LICENSE.md) for detailed terms.*

## Contact

For questions, support, or licensing inquiries, please contact:
- **Name:** [Your Name]
- **Email:** [your-email@example.com]
- **GitHub:** [https://github.com/yourusername]

---

*Thank you for checking out DevFlow Reflector! We look forward to your feedback and contributions.*
