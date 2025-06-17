from scapy.all import ARP, Ether, srp
from mac_vendor_lookup import MacLookup
from tabulate import tabulate
import csv
from datetime import datetime

def scanner_net(rango_ip):
    target_ip = rango_ip
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    arp = ARP(pdst=target_ip)
    paquete = ether/arp
    resultado = srp(paquete, timeout=3, verbose=0) [0]
    
    print("Found devices:")
    for sent, received in resultado:
        print(f"{received.psrc}-{received.hwsrc}")
        
    dispositivos = []
    for sent, received in resultado:
        ip = received.psrc
        mac = received.hwsrc
        try:
            vendor = MacLookup().lookup(mac)
        except:
            vendor = "Desconocido"
        dispositivos.append((ip,mac,vendor))
    return dispositivos

def guardar_csv(info, filename):
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["IP", "MAC","MANUFACTURER"])
        writer.writerows(info)
        
def main():
    print("[*] Escaneando red local...")
    rango = "192.168.1.0/24"  # Cambia según tu red
    dispositivos = scanner_net(rango) 
    print(tabulate(dispositivos, headers=["IP", "MAC", "Fabricante"], tablefmt="fancy_grid"))
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    archivo_salida = f"resultado_escaneo_{timestamp}.csv"
    guardar_csv(dispositivos, archivo_salida)
    print(f"\n[*] Resultados guardados en: {archivo_salida}")


if __name__ == "__main__":
    main()