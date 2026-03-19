# 🧪 Relatório — Testes de Unidade e Integração

**Disciplina:** Simulação e Teste de Software
**Atividade:** Atividade 06 — Calculadora com Histórico

---

## 🎯 1. Objetivo

O objetivo desta atividade foi desenvolver testes de unidade e integração para um sistema de calculadora com persistência de histórico, aplicando conceitos como:

* Testes de unidade
* Testes de integração
* Test doubles (stub e mock)
* Análise de cobertura de código com `coverage.py`

---

## 🧪 2. Testes de Unidade

Os testes de unidade foram implementados para validar cada operação da classe `Calculadora` de forma isolada, utilizando um **stub (MagicMock)** para o repositório.

### ✔️ Categorias implementadas:

* Entrada e saída (com pelo menos dois casos por operação)
* Tipagem (validação de tipos inválidos)
* Limites (valores extremos e casos especiais)
* Valores fora do intervalo (ex: divisão por zero)
* Mensagens de erro (`assertRaisesRegex`)
* Fluxo de controle (caminhos alternativos)

### ✔️ Observações importantes:

* Foi testado o comportamento com `bool`, observando que em Python `bool` é subclasse de `int`.
* Foram criados testes adicionais além dos exemplos fornecidos.

---

## 🔗 3. Testes de Integração

Os testes de integração foram realizados utilizando a implementação real do `HistoricoRepositorio`.

### ✔️ Cenários testados:

* Execução de operações sequenciais
* Verificação do valor final após múltiplas operações
* Consistência do histórico (`listar`)
* Quantidade de registros (`total`)
* Limpeza do histórico (`limpar`)

### ⚠️ Problema identificado:

Durante os testes, foi detectada uma inconsistência no formato da operação de subtração:

* Saída incorreta: `"5-3 = 2"`
* Saída esperada: `"5 - 3 = 2"`

### ✔️ Correção aplicada:

Foi ajustado o método `subtrair` para incluir espaços, mantendo consistência com as demais operações.

---

## 🎭 4. Test Doubles (Stub e Mock)

### 🔹 Stub

O stub foi utilizado para simular o repositório, permitindo testar a lógica da calculadora de forma independente.

✔ Exemplo:

* Execução de operações sem dependência do repositório real
* Controle de retorno de métodos como `total()`

---

### 🔹 Mock

O mock foi utilizado para verificar a interação entre a calculadora e o repositório.

✔ Foram validados:

* Se o método `salvar()` foi chamado
* Se foi chamado o número correto de vezes
* Se os argumentos passados estavam corretos
* Se não foi chamado em caso de erro

---

## 🐞 5. Identificação e Correção de Bug

Um bug intencional foi identificado no método `potencia`.

### ❌ Problema:

A operação era registrada incorretamente:

```
"2 * 3 = 8"
```

### ✔️ Correção:

Alteração para:

```
"2 ** 3 = 8"
```

### 🔍 Como foi detectado:

O erro foi identificado através de testes com **mock**, que verificaram o argumento passado ao método `salvar()`.

---

## 📊 6. Cobertura de Código

A cobertura foi medida utilizando `coverage.py`.

### 📈 Evolução da cobertura:

* Inicial: 91%
* Após melhorias: 95%
* Após ajustes finais: 100%

### ✔️ Resultado final:

```
src/calculadora.py    43      0    100%
TOTAL                113      0    100%
```

### ✔️ Ajustes realizados:

* Inclusão de testes para métodos não cobertos
* Cobertura de todos os fluxos condicionais
* Teste do método `obter_ultimo_resultado`

---

## 🧠 7. Reflexão: Stub vs Mock

| Conceito | Descrição                                                               |
| -------- | ----------------------------------------------------------------------- |
| **Stub** | Simula o comportamento de dependências, retornando valores controlados  |
| **Mock** | Verifica a interação entre componentes, validando chamadas e argumentos |

### ✔️ Diferença prática:

* Stub foi utilizado para isolar a lógica da calculadora
* Mock foi essencial para validar comunicação e detectar o bug

---

## ✅ 8. Conclusão

A atividade permitiu aplicar na prática conceitos fundamentais de teste de software, incluindo:

* Escrita de testes robustos
* Identificação de bugs através de testes
* Uso de ferramentas de cobertura
* Compreensão da diferença entre stub e mock

Ao final, foi possível atingir **100% de cobertura** no módulo principal e garantir o correto funcionamento do sistema.

---
