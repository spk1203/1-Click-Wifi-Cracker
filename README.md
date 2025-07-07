# 1-Click WiFi Cracker

A one-click automated Wi-Fi hacking tool designed to scan for networks, perform deauthentication attacks, capture WPA2 handshakes, and crack them using a dictionary wordlist. Built for ethical hacking, penetration testing, and educational research.

---

##️ Features

- Start monitor mode automatically
- Scan all nearby Wi-Fi networks
- Select target network interactively
- Perform deauthentication attacks
- Capture WPA2 4-way handshake
- Crack captured handshake using `rockyou.txt` wordlist
- Fully CLI-based and beginner-friendly

---

##️ Main Requirements

-  Kali Linux (or any Linux distro with Aircrack-ng tools)
-  An **external USB Wi-Fi adapter**
-  Adapter must support **monitor mode** and **packet injection**
-  Download and install **drivers** specific to your adapter model  
  (e.g., `MT7601U`, `RTL8812AU`, etc.)
-  Run as **root** or use `sudo`

---

## Tech Stack

- **Python 3.x**
- `airmon-ng`, `airodump-ng`, `aireplay-ng`, `aircrack-ng`
- `mac80211`/`cfg80211` kernel modules
- `rockyou.txt` wordlist (default or custom)

---

##Usage

```bash
# Clone the repo
git clone https://github.com/spk1203/1-Click-Wifi-Cracker.git
cd 1-Click-Wifi-Cracker

# Run the script
sudo python3 wifihack.py
