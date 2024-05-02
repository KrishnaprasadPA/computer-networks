# Project for Advanced Computer Networks

## Overview

This repository contains files and scripts related to the Advanced Computer Networks (ACN) project. The project focuses on analyzing network asymmetry using traceroute data.

## Directories

1. **asymmetric_nodes**: Contains files related to identifying asymmetric nodes in the network.

2. **deliverables**: Includes the final report and presentation slides for the ACN project.

3. **owl**: Contains files provided by the measurement-framework GitHub repository for analyzing OWL from pcap files.

4. **traceroute**: Includes raw traceroute data as well as processed traceroute generated during the analysis.

## Scripts

- **cleaner.py**: A Python script that takes `traceroute-i.txt` as input and provides a clean output `processed_traceroute_i.txt` in the `traceroute` directory.

- **findAsymmetry.py**: A Python script that analyzes processed traceroute data to identify sets of nodes that show asymmetry. The script outputs the asymmetric nodes, AA (asymmetry score), and total path length to a file in the `asymmetric_nodes` directory.

- **quantifyAsymmetry.py**: A Python script that takes asymmetry data files as input and generates an output with the results of asymmetric nodes, absolute asymmetry, and normalized asymmetry.

## Usage

To use the provided scripts:

1. Ensure that Python is installed on your system.
2. Process raw `traceroute_i.txt` by running `cleaner.py`
3. Run `findAsymmetry.py` to find asymmetric paths
4. Run `quantifyAsymmetry.py` to find absolute and normalized asymmetry

## Contributors

- Krishnaprasad Palamattam Aji
