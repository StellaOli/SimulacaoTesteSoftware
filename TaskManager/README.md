# Task Manager - Atividade 09

Sistema simples de gerenciamento de tarefas com testes automatizados.

## Funcionalidades
- Criar tarefas
- Listar tarefas
- Buscar por ID
- Atualizar status
- Deletar tarefas

## Tecnologias
- Python 3
- pytest
- unittest.mock

## Instalação
```bash
pip install -r requirements.txt

```

## Executar testes

```bash
python -m pytest -v

```

## Estrutura

task_manager/
    task.py
    storage.py
    repository.py

tests/
    test_task.py
    test_repository.py

---

## ✅ O que esse código cobre (exatamente o que o professor pediu):
- ✔ Teste de estado  
- ✔ Fixture (setup)  
- ✔ Teste de ciclo de vida  
- ✔ Mock (`assert_called_once`)  
- ✔ Stub (`return_value`)  
- ✔ Teste de interação entre métodos  
- ✔ Teste unitário vs componente  
