import pytest

from libpythonpro.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'remetente',
    ['carlosalvesab@gmail.com', 'foo@bar.com.br']
)
def test_remetente(remetente):
    enviador = Enviador()
    resultado = enviador.enviar(
        remetente,
        'carlosbarnabedev@gmail.com',
        'Curso Marketing',
        'Abra esse email para saber mais!'
    )
    assert remetente in resultado


@pytest.mark.parametrize(
    'remetente',
    ['', 'carlos']
)

def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente,
            'carlosbarnabedev@gmail.com',
            'Curso Marketing',
            'Abra esse email para saber mais!'
        )