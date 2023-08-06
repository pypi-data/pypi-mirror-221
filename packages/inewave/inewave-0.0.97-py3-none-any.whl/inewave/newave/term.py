from inewave.newave.modelos.term import BlocoTermUTE

from cfinterface.files.sectionfile import SectionFile
from typing import Type, TypeVar, Optional
import pandas as pd  # type: ignore

# Para compatibilidade - até versão 1.0.0
from os.path import join
import warnings


class Term(SectionFile):
    """
    Armazena os dados de entrada do NEWAVE referentes aos dados das
    usinas térmicas.
    """

    T = TypeVar("T")

    SECTIONS = [BlocoTermUTE]

    def __init__(self, data=...) -> None:
        super().__init__(data)

    @classmethod
    def le_arquivo(cls, diretorio: str, nome_arquivo="term.dat") -> "Term":
        msg = (
            "O método le_arquivo(diretorio, nome_arquivo) será descontinuado"
            + " na versão 1.0.0 - use o método read(caminho_arquivo)"
        )
        warnings.warn(msg, category=FutureWarning)
        return cls.read(join(diretorio, nome_arquivo))

    def escreve_arquivo(self, diretorio: str, nome_arquivo="term.dat"):
        msg = (
            "O método escreve_arquivo(diretorio, nome_arquivo) será"
            + " descontinuado na versão 1.0.0 -"
            + " use o método write(caminho_arquivo)"
        )
        warnings.warn(msg, category=FutureWarning)
        self.write(join(diretorio, nome_arquivo))

    def __bloco_por_tipo(self, bloco: Type[T], indice: int) -> Optional[T]:
        """
        Obtém um gerador de blocos de um tipo, se houver algum no arquivo.

        :param bloco: Um tipo de bloco para ser lido
        :type bloco: T
        :param indice: O índice do bloco a ser acessado, dentre os do tipo
        :type indice: int
        :return: O gerador de blocos, se houver
        :rtype: Optional[Generator[T], None, None]
        """
        try:
            return next(
                b
                for i, b in enumerate(self.data.of_type(bloco))
                if i == indice
            )
        except StopIteration:
            return None

    @property
    def usinas(self) -> Optional[pd.DataFrame]:
        """
        Tabela com configurações e custos das usinas térmicas.

        - Número (`int`)
        - Nome (`str`)
        - Potência Instalada (`float`)
        - FC Máximo (`float`)
        - TEIF (`float`)
        - Indisponibilidade Programada (`float`)
        - GT Min Janeiro (`float`)
        - ...
        - GT Min Dezembro (`float`)
        - GT Min D+ Anos (`float`)

        :return: A tabela como um DataFrame
        :rtype: pd.DataFrame | None
        """
        b = self.__bloco_por_tipo(BlocoTermUTE, 0)
        if b is not None:
            return b.data
        return None

    @usinas.setter
    def usinas(self, df: pd.DataFrame):
        b = self.__bloco_por_tipo(BlocoTermUTE, 0)
        if b is not None:
            b.data = df
