import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from app import app

def test_home_route():
    cliente = app.test_client()
    respuesta = cliente.get('/')
    assert respuesta.status_code == 200
    assert "mensaje" in respuesta.json
