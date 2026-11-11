# Network Device Detector

**Discover responding devices on an authorized local IPv4 network.** A small Python learning and diagnostic utility using ARP, Scapy and CSV reporting.

## What you can do

- Discover ARP responders on a local subnet.
- Display IP, MAC and a best-effort manufacturer lookup.
- Save a timestamped CSV report.

This is **not** a vulnerability scanner, internet-wide discovery tool or complete asset inventory.

## Quick start

```bash
git clone https://github.com/JotaC95/netowrkDeviceDetector.git
cd netowrkDeviceDetector
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install mac-vendor-lookup tabulate
```

**Before scanning:** open `scanner.py` and change `rango = "192.168.1.0/24"` in `main()` to the local subnet you own or are explicitly authorized to test. The range is hardcoded; there is no CLI flag yet.

```bash
sudo .venv/bin/python scanner.py
```

Raw ARP operations may require elevated permissions. Review the code before running it with `sudo`.

## Example output (illustrative)

```text
IP             MAC                Manufacturer
192.168.1.12   02:00:00:00:00:12  Unknown
```

The program writes a `resultado_escaneo_YYYYMMDD_HHMMSS.csv` file in the current working directory with `IP,MAC,MANUFACTURER` columns. Example values above are fictional.

## How it works

```text
Configured subnet -> Scapy ARP broadcast -> Responses
                                         -> MAC vendor lookup
                                         -> Terminal table + CSV
```

The tool only sees devices that respond to local ARP requests. Vendor lookup may fail, and MAC randomization can make manufacturer identification unreliable.

## Troubleshooting

| Problem | What to check |
| --- | --- |
| `ModuleNotFoundError` | `requirements.txt` currently includes only Scapy; install `mac-vendor-lookup` and `tabulate` as shown |
| No devices found | Confirm subnet, network access and permissions; some devices do not respond |
| Vendor shown as unknown | Vendor database/network lookup can fail; MAC may be randomized |
| Permission error | ARP packet capture/transmission may need elevated privileges |

## Project status

Educational utility. No automated test suite or cross-platform compatibility guarantee is documented. Future improvements: command-line subnet input, pinned complete dependencies, tests and sanitized screenshots.

## Responsible use

Only scan networks where you have permission. Avoid collecting or sharing identifiable device information without authorization.
