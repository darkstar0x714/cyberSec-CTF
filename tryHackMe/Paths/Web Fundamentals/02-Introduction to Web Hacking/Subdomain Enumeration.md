# Subdomain Enumeration

![banner](imgs/Subdomain%20Enumeration/roomBanner.png)

## Room objectives

- methods of Subdomain Enumeration
  - Brute Force
    - dnsrecon tool
  - OSINT
    - SSL/TLS Certificates (<https://crt.sh>)
    - Search Engines (Google Dork)
    - Sublist3r tool
  - Virtual Hosts
    - Brute Force using ffuf

## Tasks

### Task 1 : Brief

<details>
<summary>
What is a subdomain enumeration method beginning with B?
</summary>

```
Brute Force
```

</details>

<br>

<details>
<summary>
What is a subdomain enumeration method beginning with O?
</summary>

```
OSINT
```

</details>

<br>

<details>
<summary>
What is a subdomain enumeration method beginning with V?
</summary>

```
Virtual Host
```

</details>

---

### Task 2 : OSINT - SSL/TLS Certificates

<details>
<summary>
What domain was logged on crt.sh at 2020-12-26?
</summary>

<br>

![T2](imgs/Subdomain%20Enumeration/T2.png)

```
store.tryhackme.com
```

</details>

---

### Task 3 : OSINT - Search Engines

<details>
<summary>
What is the TryHackMe subdomain beginning with S discovered using the above Google search?
</summary>

<br>

![T3](imgs/Subdomain%20Enumeration/T3.png)

```
store.tryhackme.com
```

</details>

---

### Task 4 : OSINT - DNS Bruteforce

<details>
<summary>
What is the first subdomain found with the dnsrecon tool?
</summary>

<br>

![T4](imgs/Subdomain%20Enumeration/T4.png)

```
api.acmeitsupport.thm
```

</details>

---

### Task 5 : OSINT - Sublist3r

<details>
<summary>
What is the first subdomain discovered by sublist3r?
</summary>

<br>

![T5](imgs/Subdomain%20Enumeration/T5.png)

```
web55.acmeitsupport.thm
```

</details>

---

### Task 6 : Virtual Hosts

<details>
<summary>
What is the first subdomain discovered?
</summary>

```
delta
```

</details>

<br>

<details>
<summary>
What is the second subdomain discovered?
</summary>

```
yellow
```

</details>
