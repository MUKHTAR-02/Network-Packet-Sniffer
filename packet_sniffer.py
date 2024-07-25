import sqlite3
from scapy.all import sniff, IP, TCP, Raw
import os

# Ensure the database file is in the same directory as the script
db_path = os.path.join(os.path.dirname(__file__), 'packets.db')

def create_db():
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS packets (
                     id INTEGER PRIMARY KEY AUTOINCREMENT,
                     timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                     ip_src TEXT,
                     ip_dst TEXT,
                     tcp_sport INTEGER,
                     tcp_dport INTEGER,
                     payload TEXT
                 )''')
    conn.close()

def packet_callback(packet):
    ip_src, ip_dst, tcp_sport, tcp_dport, payload = None, None, None, None, None

    if packet.haslayer(IP):
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst

    if packet.haslayer(TCP):
        tcp_sport = packet[TCP].sport
        tcp_dport = packet[TCP].dport

    if packet.haslayer(Raw):
        payload = packet[Raw].load.decode('utf-8', 'ignore')  # Decode payload if it's bytes

    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute('''INSERT INTO packets (ip_src, ip_dst, tcp_sport, tcp_dport, payload)
                 VALUES (?, ?, ?, ?, ?)''', (ip_src, ip_dst, tcp_sport, tcp_dport, payload))
    conn.commit()
    conn.close()

def start_sniffing(count, filter):
    sniff(prn=packet_callback, count=count, filter=filter)

# Ensure the database is created
create_db()
