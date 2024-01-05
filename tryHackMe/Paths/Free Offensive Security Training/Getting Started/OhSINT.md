# OhSINT

![room banner](img/getting%20started/OhSINT/roomBanner.png)

## Room objectives

- use open source intelligence to find info. about your target.
- learn about some data extractions tools [google search - strings - binwalk - steghide - exiftool].

## Flags

### Task 1 : OhSINT

<details>
<summary>
What is this user's avatar of?
</summary>

1. after download lap attached file we will find an image
2. first start by using google photos search but the photo was too famous to find any specific info about the target
3. used `strings WindowsXP.jpg` to get all ascii values inside img
    ![Alt text](img/getting%20started/OhSINT/strings.png)
4. use `exiftool WindowsXP.jpg` to get same data with readable format.
   ![Alt text](img/getting%20started/OhSINT/exiftool.png)
5. by searching in google about `OWoodflint` we will find X (twitter) account
    ![Alt text](img/getting%20started/OhSINT/accountProfiles.png)

```text
cat
```

</details>

---

<details>
<summary>
What city is this person in?
</summary>

1. from the pervious question `step 4` we will find GPS coordinates after we search about it `54 deg 17' 41.27" N, 2 deg 15' 1.33" W` we will find this location.
   ![Alt text](img/getting%20started/OhSINT/location.png)

    so as you notice the place is middle of no where and it was misinformation
2. after go back to google search in `step 5` we will find github account with this username
   ![Alt text](img/getting%20started/OhSINT/github.png)

```text
London
```

</details>

---

<details>
<summary>
What is the SSID of the WAP he connected to?
</summary>

1. from the first question `step 5` we get a wifi MAC address.
2. by using `https://wigle.net/` site and login we will get wifi name in london.
   ![Alt text](img/getting%20started/OhSINT/wifiName.png)

```text
UnileverWiFi
```

</details>

---

<details>
<summary>
What is his personal email address?
</summary>

1. from the second question `step 2` we get Email address.

```text
OWoodflint@gmail.com
```

</details>

---

<details>
<summary>
What site did you find his email address on?
</summary>

1. from the second question `step 2` we found this info on github account.

```text
Github
```

</details>
https://oliverwoodflint.wordpress.com/author/owoodflint/

---

<details>
<summary>
Where has he gone on holiday?
</summary>

1. from the first question `step 5` in google we will find wordpress blog `https://oliverwoodflint.wordpress.com/author/owoodflint/`.
   ![Alt text](img/getting%20started/OhSINT/wordpress.png)

```text
New York
```

</details>

---

<details>
<summary>
What is the person's password?
</summary>

1. from blog post open page source code we will find the password.
   ![Alt text](img/getting%20started/OhSINT/passcode.png)

```text
pennYDr0pper.!
```

</details>
