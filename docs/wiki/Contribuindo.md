# 🤝 Contribuindo para o CTF Professor

O **CTF Professor** é um projeto modular e extensível. Você pode contribuir adicionando novos especialistas (agentes), novas capacidades técnicas (skills) ou novos fluxos de automação (workflows).

---

## 🏗️ Estrutura da Pasta `.agent/`

Toda a inteligência do sistema reside na pasta `.agent/`. Para contribuir, você trabalhará principalmente nestes diretórios:

- `agents/`: Definições de personalidade e ferramentas dos agentes.
- `skills/`: Módulos de conhecimento técnico, scripts e templates.
- `workflows/`: Definição dos comandos de barra (ex: `/start-ctf`).

---

## 🤖 Como Adicionar um Novo Agente

1.  Crie um arquivo `.md` em `.agent/agents/` (ex: `web-api-expert.md`).
2.  Defina o **System Prompt** do agente, descrevendo sua expertise e tom de voz.
3.  Liste as **Skills** que ele tem permissão para usar no frontmatter.
4.  Adicione uma seção de **Anti-Patterns** (o que o agente NÃO deve fazer).

---

## 🧠 Como Adicionar uma Nova Skill

Uma skill é um conjunto de conhecimentos e ferramentas.
1.  Crie uma pasta em `.agent/skills/`.
2.  Crie um arquivo `SKILL.md` descrevendo a metodologia (ex: como analisar tráfego USB).
3.  (Opcional) Adicione uma pasta `scripts/` para ferramentas Python/Bash auxiliares.
4.  (Opcional) Adicione uma pasta `templates/` para rascunhos de código que o agente pode usar.

---

## ⚡ Como Adicionar um Novo Workflow

Workflows são os "Slash Commands".
1.  Crie um arquivo `.md` em `.agent/workflows/` (ex: `exploit-generator.md`).
2.  Defina os passos que a IA deve seguir ao receber o comando.
3.  Use a variável `$ARGUMENTS` para capturar o que o usuário digitou após o comando.

---

## 📏 Padrões de Código e Qualidade

Para manter o projeto profissional, siga estas regras:

1.  **Clean Code**: Código direto, sem comentários óbvios, funções pequenas e nomes significativos.
2.  **i18n (Internacionalização)**: O sistema deve suportar PT-BR e EN. Scripts de interface devem lidar com encodings corretamente.
3.  **Socratic First**: Qualquer nova skill de CTF deve priorizar o ensino (perguntas) antes da execução automática.

---

## ✅ Verificação antes do Pull Request

Sempre rode os scripts de validação antes de enviar suas alterações:

```bash
# Verificação completa de segurança, lint e testes
python .agent/scripts/verify_all.py .

# Checklist incremental
python .agent/scripts/checklist.py .
```

---

## 🔗 Links Úteis
👉 [**Voltar para a Home**](Home)
