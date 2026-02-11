import json
import ast


def parse_json_data(data):
    """Converte diferentes formatos de dados para uma lista de dicionários"""
    if isinstance(data, list):
        # Se o primeiro item for uma string JSON válida (aspas duplas)
        if (
            len(data) == 1
            and isinstance(data[0], str)
            and data[0].strip().startswith("[")
        ):
            return json.loads(data[0])

        # Se a lista contém strings que parecem dicionários (aspas simples), convertemos manualmente
        try:
            return [
                ast.literal_eval(item) if isinstance(item, str) else item
                for item in data
            ]
        except (SyntaxError, ValueError):
            return data  # Retorna os dados originais se a conversão falhar

    # Se for uma string única com aspas simples, tenta converter para um dicionário
    if isinstance(data, str):
        try:
            return ast.literal_eval(data)
        except (SyntaxError, ValueError):
            return json.loads(data) if data.startswith("[") else data

    return data
