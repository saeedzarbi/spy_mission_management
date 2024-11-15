James Bond Spy Mission Management System
This project is a simple web application built with Flask that simulates a spy mission management system for managing spy missions, agents, and equipment.
Features
User Authentication with different roles:
M: Director of the organization
Q: Equipment specialist
Agent: Field agents
Analyst: Intelligence analysts
Role-Based Access Control (RBAC) to manage access to different sections based on user roles.
Mission Management: Add, view, and assign missions to agents.
Equipment Management: Add, view, and assign equipment to agents.

Prerequisites

    Python 3.6 or higher
    pip (Python package manager)

Installation and Setup
1. Clone the Repository

    git clone https://github.com/saeedzarbi/spy_mission_management.git
    cd spy-mission-management


2. Create and Activate a Virtual Environment
It's recommended to use a virtual environment to manage project dependencies.

On Windows:

    python -m venv venv
    venv\Scripts\activate

On macOS/Linux:

    python3 -m venv venv
    source venv/bin/activate

3. Install Dependencies
Install the required Python packages using pip:

    pip install -r requirements.txt

4. Initialize the Database
The application uses SQLite for data storage. Initialize the database by running the application once. This will create the spy_mission.db file and populate it with initial data.

    python app.py
After running the above command, you can stop the server by pressing Ctrl+C. The database is now set up with initial users, missions, and equipment.

6. Run the Application
Start the Flask development server:

    python app.py

The application will be accessible at http://localhost:5000.
