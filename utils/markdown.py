import os

class MarkdownUtil:

    def __init__(self, output_file="./output.md"):
        self.output_file = output_file

    def format_nse_script_block(self, ports):
        block_lines = ["\n```bash"]

        for port in ports:
            scripts = port.get("scripts", {})

            if scripts:
                block_lines.append(f"Port {port.get('port')} :")    
                for script_name, output in scripts.items():
                    line = f"{script_name}:\n{output}\n"
                    block_lines.append(line)
        
        return block_lines

    def format_hops_block(self, traceroute_port, traceroute_protocol, hops):

        first_line = f"\nTRACEROUTE (using port {traceroute_port}/{traceroute_protocol})"
        second_line = f"{"HOP":<3} {"RTT":<10} {"ADDRESS":<20}"

        block_lines = [first_line, second_line]

        for hop in hops:
            ttl = hop.get("ttl", "")
            rtt = hop.get("rtt", "")
            ip = hop.get("ipaddr", "")

            print(f"TTL : {ttl}")
            print(f"RTT : {rtt}")
            print(f"IP : {ip}")

            if ttl and rtt and ip:
                block_lines.append(f"{ttl:<3} {rtt + ' ms':<10} {ip:<20}")    
        
        return block_lines
    
    def generate_markdown(self, nmap_data):
        
        lines = []

        for host in nmap_data:
            ip = host["ip"]
            hostname = host["hostname"]
            ports = host["ports"]

            lines.append(f"### Host : {ip} ({hostname})\n" if hostname else f"### Host : {ip}\n")
            lines.append("| Port/Protocol | State | Service | Version |")
            lines.append("|---------------|-------|---------|---------|")

            for port in ports:

                port_num = port.get("port")
                port_protocol = port.get("protocol")
                port_state = port.get("state")
                port_service = port.get("service")
                port_version = port.get("version")

                line = f"| {port_num}/{port_protocol} | {port_state} | {port_service} | {port_version}"
                lines.append(line)

            
            traceroute_port = host["traceroute_port"]
            traceroute_protocol = host["traceroute_protocol"]
            hops = host["hops"]

            hops_block_lines = self.format_hops_block(traceroute_port, traceroute_protocol, hops)

            nse_block_lines = self.format_nse_script_block(ports)
            if len(nse_block_lines) > 2:
                lines.append(f"\n### NSE Scripts :\n")
                if len(hops_block_lines) > 2:
                    lines = lines + nse_block_lines + hops_block_lines + ["```"]
                else:
                    lines = lines + nse_block_lines + ["```"]
            
            lines.append("\n")
        return lines
        
    def generate_file(self, data):
        lines = self.generate_markdown(nmap_data=data)
        if not lines:
            print("No data to write. Quitting.")
            return False
        
        print(f"\nGenerating markdown file to {os.path.abspath(self.output_file)}")
        
        with open(self.output_file, "w") as file:
            for line in lines:
                file.write(f"\n{line}")
        
        print(f"Successfully wrote to file : {os.path.abspath(self.output_file)}")
        return True