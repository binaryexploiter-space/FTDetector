# **FTDetector**

A lightweight and interactive Python tool for identifying file types
using **magic header detection**, generating **MD5** and **SHA-256**
hashes, and performing **VirusTotal lookups**.\
Perfect for CTF challenges, malware analysis, DFIR, and general file
inspection.

------------------------------------------------------------------------

## **✨ Features**

### 🔍 Magic Header Detection

Detects file types using known magic bytes from the file's header.
Supports a wide range of common formats and can be expanded easily.

### 🔐 Hash Generation

FTDetector calculates the following: - **MD5** - **SHA-256**

### 🧪 VirusTotal Integration

-   Performs hash-based lookups using the VirusTotal API\
-   Fetches metadata and detection information\
-   Optionally saves VirusTotal JSON reports locally

### 💾 JSON Report Saving

VirusTotal responses can be saved automatically as:

    vt_<sha256>.json

### 🖥️ Interactive Usage

No command-line arguments required. Simply run the tool and enter the
file path when prompted.

------------------------------------------------------------------------

## **📥 Installation**

Install the required Python modules:

``` bash
pip install requests
pip install hashlib
```

> **Note:** `hashlib` is included in Python's standard library.

------------------------------------------------------------------------

## **🔑 VirusTotal Setup**

Create a file named:

    virustotalapi.txt

Place your VirusTotal API key inside it:

    YOUR_API_KEY_HERE

FTDetector will automatically load this key when performing lookups.

------------------------------------------------------------------------

## **🚀 How to Use**

1.  Run FTDetector:

    ``` bash
    python ftdetector.py
    ```

2.  Enter the path of the file you want to analyze\

3.  FTDetector will:

    -   Detect the magic header\
    -   Identify the file type\
    -   Generate MD5 and SHA-256 hashes\
    -   Ask if you want to perform a VirusTotal scan\
    -   Offer to save the JSON output

------------------------------------------------------------------------

## **📚 Magic Header Support**

FTDetector includes signatures for many common file formats, such as:

  Magic Bytes                        File Type
  ---------------------------------- --------------------------
  `4D5A`                             Windows Executable (MZ)
  `50450000`                         PE (EXE/DLL/SYS/OCX/CPL)
  `89504E47`                         PNG Image
  `25504446`                         PDF Document
  `FFD8FFE0` / `FFD8FFE1`            JPEG Image
  `4D4C5649`                         Magic Lantern MLV Video
  ... additional formats supported   

You can easily add more signatures by modifying the magic-byte
dictionary in the script.

------------------------------------------------------------------------

## **🛠️ Why FTDetector?**

-   Fast and lightweight\
-   Accurate signature-based detection\
-   Helpful for malware triage and digital forensics\
-   Ideal for CTF engineers\
-   Never executes or modifies files\
-   Easily extensible

------------------------------------------------------------------------

### Created By **binaryexploiter**
