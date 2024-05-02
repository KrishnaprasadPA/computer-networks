def is_symmetric(ip1, ip2):
    ip1_parts = ip1.split('.')
    ip2_parts = ip2.split('.')

    # Compare the first three octets
    if ip1_parts[:3] != ip2_parts[:3]:
        return False

    # Check if the last octets differ by 1
    return abs(int(ip1_parts[3]) - int(ip2_parts[3])) == 1


def process_file(input_file, output_file):
    with open(input_file, 'r') as f:
        lines = f.read().strip().split('\n\n')  # Split by empty lines

    with open(output_file, 'w') as f:
        for i in range(0, len(lines) - 1, 2):  # Loop until the second to last line
            ips = lines[i].strip().split('\n')  # Split by newline
            source_name = ips[0].split()[0]  # Extract source node name
            destination_name = lines[i + 1].strip().split()[0]  # Extract destination node name
            
            asymmetric = False
            source_ips = ips[1:]  # Remove the first IP address (node name)
            destination_ips = lines[i + 1].strip().split('\n')[1:]  # Remove the first IP address
            k = 0
            for j in range(len(source_ips)):
                if not is_symmetric(source_ips[j], destination_ips[-(j + 1)]):
                    asymmetric = True
                    k += 2
            
            if asymmetric:
                f.write(f"{source_name} and {destination_name} {k} {2*len(source_ips)-2}\n")

# Process each input file and write to corresponding asymmetry file
for i in range(1, 11):
    input_file = f"traceroute/processed_traceroute/processed_traceroute_{i}.txt"
    output_file = f"asymmetric_nodes/asymmetry_{i}.txt"
    process_file(input_file, output_file)