#-------------------------------------------------------------------------------
#made by ImSoOffline-made by ImSoOffline-made by ImSoOffline-made by ImSoOffline
#-------------------------------------------------------------------------------


#=======================================================================================
#IMPORTS
#=======================================================================================
import subprocess
import ctypes
import sys
import time
import signal
import os
import random
import json
#=======================================================================================
#DEFAULT USE VARLIB
#=======================================================================================
RESET = "\033[0m"
BOLD = "\033[1m"
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
MAGENTA = "\033[95m"
BLUE = "\033[94m"
DIM = "\033[2m"
MATRIX = "\033[38;5;40m"
memadd1 = f"0x{random.randint(0x10000000, 0xFFFFFFFF):08X}"
memadd2 = f"0x{random.randint(0x10000000, 0xFFFFFFFF):08X}"
memadd3 = f"0x{random.randint(0x10000000, 0xFFFFFFFF):08X}"
memadd4 = f"0x{random.randint(0x10000000, 0xFFFFFFFF):08X}"
memadd5 = f"0x{random.randint(0x10000000, 0xFFFFFFFF):08X}"
memadd6 = f"0x{random.randint(0x10000000, 0xFFFFFFFF):08X}"
memadd7 = f"0x{random.randint(0x10000000, 0xFFFFFFFF):08X}"
memadd8 = f"0x{random.randint(0x10000000, 0xFFFFFFFF):08X}"
#=======================================================================================
#FUNCTIONS
#=======================================================================================
dns_servers = {
    "1. Google DNS (8.8.8.8, 8.8.4.4)": (
        f"{GREEN}Pros:{RESET} Fast and globally available.\n{RED}Cons:{RESET} Logs user data."
    ),
    "2. Cloudflare DNS (1.1.1.1, 1.0.0.1)": (
        f"{GREEN}Pros:{RESET} Fastest, privacy-focused.\n{RED}Cons:{RESET} No content filtering."
    ),
    "3. OpenDNS (208.67.222.222, 208.67.220.220)": (
        f"{GREEN}Pros:{RESET} Offers parental control.\n{RED}Cons:{RESET} Collects analytics."
    ),
    "4. Quad9 (9.9.9.9, 149.112.112.112)": (
        f"{GREEN}Pros:{RESET} Blocks known malicious domains.\n{RED}Cons:{RESET} Slightly slower."
    ),
    "5. CleanBrowsing (185.228.168.9, 185.228.169.9)": (
        f"{GREEN}Pros:{RESET} Family-friendly filtering.\n{RED}Cons:{RESET} Strict blocking."
    )
}

def typeout(text, delay=0.01):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()
    

def startup_sequence():
    # Clear the terminal screen
    os.system('cls' if os.name == 'nt' else 'clear')

    # Create the boot steps with memadd variables
    steps = [
        f"[OK] CPU Scan @ {memadd1}",
        f"[OK] Reserving CPU and RAM memory @ {memadd2}",
        f"[OK] Initiating query engine @ {memadd3}",
        f"[OK] DNSSnap core files loading into RAM memory @ {memadd4}",
        f"[OK] DNSSnap kernel files loading into ROAMING folder @ {memadd5}",
        f"[OK] MAC Address Vector Table Configured @ {memadd6}",
        f"[OK] Loading Boot Sector and Master Boot Record for DNSSnap @ {memadd7}",
        f"[OK] Finished HEAP initialization @ {memadd8}",
        "MEMADDRESSES LOADED:"
    ]

    for step in steps:
        typeout(f"{GREEN}{step}{RESET}", delay=0.03)
        time.sleep(0.2)

    # Output the actual memory addresses
    for mem in [memadd1, memadd2, memadd3, memadd4, memadd5, memadd6, memadd7, memadd8]:
        typeout(f"{GREEN}{mem}{RESET}", delay=0.01)
    steps = [
        f"[OK] CPU Scan @ {memadd1}",
        f"[OK] Reserving CPU and RAM memory @ {memadd2}",
        f"[OK] Initiating query engine @ {memadd3}",
        f"[OK] DNSSnap core files loading into RAM memory @ {memadd4}",
        f"[OK] DNSSnap kernel files loading into ROAMING folder @ {memadd5}",
        f"[OK] MAC Address Vector Table Configured @ {memadd6}",
        f"[OK] Loading Boot Sector and Master Boot Record for DNSSnap @ {memadd7}",
        f"[OK] Finished HEAP initialization @ {memadd8}",
        "MEMADDRESSES LOADED:"
    ]

    for step in steps:
        print(step)
    
    # Print each memory address separately
    print(memadd1)
    print(memadd2)
    print(memadd3)
    print(memadd4)
    print(memadd5)
    print(memadd6)
    print(memadd7)
    print(memadd8)
    time.sleep(3)

def banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(rf"""{MATRIX}{BOLD}
 /$$$$$$$  /$$   /$$  /$$$$$$   /$$$$$$                               
| $$__  $$| $$$ | $$ /$$__  $$ /$$__  $$                              
| $$  \ $$| $$$$| $$| $$  \__/| $$  \__/ /$$$$$$$   /$$$$$$   /$$$$$$ 
| $$  | $$| $$ $$ $$|  $$$$$$ |  $$$$$$ | $$__  $$ |____  $$ /$$__  $$
| $$  | $$| $$  $$$$ \____  $$ \____  $$| $$  \ $$  /$$$$$$$| $$  \ $$
| $$  | $$| $$\  $$$ /$$  \ $$ /$$  \ $$| $$  | $$ /$$__  $$| $$  | $$
| $$$$$$$/| $$ \  $$|  $$$$$$/|  $$$$$$/| $$  | $$|  $$$$$$$| $$$$$$$/
|_______/ |__/  \__/ \______/  \______/ |__/  |__/ \_______/| $$____/ 
                                                            | $$      
                                                            | $$      
                                                            |__/        
{RESET}""")
    
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
    
def elevate():
    script = sys.argv[0]
    params = " ".join([f'"{arg}"' for arg in sys.argv[1:]])
    ctypes.windll.shell32.ShellExecuteW(
        None, "runas", sys.executable, f'"{script}" {params}', None, 1
    )
    time.sleep(5)
    sys.exit()
    
def list_network_adapters():
    typeout(f"{CYAN}Scanning network interfaces...{RESET}")
    time.sleep(0.5)
    output = subprocess.check_output(
        'powershell "Get-NetAdapter | Select-Object Name, Status | ConvertTo-Json"',
        shell=True
    ).decode("utf-8")

    adapters = []
    try:
        data = json.loads(output)
        if isinstance(data, dict):  # single adapter case
            data = [data]
        adapters = [(item["Name"], item["Status"]) for item in data]
    except Exception:
        print(f"{RED}Error parsing adapter list. Make sure PowerShell is available.{RESET}")
        sys.exit(1)

    print(f"\n{YELLOW}Available Adapters:{RESET}")
    for idx, (name, status) in enumerate(adapters, 1):
        status_color = GREEN if status.lower() == "up" else RED
        print(f"{MAGENTA}{idx}.{RESET} {YELLOW}{name}{RESET} - {status_color}{status}{RESET}")
        time.sleep(0.1)
    return adapters

def select_adapter(adapters):
    while True:
        try:
            idx = int(input(f"{CYAN}Select adapter #: {RESET}")) - 1
            if 0 <= idx < len(adapters):
                return adapters[idx][0]
            else:
                print(f"{RED}Invalid selection.{RESET}")
        except ValueError:
            print(f"{RED}Please enter a valid number.{RESET}")
            
def display_dns_options():
    print(f"\n{BOLD}{CYAN}--- DNS OPTIONS ---{RESET}")
    for idx, (name, desc) in enumerate(dns_servers.items(), 1):
        print(f"{GREEN}{idx}.{RESET} {name}")
        print(f"    {desc}\n")
        time.sleep(0.05)
        
def get_dns_choice():
    while True:
        try:
            choice = int(input(f"{CYAN}Choose DNS #: {RESET}"))
            if 1 <= choice <= len(dns_servers):
                dns_name = list(dns_servers.keys())[choice - 1]
                ips = dns_name.split("(")[1].split(")")[0].split(",")
                return [ip.strip() for ip in ips]
            else:
                print(f"{RED}Invalid choice.{RESET}")
        except ValueError:
            print(f"{RED}Invalid input.{RESET}")
            
def set_dns(adapter, dns_ips):
    typeout(f"{YELLOW}Configuring {adapter} with {', '.join(dns_ips)}...{RESET}", 0.01)
    dns_str = ",".join([f"'{ip}'" for ip in dns_ips])
    subprocess.run([
        "powershell",
        f"Set-DnsClientServerAddress -InterfaceAlias \"{adapter}\" -ServerAddresses ({dns_str})"
    ], check=True)
    print(f"{GREEN}✔ DNS successfully set!{RESET}")
    
def reset_dns(adapter):
    typeout(f"{RED}Reverting DNS settings for {adapter}...{RESET}", 0.01)
    subprocess.run([
        "powershell",
        f"Set-DnsClientServerAddress -InterfaceAlias \"{adapter}\" -ResetServerAddresses"
    ], check=True)
    print(f"{GREEN}✔ DNS reset to automatic.{RESET}")
    
def cleanup(signal_received=None, frame=None):
    reset_dns(selected_adapter)
    print(f"{DIM}Session terminated. DNS restored.{RESET}")
    time.sleep(1)  # Short pause before exiting
    sys.exit(0)

    
def main():
    global selected_adapter

    if not is_admin():
        print(f"{RED}❌ Administrator privileges required. Attempting elevation...{RESET}")
        time.sleep(1)
        elevate()

    startup_sequence()
    banner()

    signal.signal(signal.SIGINT, cleanup)
    signal.signal(signal.SIGTERM, cleanup)

    adapters = list_network_adapters()
    selected_adapter = select_adapter(adapters)

    display_dns_options()
    dns_ips = get_dns_choice()

    try:
        set_dns(selected_adapter, dns_ips)
        print(f"{MAGENTA}🔥 DNS active — CTRL+C to terminate and revert.{RESET}")
        while True:
            time.sleep(1)
    except Exception as e:
        print(f"{RED}❌ Error: {e}{RESET}")
        cleanup()

if __name__ == "__main__":
    main()
