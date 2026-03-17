# 🤖 Agentes e Skills do Ecossistema

O **CTF Professor** não é um único modelo de linguagem, mas um ecossistema complexo de 18 agentes e 28 skills especializadas.

---

## 👥 Os Agentes Especialistas

Cada agente tem uma personalidade e foco técnico distintos:

### Núcleo de CTF (CTF Core)
- **`ctf-professor`**: O maestro. Orquestra a sessão e garante a pedagogia socrática.
- **`challenge-classifier`**: O primeiro a entrar em cena. Classifica o desafio em 3 níveis.
- **`reverse-engineering-specialist`**: Especialista em análise de baixo nível e assembly.
- **`binary-exploit-engineer`**: Focado em pwn e corrupção de memória.
- **`crypto-analyst`**: Resolve cifras e ataques matemáticos.
- **`forensics-analyst`**: Analisa PCAPs, dumps de memória e esteganografia.
- **`malware-sandbox-analyst`**: Analisa comportamento de binários suspeitos.

### Auditoria e Segurança
- **`security-auditor`**: Revisão de código e modelagem de ameaças.
- **`penetration-tester`**: Simula o fluxo de um ataque real completo.

### Suporte e Engenharia
- **`orchestrator`**, **`debugger`**, **`project-planner`**, **`documentation-writer`**, entre outros.

---

## 🧠 Skills (Módulos de Conhecimento)

As skills são o "cérebro" técnico que os agentes utilizam. Algumas das mais importantes:

| Skill | O que ela faz? |
| :--- | :--- |
| `ctf-platform-bridge` | Conecta-se a APIs de CTFd, HTB e THM para baixar desafios e submeter flags automaticamente. |
| `ctf-triage-methodology` | Define como fazer o reconhecimento inicial sem disparar alertas. |
| `controlled-execution-framework` | Controla o ciclo "Teoria-Prever-Executar-Verificar" de exploits. |
| `security-toolchain-manager` | Sabe quais ferramentas instalar para cada tipo de desafio. |
| `ctf-writeup-architect` | Template de relatórios profissionais (PT-BR e EN). |
| `vulnerability-scanner` | Analisa padrões de código inseguro (SQLi, XSS, RCE). |

---

## 🛠️ Onde encontrar as definições?

Se você quiser ver como um agente "pensa" ou quais regras ele segue, você pode ler os arquivos Markdown na pasta `.agent/`:

- **Definições de Agentes**: `.agent/agents/*.md`
- **Lógica das Skills**: `.agent/skills/<nome-da-skill>/SKILL.md`
- **Workflows (Slash Commands)**: `.agent/workflows/*.md`

### 🔍 Dica:
Cada agente tem uma seção de **"Anti-Patterns"** que descreve comportamentos que ele deve evitar (como dar a resposta de bandeja para o aluno).

---

## 🔗 Saiba Mais
👉 [**Detalhes sobre o Sandbox Docker**](Sandbox-Docker)
