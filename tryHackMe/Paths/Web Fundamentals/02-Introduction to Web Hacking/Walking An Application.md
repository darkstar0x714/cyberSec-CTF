# Walking An Application

![banner](imgs/Walking%20An%20Application/roomBanner.png)

## Room objectives

- use manual web site discovering tools.
- built browser tools for discovering :
  - view source
  - Inspector
  - Debugger
  - Network

## Tasks

### Task 1 : Walking An Application

<details>
<summary>
I confirm that I have deployed the virtual machine and opened the website.
</summary>

```
No answer needed
```

</details>

---

### Task 2 : Exploring The Website

<details>
<summary>
Read the above.
</summary>

```
No answer needed
```

</details>

---

### Task 3 : Viewing The Page Source

<details>
<summary>
What is the flag from the HTML comment?
</summary>

`just after open page source you will find commented page with the flag`

![T3_1_1](imgs/Walking%20An%20Application/Task3_1_1.png)

<br>

![T3_1_2](imgs/Walking%20An%20Application/Task3_1_2.png)

```
THM{HTML_COMMENTS_ARE_DANGEROUS}
```

</details>

<br>

<details>
<summary>
What is the flag from the secret link?
</summary>

![T3_2_1](imgs/Walking%20An%20Application/Task3_2_1.png)

<br>

![T3_2_2](imgs/Walking%20An%20Application/Task3_2_2.png)

```
THM{NOT_A_SECRET_ANYMORE}
```

</details>

<br>

<details>
<summary>
What is the directory listing flag?
</summary>

`open page sources`

![T3_3_1](imgs/Walking%20An%20Application/Task3_3_1.png)

<br>

![T3_3_2](imgs/Walking%20An%20Application/Task3_3_2.png)

<br>

![T3_3_3](imgs/Walking%20An%20Application/Task3_3_3.png)

```
THM{INVALID_DIRECTORY_PERMISSIONS}
```

</details>

<br>

<details>
<summary>
What is the framework flag?
</summary>

![T3_4_1](imgs/Walking%20An%20Application/Task3_4_1.png)

<br>

![T3_4_2](imgs/Walking%20An%20Application/Task3_4_2.png)

<br>

![T3_4_3](imgs/Walking%20An%20Application/Task3_4_3.png)

<br>

![T3_4_4](imgs/Walking%20An%20Application/Task3_4_4.png)

```
THM{KEEP_YOUR_SOFTWARE_UPDATED}
```

</details>

---

### Task 4 : Developer Tools - Inspector

<details>
<summary>
What is the flag behind the paywall?
</summary>

`open Inspector and choose the selecting element tool and select element you want to edit and edit its css properties or delete it from page code`

![T4_1_1](imgs/Walking%20An%20Application/Task4_1_1.png)

<br>

![T4_1_2](imgs/Walking%20An%20Application/Task4_1_2.png)

<br>

![T4_1_3](imgs/Walking%20An%20Application/Task4_1_3.png)

<br>

![T4_1_4](imgs/Walking%20An%20Application/Task4_1_4.png)

```
THM{NOT_SO_HIDDEN}
```

</details>

---

### Task 5 : Developer Tools - Debugger

<details>
<summary>
What is the flag in the red box?
</summary>

`open contact page then sources and make break point in remove flag`

![T5_1_1](imgs/Walking%20An%20Application/Task5_1_1.png)

<br>

![T5_1_2](imgs/Walking%20An%20Application/Task5_1_2.png)

<br>

```
THM{CATCH_ME_IF_YOU_CAN}
```

</details>

---

### Task 6 : Developer Tools - Network

<details>
<summary>
What is the flag shown on the contact-msg network request?
</summary>

`open contact page then network and write any message we got required request with flag as shown in 1st img but it wrong after more search in tap we got right flag`

![T6_1_1](imgs/Walking%20An%20Application/Task6_1_1.png)

<br>

![T6_1_2](imgs/Walking%20An%20Application/Task6_1_2.png)

<br>

```
THM{GOT_AJAX_FLAG}
```

</details>
