# Tutorial

![roomBanner](img/getting%20started/Tutorial/roomBanner.png)

## Room objectives

- how to use try hack me platform
- connection using openVPN

## steps

1. after apply same steps in explanation i am failed to connect to try hack me network and to solve this problem:
   1. download VPN program called [windscribe](https://deploy.totallyacdn.com/desktop-apps/2.8.6/windscribe_2.8.6_amd64.deb)
   2. change directory to downloads `cd ~/Downloads`
   3. install it using this command
   `sudo dpkg -i windscribe_2.7.14_amd64.deb`
   4. open it using `windscribe-cli connect`
   5. change mode to **Stealth** mode on port **443**
   ![VPN](img/getting%20started/Tutorial/VPN.png)
   6. download your openVPN config file from [config](https://tryhackme.com/access)
   7. run it using `openvpn {YOUR_USER_NAME}.ovpn`
   8. check [connectivity](https://tryhackme.com/access)
   ![connectivity](img/getting%20started/Tutorial/connectivity.png)
   9. start machine
   10.open browser and go to your machine ip

## Flag

>flag{connection_verified}
