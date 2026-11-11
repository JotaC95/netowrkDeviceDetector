"""Discover hosts on a local IPv4 network using ARP. Scan only networks you own or administer."""
import argparse
import csv
from datetime import datetime
from ipaddress import ip_network
from pathlib import Path

from mac_vendor_lookup import MacLookup
from scapy.all import ARP, Ether, srp
from tabulate import tabulate


def scan_network(cidr: str, timeout: float = 3.0):
    network = ip_network(cidr, strict=False)
    if network.version != 4:
        raise ValueError("ARP discovery supports IPv4 only")
    if network.num_addresses > 4096:
        raise ValueError("Network too large; choose a range of 4096 addresses or fewer")
    responses, _ = srp(Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=str(network)), timeout=timeout, verbose=False)
    lookup = MacLookup()
    devices = []
    for _, received in responses:
        mac = received.hwsrc
        try:
            vendor = lookup.lookup(mac)
        except (KeyError, ValueError, OSError):
            vendor = "Unknown"
        devices.append((received.psrc, mac, vendor))
    return sorted(devices, key=lambda item: tuple(int(x) for x in item[0].split(".")))


def save_csv(devices, path: Path):
    with path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["IP", "MAC", "MANUFACTURER"])
        writer.writerows(devices)


def main():
    parser = argparse.ArgumentParser(description="ARP device discovery on an authorized local IPv4 network")
    parser.add_argument("network", help="IPv4 CIDR, for example 192.168.1.0/24")
    parser.add_argument("--timeout", type=float, default=3.0)
    parser.add_argument("--output", type=Path, default=None)
    args = parser.parse_args()
    if args.timeout <= 0:
        parser.error("--timeout must be positive")
    try:
        devices = scan_network(args.network, args.timeout)
    except ValueError as error:
        parser.error(str(error))
    print(tabulate(devices, headers=["IP", "MAC", "Manufacturer"], tablefmt="fancy_grid"))
    output = args.output or Path(f"network_scan_{datetime.now():%Y%m%d_%H%M%S}.csv")
    save_csv(devices, output)
    print(f"Saved {len(devices)} devices to {output}")


if __name__ == "__main__":
    main()
