import subprocess
import threading

def run_nmap(target_ip_address, speed):
    try:
        nmap_command = ["nmap", "-A", speed, target_ip_address]
        result = subprocess.run(nmap_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print("Result of nmap tool:")
        print(result.stdout)
        if result.stderr:
            print("Hata mesajı:")
            print(result.stderr)
    except Exception as e:
        print(f"nmap tool is occured: {e}")

def dirb_scan(domain_address):
    try:
        dirb_command = ["dirb", "https://" + domain_address]
        result = subprocess.run(dirb_command, capture_output=True, text=True)
        print("Dirb tarama sonucu:")
        print(result.stdout)
    except Exception as e:
        print(f"Dirb taraması başarısız oldu: {e}")

target_ip_address = input("Please enter the target IP address: ")
speed = input("Please enter the attack speed of nmap (between -T0,-T5): ")
domain_address = input("Please enter the domain address: ")

# Create threads
nmap_thread = threading.Thread(target=run_nmap, args=(target_ip_address, speed))
dirb_thread = threading.Thread(target=dirb_scan, args=(domain_address,))

# Start threads
nmap_thread.start()
dirb_thread.start()

# Wait for both threads to complete
nmap_thread.join()
dirb_thread.join()

print("Both scans are complete.")

