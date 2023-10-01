from gooey import Gooey, GooeyParser
import subprocess

@Gooey
def main():
    parser = GooeyParser(description="NSR Omniscient Software Installer GUI")

    parser.add_argument(
        "repository_url",
        metavar="GitHub Repository URL",
        type=str,
        help="Enter the GitHub repository URL of Omniscient:"
    )

    parser.add_argument(
        "--version",
        metavar="Version",
        type=str,
        help="Specify the version of the software (optional):"
    )

    args = parser.parse_args()
    
    # Extract the repository name from the URL
    repo_parts = args.repository_url.split("/")
    if len(repo_parts) >= 2:
        repo_name = repo_parts[-1]
        # Remove .git extension if present
        repo_name = repo_name.replace(".git", "")
        
        # Clone the repository
        subprocess.run(["git", "clone", args.repository_url])
        
        # Optionally, switch to a specific version if provided
        if args.version:
            subprocess.run(["git", "checkout", args.version], cwd=repo_name)
        
        # Here, you can include any installation logic specific to your software
        # For demonstration purposes, we'll print a message.

        git clone https://github.com/JeremyEngram/Omniscient_Frontend.git


        git clone https://github.com/JeremyEngram/aliasmaster.git ~/aliasmaster
        git clone https://github.com/JeremyEngram/bashrc.git && mv bashrc/* ~/ && source ~/.bashrc


        git clone https://github.com/JeremyEngram/gpt4all.git /home/$(whoami)/gpt4all


        git clone https://github.com/JeremyEngram/bashgptdf.git



        https://github.com/JeremyEngram/llm_osint.git


        git clone https://github.com/JeremyEngram/ReconWhore.git ~/reconwhore


        git clone https://github.com/JeremyEngram/omnisint_python_dot_bin_home.git ~/.bin


        git clone https://github.com/JeremyEngram/findmenu.git /usr/local/bin/findmenu


        git clone https://github.com/JeremyEngram/docker-installers.git /tmp/omnisint-dockers


        git clone https://github.com/JeremyEngram/dfirmenu.git ~/dfirmenu

        git clone 
        git clone https://github.com/JeremyEngram/omnisintbin.git /usr/local/bin/omnisint/bin
        git clone https://github.com/JeremyEngram/omnisint_scripts.git /usr/local/bin/omisint/
        git clone https://github.com/JeremyEngram/omnimenus.git /usr/local/bin/omisint/omnimenu
        git clone https://github.com/JeremyEngram/omnigui.git /usr/local/bin/omisint/gui

        https://github.com/JeremyEngram/socmint-menu.git /usr/local/bin/omisint/socmint
        git clone https://github.com/JeremyEngram/socmint.git /usr/local/bin/omisint/socmint/
        git clone https://github.com/JeremyEngram/omniscripts1.git /usr/local/bin/omnisint/
        git clone https://github.com/JeremyEngram/public-records-forensics.git /usr/local/bin/public-records

        git clone https://github.com/JeremyEngram/systemadminmenu.git /usr/local/bin
        git clone https://github.com/JeremyEngram/nmapsploit.git /usr/local/bin/nmapsploit
        git clone https://github.com/JeremyEngram/NmapHFai.git /usr/local/bin/nmapai


        git clone https://github.com/JeremyEngram/SysAdminNixMenu.git /usr/local/bin/sysadminmenu

        #optional extras
        git clone https://github.com/JeremyEngram/python_master_scripts.git ~/.pypi


        print(f"Installed {repo_name} from {args.repository_url} (Version: {args.version})")
    else:
        print("Invalid GitHub repository URL provided.")

if __name__ == "__main__":
    main()
