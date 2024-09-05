# Network Packet Sniffer Web Application

## Overview

The **Network Packet Sniffer Web Application** is a web-based tool for capturing and analyzing network packets in real-time. Built using Flask and Scapy, this application allows users to start packet sniffing, view captured data, and manage network traffic insights through a simple web interface.

## Features

- **Real-time Packet Capture**: Sniffs network packets and saves relevant information to a SQLite database.
- **Web Interface**: Provides an intuitive UI for starting the sniffing process and displaying captured packet data.
- **API Access**: Retrieve packet data in JSON format through a RESTful API endpoint.

## Prerequisites

Before running the application, ensure you have the following installed:

- Python 3.x
- Flask
- Scapy
- SQLite

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/packet-sniffer-web-app.git
   cd packet-sniffer-web-app
