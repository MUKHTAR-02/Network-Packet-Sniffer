# Download some dependencies 
# pip install Flask
# pip install Flask-SQLAlchemy
# pip install SQLAlchemy

# Run the commands:
# 1- To sniff 5 data packets
# python packet_sniffer.py --count 5 

# 2- To sniff data packets of HTTP type
# python packet_sniffer.py --filter "tcp port 80"

# for accessing the data from sqlite3
# sqlite3 packets.db 
# SELECT * FROM packets;