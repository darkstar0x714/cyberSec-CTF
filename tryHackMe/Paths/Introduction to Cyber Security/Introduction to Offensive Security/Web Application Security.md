# Web Application Security

![banner](imgs/Web%20Application%20Security/roomBanner.png)

## Room objectives

- what is web app.
- some of web app. vulnerabilities
  - brute force
  - injection attacks
  - Identification and Authentication Failure
  - Broken Access Control
  - Cryptographic Failures
  - Insecure Direct Object References (IDOR)

## Tasks

### Task 1 : Introduction

<details>
<summary>
What do you need to access a web application?
</summary>

```
browser
```

</details>

---

### Task 2 : Web Application Security Risks

<details>
<summary>
You discovered that the login page allows an unlimited number of login attempts without trying to slow down the user or lock the account. What is the category of this security risk?
</summary>

```
Identification and Authentication Failure
```

</details>

<details>
<summary>
You noticed that the username and password are sent in clear text without encryption. What is the category of this security risk?
</summary>

```
Cryptographic Failures
```

</details>

---

### Task 3 : Practical Example of Web Application Security

1. after open web app go to **Your Activity** tab.
    ![Alt text](imgs/Web%20Application%20Security/userActivity.png)
2. after try user ID in URL many times we found user 9 called **Alya** working as **Database Administrator** and have access to revert changes in DB.
    ![Alt text](imgs/Web%20Application%20Security/alya.png)
3. after revert all changes the flag will appear.

<details>
<summary>
Check the other users to discover which user account was used to make the malicious changes and revert them. After reverting the changes, what is the flag that you have received?
</summary>

```
THM{IDOR_EXPLORED}
```

</details>
