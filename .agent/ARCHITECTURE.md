# ARCHITECTURE.md - Sistema CTF Professor

> Referência arquitetural completa para o ecossistema de agentes do CTF Professor.

---

## Visão Geral do Sistema

O sistema CTF Professor é um ambiente pedagógico de cibersegurança construído no framework Antigravity Kit. Ele utiliza agentes, habilidades (skills) e fluxos de trabalho (workflows) especializados para ensinar a metodologia de CTF através de questionamentos socráticos e aprendizado guiado.

**Idiomas:** EN + PT-BR (detectado automaticamente por mensagem, padrão PT-BR)

---

## Estrutura de Diretórios

```
.agent/
├── agents/           # 18 definições de agentes
├── skills/           # 28 módulos de habilidades (SKILL.md + scripts/templates)
├── workflows/        # 13 comandos de barra (slash commands)
├── rules/
│   └── GEMINI.md     # Regras globais de comportamento + detecção de idioma
├── scripts/          # Scripts utilitários globais
├── ARCHITECTURE.md   # Este arquivo
└── SECURITY.md       # Políticas de segurança
```

---

## Elenco de Agentes

### Agentes Principais de CTF (Criados para este projeto)

| Agente | Papel | Habilidades (Skills) Principais | Gatilhos |
|:---|:---|:---|:---|
| `ctf-professor` | **Orquestrador principal** para sessões de aprendizado de CTF | triage, toolchain, execution, writeup, classifier, hints | ctf, challenge, flag, lesson |
| `challenge-classifier` | Primeiro agente em cada sessão — classificação em 3 níveis | ctf-challenge-classifier, triage | classify, triage, category |
| `reverse-engineering-specialist` | Análise binária (estática primeiro) | RE analysis, triage, toolchain | reverse, decompile, ghidra, crackme |
| `binary-exploit-engineer` | Exploração de corrupção de memória (Pwn) | binary exploitation, controlled execution, RE | pwn, exploit, buffer overflow, rop |
| `crypto-analyst` | Análise matemática de cifras | cryptography-analysis, triage, toolchain | crypto, cipher, rsa, aes, hash |
| `forensics-analyst` | Investigação de evidências digitais | forensics-investigation, triage, toolchain | forensics, pcap, memory, stego |
| `malware-sandbox-analyst` | Análise segura de malware | malware-sandboxing, RE analysis, toolchain | malware, sandbox, suspicious |

### Agentes de Segurança (Do projeto original, mantidos)

| Agente | Papel |
|:---|:---|
| `security-auditor` | Revisão de segurança de código e avaliação de vulnerabilidades |
| `penetration-tester` | Metodologia de teste de segurança ofensiva (Pentest) |

### Agentes de Suporte (Do projeto original, mantidos)

| Agente | Papel |
|:---|:---|
| `orchestrator` | Coordenação multi-agente |
| `project-planner` | Metodologia de projeto em 4 fases |
| `debugger` | Diagnóstico e resolução de bugs |
| `explorer-agent` | Análise e navegação na base de código |
| `code-archaeologist` | Compreensão de código legado |
| `documentation-writer` | Redação técnica |
| `product-manager` | Priorização de recursos |
| `product-owner` | Requisitos e aceitação |
| `test-engineer` | Estratégia de testes |

---

## Conjunto de Habilidades (Skill Stack)

### Habilidades de Domínio CTF (Criadas para este projeto)

| Habilidade (Skill) | Categoria | Propósito |
|:---|:---|:---|
| `ctf-challenge-classifier` | Classificação | Taxonomia em 3 níveis (Tipo/Categoria/Classe) + árvore de decisão + `classify.py` |
| `ctf-triage-methodology` | Triagem | Pipeline de análise das Fases A-D + prompts socráticos bilíngues |
| `hint-generation-engine` | Pedagogia | Dicas progressivas em 3 níveis com imposição de "gates" |
| `reverse-engineering-analysis` | RE | Pipeline de 4 fases (identificar/desmontar/descompilar/dinâmica) |
| `binary-exploitation-guide` | Pwn | 6 classes de exploração + bypass de proteção + `rop_chain_scaffold.py` |
| `web-exploitation-methodology` | Web | Regra manual primeiro, matriz OWASP, imersões em SQLi/XSS/SSTI |
| `cryptography-analysis` | Criptografia | Identificação de cifra, tabelas de ataque RSA/AES/hash, foco matemático |
| `forensics-investigation` | Forense | PCAP, memória (Volatility 3), esteganografia, disco, extração de arquivos (carving) |
| `osint-methodology` | OSINT | Pipeline passivo primeiro, limites éticos |
| `malware-sandboxing` | Malware | Isolamento Docker, análise comportamental, extração de IoC |
| `security-toolchain-manager` | Ferramentas | Matriz de ferramentas ciente da categoria (7 domínios) + explicações em PT-BR |
| `controlled-execution-framework` | Exploração | `exploit_scaffold.py` + ciclo iterativo Teoria-Previsão-Execução-Verificação |
| `ctf-writeup-architect` | Documentação | Mapeamento CVSS/CVE + templates bilíngues (EN/PT-BR) |

