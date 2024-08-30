# illumio_technical_assessment

## Project Overview

This project contains a Python program that parses flow log data from a file and maps each row to a tag based on a lookup table defined in a CSV file. It generates two outputs: the count of matches for each tag and the count of matches for each port/protocol combination. The program handles the flow log format version 2 only and ensures that the matches are case-insensitive.

## Assumptions

1. The log file (flow_logs.txt) and the lookup table (lookup_table.csv) must be in the same directory as the script.
2. The log file format assumes entries are space-separated and contain all expected fields.
3. The protocol in the lookup table is assumed to be either tcp, udp, or icmp.
4. The input files should have the following names and format (flow_logs.txt, and lookup_table.csv)

## Requirements

1. Ensure that Python 3.x is installed


## Instructions to run

1. Clone the project `git clone https://github.com/mreddyn/illumio_technical_assessment.git`
2. Go to the root directory and run the command `python3 parseLogFile.py`
3. Output is generated in the file output_counts.csv

## Input format

```
flow_logs.txt
2 123456789012 eni-0a1b2c3d 10.0.1.201 198.51.100.2 443 49153 6 25 20000 1620140761 1620140821 ACCEPT OK
2 123456789012 eni-4d3c2b1a 192.168.1.100 203.0.113.101 23 49154 6 15 12000 1620140761 1620140821 REJECT OK
2 123456789012 eni-5e6f7g8h 192.168.1.101 198.51.100.3 25 49155 6 10 8000 1620140761 1620140821 ACCEPT OK
2 123456789012 eni-9h8g7f6e 172.16.0.100 203.0.113.102 110 49156 6 12 9000 1620140761 1620140821 ACCEPT OK
2 123456789012 eni-7i8j9k0l 172.16.0.101 192.0.2.203 993 49157 6 8 5000 1620140761 1620140821 ACCEPT OK
2 123456789012 eni-6m7n8o9p 10.0.2.200 198.51.100.4 143 49158 6 18 14000 1620140761 1620140821 ACCEPT OK
```

```
lookup_table.csv
dstport,protocol,tag
25,tcp,sv_P1
68,udp,sv_P2
23,tcp,sv_P1
31,udp,SV_P3
443,tcp,sv_P2
22,tcp,sv_P4
3389,tcp,sv_P5
0,icmp,sv_P5
110,tcp,email
993,tcp,email
143,tcp,email
```

## Output format

```
Tag Counts:
Tag,Count
sv_P2,1
sv_P1,2
email,3
Untagged,8

Protocol Combination Counts:
Port,Protocol,Count
443,tcp,1
23,tcp,1
25,tcp,1
110,tcp,1
993,tcp,1
143,tcp,1
1024,tcp,1
80,tcp,1
1030,tcp,1
56000,tcp,1
49321,tcp,1
49152,tcp,1
49153,tcp,1
49154,tcp,1
```
