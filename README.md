# 🏭 Gestão de Peças — Controle de Qualidade e Armazenamento

**Disciplina:** Algoritmos e Lógica de Programação — UNIFECAF  
**Desafio:** Automação Digital para Gestão de Peças, Qualidade e Armazenamento

---

## 📋 Sobre o Projeto

Sistema desenvolvido em Python para automatizar o controle de qualidade de peças industriais em uma linha de montagem. O programa substitui a inspeção manual, avaliando automaticamente cada peça com base em critérios de qualidade pré-definidos e organizando as peças aprovadas em caixas com capacidade limitada.

### Critérios de Aprovação

| Critério      | Valor Aceito         |
|---------------|----------------------|
| Peso          | Entre 95g e 105g     |
| Cor           | Azul ou Verde        |
| Comprimento   | Entre 10cm e 20cm    |

Uma peça só é **aprovada** se atender **todos** os três critérios simultaneamente.

---

## 🖥️ Funcionalidades (Menu Interativo)

| Opção | Funcionalidade                    | Descrição                                                            |
|-------|-----------------------------------|----------------------------------------------------------------------|
| 1     | Cadastrar nova peça               | Recebe ID, peso, cor e comprimento; avalia e classifica a peça       |
| 2     | Listar peças aprovadas/reprovadas | Exibe todas as peças com seus dados e motivos de reprovação          |
| 3     | Remover peça cadastrada           | Remove uma peça pelo ID (aprovada ou reprovada)                      |
| 4     | Listar caixas fechadas            | Mostra as caixas já fechadas (10 peças cada) e a caixa atual        |
| 5     | Gerar relatório final             | Relatório consolidado com totais, taxa de aprovação e detalhamentos  |
| 0     | Sair                              | Encerra o programa                                                   |

---

## 📝 Exemplos de Entradas e Saídas

### Exemplo 1 — Peça Aprovada

```
Entrada:
  ID da peça: P001
  Peso (g): 100
  Cor: azul
  Comprimento (cm): 15

Saída:
  ✅ Peça 'P001' APROVADA e armazenada na caixa atual.
```

### Exemplo 2 — Peça Reprovada

```
Entrada:
  ID da peça: P002
  Peso (g): 110
  Cor: vermelho
  Comprimento (cm): 25

Saída:
  ❌ Peça 'P002' REPROVADA.
   Motivos:
   • Peso fora do padrão (110.0g) — aceito: 95.0g a 105.0g
   • Cor inválida ('vermelho') — aceitas: azul, verde
   • Comprimento fora do padrão (25.0cm) — aceito: 10.0cm a 20.0cm
```

### Exemplo 3 — Relatório Final

```
  📊  RELATÓRIO FINAL CONSOLIDADO

  Total de peças cadastradas:    12
  Total de peças APROVADAS:      10
  Total de peças REPROVADAS:     2
  Taxa de aprovação:             83.3%

  Caixas fechadas:               1
  Peças na caixa atual (aberta): 0/10
```

---

## 🏗️ Estrutura do Código

```
gestao_pecas.py
├── Constantes (limites de peso, cor, comprimento, capacidade da caixa)
├── Estruturas de dados (listas para peças e caixas)
├── Funções de validação
│   ├── validar_peca() — avalia critérios e retorna motivos
│   └── armazenar_peca_aprovada() — gerencia caixas
├── Funções do menu
│   ├── cadastrar_peca()
│   ├── listar_pecas()
│   ├── remover_peca()
│   ├── listar_caixas_fechadas()
│   └── gerar_relatorio()
└── main() — loop do menu interativo
```

---

## 🛠️ Tecnologias

- **Linguagem:** Python 3
- **Bibliotecas:** Nenhuma externa (100% biblioteca padrão)

---

## 📄 Licença

Projeto acadêmico — UNIFECAF 2026.
