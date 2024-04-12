# Operating System Security

![banner](imgs/Operating%20System%20Security/roomBanner.png)

## Room objectives

- what is OS.
- most famous OSs in market
- CIA triad:
  - Confidentiality: You want to ensure that secret and private files and           information are only available to intended persons.
  - Integrity: It is crucial that no one can tamper with the files stored on your system or while being transferred on the network.
  - Availability: You want your laptop or smartphone to be available to use anytime you decide to use it.
- Authentication and Weak Passwords
- Weak File Permissions
- Access to Malicious Programs

## Tasks

### Task 1 : Introduction to Operating System Security

<details>
<summary>
Which of the following is not an operating system?
AIX - Android - Chrome OS - Solaris - Thunderbird
</summary>

```
Thunderbird
```

</details>

---

### Task 2 : Common Examples of OS Security

<details>
<summary>
Which of the following is a strong password, in your opinion?
iloveyou - 1q2w3e4r5t - LearnM00r - qwertyuiop
</summary>

```
LearnM00r
```

</details>

---

### Task 3 : Practical Example of OS Security

1. after run the machine we got init access with exposed usr name and password using `ssh sammie@10.10.86.228` and password of `dragon`.
![Alt text](imgs/Operating%20System%20Security/gotAccess.png)
2. we got all system users name using `cd .. ; ls` and also a hint in txt.
![Alt text](imgs/Operating%20System%20Security/systemUserList.png)
3. after that we will try to login into johnny account using `ssh johnny@10.10.86.228` with to used passwords after several tries we got password **`abc123`**
![Alt text](imgs/Operating%20System%20Security/sucsessLogin_abc123.png)
4. after that we search in history to find any leaked password by johnny using `history` and we found **`happyHack!NG`**
![Alt text](imgs/Operating%20System%20Security/rootPassword.png)
5. when we log-in as root we will got flag **`THM{YouGotRoot}`**
![Alt text](imgs/Operating%20System%20Security/rootFlag.png)

<details>
<summary>
Based on the top 7 passwords, let’s try to find Johnny’s password. What is the password for the user johnny?
</summary>

```
abc123
```

</details>

---

<details>
<summary>
Once you are logged in as Johnny, use the command history to check the commands that Johnny has typed. We expect Johnny to have mistakenly typed the root password instead of a command. What is the root password?
</summary>

```
happyHack!NG
```

</details>

---

<details>
<summary>
While logged in as Johnny, use the command su - root to switch to the root account. Display the contents of the file flag.txt in the root directory. What is the content of the file?
</summary>

```
THM{YouGotRoot}
```

</details>
