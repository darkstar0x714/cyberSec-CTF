# Intro to SSRF

![banner](imgs/Intro%20to%20SSRF/roomBanner.png)

## Room objectives

- what is SSRF?
- Types of SSRF
  - regular SSRF
  - Blind SSRF
- SSRF impact?
- Finding an SSRF methods

## Tasks

### Task 1 : What is an SSRF?

<details>
<summary>
What does SSRF stand for?
</summary>

```
Server-Side Request Forgery
```

</details>

<br>

<details>
<summary>
As opposed to a regular SSRF, what is the other type?
</summary>

```
Blind
```

</details>

---

### Task 2 : SSRF Examples

<details>
<summary>
What is the flag from the SSRF Examples site?
</summary>

<br>

1. after edit request URL `https://website.thm/item/2?server=server.website.thm/flag?id=9`
2. but we got nothing so we add `&` symbol to end of URL `https://website.thm/item/2?server=server.website.thm/flag?id=9&`
3. we got `https://website.thm/item/2?server=server.website.thm/flag?id=9&.website.thm/api/item?id=2` as requested from server so for the browser & is the end of url and we bypassed the protection and got the flag.

![flag](imgs/Intro%20to%20SSRF/T2.png)

```
THM{SSRF_MASTER}
```

</details>

---

### Task 3 : Finding an SSRF

<details>
<summary>
What website can be used to catch HTTP requests from a server?
</summary>

```
requestbin.com
```

</details>

---

### Task 4 : Defeating Common SSRF Defenses

<details>
<summary>
What method can be used to bypass strict rules?
</summary>

```
Open Redirect
```

</details>

<br>

<details>
<summary>
What IP address may contain sensitive data in a cloud environment?
</summary>

```
169.254.169.254
```

</details>

<br>

<details>
<summary>
What type of list is used to permit only certain input?
</summary>

```
Allow List
```

</details>

<br>

<details>
<summary>
What type of list is used to stop certain input?
</summary>

```
Deny List
```

</details>

---

### Task 5 : SSRF Practical

<details>
<summary>
What is the flag from the /private directory?
</summary>

<br>

1. at first we visit `https://10-10-41-185.p.thmlabs.com/customers/new-account-page` and make an account.

   ![flag](imgs/Intro%20to%20SSRF/T5_1.png)

2. after choose any avatar and press `submit` we got the avatar.

   ![flag](imgs/Intro%20to%20SSRF/T5_2.png)

3. by open inspect tool and change the requested link to many payload all of them fail till i make link is `assets/../private` with this track we got some thing interesting the avatar disappeared!

   ![flag](imgs/Intro%20to%20SSRF/T5_3.png)

4. after carefully check the page code we got an base64 encoding value `VEhNe1lPVV9XT1JLRURfT1VUX1RIRV9TU1JGfQ==`
5. we used [cyberChef](https://gchq.github.io/CyberChef/#recipe=From_Base64('A-Za-z0-9%2B/%3D',true,false)&input=VkVoTmUxbFBWVjlYVDFKTFJVUmZUMVZVWDFSSVJWOVRVMUpHZlE9PQ) to decode it and we got the flag.

```
THM{YOU_WORKED_OUT_THE_SSRF}
```

</details>
