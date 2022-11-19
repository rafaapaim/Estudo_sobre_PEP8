from typing import List, Dict, Union


class EstatisticaDetalhada:
    def __init__(self, dia: str, agencia: int) -> None:
        self.dia = dia
        self.agencia = agencia

    def roda_estatistica(self, clientes_atendidos: List[str]) -> Dict:
        estatistica: Dict[str, Union[List[str], str, int]] = {}
        estatistica['dia'] = self.dia
        estatistica['agencia'] = self.agencia
        estatistica['clientes_atendidos'] = clientes_atendidos
        estatistica['quantidade_clientes_atendidos'] = ( 
            # Maximo de colunas é 79, por isso usa parênteses e quebra de linha
            len(clientes_atendidos)
        )
        return estatistica
        