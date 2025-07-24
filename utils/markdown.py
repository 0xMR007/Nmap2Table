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
        
        block_lines.append("```")
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

            block_lines = self.format_nse_script_block(ports)
            if len(block_lines) > 2:
                lines.append(f"### NSE Scripts :\n")
                lines = lines + block_lines
            
            lines.append("\n")
        return lines
        
    def generate_file(self, data):
        lines = self.generate_markdown(nmap_data=data)
        if not lines:
            print("No data to write. Quitting.")
            return False
        
        print(f"Generating output to {os.path.abspath(self.output_file)}")
        
        with open(self.output_file, "w") as file:
            for line in lines:
                file.write(f"\n{line}")
        
        print(f"Successfully wrote to file : {os.path.abspath(self.output_file)}")
        return True