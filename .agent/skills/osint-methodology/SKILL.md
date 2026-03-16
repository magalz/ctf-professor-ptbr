---
name: osint-methodology
description: Pedagogical framework for OSINT CTF challenges. Covers passive reconnaissance, geolocation, social media intelligence, metadata analysis, and ethical boundaries. Enforces passive-before-active.
allowed-tools: Read, Bash, Glob
---

# OSINT Methodology

> The best intelligence is gathered without the target ever knowing you looked.

---

## 1. Core Principle: Passive Before Active

**Never perform active scanning or direct interaction with a target until passive reconnaissance is exhausted.**

| Phase | Activity | Detection Risk |
|:---|:---|:---|
| **Passive** | Public data, cached pages, WHOIS, DNS records | None |
| **Semi-passive** | Third-party tools (Shodan, Censys) that may log queries | Minimal |
| **Active** | Direct scanning, social engineering, direct contact | High |

**Pedagogical Gate:** Student must explain what passive recon revealed before moving to active methods.

---

## 2. OSINT Investigation Pipeline

### Phase A: Target Definition

1. What exactly are we looking for? (person, location, organization, infrastructure)
2. What information do we already have? (name, image, username, IP, domain)
3. What constraints exist? (CTF scope, ethical boundaries, legal limits)

### Phase B: Passive Reconnaissance

#### Identity & Social Media (SOCMINT)

| Technique | Tools | What to Look For |
|:---|:---|:---|
| Username search | `sherlock`, `whatsmyname` | Same username across platforms |
| Profile analysis | Manual browser | Bio, links, followers, activity patterns |
| Email search | `holehe`, Hunter.io | Email presence on services |
| Reverse image | Google Images, TinEye, Yandex | Other occurrences of profile photos |

#### Domain & Infrastructure

| Technique | Tools | What to Look For |
|:---|:---|:---|
| WHOIS lookup | `whois`, whois.domaintools.com | Registrant name, email, dates |
| DNS records | `dig`, `nslookup`, dnsdumpster.com | A, MX, TXT, CNAME records |
| Subdomain enum | `subfinder`, crt.sh | Hidden subdomains via cert transparency |
| Historical data | Wayback Machine | Previous versions of websites |
| Certificate search | crt.sh | All domains on same certificate |

#### Geolocation

| Technique | Tools | What to Look For |
|:---|:---|:---|
| Image metadata | `exiftool` | GPS coordinates, camera model, timestamp |
| Visual clues | Manual analysis | Signs, landmarks, vegetation, architecture, sun position |
| Street View | Google/Bing Maps | Match visual clues to locations |
| Satellite imagery | Google Earth | Terrain, building shapes, road patterns |

#### Data Breach Analysis

| Technique | Tools | What to Look For |
|:---|:---|:---|
| Email in breaches | HaveIBeenPwned | Which services were compromised |
| Password patterns | Dehashed (ethical use) | Reused passwords, common patterns |
| Data dumps | IntelX, Pastebin search | Leaked documents, credentials |

### Phase C: Dorking

| Platform | Syntax | Example |
|:---|:---|:---|
| **Google** | `site:`, `inurl:`, `filetype:`, `intitle:` | `site:example.com filetype:pdf` |
| **GitHub** | `filename:`, `extension:`, `org:` | `filename:.env password` |
| **Shodan** | `port:`, `org:`, `product:` | `port:22 org:"Company Name"` |

### Phase D: Analysis & Correlation

1. Cross-reference findings from different sources
2. Build a timeline of activity
3. Create relationship maps (who connects to whom)
4. **Pedagogical Action:** Student presents their findings as a coherent narrative

---

## 3. Ethical Boundaries

> **These rules are absolute. No exceptions.**

| ✅ Acceptable | ❌ Never Acceptable |
|:---|:---|
| Searching public information | Social engineering real people |
| Using WHOIS/DNS records | Accessing accounts without authorization |
| Analyzing public social media | Harassing or contacting targets |
| Reading cached/archived pages | Exploiting real systems outside CTF scope |
| Metadata from CTF-provided files | Using breach data against real individuals |
| Google/GitHub dorking on CTF domains | Dorking against real organizations without permission |

**Pedagogical Action:** Before any OSINT task, remind the student of these boundaries.

---

## 4. Bilingual Prompts

### PT-BR
- "Que informacoes publicas podemos encontrar sem interagir diretamente com o alvo?"
- "O que os metadados desta imagem revelam? Coordenadas GPS?"
- "Antes de usar ferramentas ativas, o que a reconhecimento passivo nos mostrou?"
- "Quais limites eticos precisamos respeitar nesta investigacao?"

### EN
- "What public information can we find without directly interacting with the target?"
- "What do this image's metadata reveal? GPS coordinates?"
- "Before using active tools, what has passive recon shown us?"
- "What ethical boundaries must we respect in this investigation?"

---

## 5. Anti-Patterns

| ❌ Do Not | ✅ Instead Do |
|:---|:---|
| Start with active scanning | Exhaust passive recon first |
| Skip ethical boundary discussion | Always remind the student of scope limits |
| Ignore image metadata | Always run `exiftool` on provided images |
| Focus only on one source | Cross-reference multiple data sources |
| Forget to check Wayback Machine | Historical data often contains removed information |
