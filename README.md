# Python Network System Manager

A Python-based database application for managing network devices, networks, and connections using Oracle Database, with NetworkX and Matplotlib for network visualization.

## Project Overview

This project is a command-line application developed in Python and connected to an Oracle Database.
It provides a simple system for storing and managing network-related information, including devices, device types, networks, and connections. The application also includes a graphical visualization feature that represents device connections within a selected network.
## Key Features

* Add network devices
* View registered devices and their information
* Delete devices
* Add network connections 
* View network connections
* Add networks
* View networks
* Select a network and visualize its device connections
* Store and retrieve data using Oracle Database
* Display network relationships using NetworkX and Matplotlib

## Technologies Used
* Python
* Oracle Database
* SQL
* Python-oracledb
* NetworkX
* Matplotlib
* python-dotenv
* Git & GitHub

## Database

The database contains entities for managing:

* Devices
* Device Types
* Networks
* Connections

The database structure and table creation scripts are available in:

`sql/database.sql`

## Data Management

The application communicates with the Oracle Database through Python using the oracledb library.
Users can perform database operations directly through the application's command-line menu, including adding, viewing, and deleting records.

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
```
**Python Network Visualization**

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

Tala Al-Shahri
