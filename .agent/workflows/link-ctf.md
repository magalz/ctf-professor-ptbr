---
description: Link your CTF platform accounts (CTFd, HackTheBox, TryHackMe) to enable automated challenge intake and flag submission.
---

# /link-ctf — Connect CTF Platforms

$ARGUMENTS

---

## Task

### Step 1: Platform Selection
Ask the user which platform they want to connect:
- **CTFd** (Self-hosted or Cloud)
- **HackTheBox**
- **TryHackMe**

### Step 2: Guided Configuration
Provide specific instructions based on the choice:

#### For CTFd:
1. Log in to your CTFd instance.
2. Go to **Settings** > **Access Tokens**.
3. Generate a new token and provide the **Platform URL** and **Token**.

#### For HackTheBox:
1. Log in to [app.hackthebox.com](https://app.hackthebox.com/).
2. Go to **Profile Settings** > **App Tokens**.
3. Create a new token and provide it here.

#### For TryHackMe:
1. Log in to [tryhackme.com](https://tryhackme.com/).
2. Open Browser DevTools (F12) > Application/Storage > Cookies.
3. Find the `connect.sid` cookie and provide its value.

### Step 3: Persistence
1. Invoke `install_setup.py` (or a dedicated integration script) to save the values to the local `.env` file.
2. Ensure the user knows their credentials are safe and only stored locally.

### Step 4: Verification
1. Test the connection by fetching a basic profile or challenge list.
2. Confirm success: "✅ Connection established with [Platform]!"

---

## Rules
- **Never** display full tokens in the chat output.
- **Explain** that the `.env` file is ignored by Git for security.
- **Language** detection (PT-BR/EN) must be active.
