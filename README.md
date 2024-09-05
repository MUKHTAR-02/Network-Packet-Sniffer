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

- Works well on various network interfaces.
- Ensure you have the necessary permissions to capture network packets on your machine.

### Prerequisites

- Python 3.x
- Flask
- Scapy
- SQLite

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/packet-sniffer-web-app.git
   ```
   ```bash
   cd packet-sniffer-web-app
   ```
   
