import oracledb
import os
from dotenv import load_dotenv
import networkx as nx
import matplotlib.pyplot as plt

load_dotenv()

connection = oracledb.connect(
    user=os.getenv("ORACLE_USER"),
    password=os.getenv("ORACLE_PASSWORD"),
    dsn=os.getenv("ORACLE_DSN")
)
cursor = connection.cursor()


print("Successfully connected to Oracle Database")

while True:
    print("\n===== Network Device Manager =====")
    print("1. Add Device")
    print("2. View Devices")
    print("3. Delete Device")
    print("4. Add Connection")
    print("5. View Connections")
    print("6. Add Network")
    print("7. View Networks")
    print("8. show Network graph")
    print("9. Exit")

    choice = input("Choose an option: ").strip()

    # 1. Add Device
    if choice == "1":
        print("\n--- Add Device ---")
        name = input("Device name: ")
        ip_address = input("IP address: ")
        mac_address = input("MAC address: ")
        status = input("Status: ")

        print("\nAvailable Device Types:")
        cursor.execute(
            """
            SELECT Type_ID, Type_Name
            FROM Device_Type
            ORDER BY Type_ID
        """
        )
        device_types = cursor.fetchall()

        for type_id, type_name in device_types:
            print(f"{type_id}. {type_name}")

        type_id = input("Choose Device Type ID: ")

        cursor.execute(
            """
            INSERT INTO Device
            (Name, IP_Address, MAC_Address, Status, Type_ID)
            VALUES (:1, :2, :3, :4, :5)
        """,
            (name, ip_address, mac_address, status, type_id),
        )

        connection.commit()
        print("Device added successfully!")

    # 2. View Devices
    elif choice == "2":
        print("\n--- Devices ---")
        cursor.execute(
            """
            SELECT
                d.Device_ID,
                d.Name,
                d.IP_Address,
                d.MAC_Address,
                d.Status,
                dt.Type_Name
            FROM Device d
            LEFT JOIN Device_Type dt
                ON d.Type_ID = dt.Type_ID
            ORDER BY d.Device_ID
        """
        )
        devices = cursor.fetchall()

        if not devices:
            print("No devices found.")
        else:
            for device in devices:
                print(
                    f"ID: {device[0]} | "
                    f"Name: {device[1]} | "
                    f"IP: {device[2]} | "
                    f"MAC: {device[3]} | "
                    f"Status: {device[4]} | "
                    f"Type: {device[5]}"
                )

    # 3. Delete Device
    elif choice == "3":
        print("\n--- Delete Device ---")
        device_id = input("Enter Device ID: ")

        cursor.execute(
            """
            DELETE FROM Device
            WHERE Device_ID = :1
        """,
            (device_id,),
        )

        connection.commit()

        if cursor.rowcount > 0:
            print("Device deleted successfully!")
        else:
            print("Device not found.")

    # 4. Add Connection
    elif choice == "4":
        print("\n--- Add Connection ---")

        print("\nAvailable Networks:")
        cursor.execute(
            """
            SELECT Network_ID, Network_Name
            FROM Network
            ORDER BY Network_ID
        """
        )
        networks = cursor.fetchall()

        if not networks:
            print("No networks found. Please add a network first.")
            continue

        for network_id, network_name in networks:
            print(f"{network_id}. {network_name}")

        network_id = input("Choose Network ID: ")
        source_device_id = input("Source Device ID: ")
        destination_device_id = input("Destination Device ID: ")
        connection_type = input("Connection Type: ")

        cursor.execute(
            """
            INSERT INTO Connection
            (Source_Device_ID,
             Destination_Device_ID,
             Connection_Type,
             Network_ID)
            VALUES (:1, :2, :3, :4)
        """,
            (source_device_id, destination_device_id, connection_type, network_id),
        )

        connection.commit()
        print("Connection added successfully!")

    # 5. View Connections
    elif choice == "5":
        print("\n--- Connections ---")
        cursor.execute(
            """
            SELECT
                c.Connection_ID,
                n.Network_Name,
                s.Name AS Source_Device,
                d.Name AS Destination_Device,
                c.Connection_Type
            FROM Connection c
            JOIN Device s
                ON c.Source_Device_ID = s.Device_ID
            JOIN Device d
                ON c.Destination_Device_ID = d.Device_ID
            JOIN Network n
                ON c.Network_ID = n.Network_ID
            ORDER BY c.Connection_ID
        """
        )
        connections = cursor.fetchall()

        if not connections:
            print("No connections found.")
        else:
            for conn in connections:
                print(
                    f"Connection ID: {conn[0]} | "
                    f"Network: {conn[1]} | "
                    f"From: {conn[2]} | "
                    f"To: {conn[3]} | "
                    f"Type: {conn[4]}"
                )

    # 8. Add Network
    elif choice == "6":
        print("\n--- Add Network ---")
        network_name = input("Network name: ")

        cursor.execute(
            """
            INSERT INTO Network (Network_Name)
            VALUES (:1)
        """,
            (network_name,),
        )

        connection.commit()
        print("Network added successfully!")

        # 9. View Networks
    elif choice == "7":
        print("\n--- Networks ---")
        cursor.execute(
            """
                SELECT Network_ID, Network_Name
                FROM Network
                ORDER BY Network_ID
            """
        )
        networks = cursor.fetchall()

        if not networks:
            print("No networks found.")
        else:
            for network in networks:
                print(f"Network ID: {network[0]} | " f"Name: {network[1]}")

            # 8. Show Network Graph
    elif choice == "8":
        print("\n--- Show Network Graph ---")

        # Show available networks
        cursor.execute(
            """
                SELECT Network_ID, Network_Name
                FROM Network
                ORDER BY Network_ID
            """
        )

        networks = cursor.fetchall()

        if not networks:
            print("No networks found.")
            continue

        for network_id, network_name in networks:
            print(f"{network_id}. {network_name}")

        network_id = input("Choose Network ID: ")

        # Get connections for selected network
        cursor.execute(
            """
                SELECT
                    c.Source_Device_ID,
                    c.Destination_Device_ID
                FROM Connection c
                WHERE c.Network_ID = :1
            """,
            (network_id,),
        )

        connections = cursor.fetchall()

        if not connections:
            print("No connections found for this network.")
            continue

        # Create Graph
        G = nx.Graph()

        # Add connections
        for source_id, destination_id in connections:
            G.add_edge(source_id, destination_id)

        # Get device names
        cursor.execute(
            """
                SELECT Device_ID, Name
                FROM Device
            """
        )

        devices = cursor.fetchall()

        device_names = {}

        for device_id, name in devices:
            device_names[device_id] = name

        # Draw Graph
        plt.figure(figsize=(10, 7))

        pos = nx.spring_layout(G, seed=42)

        nx.draw(
            G,
            pos,
            labels={
                device_id: device_names.get(device_id, str(device_id))
                for device_id in G.nodes
            },
            with_labels=True,
            node_size=2500,
            font_size=10,
        )

        plt.title(f"Network Graph - {network_id}")
        plt.show()

    # 10. Exit
    elif choice == "9":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please choose 1-10.")

        X
cursor.close()
connection.close()
