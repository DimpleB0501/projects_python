# Setup SSH in raspberry pi
1. Set up your local network and wireless connectivity
Make sure your Raspberry Pi is properly set up and connected. If you are using wireless networking, this can be enabled via the desktop's user interface, or using the command line.
If you are not using wireless connectivity, plug your Raspberry Pi directly into the router.
You will need to note down the IP address of your Pi in order to connect to it later. Using the `ifconfig` command will display information about the current network status, including the IP address, or you can use `hostname -I` to display the IP addresses associated with the device.

2. Enable SSH
As of the November 2016 release, Raspbian has the SSH server disabled by default. 
It can be enabled manually from the desktop by: 
    - Launch Raspberry Pi Configuration from the Preferences menu
    - Navigate to the Interfaces tab
    - Select Enabled next to SSH
    - Click OK

# SSH
- SSH requirements both server and client on internet.
- Running the SSH client
    - Open a terminal and type `ssh <username>@<domainname>`
    **username** is user name on the server machine and **domainname** is address of server machine. First time, you will get a message __address could not be authenticated__ enter **yes** to continue.
- Access raspberry pi without connecting it to a monitor/keyboard `sudo rm /etc/ssh/ssh_host_* && sudo dpkg-reconfigure openssh-server`.

    
