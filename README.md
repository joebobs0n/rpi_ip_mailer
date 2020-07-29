# Raspberry Pi IP Mailer
This script emails your Raspberry Pi's local IP address to a given gmail address at startup. This is to remove the guesswork involved with having a Raspberry Pi setup for headless operation. Too many times I have been using a Pi and had to do some weird workaround or query my modem for all alocated IP address and find out wich one is my Pi. This removes the headache and tells you directly and immediately when your Pi starts up!

# How to use:
## Email Setup:
* Create (or use) a throwaway gmail account.
* Turn on "Less Secure Apps" for your throwaway google account (information here: https://support.google.com/accounts/answer/6010255?hl=en)
* (Optional) Setup forwarding filter on the throwaway account to forward just the IP address emails to your personal email. This ensures that your personal email is secure (since turning on "Less Secure Apps" opens possible security issues) and you can receive it on non-gmail accounts.

## Raspberry Pi Setup:
* Download the "startup_mailer.py" script
* Modify lines 8 and 9 for the throwaway email address and password
* (Optional) Create a folder in your home directory (not root) and place the script in the folder
* Open a terminal and navigate to where the script is located
* Type: "sudo chmod +x startup_mailer.py"
* Type: "sudo nano /etc/rc.local"
* Add "python3 home/pi/\<Optional Folder\>/startup_mailer.py" before the "exit 0" at the bottom of the file
* Save and close ("ctrl+x", "y", "enter")
* Reboot ("sudo shutdown -r now" or "sudo reboot") and verify that you receive an email with the Pi's IP address
