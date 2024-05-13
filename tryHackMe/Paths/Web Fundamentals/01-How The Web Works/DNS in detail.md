# DNS in detail

![banner](imgs/DNS%20in%20detail/roomBanner.png)

## Room objectives

- what is DNS?
- Domain Hierarchy
- Domain levels
  - TLD
  - Second-Level Domain
  - Subdomain
- Record Types
  - A
  - AAAA
  - CNAME
  - MX
  - TXT
- DNS Types
  - Recursive DNS
  - Root DNS
  - Authoritative DNS

## Tasks

### Task 1 : What is DNS?

<details>
<summary>
What does DNS stand for?
</summary>

```
Domain Name System
```

</details>

---

### Task 2 : Domain Hierarchy

<details>
<summary>
What is the maximum length of a subdomain?
</summary>

```
63
```

</details>

<details>
<summary>
Which of the following characters cannot be used in a subdomain ( 3 b _ - )?
</summary>

```
_
```

</details>

<details>
<summary>
What is the maximum length of a domain name?
</summary>

```
253
```

</details>

<details>
<summary>
What type of TLD is .co.uk?
</summary>

```
ccTLD
```

</details>

---

### Task 3 : Record Types

<details>
<summary>
What type of record would be used to advise where to send email?
</summary>

```
MX
```

</details>

<details>
<summary>
What type of record handles IPv6 addresses?
</summary>

```
AAAA
```

</details>

---

### Task 4 : Making A Request

<details>
<summary>
What field specifies how long a DNS record should be cached for?
</summary>

```
TTL
```

</details>

<details>
<summary>
What type of DNS Server is usually provided by your ISP?
</summary>

```
recursive
```

</details>

<details>
<summary>
What type of server holds all the records for a domain?
</summary>

```
authoritative
```

</details>

---

### Task 5 : Practical

<details>
<summary>
What is the CNAME of shop.website.thm?
</summary>

![cname](imgs/DNS%20in%20detail/cname.png)

```
shops.myshopify.com
```

</details>

<details>
<summary>
What is the value of the TXT record of website.thm?
</summary>

![txt](imgs/DNS%20in%20detail/txt.png)

```
THM{7012BBA60997F35A9516C2E16D2944FF}
```

</details>

<details>
<summary>
What is the numerical priority value for the MX record?
</summary>

![mx](imgs/DNS%20in%20detail/mx.png)

```
30
```

</details>

<details>
<summary>
What is the IP address for the A record of www.website.thm?
</summary>

![A](imgs/DNS%20in%20detail/A.png)

```
10.10.10.10
```

</details>
