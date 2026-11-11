# Network Device Detector

**Python ARP network discovery and CSV reporting**

A small network-diagnostics project that discovers devices responding to ARP on a local IPv4 subnet, displays IP/MAC addresses and attempts to identify manufacturers. Built to practice networking and Python troubleshooting.

## What the current code does

- Sends ARP requests with Scapy to a configured local subnet.
- Prints discovered IP and MAC addresses.
- Looks up MAC vendors using `mac-vendor-lookup` (unknown vendors are labelled accordingly).
- Displays a terminal table and saves timestamped CSV results.

## Stack

Python, Scapy, mac-vendor-lookup, tabulate, CSV.

## Run locally

Use only on networks you own or are explicitly authorized to assess.

```bash
git clone https://github.com/JotaC95/netowrkDeviceDetector.git
cd netowrkDeviceDetector
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install mac-vendor-lookup tabulate
sudo .venv/bin/python scanner.py
```

**Configuration:** The current `scanner.py` hardcodes `192.168.1.0/24` in `main()`. Edit that value to match your authorized subnet before running. Elevated permissions may be necessary for raw ARP packets. `requirements.txt` currently lists only Scapy, so the two additional packages are installed explicitly above.

## Example output format

```text
IP             MAC                Manufacturer
192.168.1.x    aa:bb:cc:dd:ee:ff  Unknown
```

*Illustrative format, not a real scan result.* A timestamped `resultado_escaneo_YYYYMMDD_HHMMSS.csv` contains IP, MAC and manufacturer columns.

## Limitations and planned improvements

- ARP only reaches the local broadcast domain; it does not discover arbitrary internet hosts.
- Vendor lookup can fail or be inaccurate; devices may randomize MAC addresses.
- The subnet is currently hardcoded; configurable CLI options and test coverage are future improvements.
- No claim of a security vulnerability assessment or comprehensive network inventory.

## Engineering value

Demonstrates basic Layer 2 discovery, Python packet tooling, structured output and practical network troubleshooting.
