# Linux Fundamentals Part 3

![Alt text](img/Linux%20Fundamentals%20Part%203/roomBanner.png)

## Room objectives

- some commands
  - echo
  - nano
  - vim
- transfer data through network using ssh & SCP

## Tasks

### Task 1 : Introduction

<details>
<summary>
Let's proceed!
</summary>

```text
No answer needed
```

</details>

### Task 2 : Deploy Your Linux Machine

<details>
<summary>
I've logged into the Linux Fundamentals Part 3 machine using SSH and have deployed the AttackBox successfully!
</summary>

1. start the machine
2. start attack box OR openVPN
3. connect to the machine using SSH `ssh tryhackme@MACHINE_IP -y`
4. accept connection `yes`
5. type machine password `tryhackme`
  
   ![alt-text](img/Linux%20Fundamentals%20Part%203/sshConnection.png)

```text
No answer needed
```

</details>

### Task 3 : Terminal Text Editors

<details>
<summary>
Create a file using Nano
</summary>

```text
No answer needed
```

</details>

---

<details>
<summary>
Edit "task3" located in "tryhackme"'s home directory using Nano. What is the flag?
</summary>

just read the task

  ![alt-text](img/Linux%20Fundamentals%20Part%203/flag1command.png)
  ![alt-text](img/Linux%20Fundamentals%20Part%203/flag1.png)

```text
THM{TEXT_EDITORS}
```

</details>

### Task 4 : General/Useful Utilities

<details>
<summary>
Ensure you are connected to the deployed instance (MACHINE_IP)
</summary>

using ping command to check machine up or not `ping MACHINE_IP` then close connection `ctrl + c`

  ![alt-text](img/Linux%20Fundamentals%20Part%203/task4_1png.png)

```text
No answer needed
```

</details>

---

<details>
<summary>
Now, use Python 3's "HTTPServer" module to start a web server in the home directory of the "tryhackme" user on the deployed instance.
</summary>

deploy server on machine using python command `python3 -m http.server`

  ![alt-text](img/Linux%20Fundamentals%20Part%203/downloadServerDeploy.png)

```text
No answer needed
```

</details>

---

<details>
<summary>
Download the file http://MACHINE_IP:8000/.flag.txt onto the TryHackMe AttackBox, What are the contents?
</summary>

on your machine or your attackBox download the hidden file using `wget http://MACHINE_IP:8000/.flag.txt`

and show file content using `cat .flag.txt`

  ![alt-text](img/Linux%20Fundamentals%20Part%203/flagDownload.png)

```text
THM{WGET_WEBSERVER}
```

</details>

---

<details>
<summary>
Create and download files to further apply your learning -- see how you can read the documentation on Python3's "HTTPServer" module, Use Ctrl + C to stop the Python3 HTTPServer module once you are finished.
</summary>

on your machine or your attackBox download the hidden file using `wget http://MACHINE_IP:8000/.flag.txt`

and show file content using `cat .flag.txt`

  ![alt-text](img/Linux%20Fundamentals%20Part%203/flagDownload.png)

```text
No answer needed
```

</details>

### Task 5 : Processes 101

<details>
<summary>
Read me!
</summary>

```text
No answer needed
```

</details>

---

<details>
<summary>
If we were to launch a process where the previous ID was "300", what would the ID of this new process be?
</summary>

```text
301
```

</details>

---

<details>
<summary>
If we wanted to cleanly kill a process, what signal would we send it?
</summary>

```text
SIGTERM
```

</details>

---

<details>
<summary>
Locate the process that is running on the deployed instance (MACHINE_IP). What flag is given?
</summary>

just print and search in background process using `ps aux | grep THM`

  ![alt-text](img/Linux%20Fundamentals%20Part%203/task5_4.png)

```text
THM{PROCESSES}
```

</details>

---

<details>
<summary>
What command would we use to stop the service "myservice"?
</summary>

```text
systemctl stop myservice
```

</details>

---

<details>
<summary>
What command would we use to start the same service on the boot-up of the system?
</summary>

```text
systemctl enable myservice
```

</details>

---

<details>
<summary>
What command would we use to bring a previously backgrounded process back to the foreground?
</summary>

```text
fg
```

</details>

### Task 6 : Maintaining Your System: Automation

<details>
<summary>
Ensure you are connected to the deployed instance and look at the running crontabs.
</summary>

```text
No answer needed
```

</details>

---

<details>
<summary>
When will the crontab on the deployed instance (MACHINE_IP) run?
</summary>

by running `crontab -e,`

  ![alt-text](img/Linux%20Fundamentals%20Part%203/task6_2.png)

```text
@reboot
```

</details>

### Task 7 : Maintaining Your System: Package Management

<details>
<summary>
Since TryHackMe instances do not have an internet connection...this task only requires you to read through the material.
</summary>

```text
No answer needed
```

</details>

### Task 8 : Maintaining Your System: Logs

<details>
<summary>
Look for the apache2 logs on the deployable Linux machine
</summary>

just go to this path `cd /var/log/apache2/`

  ![alt-text](img/Linux%20Fundamentals%20Part%203/task8.png)


```text
No answer needed
```

</details>

---

<details>
<summary>
What is the IP address of the user who visited the site?
</summary>

show file contains `cat access.log.1`

  ![alt-text](img/Linux%20Fundamentals%20Part%203/task8.png)

```text
10.9.232.111
```

</details>

---

<details>
<summary>
What file did they access?
</summary>

show file contains `cat access.log.1`

  ![alt-text](img/Linux%20Fundamentals%20Part%203/task8.png)
  
```text
catsanddogs.jpg
```

</details>
