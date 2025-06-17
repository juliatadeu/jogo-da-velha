__all__ = ["insere_lance", "consulta_tabuleiro", "partida_acabou"]

from tabuleiro import insere_lance as tabuleiro_insere, retorna_tabuleiro
from condicoes import partida_acabou as verifica_fim

"""
    Nome: insere_lance(i, j, mark)

    Objetivo:
        Inserir um lance no tabuleiro, verificando validade por meio do módulo tabuleiro.

    Acoplamento:
        - parâmetros: i (int), j (int), mark (int)
        - retorno: int — 1 se jogada foi bem-sucedida; 0 caso contrário.

    Condições de Acoplamento:
        AE: posição dentro dos limites e livre.
        AS: valor inserido no tabuleiro, se válido.

    Descrição:
        1) Encaminha a jogada para a função insere_lance do módulo tabuleiro.
        2) Retorna o resultado.

    Hipóteses:
        - `mark` deve ser 0 (X) ou 1 (O).
"""
def insere_lance(i, j, mark):
    return tabuleiro_insere(i, j, mark)

"""
    Nome: consulta_tabuleiro()

    Objetivo:
        Consultar o estado atual do tabuleiro da partida em andamento.

    Acoplamento:
        - retorno: matriz 3x3 com os valores do tabuleiro.

    Condições de Acoplamento:
        AE: chamada sem parâmetros.
        AS: retorna cópia segura da matriz.

    Descrição:
        1) Solicita ao módulo tabuleiro a matriz atual.
        2) Retorna a cópia obtida.

    Hipóteses:
        - Usado para exibir o estado do jogo ou para análise por outro módulo.
"""
def consulta_tabuleiro():
    return retorna_tabuleiro()

"""
    Nome: partida_acabou()

    Objetivo:
        Verificar se a partida terminou com vitória, empate ou ainda está em andamento.

    Acoplamento:
        - retorno: int — -1 (não acabou), 0 (X venceu), 1 (O venceu), 2 (empate)

    Condições de Acoplamento:
        AE: chamada sem parâmetros.
        AS: retorno do status da partida.

    Descrição:
        1) Consulta o tabuleiro atual.
        2) Encaminha a matriz para o módulo de condições.
        3) Retorna o resultado da verificação.

    Hipóteses:
        - Verificado após cada jogada.

    Restrições:
        - Deve retornar valor coerente com as regras do jogo.
"""
def partida_acabou():
    matriz = retorna_tabuleiro()
    return verifica_fim(matriz)
