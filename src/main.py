from src.parser import XMLParser
from utils.markdown import MarkdownUtil
import sys

# Usage : python -m src.main nmap_scan.xml outputfile.md

def main():

    print("Starting main script...\n")

    if len(sys.argv) < 3:
        print("Error, please respect the script usage.")
        print("Usage : python -m src.main nmap_scan.xml outputfile.md")
        sys.exit(1)
    
    else:
        nmap_file = sys.argv[1]
        output_file = sys.argv[2]

        parser = XMLParser(file_path=nmap_file)
        markdown_util = MarkdownUtil(output_file=output_file)
        data = parser.extract_nmap_data()
        markdown_util.generate_file(data)

if __name__ == "__main__":
    main()