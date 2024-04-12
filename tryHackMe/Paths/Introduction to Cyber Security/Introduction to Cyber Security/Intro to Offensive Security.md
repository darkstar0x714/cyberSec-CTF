# Intro to Offensive Security

![banner](imgs/Intro%20to%20Offensive%20Security/roomBanner.png)

## Room objectives

- hack your first machine
- know path traversal vulnerability
- basic use of GoBuster

## Tasks

### Task 1

just read the tutorial to know difference between  Offensive Security & Defensive Security

<details>
<summary>
Which of the following options better represents the process where you simulate a hacker's actions to find vulnerabilities in a system?
</summary>

```
Offensive Security
```

</details>

### Task 2

1. start the machine
2. go to link `http://fakebank.com`
   ![Alt text](imgs/Intro%20to%20Offensive%20Security/siteHome.png)
3. run GoBuster to search for hidden dir `gobuster -u http://fakebank.com -w wordlist.txt dir`
4. you will get response 200 on page called `/bank-transfer`
   ![Alt text](imgs/Intro%20to%20Offensive%20Security/gobuster.png)
5. Transfer $2000 from the bank account 2276, to your account (account number 8881).
    ![Alt text](imgs/Intro%20to%20Offensive%20Security/transfare.png)
6. return to home.

<details>
<summary>
Above your account balance, you should now see a message indicating the answer to this question. Can you find the answer you need?
</summary>

```
BANK-HACKED
```

</details>
  
---

<details>
<summary>
If you were a penetration tester or security consultant, this is an exercise you’d perform for companies to test for vulnerabilities in their web applications; find hidden pages to investigate for vulnerabilities.
</summary>

```
No answer needed
```

</details>

---

<details>
<summary>
Terminate the machine by clicking the red "Terminate" button at the top of the page.
</summary>

```
No answer needed
```

</details>

### Task 3

just read the success stores

<details>
<summary>
Read the above, and continue with the next room!
</summary>

```
No answer needed
```

</details>
