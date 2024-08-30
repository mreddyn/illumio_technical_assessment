# illumio_technical_assessment

## Project Overview

This project contains a Python program that parses flow log data from a file and maps each row to a tag based on a lookup table defined in a CSV file. It generates two outputs: the count of matches for each tag and the count of matches for each port/protocol combination. The program handles the flow log format version 2 only and ensures that the matches are case-insensitive.

## Assumptions

1. The log file (flow_logs.txt) and the lookup table (lookup_table.csv) must be in the same directory as the script.
2. The log file format assumes entries are space-separated and contain all expected fields.
3. The protocol in the lookup table is assumed to be either tcp, udp, or icmp.

## Requirements

Ensure that Python 3.x is installed


## Instructions to run

1. Clone the project


## Input format



## Output format