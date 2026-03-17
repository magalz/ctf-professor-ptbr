# 🧠 Modelos de IA e Custos (Pro vs Flash)

O **CTF Professor** utiliza IAs de fronteira (Large Language Models) para analisar binários, interagir com o terminal e atuar como seu mentor socrático. Escolher o modelo certo é a diferença entre uma experiência de aprendizado incrível e horas de frustração.

---

## 🏆 A Regra de Ouro: Use Sempre o Modelo "Pro"

Para 99% das tarefas de cibersegurança neste projeto, **recomendamos expressamente o uso de modelos da classe "Pro"** (ex: `gemini-1.5-pro` ou equivalente de ponta).

### Por que não usar o modelo "Flash" ou "Mini"?

Embora modelos como o *Gemini 1.5 Flash* sejam incrivelmente rápidos e quase gratuitos, eles falham em cenários críticos de segurança:

1.  **Engenharia Reversa e Pwn**: Modelos menores não conseguem manter o contexto complexo de registradores, *ROP chains* ou leitura de código Assembly profundo.
2.  **Alucinação de Comandos**: O Flash tende a "inventar" flags de linha de comando que não existem (ex: `nmap --scan-all-vulns`), resultando em erros e perda de tempo no terminal.
3.  **A Nuance Socrática**: O método de ensino do Professor requer muita sutileza. O modelo precisa saber a resposta, avaliar o que você digitou e responder com uma pergunta que guie seu raciocínio sem entregar a flag de bandeja. Modelos menores estragam a surpresa ou avaliam sua resposta de forma errada.

*Use o Flash apenas se você for processar um log gigante de PCAP (centenas de milhares de linhas) apenas para extração de texto bruto.*

---

## ⚙️ Como Configurar o Modelo no Gemini CLI

Você define qual modelo deseja usar na hora de iniciar o programa no seu terminal.

Se você iniciar apenas com `gemini`, ele pode assumir um modelo padrão. Para forçar o uso do modelo Pro (Recomendado), inicie a CLI com a flag `--model`:

```bash
gemini --model gemini-1.5-pro
```

*(Dica: Você pode criar um `alias` no seu bashrc/zshrc para não ter que digitar isso toda vez).*

---

## 💰 Custos e Cotas (O que você precisa saber)

O uso de IAs através de API tem custos. Aqui está uma visão honesta de como isso impacta seu bolso ao resolver CTFs.

*Nota: Valores baseados nos preços da Google AI Studio no momento da escrita deste documento.*

### Opção 1: Uso Gratuito (Free Tier)
O Google AI Studio oferece uma cota **gratuita** muito generosa para desenvolvedores:
*   **Gemini 1.5 Pro**: Até 50 requisições por dia.
*   **Gemini 1.5 Flash**: Até 1.500 requisições por dia.

**Para estudantes**: A cota de 50 requests/dia do modelo Pro geralmente é mais que suficiente para resolver de 2 a 3 CTFs completos por dia de forma guiada, sem gastar um centavo.

### Opção 2: Usuários Premium (Google One AI Premium / Advanced)
Se você assina o Google One com acesso aos modelos avançados, você tem acesso prioritário, mas é importante verificar se sua assinatura se estende ao uso da **API de Desenvolvedor**, que muitas vezes é faturada separadamente do uso web (chat no navegador).

### Opção 3: Pay-As-You-Go (Pago pelo uso)
Se você esgotar a cota gratuita ou precisar de limites maiores corporativos, você pagará por token processado.

*   **Estimativa de um desafio de CTF completo** (aprox. 5 a 8 interações densas):
    *   *Tokens de Entrada (Prompt + Histórico)*: ~40.000 tokens
    *   *Tokens de Saída (Respostas)*: ~5.000 tokens
*   **Custo no Modelo Pro**: ~$0.15 a $0.25 USD por desafio (Cerca de R$ 1,00 a R$ 1,50).
*   **Custo no Modelo Flash**: ~$0.005 USD por desafio (Praticamente de graça).

**Estratégia de Economia**: Em desafios muito longos, o "histórico" da conversa fica gigante e caro. O sistema cria automaticamente o arquivo `notes.md` na pasta do seu desafio. Se a conversa ficar muito longa, você pode limpar a sessão do CLI e reiniciar apontando para a mesma pasta. A IA lerá o `notes.md` e continuará exatamente de onde você parou, custando muito menos tokens de contexto!

---

## 🔗 Próximos Passos
👉 [**Retornar para a Home da Wiki**](Home)
