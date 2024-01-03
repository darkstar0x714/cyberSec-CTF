# Introductory Researching

![banner](img/getting%20started/%20Introductory%20Researching/banner.png)

## Room objectives

- importance of searching in cyber sec. career.
- most important recourse [Google - man - Exploit DB - CVE Mitre - NVD - ....].
- what is CVE (Common Vulnerabilities and Exposures).
- use of searchsploit tool for search in ExploitDB.
- usee man command in linux.
- Any information can potentially be useful !

## Tasks

### Task 1 : Introduction

Effective research is crucial for hackers due to the extensive knowledge required to break into systems. No one knows everything, and research is essential for problem-solving. As experience grows, so does the complexity of research, particularly in information security. This overview will cover key resources and help develop a personalized research methodology. Topics include research questions, vulnerability searching tools, and Linux Manual Pages.

<details>
<summary>
Read the Introduction
</summary>
```
No answer needed
```
</details>

### Task 2 : Example Research Question

just an example about how to search google is your friend

<details>
<summary>
In the Burp Suite Program that ships with Kali Linux, what mode would you use to manually send a request (often repeating a captured request numerous times)?
</summary>

```text
Repeater
```

</details>

---

<details>
<summary>
What hash format are modern Windows login passwords stored in?
</summary>

```text
NTLM
```

</details>

---

<details>
<summary>
What are automated tasks called in Linux?
</summary>

```text
Cron Jobs
```

</details>

---

<details>
<summary>
What number base could you use as a shorthand for base 2 (binary)?
</summary>

```text
Base 16
```

</details>

---

<details>
<summary>
If a password hash starts with $6$, what format is it (Unix variant)?
</summary>

```text
sha512crypt
```

</details>

### Task 3 : Vulnerability Searching

read task to know what is CVE

- open ExploitDB website or just use `searchsploit`

<details>
<summary>
What is the CVE for the 2020 Cross-Site Scripting (XSS) vulnerability found in WPForms?
</summary>

![Alt text](img/getting%20started/%20Introductory%20Researching/CVE-2020-10385.png)

![Alt text](img/getting%20started/%20Introductory%20Researching/CVE-2020-10385%20Details.png)

```text
CVE-2020-10385
```

</details>

---

<details>
<summary>
There was a Local Privilege Escalation vulnerability found in the Debian version of Apache Tomcat, back in 2016. What's the CVE for this vulnerability?
</summary>

1. update your local exploitDB copy `searchsploit -u`
2. open terminal and type `searchsploit`
3. type key words of your search `searchsploit Apache Tomcat Debian`

    ![Alt text](img/getting%20started/%20Introductory%20Researching/CVE-2016-1240.png)

4. to get more info about exploit  `cat /usr/share/exploitdb/exploits/linux/local/40450.txt`

   ![Alt text](img/getting%20started/%20Introductory%20Researching/CVE-2016-1240%20details.png)

```text
CVE-2016-1240
```

</details>

---

<details>
<summary>
What is the very first CVE found in the VLC media player?
</summary>

1. open exploitDB and search for vlc & sort by date

    ![Alt text](img/getting%20started/%20Introductory%20Researching/CVE-2007-0017.png)

    ![Alt text](img/getting%20started/%20Introductory%20Researching/CVE-2007-0017%20Details.png)

```text
CVE-2007-0017
```

</details>

---

<details>
<summary>
If you wanted to exploit a 2020 buffer overflow in the sudo program, which CVE would you use?
</summary>

1. type key words of your search `searchsploit sudo 2020 buffer overflow`

    ![Alt text](img/getting%20started/%20Introductory%20Researching/CVE-2019-18634.png)

2. to get more info about exploit  `cat /usr/share/exploitdb/exploits/linux/dos/47995.txt`

   ![Alt text](img/getting%20started/%20Introductory%20Researching/CVE-2019-18634%20details.png)

```text
CVE-2019-18634
```

</details>

### Task 4 : Manual Pages

<details>
<summary>
SCP is a tool used to copy files from one computer to another.

What switch would you use to copy an entire directory?
</summary>

- by using `man` command combined with pipeline to `grep` to find specific string in manual page

![Alt text](img/getting%20started/%20Introductory%20Researching/man1.png)  

```text
-r
```

</details>

---

<details>
<summary>
fdisk is a command used to view and alter the partitioning scheme used on your hard drive.

What switch would you use to list the current partitions?
</summary>

- by using `man` command combined with pipeline to `grep` to find specific string in manual page

![Alt text](img/getting%20started/%20Introductory%20Researching/man2.png)

```text
-l
```

</details>

---

<details>
<summary>
nano is an easy-to-use text editor for Linux, There are arguably better editors (Vim, being the obvious choice); however, nano is a great one to start with.

What switch would you use to make a backup when opening a file with nano?
</summary>

- by using `man` command combined with pipeline to `grep` to find specific string in manual page

![Alt text](img/getting%20started/%20Introductory%20Researching/man3.png)

```text
-B
```

</details>

---

<details>
<summary>
Netcat is a basic tool used to manually send and receive network requests.

What command would you use to start netcat in listen mode, using port 12345?
</summary>

- by using `man` command combined with pipeline to `grep` to find specific string in manual page with `-e` ket for each word to find more than one

![Alt text](img/getting%20started/%20Introductory%20Researching/man4.png)

```text
nc -l -p 12345
```

</details>

### Task 5 : Final Thoughts

```text
No answer needed
```
