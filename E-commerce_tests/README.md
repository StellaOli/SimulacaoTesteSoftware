# 🧪 E-commerce API — Testes de Qualidade e Desempenho

## 📌 Descrição

Este projeto tem como objetivo aplicar práticas de **testes automatizados, desempenho, carga e estresse** em uma API de e-commerce, avaliando sua confiabilidade, tempo de resposta e capacidade de escalabilidade sob diferentes condições de uso.

A proposta consiste em simular cenários reais de utilização do sistema, desde acessos normais até situações extremas de sobrecarga.

---

## 🎯 Objetivos

- Validar o funcionamento da API por meio de testes automatizados  
- Medir o tempo de resposta das requisições  
- Avaliar o comportamento sob carga crescente de usuários  
- Identificar limites de capacidade e pontos de falha  
- Analisar a escalabilidade do sistema  

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.13**
- **pytest** → testes automatizados  
- **pytest-benchmark** → análise de desempenho  
- **Locust** → testes de carga e estresse  
- **FastAPI + Uvicorn** → API testada  

---

## 🧪 Tipos de Testes Implementados

### 1. ✅ Testes Funcionais e de Segurança

Verificam se a API responde corretamente e se endpoints críticos funcionam como esperado.

**Resultado:**

2 passed in 4.19s

✔️ Todos os testes passaram com sucesso.

---

### 2. ⚡ Teste de Desempenho (Benchmark)

Medição do tempo de resposta da API.

**Resultado:**

Tempo médio: ~200 ms
OPS: ~4.98


✔️ O sistema apresentou **tempo de resposta estável e consistente**.

---

### 3. 📈 Teste de Carga

Simulação de uso com múltiplos usuários simultâneos.

**Configuração:**
- 500 usuários  
- Ramp-up: 50 usuários/s  

**Resultados:**

| Endpoint        | Requests | Falhas | Tempo Médio |
|----------------|---------|--------|------------|
| GET /produto/1 | 2592    | 0      | 98 ms      |
| POST /compra   | 834     | 0      | 93 ms      |
| **Total**      | 3426    | 0      | 96 ms      |

✔️ **0% de falhas**  
✔️ Tempo de resposta baixo  
✔️ Sistema estável sob carga moderada  

---

### 4. 💥 Teste de Estresse

Simulação de cenário extremo para identificar o limite do sistema.

**Configuração:**
- 2000 usuários  
- Ramp-up: 150 usuários/s  

**Resultados:**

- Requisições totais: ~88.000+  
- ❌ Taxa de falha: **~85%**  
- ⏱️ Tempo médio: **~2400 ms**  
- 📈 RPS: **~250–320 req/s**  
- ⏱️ Tempo máximo: **~17s**  

---

## 📊 Análise dos Resultados

### 🔹 Comportamento sob diferentes cargas

| Cenário        | Resultado |
|----------------|----------|
| Baixa carga    | Estável  |
| Carga moderada | Estável  |
| Alta carga     | Degradação |
| Estresse       | Colapso  |

---

### 🔹 Principais observações

- O sistema mantém **bom desempenho até ~500 usuários**  
- A partir de cargas extremas:
  - O tempo de resposta cresce significativamente  
  - O sistema passa a apresentar alta taxa de falhas  
- O ponto de saturação ocorre próximo de **2000 usuários simultâneos**  

---

### 🔹 Possíveis gargalos identificados

- Limitação de recursos (CPU/memória)  
- Falta de controle de concorrência  
- Ausência de:
  - cache  
  - fila de processamento  
  - balanceamento de carga  

---

## 🧠 Conclusão

O sistema apresenta:

✔️ Boa performance em cenários normais e moderados  
⚠️ Limitações claras de escalabilidade  
❌ Falhas críticas sob alta concorrência  

Mesmo com um ramp-up controlado (150 usuários/s), o sistema demonstrou **saturação severa**, indicando necessidade de otimizações para ambientes de alta demanda.

---

## 🚀 Melhorias Futuras

- Implementação de **cache (Redis)**  
- Uso de **load balancer**  
- Otimização de queries e acesso a dados  
- Implementação de **rate limiting mais robusto**  
- Uso de **filas assíncronas (RabbitMQ/Kafka)**  
- Testes com diferentes perfis de carga (gradual vs explosivo)  

---

## ▶️ Como Executar os Testes

### 🔹 Testes automatizados
```bash
pytest -v

```

### 🔹 Teste de desempenho
```bash
pytest --benchmark-only
```

### 🔹 Teste de carga
```bash
locust -f locust/locust_carga.py
```

### 🔹 Teste de estresse
```bash
locust -f locust/locust_estresse.py --users 2000 --spawn-rate 150 --headless
```

📌 Considerações Finais

Este projeto demonstra, de forma prática, a importância de:

Testes contínuos
Monitoramento de performance
Planejamento de escalabilidade

Além disso, evidencia como um sistema funcional pode não estar preparado para alta demanda, reforçando a necessidade de testes além do nível funcional.