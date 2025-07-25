import os
import argparse
import xml.etree.ElementTree as ET

unknown = 'N/A'

def parse_args():
    parser = argparse.ArgumentParser(
        description="Convert Nmap XML to Markdown",
        usage="python -m src.main -i <NMAP_FILE>.xml -o <OUTPUT_FILE>.md"
    )
    parser.add_argument("-i", "--input", help="Nmap scan result in XML format")
    parser.add_argument("-o", "--output",help="Output markdown file")
    return parser.parse_args()

class XMLParser:

    FILE_PATH = "./tests/data/nmap_sample.xml"

    def __init__(self, file_path=FILE_PATH):

        file_path = os.path.abspath(file_path)
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"File not found : {file_path}")
        
        self.file = file_path
        self.tree = ET.parse(file_path)
        self.root = self.tree.getroot()
        self.hosts = self.root.findall("host")

    def extract_nmap_data(self):

        print(f"Extracting nmap data from {os.path.abspath(self.file)}")
        
        result = []

        for host in self.hosts:
            ip = host.find("address").get("addr", unknown)

            hostname_elem = host.find('hostnames/hostname')
            hostname = hostname_elem.get('name' , "") if hostname_elem is not None else ""

            os_elem = host.find("os")
            os_name = ""
            os_accuracy = ""

            trace_elem = host.find("trace")
            trace_port = ""
            trace_protocol = ""

            hop_ttl = ""
            hop_rtt = ""
            hop_ip_addr = ""

            hops_info = []

            if os_elem is not None:
                os_match_elem = os_elem.find("osmatch")
                if os_match_elem is not None:
                    os_name = os_match_elem.get("name", "")
                    os_accuracy = os_match_elem.get("accuracy", "")

            if trace_elem is not None:
                trace_port = trace_elem.get("port", "")
                trace_protocol = trace_elem.get("proto", "")
                hop_elems = trace_elem.findall("hop")

                if hop_elems:
                    for elem in hop_elems:
                        if elem is not None:
                            hop_ttl = elem.get("ttl", "")
                            hop_rtt = elem.get("rtt", "")
                            hop_ip_addr = elem.get("ipaddr", "")
                            hops_info.append({
                                "ttl" : hop_ttl,
                                "rtt" : hop_rtt,
                                "ipaddr" : hop_ip_addr
                            })
                
            ports_info = []

            for port in host.findall("ports/port"):
                port_id = port.get("portid", unknown)
                protocol = port.get("protocol", "")

                state = ""
                service_name = ""
                service_version = ""
                service_product = ""
                full_version = ""
                service_extra_info = ""

                state_elem = port.find("state")
                service_elem = port.find("service")

                if protocol is not None:
                    state = state_elem.get("state", "N/A") if state_elem is not None else ""
                    if service_elem is not None:
                        service_name = service_elem.get("name" , "")
                        service_version = service_elem.get("version" , "")
                        service_product = service_elem.get("product" , "")
                        full_version = f"{service_product} {service_version}".strip()
                        service_extra_info = service_elem.get("extrainfo" , "")

                scripts = {script.get("id", "") : script.get("output", "") for script in port.findall("script")}

                ports_info.append({
                    "port" : int(port_id),
                    "protocol" : protocol,
                    "state" : state,
                    "service" : service_name,
                    "version" : full_version,
                    "extrainfo" : service_extra_info,
                    "scripts" : scripts if scripts else {}
                })

            result.append({
                "ip" : ip,
                "hostname" : hostname,
                "ports" : ports_info,
                "os_name" : os_name,
                "os_accuracy" : os_accuracy,
                "traceroute_port" : trace_port,
                "traceroute_protocol" : trace_protocol,
                "hops" : hops_info
            })
        
        return result