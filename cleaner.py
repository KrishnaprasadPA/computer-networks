
def clean_traceroute(input_file, output_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    with open(output_file, 'w') as f:
        for i in range(len(lines)):
            if lines[i].startswith("Traceroute from"):
                f.write(lines[i].split("Traceroute from ")[1].rstrip() + "\n")
                i += 2
                while i < len(lines) and not lines[i].startswith("Traceroute from"):
                    if lines[i].strip():  # Check if the line is not empty
                        hop_info = lines[i].split()
                        if len(hop_info) > 1:  # Check if there are at least two items in the line
                            ip_address = hop_info[1]  # Use the second item as the IP address
                            if ip_address != "*":
                                f.write(ip_address + "\n")
                            else:
                                for j in range(1, len(hop_info)):
                                    if hop_info[j] != "*":
                                        ip_address = hop_info[j]
                                        f.write(ip_address + "\n")
                                        break
                    i += 1
                f.write("\n")

for i in range(1, 11):
    input_file = f"traceroute/raw_traceroute/traceroute-{i}.txt"
    output_file = f"traceroute/processed_traceroute/processed_traceroute_{i}.txt"
    clean_traceroute(input_file, output_file)