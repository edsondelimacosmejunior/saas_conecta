import ast


def transformar_em_dict(valor):
    if isinstance(valor, str):  # Verifica se o valor é uma string
        try:
            return ast.literal_eval(valor)  # Tenta converter para dicionário
        except (ValueError, SyntaxError):
            raise ValueError("A string fornecida não é um dicionário válido.")
    elif isinstance(valor, dict):  # Se já for um dicionário
        return valor
    else:
        raise TypeError("O valor fornecido não é uma string nem um dicionário.")
