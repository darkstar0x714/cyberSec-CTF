# Content Discovery

![banner](imgs/Content%20Discovery/roomBanner.png)

## Room objectives

- methods of Content Discovery :
  - manual
  - automated
  - OSINT

## Tasks

### Task 1 : What Is Content Discovery?

<details>
<summary>
What is the Content Discovery method that begins with M?
</summary>

```
Manually
```

</details>

<br>

<details>
<summary>
What is the Content Discovery method that begins with A?
</summary>

```
Automated
```

</details>

<br>

<details>
<summary>
What is the Content Discovery method that begins with O?
</summary>

```
OSINT
```

</details>

---

### Task 2 : Manual Discovery - Robots.txt

<details>
<summary>
What is the directory in the robots.txt that isn't allowed to be viewed by web crawlers?
</summary>

![T2](imgs/Content%20Discovery/T2.png)

<br>

```
/staff-portal
```

</details>

---

### Task 3 : Manual Discovery - Favicon

<details>
<summary>
What framework did the favicon belong to?
</summary>

`after get MD5sum hash we search at : https://wiki.owasp.org/index.php/OWASP_favicon_database`

![T3](imgs/Content%20Discovery/T3_1.png)

<br>

![T3](imgs/Content%20Discovery/T3_2.png)

```
cgiirc
```

</details>

---

### Task 4 : Manual Discovery - Sitemap.xml

<details>
<summary>
What is the path of the secret area that can be found in the sitemap.xml file?
</summary>

![T4](imgs/Content%20Discovery/T4.png)

```
/s3cr3t-area
```

</details>

---

### Task 5 : Manual Discovery - HTTP Headers

<details>
<summary>
What is the flag value from the X-FLAG header?
</summary>

![T5](imgs/Content%20Discovery/T5.png)

```
THM{HEADER_FLAG}
```

</details>

---

### Task 6 : Manual Discovery - Framework Stack

<details>
<summary>
What is the flag from the framework's administration portal?
</summary>

![T6](imgs/Content%20Discovery/T6_1.png)

<br>

![T6](imgs/Content%20Discovery/T6_2.png)

```
THM{CHANGE_DEFAULT_CREDENTIALS}
```

</details>

---

### Task 7 : OSINT - Google Hacking / Dorking

<details>
<summary>
What Google dork operator can be used to only show results from a particular site?
</summary>

```
site:
```

</details>

---

### Task 8 : OSINT - Wappalyzer

<details>
<summary>
What online tool can be used to identify what technologies a website is running?
</summary>

```
Wappalyzer
```

</details>

---

### Task 9 : OSINT - Wayback Machine

<details>
<summary>
What is the website address for the Wayback Machine?
</summary>

```
https://archive.org/web/
```

</details>

---

### Task 10 : OSINT - GitHub

<details>
<summary>
What is Git?
</summary>

```
version control system
```

</details>

---

### Task 11 : OSINT - S3 Buckets

<details>
<summary>
What URL format do Amazon S3 buckets end in?
</summary>

```
.s3.amazonaws.com
```

</details>

---

### Task 12 : Automated Discovery

<br>

![T12](imgs/Content%20Discovery/T12.png)

<details>
<summary>
What is the name of the directory beginning "/mo...." that was discovered?
</summary>

```
/monthly
```

</details>

<br>

<details>
<summary>
What is the name of the log file that was discovered?
</summary>

```
/development.log
```

</details>
