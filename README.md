# Network System Manager

A Python-based network device management system connected to an Oracle Database.

The project allows users to manage network devices, connections, and networks through a simple command-line interface. It also provides a graphical visualization of network connections using NetworkX and Matplotlib.

## Features

*-Add network devices
*-View registered devices
*-Delete devices
*-Add network connections
*-View network connections
*-Add networks
*-View networks
*-Display a graphical representation of a selected network
*-Store and retrieve data using Oracle Database

## Technologies Used
*-Python
*-Oracle Database
*-SQL
*-Python
*-oracledb
*-NetworkX
*-Matplotlib
*-python-dotenv
*-Git & GitHub

## Database

The database contains entities for managing:

*-Devices
*-Device Types
*-Networks
*-Connections
*-Ping Logs

The database structure and table creation scripts are available in:

`sql/database.sql`

## Project Structure
```text
NetworkSystemManager/
│
├── NetworkSystemManagerrrr.py
├── NetworkSystemManager.sln
├── NetworkSystemManager.pyproj
├── requirements.txt
├── .gitignore
│
├── sql/
│   └── database.sql
│
└── screenshots/

**Network Visualization**

The project uses NetworkX and Matplotlib to visualize the connections between devices in a selected network.

The graph represents devices as nodes and their connections as edges.

**Security** 

Database credentials are stored in a .env file and are excluded from GitHub using .gitignore.

The .env file is not included in this repository.

**Installation** 

Clone the repository:

git clone https://github.com/newtala83-design/NetworkSystemManager.git

Install the required Python packages:

pip install -r requirements.txt

Configure the .env file with your Oracle Database connection information.

Then run: 
python NetworkSystemManagerrrr.py

**Author**

Tala Saad Al-Shahri
