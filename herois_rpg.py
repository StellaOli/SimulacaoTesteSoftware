def calcular_ataque_total(forca: int, arma: int, nivel: int) -> int:
   
    ataque = forca * 2 + arma
   # mutação 1
   # ataque = forca * 2 - arma  

    if nivel >= 10:
        ataque += 5

    return ataque


def calcular_defesa_total(armadura: int, agilidade: int, escudo: bool) -> int:
   
    defesa = armadura + (agilidade // 2)
   # mutação 2
   # defesa = armadura + (agilidade * 2)

    if escudo:
        defesa += 5

    return defesa


def classe_heroi(forca: int, inteligencia: int, agilidade: int) -> str:
    
    if forca >= inteligencia and forca >= agilidade:
        return "Guerreiro"
    elif inteligencia > forca and inteligencia >= agilidade:
   # mutação 3
   # elif inteligencia < forca and inteligencia >= agilidade:    
        return "Mago"
    else:
        return "Ladino"


def calcular_dano_final(ataque: int, defesa_inimigo: int, critico: bool) -> int:
   
    dano = ataque - defesa_inimigo
      
    if dano < 0:
    # mutação 4
    # if dano > 0:
        dano = 0

    if critico:
        dano *= 2

    return dano


def pode_usar_habilidade(classe: str, mana: int, stamina: int) -> bool:
   
    if classe == "Mago":
        return mana >= 20
    elif classe == "Guerreiro":
        return stamina >= 15   
    elif classe == "Ladino":
       # mutação
       # return stamina >= 10 or mana >= 5
        return stamina >= 10 and mana >= 5

    return False
