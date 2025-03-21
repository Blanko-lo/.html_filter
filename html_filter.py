import os
from tabulate import tabulate

def print_banner():
    banner = """
   ██╗  ██╗████████╗███╗   ███╗██╗         ███████╗██╗██╗  ████████╗███████╗██████╗     
   ██║  ██║╚══██╔══╝████╗ ████║██║         ██╔════╝██║██║  ╚══██╔══╝██╔════╝██╔══██╗    
   ███████║   ██║   ██╔████╔██║██║         █████╗  ██║██║     ██║   █████╗  ██████╔╝    
   ██╔══██║   ██║   ██║╚██╔╝██║██║         ██╔══╝  ██║██║     ██║   ██╔══╝  ██╔══██╗    
██╗██║  ██║   ██║   ██║ ╚═╝ ██║███████╗    ██║     ██║███████╗██║   ███████╗██║  ██║    

    """
    print(banner)


def search_html_files(directory, search_strings, output_file):
   
    found_strings = []

    
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        for search_string in search_strings:
                            if search_string in content:
                                found_strings.append([search_string, file_path])
                except Exception as e:
                    print(f"Error reading {file_path}: {e}")

    
    with open(output_file, 'w', encoding='utf-8') as out_file:
        if found_strings:
            table = tabulate(found_strings, headers=["Found String", "File Path"], tablefmt="grid")
            out_file.write(table + '\n')
        else:
            out_file.write("No matches found.\n")

    print(f"Search complete. Found strings written to {output_file}")

if __name__ == "__main__":
    print_banner()  
   
   
    directory_to_search = input("Enter the directory to search: ")
    
    
    search_strings = input("Enter the strings to search for (comma-separated): ").split(',')
    search_strings = [s.strip() for s in search_strings]  

    
    output_file = input("Enter the output file name (ie. output.txt): ")

    
    search_html_files(directory_to_search, search_strings, output_file)

