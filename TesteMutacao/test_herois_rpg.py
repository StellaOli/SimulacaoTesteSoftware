from herois_rpg import *


def test_ataque_basico():
    assert calcular_ataque_total(10, 5, 1) == 25


def test_ataque_bonus_nivel():
    assert calcular_ataque_total(10, 5, 10) == 30


def test_defesa_sem_escudo():
    assert calcular_defesa_total(10, 6, False) == 13


def test_defesa_com_escudo():
    assert calcular_defesa_total(10, 6, True) == 18


def test_classe_guerreiro():
    assert classe_heroi(10, 5, 4) == "Guerreiro"


def test_classe_mago():
    assert classe_heroi(3, 10, 5) == "Mago"


def test_classe_ladino():
    assert classe_heroi(5, 4, 9) == "Ladino"


def test_dano_sem_critico():
    assert calcular_dano_final(20, 5, False) == 15


def test_dano_critico():
    assert calcular_dano_final(20, 5, True) == 30


def test_pode_usar_magia():
    assert pode_usar_habilidade("Mago", 25, 0) == True
