# Intro to Digital Forensics

![banner](imgs/Intro%20to%20Digital%20Forensics/roomBanner.png)

## Room objectives

- what is Digital Forensics
- process of collecting and Process Digital Forensics
- explore files meta data
- some tools:
  - pdfinfo
  - exiftool

## Tasks

### Task 1 : Introduction To Digital Forensics

<details>
<summary>
Consider the desk in the photo above. In addition to the smartphone, camera, and SD cards, what would be interesting for digital forensics?
</summary>

```
laptop
```

</details>

---

### Task 2 : Digital Forensics Process

<details>
<summary>
It is essential to keep track of who is handling it at any point in time to ensure that evidence is admissible in the court of law. What is the name of the documentation that would help establish that?
</summary>

```
chain of custody
```

</details>

---

### Task 3 : Practical Example of Digital Forensics

1. after download digital assets and extract it.
2. use `pdfinfo` tool to analyze pdf file `pdfinfo ransom-letter.pdf`
    ![img](imgs/Intro%20to%20Digital%20Forensics/pdfinfo.png)

<details>
<summary>
Using pdfinfo, find out the author of the attached PDF file, ransom-letter.pdf.
</summary>

```
Ann Gree Shepherd
```

</details>

---

1. use `exiftool` tool to extract img meta data and search for GPS `exiftool letter-image.jpg | grep gps -i`
2. search for this coordinates in google maps
    ![img](imgs/Intro%20to%20Digital%20Forensics/gpsLocation.png)

<details>
<summary>
Using exiftool or any similar tool, try to find where the kidnappers took the image they attached to their document. What is the name of the street?
</summary>

```
milk street
```

</details>

---

1. use `exiftool` tool to extract img meta data and search for model `exiftool letter-image.jpg | grep model -i`
    ![img](imgs/Intro%20to%20Digital%20Forensics/camModel.png)

<details>
<summary>
What is the model name of the camera used to take this photo?
</summary>

```
Canon EOS R6
```

</details>
