---
description: Gera um modelo de ameaça alinhado ao STRIDE após a captura da flag. Mapeia a vulnerabilidade do CTF para o risco corporativo com pontuação CVSS, árvore de ataque e plano de remediação.
---

# /threat-model - Modelo de Ameaça Pós-Captura

$ARGUMENTS

---

## Tarefa

Este comando gera um modelo de ameaça estruturado baseado na vulnerabilidade explorada durante a sessão de CTF. Ele preenche a lacuna entre o CTF competitivo e a análise de segurança do mundo real.

### Passos:

1. **Coleta de Contexto**: Revise o exploit e a classificação da sessão atual.
   - Se não houver sessão ativa, pergunte: "Describe the vulnerability you want to model." / "Descreva a vulnerabilidade que deseja modelar."

2. **Gerar Análise STRIDE**:

   ```
   ## Modelo de Ameaça: [Nome da Vulnerabilidade]

   ### Classificação STRIDE

   | Ameaça | Aplica-se? | Descrição |
   |:---|:---|:---|
   | **S**poofing (Falsificação) | [Sim/Não] | [Como a identidade pode ser falsificada] |
   | **T**ampering (Adulteração) | [Sim/Não] | [Como os dados podem ser modificados] |
   | **R**epudiation (Repúdio) | [Sim/Não] | [Como as ações podem ser negadas] |
   | **I**nformation Disclosure (Vazamento de Informação) | [Sim/Não] | [Quais dados são expostos] |
   | **D**enial of Service (Negação de Serviço) | [Sim/Não] | [Como a disponibilidade é afetada] |
   | **E**levation of Privilege (Elevação de Privilégio) | [Sim/Não] | [Como os privilégios podem ser elevados] |

   ### Pontuação CVSS v3.1
   [Detalhamento completo do CVSS com justificativa para cada métrica]

   ### Árvore de Ataque (Attack Tree)
   [Diagrama Mermaid mostrando os caminhos de ataque]

   ### Impacto Corporativo
   [Onde esta vulnerabilidade existe em ambientes corporativos]

   ### Plano de Remediação
   [Correções específicas em nível de código, infraestrutura e processo]
   ```

3. **Apresentar** no idioma detectado do aluno.

4. **Acompanhamento**: Pergunte se o aluno deseja explorar mais as medidas defensivas.

---

## Exemplos de Uso

```
/threat-model
/threat-model Injeção SQL na autenticação
/threat-model Buffer overflow no serviço de autenticação
```

---

## Regras

- **Apenas após a captura da flag ou conclusão do exploit** — esta é uma ferramenta educacional pós-exploração
- **O idioma segue o idioma da sessão**
- **STRIDE e CVSS devem ser totalmente preenchidos** — sem atalhos
