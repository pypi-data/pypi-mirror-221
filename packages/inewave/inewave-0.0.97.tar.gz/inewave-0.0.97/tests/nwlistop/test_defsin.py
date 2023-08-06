from inewave.nwlistop.defsin import DefSIN

from tests.mocks.mock_open import mock_open
from unittest.mock import MagicMock, patch

from tests.mocks.arquivos.defsin import MockDefSIN

ARQ_TESTE = "./tests/mocks/arquivos/__init__.py"


def test_atributos_encontrados_defsin():
    m: MagicMock = mock_open(read_data="".join(MockDefSIN))
    with patch("builtins.open", m):
        n = DefSIN.read(ARQ_TESTE)
        assert n.valores is not None
        assert n.valores.iloc[0, 0] == 2022
        assert n.valores.iloc[-1, -1] == 0.0


def test_atributos_nao_encontrados_defsin():
    m: MagicMock = mock_open(read_data="")
    with patch("builtins.open", m):
        n = DefSIN.read(ARQ_TESTE)
        assert n.valores is None


def test_eq_defsin():
    m: MagicMock = mock_open(read_data="".join(MockDefSIN))
    with patch("builtins.open", m):
        n1 = DefSIN.read(ARQ_TESTE)
        n2 = DefSIN.read(ARQ_TESTE)
        assert n1 == n2


# Não deve ter teste de diferença, visto que o atributo é
# implementado como Lazy Property.
