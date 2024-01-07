# Linux Fundamentals Part 1

![Alt text](img/Linux%20Fundamentals%20Part%202/roomBanner.png)

## Room objectives

- flags and arguments.
- copying and moving files
- access mechanisms
- Running your first few scripts and executables
- Secure Shell SSH connection
- some commands
  - touch
  - mkdir
  - cp
  - mv
  - rm
  - file

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

### Task 2 : Accessing Your Linux Machine Using SSH (Deploy)

- just follow steps in task

<details>
<summary>
I've logged into the Linux Fundamentals Part 2 machine using SSH!
</summary>

```text
No answer needed
```

</details>

### Task 3 : Introduction to Flags and Switches

- read the task and man page

<details>
<summary>
Explore the manual page of the ls command
</summary>

```text
No answer needed
```

</details>

---

<details>
<summary>
What directional arrow key would we use to navigate down the manual page?
</summary>

```text
down
```

</details>

---

<details>
<summary>
What flag would we use to display the output in a "human-readable" way?
</summary>

- by using command `man ls | grep human`
  
  ![alt-text](img/Linux%20Fundamentals%20Part%202/ls.png)

```text
-h
```

</details>

### Task 4 : Filesystem Interaction Continued

- read the task

<details>
<summary>
How would you create the file named "newnote"?
</summary>

```text
touch newnote
```

</details>

---

<details>
<summary>
On the deployable machine, what is the file type of "unknown1" in "tryhackme's" home directory?
</summary>

- by using command `file unknown1`
  
  ![alt-text](img/Linux%20Fundamentals%20Part%202/fileType.png)

```text
ASCII text
```

</details>

---

<details>
<summary>
How would we move the file "myfile" to the directory "myfolder"
</summary>

```text
mv myfile myfolder
```

</details>

---

<details>
<summary>
What are the contents of this file?
</summary>

- by using command `cat myfile`
  
  ![alt-text](img/Linux%20Fundamentals%20Part%202/fileContants.png)

```text
THM{FILESYSTEM}
```

</details>

---

<details>
<summary>
Continue to apply your knowledge and practice the commands from this task.
</summary>

- by using command `cat myfile`
  
  ![alt-text](img/Linux%20Fundamentals%20Part%202/fileContants.png)

```text
No answer needed
```

</details>

### Task 5 : Permissions 101

- read the task and man page

<details>
<summary>
On the deployable machine, who is the owner of "important"?
</summary>

- by list files and folders in dir using `ls -l` we will find
  
  ![alt-text](img/Linux%20Fundamentals%20Part%202/user2.png)

```text
user2
```

</details>

---

<details>
<summary>
What would the command be to switch to the user "user2"?
</summary>

```text
su user2
```

</details>

---

<details>
<summary>
Now switch to this user "user2" using the password "user2"
</summary>

- just make `su user2` and enter `user2` as password

```text
No answer needed
```

</details>

---

<details>
<summary>
Output the contents of "important", what is the flag?
</summary>

- show file contents `cat important`
  ![alt-text](img/Linux%20Fundamentals%20Part%202/user2.png)

```text
THM{SU_USER2}
```

</details>

### Task 6 : Common Directories

- read the task

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
What is the directory path that would we expect logs to be stored in?
</summary>

```text
/var/log
```

</details>

---

<details>
<summary>
What root directory is similar to how RAM on a computer works?
</summary>

```text
/tmp
```

</details>

---

<details>
<summary>
Name the home directory of the root user
</summary>

```text
/root
```

</details>

---

<details>
<summary>
Now apply your learning and navigate through these directories on the deployed Linux machine.
</summary>

```text
No answer needed
```

</details>

### Task 7 : Conclusions and Summaries

<details>
<summary>
Proceed to the next task to continue your learning
</summary>

```text
No answer needed
```

</details>

### Task 8 : Linux Fundamentals Part 3

<details>
<summary>
Terminate the machine from task 2!
</summary>

```text
No answer needed
```

</details>

---

<details>
<summary>
Join Linux Fundamentals Part 3!
</summary>

```text
No answer needed
```

</details>
