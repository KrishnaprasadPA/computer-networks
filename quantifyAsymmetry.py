from collections import defaultdict
import statistics

# Dictionary to store counts of node pairs
node_counts = defaultdict(int)
aa_value = defaultdict(list)
distance = defaultdict(list)

# Iterate over each asymmetry file
for i in range(1, 11):
    input_file = f"asymmetric_nodes/asymmetry_{i}.txt"
    
    # Read the asymmetry file
    with open(input_file, 'r') as f:
        lines = f.readlines()
    
    # Count occurrences of each node pair
    for line in lines:
        nodes = line.strip().split()[0:3]  # Extract node pair
        aa_value[tuple(nodes)].append(line.strip().split()[3])
        distance[tuple(nodes)].append(line.strip().split()[4])
        node_counts[tuple(nodes)] += 1

# Write lines to output file if occurrence average > 0.5
with open("output.txt", 'w') as f_out:
    for node_pair, count in node_counts.items():
        if count / 10 > 0.5:
            aa = statistics.mode(aa_value[node_pair])
            dist = statistics.mode(distance[node_pair])
            f_out.write(f"{node_pair[0]} and {node_pair[2]} {aa} {float (aa)/float (dist)} {dist}\n")
