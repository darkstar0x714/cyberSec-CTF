# HTTP in Detail

![banner](imgs/HTTP%20in%20Detail/roomBanner.png)

## Room objectives

- what is HTTP?
- what is HTTPS?
- Requests And Responses
- headers
- HTTP Methods
- HTTP Status Codes
- intro to Cookies

## Tasks

### Task 1 : What is HTTP(S)?

<details>
<summary>
What does HTTP stand for?
</summary>

```
hyper text transfer protocol
```

</details>

<details>
<summary>
What does the S in HTTPS stand for?
</summary>

```
Secure
```

</details>

<details>
<summary>
On the mock webpage on the right there is an issue, once you've found it, click on it. What is the challenge flag?
</summary>

`the site is not secure with https certificate`

```
THM{INVALID_HTTP_CERT}
```

</details>

---

### Task 2 : Requests And Responses

<details>
<summary>
What HTTP protocol is being used in the above example?
</summary>

```
http/1.1
```

</details>

<details>
<summary>
What response header tells the browser how much data to expect?
</summary>

```
content-Length 
```

</details>

---

### Task 3 : HTTP Methods

<details>
<summary>
What method would be used to create a new user account?
</summary>

```
post
```

</details>

<details>
<summary>
What method would be used to update your email address?
</summary>

```
put 
```

</details>

<details>
<summary>
What method would be used to remove a picture you've uploaded to your account?
</summary>

```
delete 
```

</details>

<details>
<summary>
What method would be used to view a news article?
</summary>

```
get 
```

</details>

---

### Task 4 : HTTP Status Codes

<details>
<summary>
What response code might you receive if you've created a new user or blog post article?
</summary>

```
201
```

</details>

<details>
<summary>
What response code might you receive if you've tried to access a page that doesn't exist?
</summary>

```
404 
```

</details>

<details>
<summary>
What response code might you receive if the web server cannot access its database and the application crashes?
</summary>

```
503 
```

</details>

<details>
<summary>
What response code might you receive if you try to edit your profile without logging in first?
</summary>

```
401 
```

</details>

---

### Task 5 : Headers

<details>
<summary>
What header tells the web server what browser is being used?
</summary>

```
User-Agent
```

</details>

<details>
<summary>
What header tells the browser what type of data is being returned?
</summary>

```
Content-Type 
```

</details>

<details>
<summary>
What header tells the web server which website is being requested?
</summary>

```
Host 
```

</details>

---

### Task 6 : Cookies

<details>
<summary>
Which header is used to save cookies to your computer?
</summary>

```
set-cookies
```

</details>

---

### Task 7 : Making Requests

<details>
<summary>
Make a GET request to /room
</summary>

![parameters](imgs/HTTP%20in%20Detail/room.png)

```
THM{YOU'RE_IN_THE_ROOM}
```

</details>

<details>
<summary>
Make a GET request to /blog and using the gear icon set the id parameter to 1 in the URL field
</summary>

![parameters](imgs/HTTP%20in%20Detail/id1.png)

![get request](imgs/HTTP%20in%20Detail/id2.png)

```
THM{YOU_FOUND_THE_BLOG}
```

</details>

<details>
<summary>
Make a DELETE request to /user/1
</summary>

![post request](imgs/HTTP%20in%20Detail/delete.png)

```
THM{USER_IS_DELETED}
```

</details>

<details>
<summary>
Make a PUT request to /user/2 with the username parameter set to admin
</summary>

![parameters](imgs/HTTP%20in%20Detail/put1.png)

![put request](imgs/HTTP%20in%20Detail/put2.png)

```
THM{USER_HAS_UPDATED}
```

</details>

<details>
<summary>
POST the username of thm and a password of letmein to /login
</summary>

![parameters](imgs/HTTP%20in%20Detail/post1.png)

![post request](imgs/HTTP%20in%20Detail/post2.png)

```
THM{HTTP_REQUEST_MASTER}
```

</details>
