from typing import Annotated

from pydantic import UUID4, Field

from workout_api.contrib.schemas import BaseSchema


class CentroTreinamentoIn(BaseSchema):
    nome: Annotated[
        str,
        Field(
            description="Nome do CT(Centro de Treinamento)",
            example="CT Sparta",
            max_length=20,
        ),
    ]
    endereco: Annotated[
        str,
        Field(
            description="Rua do CT(Centro de Treinamento)",
            example="Rua Alguma Coisa de Algo",
            max_length=60,
        ),
    ]
    proprietario: Annotated[
        str,
        Field(
            description="Proprietario do CT(Centro de Treinamento)",
            example="Lucas",
            max_length=30,
        ),
    ]


class CentroTreinamentoAtleta(BaseSchema):
    nome: Annotated[
        str,
        Field(
            description="Nome do centro de treinamento",
            example="CT Esparta",
            max_length=20,
        ),
    ]


class CentroTreinamentoOut(CentroTreinamentoIn):
    id: Annotated[UUID4, Field(description="Identificador do centro de treinamento")]
