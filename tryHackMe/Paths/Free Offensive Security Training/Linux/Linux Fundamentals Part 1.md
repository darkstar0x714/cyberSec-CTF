# Linux Fundamentals Part 1

![Alt text](img/Linux%20Fundamentals%20Part%201/roomBanner.png)

## Room objectives

- what is linux operating system?
- Running your very first commands on linux os.
- learn essential commands used to interact with the file system.
- Flavours of Linux?!
- some commands
  - echo
  - whoami
  - ls
  - nano
  - cd
  - pwd
  - cat
  - find
  - locate
  - grep
- Linux operators
  - &
  - &&
  - |
  - ||
  - >
  - >>

## Tasks

### Task 1 : Introduction

Welcome to the first part of the "Linux Fundamentals" room series. You're most likely using a Windows or Mac machine, both are different in visual design and how they operate. Just like Windows, iOS and MacOS, Linux is just another operating system and one of the most popular in the world powering smart cars, android devices, supercomputers, home appliances, enterprise servers, and more.

<details>
<summary>
Let's get started!
</summary>

```text
No answer needed
```

</details>

### Task 2 : A Bit of Background on Linux

just an example about how to search google is your friend

<details>
<summary>
Research: What year was the first release of a Linux operating system?
</summary>

- just search oon google `linux release year` you will find the answer `September 17, 1991`

```text
1991
```

</details>

### Task 3 : Interacting With Your First Linux Machine (In-Browser)

- just `Start Machine` and `Split Screen` from page header.

<details>
<summary>
I've deployed my first Linux machine!
</summary>

```text
No answer needed
```

</details>

### Task 4 : Running Your First few Commands

<details>
<summary>
If we wanted to output the text "TryHackMe", what would our command be?
</summary>

```text
echo TryHackMe
```

</details>

---

<details>
<summary>
What is the username of who you're logged in as on your deployed Linux machine?
</summary>

![Alt text](img/Linux%20Fundamentals%20Part%201/whoami.png)

```text
tryhackme
```

</details>

### Task 5 : Interacting With the Filesystem

<details>
<summary>
On the Linux machine that you deploy, how many folders are there?
</summary>

- using `ls` command

    ![Alt text](img/Linux%20Fundamentals%20Part%201/ls.png)

```text
4
```

</details>

---

<details>
<summary>
Which directory contains a file?
</summary>

- you can traverse manually through each folder using `cd folder1 && ls`
- or just write a traversal bash code to do the job for us.

    ```bash
    #!/bin/bash
    for n in {1..4}; do
    folder="folder$n"
    cd "$folder" && ls && pwd && cd ..
    done
    ```

- then save it in script.sh `nano script.sh`
- make it executable `chmod +x script.sh`
- run it `./script.sh`

    ![Alt text](img/Linux%20Fundamentals%20Part%201/script.png)

```text
folder4
```

</details>

---

<details>
<summary>
What is the contents of this file?
</summary>

- go t path and print note.txt `cd /home/tryhackme/folder4 && cat note.txt`

    ![Alt text](img/Linux%20Fundamentals%20Part%201/note.png)

```text
Hello World
```

</details>

---

<details>
<summary>
Use the cd command to navigate to this file and find out the new current working directory. What is the path?
</summary>

![Alt text](img/Linux%20Fundamentals%20Part%201/note.png)

```text
/home/tryhackme/folder4
```

</details>

### Task 6 : Searching for Files

just read the tutorial

<details>
<summary>
Use grep on "access.log" to find the flag that has a prefix of "THM". What is the flag?
</summary>

![Alt text](img/Linux%20Fundamentals%20Part%201/flag.png)

```text
THM{ACCESS}
```

</details>

---

<details>
<summary>
And I still haven't found what I'm looking for!
</summary>

```text
No answer needed
```

</details>

### Task 7 : An Introduction to Shell Operators

just read the tutorial

<details>
<summary>
If we wanted to run a command in the background, what operator would we want to use?
</summary>

```text
&
```

</details>

---

<details>
<summary>
If I wanted to replace the contents of a file named "passwords" with the word "password123", what would my command be?
</summary>

```text
echo password123 > passwords
```

</details>

---

<details>
<summary>
Now if I wanted to add "tryhackme" to this file named "passwords" but also keep "passwords123", what would my command be
</summary>

```text
echo tryhackme >> passwords
```

</details>

---

<details>
<summary>
Now use the deployed Linux machine to put these into practice
</summary>

```text
No answer needed
```

</details>

### Task 8 : Conclusions & Summaries

<details>
<summary>
I'll have a play around!
</summary>

```text
No answer needed
```

</details>

### Task 9 : Linux Fundamentals Part 2

<details>
<summary>
Terminate the machine deployed in this room from task 3.
</summary>

```text
No answer needed
```

</details>

---

<details>
<summary>
Join Linux Fundamentals Part 2!
</summary>

```text
No answer needed
```

</details>
