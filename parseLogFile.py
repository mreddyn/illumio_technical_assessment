import csv
from collections import defaultdict

def read_lookup_table(lookup_file):
    """
    Reads the lookup table CSV file and returns a dictionary with (dstport, protocol) as keys and tag as value.
    """
    lookup_table = {}
    try:
        with open(lookup_file, mode='r', newline='', encoding='ascii') as file:
            reader = csv.reader(file)
            next(reader)
            for dstport, protocol, tag in reader:
                key = (dstport.strip(), protocol.lower().strip())
                lookup_table[key] = tag.strip()
    except Exception as e:
        print(f"Error reading lookup file: {e}")
    print(lookup_table)
    return lookup_table

def parse_flow_logs(flow_log_file, lookup_table):
    """
    Parses the flow log file and maps each flow log entry to a tag using the lookup table.
    Generates counts for each tag and port/protocol combination.
    """
    tag_counts = defaultdict(int)
    port_protocol_counts = defaultdict(int)
    untagged_count = 0

    try:
        with open(flow_log_file, mode='r', newline='', encoding='ascii') as file:
            for line in file:
                parts = line.strip().split()
                
                # Process only if the log format is version 2
                if parts[0] == '2':
                    # Extract necessary fields
                    dstport = parts[5]  # Destination port
                    protocol = parts[7]  # Protocol (as number)
                    
                    # Convert protocol number to string ('tcp', 'udp', etc.)
                    protocol_str = protocol_to_string(protocol)
                    
                    protocol_key = protocol_str.lower()
                    port_protocol_counts[(dstport, protocol_str)] += 1
                    # Check for tag in the lookup table
                    tag = lookup_table.get((dstport, protocol_key))
                    if tag:
                        tag_counts[tag] += 1
                    else:
                        untagged_count += 1
                    

    except Exception as e:
        print(f"Error reading flow log file: {e}")

    return tag_counts, port_protocol_counts, untagged_count

def protocol_to_string(protocol_num):
    """
    Converts protocol number to string. Currently supports TCP and UDP only.
    """
    if protocol_num == '6':
        return 'tcp'
    elif protocol_num == '17':
        return 'udp'
    elif protocol_num == '1':
        return 'icmp'
    else:
        return 'unknown'

def write_output(tag_counts, port_protocol_counts, untagged_count, output_filename):
    """
    Writes the output files with tag counts and port/protocol combination counts.
    """
    # Writing Tag Counts
    with open(output_filename, mode='w', newline='', encoding='ascii') as file:
        writer = csv.writer(file)
        writer.writerow(['Tag Counts:'])
        writer.writerow(['Tag', 'Count'])
        for tag, count in tag_counts.items():
            writer.writerow([tag, count])
            
    # Writing untagged counts
        writer.writerow(['Untagged', untagged_count])
        writer.writerow([])

    # Writing Port/Protocol Combination Counts
        writer.writerow(['Protocol Combination Counts:'])
        writer.writerow(['Port', 'Protocol', 'Count'])
        for (port, protocol), count in port_protocol_counts.items():
            writer.writerow([port, protocol, count])

def main():
    # Define input files
    lookup_file = 'lookup_table.csv'
    flow_log_file = 'flow_logs.txt'
    
    # Define output file
    output_file_name = 'output_counts.csv'

    # Read lookup table
    lookup_table = read_lookup_table(lookup_file)

    # Parse flow logs and generate counts
    tag_counts, port_protocol_counts,  untagged_count = parse_flow_logs(flow_log_file, lookup_table)

    # Write output files
    write_output(tag_counts, port_protocol_counts, untagged_count, output_file_name)

if __name__ == "__main__":
    main()
