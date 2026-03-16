# CTF Writeup: [Nome do Desafio]

**Categoria:** [Web/Pwn/Crypto/Forense/OSINT/RE/Rede/Cloud/Mobile/AI-ML/Hardware/Misc]
**Dificuldade:** [Iniciante/Intermediário/Avançado]
**Plataforma:** [CTFd/HackTheBox/TryHackMe/Outro]
**Data:** [YYYY-MM-DD]

---

## 1. Resumo Executivo
*Forneça uma visão geral de 2-3 frases sobre o desafio e a vulnerabilidade principal explorada.*

## 2. Reconhecimento & Triagem
*Documente a fase de análise inicial.*
* **Classificação:** [Saída do challenge-classifier — Tipo CTF / Categoria / Classe / Dificuldade]
* **Hipótese Inicial:** O que o artefato/cenário indicava inicialmente?
* **Ferramentas Utilizadas:** (ex: `file`, `strings`, `nmap`, `checksec`)
* **Descobertas Principais:** Qual output específico apontou para a vulnerabilidade?

## 3. Análise da Vulnerabilidade (A Teoria)
*Explique a causa raiz da falha.*
* **Mecanismo:** Como o sistema vulnerável processa os dados?
* **A Falha:** Onde exatamente a lógica falha? (Inclua trechos de código relevantes se engenharia reversa foi aplicada).
* **Contexto Histórico:** Esta vulnerabilidade já foi observada em sistemas reais? (CVEs relevantes)

## 4. Exploração (A Execução)
*Reprodução passo-a-passo do ataque.*
1. **Preparação:** Configuração do ambiente ou payload.
2. **Execução:** O comando ou script específico utilizado (inclua o código `exploit.py` ou comandos do terminal).
3. **Resultado:** Como o sistema respondeu e a aquisição da flag.

## 5. Impacto Real & Mitigação
*Conecte o CTF à segurança corporativa.*
* **Cenário Corporativo:** Onde esta vulnerabilidade seria tipicamente encontrada em uma rede corporativa?
* **Remediação:** Como corrigir.
  * *Nível de código:* (ex: sanitização de entrada, funções seguras).
  * *Nível de infraestrutura:* (ex: regras de WAF, segmentação de rede, redução de privilégios).

## 6. Mapeamento da Vulnerabilidade

| Métrica | Valor | Justificativa |
|:---|:---|:---|
| CVE | [CVE-XXXX-XXXXX ou Customizado] | [Breve explicação] |
| CVSS Score | [X.X] | [Resumo do motivo] |
| Vetor de Ataque | [Rede/Adjacente/Local/Físico] | [Por quê] |
| Complexidade | [Baixa/Alta] | [Por quê] |
| Confidencialidade | [Nenhuma/Baixa/Alta] | [Por quê] |
| Integridade | [Nenhuma/Baixa/Alta] | [Por quê] |
| Disponibilidade | [Nenhuma/Baixa/Alta] | [Por quê] |

## 7. Lições Aprendidas
*O que o estudante deve levar desta experiência?*
* **Técnica principal aprendida:**
* **Ferramentas dominadas:**
* **Erro mais comum evitado:**
