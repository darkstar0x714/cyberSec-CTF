# Packets & Frames

![banner](imgs/Packets_Frames/roomBanner.png)

## Room objectives

- difference between packets and frame
- some of packet headers
  - Time To Live
  - Checksum
  - Source Address
  - Destination Address
- difference between TCP and UDP
- what is ports?
- [most famous ports](http://www.vmaxx.net/techinfo/ports.htm)
  - File Transfer Protocol (FTP) on 21
  - Secure Shell (SSH) on 22
  - HyperText Transfer Protocol (HTTP) on 80
  - HyperText Transfer Protocol Secure (HTTPS) on 443
  - Server Message Block (SMB) on 445
  - Remote Desktop Protocol (RDP) on 3389

## Tasks

### Task 1 : What are Packets and Frames

<details>
<summary>
What is the name for a piece of data when it does have IP addressing information?
</summary>

```
packet
```

</details>

<details>
<summary>
What is the name for a piece of data when it does not have IP addressing information?
</summary>

```
frame
```

</details>

---

### Task 2 : TCP/IP (The Three-Way Handshake)

<details>
<summary>
What is the header in a TCP packet that ensures the integrity of data?
</summary>

```
Checksum
```

</details>

<details>
<summary>
Provide the order of a normal Three-way handshake (with each step separated by a comma)
</summary>

```
SYN,SYN/Ack,ACk
```

</details>

---

### Task 3 : Practical - Handshake

<details>
<summary>
What is the value of the flag given at the end of the conversation?
</summary>

```
THM{TCP_CHATTER}
```

</details>

---

### Task 4 : UDP/IP

<details>
<summary>
What does the term "UDP" stand for?
</summary>

```
User Datagram Protocol
```

</details>

<details>
<summary>
What type of connection is "UDP"?
</summary>

```
stateless
```

</details>
<details>
<summary>
What protocol would you use to transfer a file?
</summary>

```
tcp
```

</details>
<details>
<summary>
What protocol would you use to have a video call?
</summary>

```
udp
```

</details>

---

### Task 5 : Ports 101 (Practical)

<details>
<summary>
What is the flag received from the challenge?
</summary>

```
THM{YOU_CONNECTED_TO_A_PORT}
```

</details>

---

### Task 6 : Continue Your Learning: Extending Your Network

<details>
<summary>
Terminate the static site lab deployed in tasks 3 and 5.
</summary>

```
No answer needed
```

</details>

<details>
<summary>
Join the "Extending Your Network" room to continue your learning.
</summary>

```
No answer needed
```

</details>
