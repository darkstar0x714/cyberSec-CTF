# Introductory Networking

![Alt text](img/Introductory%20Networking/roomBanner.png)

## Room objectives

- provide a beginner's introduction to the basic principles of networking.
- The OSI Model.
- The TCP/IP Model.
- An introduction to basic networking tools.
- Encapsulation

## Tasks

### Task 1 : Introduction

The aim of this room is to provide a beginner's introduction to the basic principles of networking. Networking is a massive topic, so this really will just be a brief overview; however, it will hopefully give you some foundational knowledge of the topic, which you can build upon for yourself.

<details>
<summary>
Let's get started!
</summary>

```text
No answer needed
```

</details>

### Task 2 :  The OSI Model: An Overview

In practice, it's actually the more compact TCP/IP model that real-world networking is based off; however the OSI model, in many ways, is easier to get an initial understanding from.

<details>
<summary>
Which layer would choose to send data over TCP or UDP?
</summary>

- using `Transport` layer

```text
4
```

</details>

---

<details>
<summary>
Which layer checks received information to make sure that it hasn't been corrupted?
</summary>

- using `Data link` layer

```text
2
```

</details>

---

<details>
<summary>
In which layer would data be formatted in preparation for transmission?
</summary>

- using `Data link` layer

```text
2
```

</details>

---

<details>
<summary>
Which layer transmits and receives data?
</summary>

- using `Physical` layer

```text
1
```

</details>

---

<details>
<summary>
Which layer encrypts, compresses, or otherwise transforms the initial data to give it a standardised format?
</summary>

- using `Presentation` layer

```text
6
```

</details>

---

<details>
<summary>
Which layer tracks communications between the host and receiving computers?
</summary>

- using `Session` layer

```text
5
```

</details>

---

<details>
<summary>
Which layer accepts communication requests from applications?
</summary>

- using `Application` layer

```text
7
```

</details>

---

<details>
<summary>
Which layer handles logical addressing?
</summary>

- using `Network` layer

```text
3
```

</details>

---

<details>
<summary>
When sending data over TCP, what would you call the "bite-sized" pieces of data?
</summary>

the transport layer then divides the transmission up into bite-sized pieces (over TCP these are called segments, over UDP they're called datagrams).

```text
segments
```

</details>

---

<details>
<summary>
[Research] Which layer would the FTP protocol communicate with?
</summary>

```text
7
```

</details>

---

<details>
<summary>
Which transport layer protocol would be best suited to transmit a live video?
</summary>

for faster transportation we should use UDP.

```text
udp
```

</details>

### Task 3 : Encapsulation

As the data is passed down each layer of the model, more information containing details specific to the layer in question is added on to the start of the transmission. As an example, the header added by the Network Layer would include things like the source and destination IP addresses, and the header added by the Transport Layer would include (amongst other things) information specific to the protocol being used. The data link layer also adds a piece on at the end of the transmission, which is used to verify that the data has not been corrupted on transmission; this also has the added bonus of increased security, as the data can't be intercepted and tampered with without breaking the trailer. This whole process is referred to as encapsulation; the process by which data can be sent from one computer to another.

<details>
<summary>
How would you refer to data at layer 2 of the encapsulation process (with the OSI model)?
</summary>

```text
frames
```

</details>

---

<details>
<summary>
How would you refer to data at layer 4 of the encapsulation process (with the OSI model), if the UDP protocol has been selected?
</summary>

```text
datagram
```

</details>

---

<details>
<summary>
What process would a computer perform on a received message?
</summary>

```text
de-encapsulation 
```

</details>

---

<details>
<summary>
Which is the only layer of the OSI model to add a trailer during encapsulation?
</summary>

```text
data link
```

</details>

---

<details>
<summary>
Does encapsulation provide an extra layer of security (Aye/Nay)?
</summary>

- added bonus of increased security, as the data can't be intercepted and tampered with without breaking the trailer.

```text
Aye
```

</details>

### Task 3 : Encapsulation