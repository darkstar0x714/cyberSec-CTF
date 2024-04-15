# Intro to Defensive Security

![banner](imgs/Intro%20to%20Defensive%20Security/roomBanner.png)

## Room objectives

- difference between  Offensive Security & Defensive Security.
- some of blue team roles [security awareness - managing assets - patching systems - Setting up security devices]
- some blue team jobs:-
  - Security Operations Center (SOC) : mainly work in [Unauthorized activity and Network intrusions detection - Policy violations from outsiders or insiders - installing a proper update or patch for discovered vulnerability]
  - Threat Intelligence : gather about actual and potential enemies, by collect data from internal sources like logs and external like forums into a format suitable for analysis to know more about attackers, it aims to create a list of recommendations and actionable steps.
  - Digital Forensics and Incident Response (DFIR): analyzing evidence of an attack to know who and how attack is done, Incident response specifies the methodology that should be followed to handle different attack scenarios.
  - Malware Analysis: Malware analysis aims to learn about such malicious programs.
- what is SIEM.

## Tasks

### Task 1 : Introduction to Defensive Security

just read the tutorial to know difference between  Offensive Security & Defensive Security and some of blue team roles.

<details>
<summary>
Which team focuses on defensive security?
</summary>

```
blue team
```

</details>

### Task 2 : Areas of Defensive Security

just read the tutorial to know difference between different blue team jobs.

<details>
<summary>
What would you call a team of cyber security professionals that monitors a network and its systems for malicious events?
</summary>

```
security operation center
```

</details>

---

<details>
<summary>
What does DFIR stand for?
</summary>

```
digital forensics and incident respond
```

</details>

---

<details>
<summary>
Which kind of malware requires the user to pay money to regain access to their files?
</summary>

```
ransomware
```

</details>

### Task 3 : Practical Example of Defensive Security

practical DFIR role play.

1. start the machine
2. take the IP of red alert and press on red alert
   ![Alt text](imgs/Intro%20to%20Defensive%20Security/challangeUI.png)
3. search on IP scanner of malicious IPs in sites like AbuseIPDB.
   ![Alt text](imgs/Intro%20to%20Defensive%20Security/alertIP.png)
4. after notify SOC team block the IP.
   ![Alt text](imgs/Intro%20to%20Defensive%20Security/blockIP.png)

<details>
<summary>
What is the flag that you obtained by following along?
</summary>

```
THM{THREAT-BLOCKED}
```

</details>
