import socket
import struct

def send_packet(ip_address, port, packet_data, count):
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        for _ in range(count):
            # Pack the packet data as 16-bit unsigned short
            packet = struct.pack('!H', packet_data)

            # Send the packet
            sock.sendto(packet, (ip_address, port))
            print("Packet sent successfully.")
    except socket.error as e:
        print("Failed to send packet:", e)
    finally:
        # Close the socket
        sock.close()

# Example usage
ip_address = 'IP'  # Replace with the destination IP address
port = 80  # Replace with the destination port
packet_data = 1234  # Replace with the 16-bit packet data
packet_count = 30000000

send_packet(ip_address, port, packet_data, packet_count)
