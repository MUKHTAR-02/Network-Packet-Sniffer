# Network Packet Sniffer Web Application
No need to worry about monitoring network traffic, the Network Packet Sniffer Web Application is here! With this tool, you can easily capture and analyze network packets, view real-time data, and access packet information through a simple web interface and a RESTful API. 🌐📊

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Recommended](#recommended)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Example](#example)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The **Network Packet Sniffer Web Application** is designed to capture and display network packets in real-time. Utilizing Flask for the web interface and Scapy for packet sniffing, this application provides a user-friendly way to monitor network traffic and access packet data through a RESTful API.

## Features

- **Real-time Packet Capture**: Sniffs network packets and stores them in a SQLite database.
- **Web Interface**: Allows users to start sniffing, configure packet capture, and view packet data.
- **API Access**: Provides a RESTful API endpoint to retrieve packet data in JSON format.

## Getting Started

Follow these instructions to get the Network Packet Sniffer Web Application up and running on your local machine.

### Recommended
- Ensure you have the necessary permissions to capture network packets on your machine.

### Prerequisites

- Python 3.x
- Flask
- Scapy
- SQLite

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/MUKHTAR-02/Network-Packet-Sniffer
   cd packet-sniffer-web-app

2. Install the required dependencies:
      ```bash
   pip install -r requirements.txt

3. The SQLite database will be automatically created when you run the application for the first time.

## Usage

1. Start the Flask application:
   ```bash
   python app.py

2. Open your web browser and navigate to http://localhost:5500.

3. Use the web interface to start packet sniffing by specifying the number of packets and filter type, then view the captured packet data in the table.

4. Access the packet data via the API at http://localhost:5500/api/packets.
      
## Example

1. Start the application:
   ```bash
   python app.py

2. Fetch packet data via API:
   ```bash
   curl http://localhost:5500/api/packets

   
3. Example JSON Response:
   ```bash
   [
    {
        "id": 1,
        "timestamp": "2024-09-05T12:34:56",
        "ip_src": "192.168.1.1",
        "ip_dst": "192.168.1.2",
        "tcp_sport": 12345,
        "tcp_dport": 80,
        "payload": "GET / HTTP/1.1\r\n..."
    }
   ]

## Contribution

- If you would like to contribute to this project, feel free to open an issue or submit a pull request we need more coders like you. Welcome!

## License

- This project is licensed under the <a href = "LICENSE"> MIT License</a>
- Feel free to suggest about more features and improvements.
