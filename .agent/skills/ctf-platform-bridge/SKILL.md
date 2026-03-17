---
name: ctf-platform-bridge
description: Framework for integrating with CTF platforms (CTFd, HackTheBox, TryHackMe). Handles automated challenge ingestion, file downloads, and flag submission.
allowed-tools: Read, Write, Bash, Python
---

# CTF Platform Bridge

> Connect the Professor directly to your favorite CTF platforms.

## 1. Supported Platforms

| Platform | Authentication | Core Features |
| :--- | :--- | :--- |
| **CTFd** | API Token (v1) | Fetch metadata, download files, submit flags |
| **HackTheBox** | App Token (v4) | List challenges, user info |
| **TryHackMe** | Session Cookie / Room Code | Fetch room tasks and metadata |

---

## 2. Security Guidelines

1.  **Secret Protection**: Never log or print API tokens or session cookies.
2.  **Rate Limiting**: Always respect platform rate limits to avoid IP bans.
3.  **Local Storage**: Store credentials only in the local `.env` file (never commit).
4.  **Privacy**: Do not exfiltrate challenge data outside the local workspace.

---

## 3. Integration Workflow

### Phase A: Linking
User runs `/link-ctf` or configures during `/install`. Credentials are saved to `.env`.

### Phase B: Automated Ingestion
When a URL is provided to `/start-ctf`:
1.  **Identify** the platform from the URL.
2.  **Fetch** challenge title, description, and category.
3.  **Download** attachments directly to the sandbox workspace.
4.  **Hand over** to `challenge-classifier`.

### Phase C: Flag Submission
1.  **Detect** flag capture in the chat.
2.  **Confirm** with user: "I found the flag. Should I submit it to [Platform]?"
3.  **Submit** via `platform_client.py` and report status.

---

## 4. Troubleshooting

| Issue | Potential Solution |
| :--- | :--- |
| 401 Unauthorized | Check if the API Token is valid or expired. |
| Connection Timeout | Verify network access from the host. |
| File Download Failed | Ensure the sandbox workspace folder is writable. |
| Subdomain not found | For CTFd, ensure the full URL (including subdomain) is configured. |
