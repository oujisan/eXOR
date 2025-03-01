# 🔐 **eXOR (XOR Cipher)**

A simple and flexible XOR-based encryption and decryption tool for text and files. Supports keys in string or hexadecimal format, ideal for basic data obfuscation needs.

---

## ✨ **Main Features**

✅ Encrypt and decrypt text and files.\
✅ Supports keys in **string** or **hexadecimal** format.\
✅ Compatible with multiple operating systems (Windows, Linux, macOS, Android).

---

## 📥 **Installation and Usage**

### 1. 🐍 **Prepare Python**

Ensure **Python 3.13.1** or a newer version is installed on your system:

- **Windows**: Download from [python.org](https://www.python.org/downloads/).
- **Linux/macOS**: Use your system's package manager like `apt`, `yum`, or `brew`.

### 2. 📂 **Download eXOR**

Clone the repository from GitHub to your local directory:

```bash
git clone https://github.com/oujisan/eXOR.git
cd eXOR
```

### 3. 🛠️ **Configure PATH**

#### ➤ **Windows**:

1. Press `Win + R`, type `sysdm.cpl`, and press **Enter**.
2. Select **Advanced** → click **Environment Variables**.
3. Add the **eXOR** directory path to **Path**. Example:

```
C:\Users\oujisan\eXOR
```

#### ➤ **Linux/macOS**:

Run the installation script:

```bash
chmod +x install.sh
./install.sh
```

### 4. ✅ **Verify Installation**

Ensure eXOR is installed correctly by running:

```bash
exor --help
```

💡 **If you encounter errors** or want to run it manually, use:

```bash
python exor.py
```

---

## 📊 **Argument Documentation**

### 📌 **Basic Syntax:**

```bash
exor [MODE] [INPUT] [KEY] [OUTPUT]
```

### 📌 **Argument Options:**

| Option                 | Description                                  |
| ---------------------- | -------------------------------------------- |
| `-h`, `--help`         | Display help message and exit.               |
| `-e`, `--encrypt`      | Encrypt text. Example: `-e "HelloWorld"`.    |
| `-d`, `--decrypt`      | Decrypt text. Example: `-d "EncryptedText"`. |
| `-ef`, `--encryptfile` | Encrypt a file. Example: `-ef file.png`.     |
| `-df`, `--decryptfile` | Decrypt a file. Example: `-df file.enc`.     |

### 🔑 **Key Modes:**

| Option            | Description                                       |
| ----------------- | ------------------------------------------------- |
| `-k`, `--key`     | Key in plain text format. Example: `-k "mykey"`.  |
| `-kh`, `--keyhex` | Key in hexadecimal format. Example: `-kh 6d7978`. |

### 📤 **Output Option:**

| Option           | Description              |
| ---------------- | ------------------------ |
| `-o`, `--output` | Specify the output file. |

---

## 📌 **Usage Examples**

### 🔒 **Encrypt Text**

```bash
exor -e "HelloWorld" -k "ohayo"
```

### 🔓 **Decrypt Text with Hexadecimal Key**

```bash
exor -d 271006051c36011d190e -kh 6f756a6973616e
```

### 🗂️ **Encrypt a File**

```bash
exor -ef image.png -k "oujisan" -o secret.enc
```

### 📂 **Decrypt a File**

```bash
exor -df secret.enc -k "oujisan" -o image.png
```

---

## 🧰 **Build-In**

- Python **3.13.1** or newer.

📅 **Created Date:** Sunday, March 02, 2025

---

🎉 **Enjoy using eXOR!** If you encounter any issues or have questions, feel free to open an issue on our GitHub repository. 🚀

