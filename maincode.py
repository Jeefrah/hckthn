
import subprocess

target_ip_address = input("Please enter the  target ip adress:  ")
speed = input("Please enter the attack speed of nmap ( between T0-T5 ) :  ")


def run_nmap(target_ip_address , speed):
    try:
        
        nmap_command = ["nmap", "-A", speed , target_ip_address]
        result = subprocess.run(nmap_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print("Result of nmap tool:")
        print(result.stdout)
        if result.stderr:
            print("Hata mesajı:")
            print(result.stderr)
    except Exception as e:
        print(f"nmap tool is occured: {e}")


run_nmap(target_ip_address,speed)
