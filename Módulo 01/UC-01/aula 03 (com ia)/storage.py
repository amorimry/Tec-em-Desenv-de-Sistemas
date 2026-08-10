import json
import os
from typing import List, Dict, Any, Tuple

from classes import Cliente, Servico, Agendamento


STORAGE_PATH = os.path.join(os.path.dirname(__file__), "storage.json")


def _read_storage() -> Dict[str, Any]:
    if not os.path.exists(STORAGE_PATH):
        return {"clientes": [], "servicos": [], "agendamentos": []}

    with open(STORAGE_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def _write_storage(data: Dict[str, Any]) -> None:
    with open(STORAGE_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def load_data() -> Tuple[List[Cliente], List[Servico], List[Agendamento]]:
    data = _read_storage()

    clientes: List[Cliente] = []
    for c in data.get("clientes", []):
        clientes.append(Cliente(c["nome"], c["telefone"], c["cpf"], c["email"]))

    servicos: List[Servico] = []
    for s in data.get("servicos", []):
        servicos.append(Servico(s["nome"], float(s["valor"]), s["duracao"]))

    # Para montar Agendamento precisamos localizar objetos
    clientes_por_cpf = {c.cpf: c for c in clientes}
    servicos_por_nome = {s.nome: s for s in servicos}

    agendamentos: List[Agendamento] = []
    for a in data.get("agendamentos", []):
        cpf = a["cliente_cpf"]
        servico_nome = a["servico_nome"]

        cliente_obj = clientes_por_cpf.get(cpf)
        servico_obj = servicos_por_nome.get(servico_nome)

        # Se algum item não existir na base, ignora (evita quebra)
        if cliente_obj is None or servico_obj is None:
            continue

        agendamentos.append(
            Agendamento(cliente_obj, servico_obj, a["data"], a["horario"])
        )

    return clientes, servicos, agendamentos


def save_data(clientes: List[Cliente], servicos: List[Servico], agendamentos: List[Agendamento]) -> None:
    data = {
        "clientes": [
            {"nome": c.nome, "telefone": c.telefone, "cpf": c.cpf, "email": c.email}
            for c in clientes
        ],
        "servicos": [
            {"nome": s.nome, "valor": s.valor, "duracao": s.duracao}
            for s in servicos
        ],
        "agendamentos": [
            {
                "cliente_cpf": a.cliente.cpf,
                "servico_nome": a.servico.nome,
                "data": a.data,
                "horario": a.horario,
            }
            for a in agendamentos
        ],
    }

    _write_storage(data)

