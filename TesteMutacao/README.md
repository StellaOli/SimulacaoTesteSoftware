# 🧪 Testes de Mutação em Sistema de Heróis RPG

## 📌 Descrição do Projeto

Este projeto consiste no desenvolvimento de um conjunto de funções em Python relacionadas a um sistema de heróis de RPG, juntamente com a aplicação de testes unitários e testes de mutação.

O objetivo principal é avaliar a qualidade dos testes implementados, verificando sua capacidade de detectar alterações no código (mutações).

---

## ⚙️ Funcionalidades Implementadas

O sistema possui cinco funções principais:

* `calcular_ataque_total`: calcula o ataque do herói com base em atributos e nível
* `calcular_defesa_total`: calcula a defesa considerando armadura, agilidade e escudo
* `classe_heroi`: determina a classe do herói (Guerreiro, Mago ou Ladino)
* `calcular_dano_final`: calcula o dano causado ao inimigo
* `pode_usar_habilidade`: verifica se o herói pode utilizar habilidades especiais

---

## 🧪 Testes Unitários

Os testes foram implementados utilizando a biblioteca **pytest**.

### ▶️ Como executar os testes

```bash
python -m pytest -v
```

Os testes cobrem diferentes cenários, incluindo:

* casos normais
* valores limite
* variações de classe e atributos
* uso de habilidades e dano crítico

---

## 🧬 Teste de Mutação

O teste de mutação foi realizado com o objetivo de avaliar a eficácia dos testes unitários.

Foram utilizadas duas abordagens:

---

### 🔧 1. Mutação Manual

Foram criadas mutações manualmente através da substituição de operadores no código, como:

* `+` → `-`
* `*` → `+`
* `>=` → `>`
* `and` → `or`
* `==` → `!=`

Após cada alteração, os testes foram executados novamente.

#### 📊 Resultado (exemplo)

| Mutação | Detectada |
| ------- | --------- |
| M1      | ✔         |
| M2      | ✔         |
| M3      | ✔         |
| M4      | ✔         |
| M5      | ✔         |

---

### 🤖 2. Mutação Automatizada (Mutmut)

Foi utilizada a ferramenta **Mutmut** para geração automática de mutações.

#### ▶️ Execução

```bash
python -m mutmut run --max-children 1
```

#### ▶️ Visualizar resultados

```bash
python -m mutmut results
```

---

## 📊 Resultados Obtidos

| Método | Mutantes Gerados | Detectados | Sobreviventes |
| ------ | ---------------- | ---------- | ------------- |
| Manual | 5                | 5          | 0             |
| Mutmut | 62               | 34         | 28            |

### 📈 Taxa de detecção

A taxa de mutações detectadas foi de aproximadamente:

**54,8%**

---

## 🔎 Análise dos Resultados

Os testes unitários foram capazes de detectar uma parte significativa das mutações. No entanto, a existência de mutações sobreviventes indica que:

* Nem todos os caminhos do código estão sendo testados
* Algumas condições não possuem testes específicos
* Existem oportunidades de melhoria na cobertura dos testes

---

## 🚀 Possíveis Melhorias

* Adicionar testes para casos limites
* Criar testes específicos para cada classe de herói
* Validar combinações de atributos mais variadas
* Aumentar a cobertura de condições booleanas

---

## 🛠️ Tecnologias Utilizadas

* Python 3.x
* pytest
* mutmut

---

## 📌 Conclusão

A utilização de testes de mutação permitiu avaliar de forma mais profunda a qualidade dos testes unitários. A abordagem automatizada revelou falhas que não seriam facilmente identificadas apenas com testes tradicionais, reforçando a importância dessa técnica no desenvolvimento de software confiável.

---
