from src.parser import XMLParser, parse_args
from utils.markdown import MarkdownUtil

# Usage : python -m src.main nmap_scan.xml outputfile.md

def main():

    print("Starting main script...\n")

    args = parse_args()

    parser = XMLParser(file_path=args.input)
    markdown_util = MarkdownUtil(output_file=args.output)
    data = parser.extract_nmap_data()
    markdown_util.generate_file(data)

if __name__ == "__main__":
    main()