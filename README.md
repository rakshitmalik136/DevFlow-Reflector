# DevFlow Reflector

DevFlow Reflector is an interactive tool that merges Git history visualization with a personal productivity journal. It parses your local Git logs to generate dynamic graphs of your commit history and branch evolution while allowing you to attach journal entries to your commits or work sessions. This MVP is designed as a standalone web application, with a roadmap to transform it into an extension (e.g., for VS Code or GitHub or others) in the future.

---

## 🚀 Overview

- **Interactive Git Visualizations:** Automatically generate graphs and dashboards to display commit trends, branch activity, and key contribution metrics.
- **Productivity Journaling:** Add personal notes or reflections linked to specific commits or time periods, creating a historical record of insights, challenges, and improvements.
- **Local Data Handling:** All processing is done locally by parsing Git logs and storing data (using SQLite or JSON files), ensuring privacy and compliance with FOSS principles.
- **Extension-Ready Architecture:** The MVP is built modularly so that the core functionality can later be integrated as an extension for VS Code, GitHub, or others.

---

## 🛠️ Key Features

1. **GitFlow Visualization**
   - Parse local Git logs to extract commit data (timestamps, messages, branches).
   - Display interactive graphs showing commit frequency, branch merges, and overall repository evolution.
   - Provide a metrics dashboard with insights (average time between commits, commit streaks, etc.).

2. **Productivity Tracking & Journaling**
   - Allow users to create journal entries linked to specific commits or time ranges.
   - Generate daily/weekly overviews correlating commit activity with reflective notes.
   - Support local storage of journal data for privacy and offline usage.

3. **Modular & Extension-Ready**
   - It is a standalone web application for the Now.
   - Designed with a modular codebase, making it easier to refactor as a VS Code or GitHub extension or any other code-editors extension later.
   - Uses webviews/components that can be repurposed for in-editor interfaces.

---

## 📂 Codebase Directory Structure

Below is a suggested directory structure for the MVP. This structure separates backend and frontend code while anticipating future integration into an extension framework.

```
devflow-reflector/
│
├── backend/
│   ├── main.py             # Entry point for the API server (Flask/FastAPI)
│   ├── git_parser.py       # Module to parse local Git logs
│   ├── db_manager.py       # Handles local data storage (SQLite/JSON)
│   ├── analytics.py        # Processes commit data to generate insights
│   ├── requirements.txt    # Python dependencies
│   └── tests/              # Backend unit and integration tests
│
├── frontend/
│   ├── public/
│   │   ├── index.html      # HTML template for the web application
│   │   └── assets/         # Static assets (images, icons, CSS)
│   │
│   ├── src/
│   │   ├── components/     # React components (charts, journal entry forms, dashboards)
│   │   ├── pages/          # Main app pages (Dashboard, Journal, Settings)
│   │   ├── App.js          # Root React component
│   │   ├── index.js        # Entry point for the React app
│   │   └── api.js          # Handles API calls to the backend
│   │
│   ├── package.json        # Frontend dependencies and scripts
│   └── README.md           # Frontend-specific documentation (if needed)
│
├── extension/              # (Optional) Future VS Code/GitHub extension code
│   ├── manifest.json       # Extension manifest file
│   ├── extension.js        # Main extension logic (to be developed)
│   └── webview/            # Reusable webview components for extension integration
│
├── docs/                   # Additional documentation, design docs, and user guides
│   └── architecture.md     # Architecture and roadmap documentation
│
├── .gitignore              # Files and directories to ignore in Git
├── LICENSE                 # Project license (e.g., MIT)
└── setup.sh                # Quick setup script to install dependencies and run the project
```

---

## 📥 Installation & Setup

### **Prerequisites**
- **Backend:** Python 3.8+ (with pip)
- **Frontend:** Node.js 16+ and npm
- **Git:** Ensure Git is installed and available in your PATH

### **Steps**

1. **Clone the Repository**
   ```sh
   git clone https://github.com/yourusername/devflow-reflector.git
   cd devflow-reflector
   ```

2. **Setup the Backend**
   ```sh
   cd backend
   pip install -r requirements.txt
   python main.py
   ```
   This starts the API server that handles Git parsing and data analytics.

3. **Setup the Frontend**
   ```sh
   cd ../frontend
   npm install
   npm start
   ```
   The frontend will launch in your browser, connecting to the backend API.

4. **(Optional) Explore Extension Code**
   The `extension/` directory contains a placeholder for future VS Code or GitHub extension integration. This is where you’d adapt webview components and integrate with extension APIs.

---

## 🚀 Usage

1. **Run the Application:**
   - Start both the backend and frontend as described above.
   - Open your browser to view the dashboard.

2. **Link a Local Git Repository:**
   - Configure the application to point to your local Git repository (this may involve editing a configuration file or using a command-line argument).

3. **Visualize & Journal:**
   - Explore the interactive Git visualizations.
   - Create journal entries linked to specific commits or time ranges.
   - Use the dashboard to review insights and track your productivity over time.

4. **Plan for Future Extension:**
   - Review the `extension/` directory to understand how the MVP can later be packaged as an extension for VS Code or GitHub.

---

## 📜 License

This project is licensed under the **Apache2.0 License**. See the [LICENSE](./LICENSE) file for details.

---

## 👨‍💻 Contributing

Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a feature branch (`feature/your-feature-name`).
3. Commit your changes with clear messages.
4. Open a pull request detailing your changes.

For major changes, please open an issue first to discuss what you would like to change.

---

## 📧 Contact

For questions or suggestions, please open an issue in the repository.

---

*DevFlow Reflector aims to make your development journey more insightful and productive by bridging raw commit data with reflective journaling. Enjoy using and contributing to the project!*