### Habilidades de Suporte (Do projeto original, mantidas)

| Habilidade (Skill) | Propósito |
|:---|:---|
| `clean-code` | Padrões de qualidade de código |
| `brainstorming` | Estrutura de questionamento socrático |
| `intelligent-routing` | Seleção automática de agente |
| `i18n-localization` | Padrões de internacionalização |
| `red-team-tactics` | Metodologia ofensiva |
| `vulnerability-scanner` | Verificação automatizada de segurança |
| `code-review-checklist` | Padrões de revisão de código |
| `architecture` | Padrões de arquitetura de sistema |
| `bash-linux` | Referência de script Shell |
| `powershell-windows` | Referência PowerShell |
| `python-patterns` | Melhores práticas em Python |
| `testing-patterns` | Metodologia de testes |
| `behavioral-modes` | Configuração de comportamento do agente |
| `parallel-agents` | Coordenação multi-agente |
| `plan-writing` | Metodologia de planejamento de tarefas |

---

## Referência Rápida de Workflows

### Workflows de CTF (Criados para este projeto)

| Comando | Propósito | Agente Principal |
|:---|:---|:---|
| `/install` | Configurar ambiente, compilar Docker, instalar dependências | orchestrator / support |
| `/list-ctf` | Listar todos os desafios locais na pasta CTFs/ | support |
| `/start-ctf` | Iniciar resolução de CTF (4 modos de entrada, classificação obrigatória) | ctf-professor |
| `/classify-challenge` | Classificação independente sem resolução | challenge-classifier |
| `/hint` | Dica progressiva (3 níveis com gate) | ctf-professor |
| `/analyze-binary` | Análise binária → roteamento automático para RE ou Pwn | RE/Pwn specialist |
| `/explain-vulnerability` | Explicação puramente educacional (sem contexto de CTF) | ctf-professor |
| `/threat-model` | Modelo de ameaça STRIDE pós-captura da flag | ctf-professor |
| `/replay-exploit` | Teste de retenção — reproduzir e explicar | ctf-professor |

### Workflows de Suporte (Do projeto original, mantidos)

| Comando | Propósito |
|:---|:---|
| `/brainstorm` | Sessão de ideação socrática |
| `/debug` | Workflow de diagnóstico de bugs |
| `/debug-exploit` | Depuração de exploit |
| `/orchestrate` | Coordenação de tarefas multi-agente |
| `/plan` | Planejamento de projeto |
| `/writeup` | Gerar writeup (relatório) de CTF |

---

## Modelo de Entrada: `/start-ctf`

```
INPUT DO USUÁRIO
│
├── Modo A: Direto ("/start-ctf")
│   └── Pede descrição ou arquivos
│
├── Modo B: Texto + Arquivos ("/start-ctf Injeção SQL..." + source.php)
│   └── Extrai descrição + inventaria arquivos
│
└── Modo C: Imagem + Arquivos ("/start-ctf" + print da tela + binário)
    └── Lê o texto do print da tela + inventaria arquivos

         ↓

┌─────────────────────────┐
│  challenge-classifier   │ ← SEMPRE invocado
│  (Classificação 3 níveis)
└────────────┬────────────┘
             ↓
┌─────────────────────────┐
│  Usuário confirma ou    │
│  corrige classificação  │
└────────────┬────────────┘
             ↓
┌─────────────────────────┐
│  ctf-professor          │
│  Início do Ciclo:       │
│  (Triagem → Ferramentas │
│   → Exploração →        │
│   Writeup)              │
└─────────────────────────┘
```

---

## Mapa de Delegação de Agentes

```
ctf-professor (orquestrador)
├── challenge-classifier ← classificação
├── reverse-engineering-specialist ← desafios de RE (Eng. Reversa)
│   └── binary-exploit-engineer ← se serviço remoto for encontrado
├── binary-exploit-engineer ← desafios de Pwn
│   └── reverse-engineering-specialist ← se precisar de RE estática profunda
├── crypto-analyst ← desafios de Criptografia
├── forensics-analyst ← desafios de Forense
│   └── reverse-engineering-specialist ← se malware for encontrado na evidência
├── malware-sandbox-analyst ← binários suspeitos
│   └── reverse-engineering-specialist ← para RE profunda
└── security-auditor / penetration-tester ← revisão de código / pentest
```

---

## Detecção de Idioma (R2)

- Detectado automaticamente por mensagem (EN ou PT-BR)
- Padrão em caso de ambiguidade: **PT-BR**
- Código/comandos permanecem em Inglês
- Jargões de segurança podem permanecer em Inglês nas explicações em PT-BR
- Todos os prompts socráticos possuem variantes bilíngues
