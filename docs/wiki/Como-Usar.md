# 🎮 Como Usar o CTF Professor

Interagir com o sistema é simples e intuitivo. O orquestrador detectará seu idioma automaticamente e iniciará o ciclo de aprendizado.

---

## 🏗️ O Ciclo de Aprendizado (7 Fases)

Cada desafio segue rigorosamente este ciclo para garantir que você realmente aprenda:

1.  **Classificação**: Taxonomia em 3 níveis (Tipo/Categoria/Classe).
2.  **Análise de Cenário**: Entendemos o contexto antes de tocar no teclado.
3.  **Reconhecimento Guiado**: Identificação de vetores de ataque com explicações.
4.  **Base Teórica**: Você deve entender a vulnerabilidade antes de usar as ferramentas.
5.  **Exploração Controlada**: Construção do exploit passo a passo com "gates" socráticas.
6.  **Captura da Flag**: Validação do sucesso e explicação do impacto.
7.  **Mitigação e Writeup**: Traduzimos a falha técnica em risco de negócio real.

---

## 🛠️ Comandos Disponíveis (Slash Commands)

### Iniciar um Desafio (`/start-ctf`)
Este é o comando principal. Ele aceita três modos de entrada:
- **Modo Bare**: Digite apenas `/start-ctf` e o sistema pedirá detalhes.
- **Modo Texto + Arquivos**: `/start-ctf Injecao SQL` e anexe os arquivos fonte.
- **Modo Imagem + Arquivos**: Anexe um print do desafio do CTF e digite `/start-ctf`.

### Obter Dicas (`/hint`)
Dicas progressivas em 3 níveis:
1.  **Conceito**: Explicação teórica sem dar a solução.
2.  **Estratégia**: Como você deve abordar o problema.
3.  **Execução**: Quase o comando final, mas ainda exigindo esforço seu.

### Outros Comandos Importantes

- `/analyze-binary`: Análise profunda de um binário ELF ou PE.
- `/explain-vulnerability [nome]`: Peça uma aula teórica sobre qualquer falha.
- `/threat-model`: Gera um modelo STRIDE de ameaças após a captura da flag.
- `/writeup`: Cria um relatório técnico e educacional da sessão.
- `/replay-exploit`: Um teste de retenção para verificar se você entendeu o processo.

---

## 💡 Dicas para uma melhor Experiência

- **Seja Específico**: Quanto mais contexto você der sobre o desafio, melhor o `challenge-classifier` fará o trabalho dele.
- **Não Pule Etapas**: O professor aplicará "Socratic Gates" (bloqueios socráticos). Se você tentar rodar um exploit sem explicar a teoria, ele poderá pedir que você reflita antes.
- **Anexe o que for Útil**: Arquivos `.c`, `.php`, binários ou até capturas de pacotes (`.pcap`) ajudam o sistema a ser muito mais preciso.

---

## 🛡️ Próximo Passo
Aprenda mais sobre os bastidores do sistema:
👉 [**Conheça os Agentes e Skills**](Agentes-e-Skills)
