# Network Security

![banner](imgs/Network%20Security/roomBanner.png)

## Room objectives

- some security devices [Firewall - Intrusion Detection System (IDS) - Intrusion Prevention System (IPS) - Virtual Private Network (VPN)].
- some softwares [host firewalls - Antivirus].
- [cyber kill chain](https://www.lockheedmartin.com/en-us/capabilities/cyber/cyber-kill-chain.html) like:
  - Recon: Recon, short for reconnaissance, refers to the step where the attacker tries to learn as much as possible about the target. Information such as the types of servers, operating system, IP addresses, names of users, and email addresses, can help the attack’s success.
  - Weaponization: This step refers to preparing a file with a malicious component, for example, to provide the attacker with remote access.
  - Delivery: Delivery means delivering the “weaponized” file to the target via any feasible method, such as email or USB flash memory.
  - Exploitation: When the user opens the malicious file, their system executes the malicious component.
  - Installation: The previous step should install the malware on the target system.
  - Command & Control (C2): The successful installation of the malware provides the attacker with a command and control ability over the target system.
  - Actions on Objectives: After gaining control over one target system, the attacker has achieved their objectives. One example objective is Data Exfiltration (stealing target’s data).
- nmap
- using ftp server

## Tasks

### Task 1 : Introduction

<details>
<summary>
What type of firewall is Windows Defender Firewall?
</summary>

```
host firewall
```

</details>

---

### Task 2 : Methodology

<details>
<summary>
During which step of the Cyber Kill Chain does the attacker gather information about the target?
</summary>

```
recon
```

</details>

---

### Task 3 : Practical Example of Network Security

1. at first we scan server using nmap tool `nmap 10.10.40.80` we found open FTP server.
2. then try to connect anonymous using `ftp anonymous@10.10.40.80`
3. after that we download file called secret `get secret.txt`
4. close FTP server using `quit`
5. read secret file `cat secret.txt`
![banner](imgs/Network%20Security/getPasswordFromFTP.png)

<details>
<summary>
What is the password in the secret.txt file?
</summary>

```
ABC789xyz123
```

</details>

1. try to connect using ssh with found password stored in FTP server using `ssh root@10.10.40.80` and it worked fine.
2. read the root flag using `cat flag.txt`
3. after that we read final task flag in librarian `cd /home/librarian ; cat flag.txt`
![banner](imgs/Network%20Security/rootFlag.png)

<details>
<summary>
What is the content of the flag.txt in the /root directory?
</summary>

```
THM{FTP_SERVER_OWNED}
```

</details>

<details>
<summary>
What is the content of the flag.txt in the /home/librarian directory?
</summary>

```
THM{LIBRARIAN_ACCOUNT_COMPROMISED}
```

</details>
