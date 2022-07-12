from libpythonpro.spam.enviador_de_email import Enviador


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None

def test_remetente():
    enviador = Enviador()
    resultado = enviador.enviar(
        'carlosalvesab@gmail.com',
        'carlosbarnabedev@gmail.com',
        'Curso Marketing',
        'Abra esse email para saber mais!'
    )
    assert 'carlosalvesab@gmail.com' in resultado