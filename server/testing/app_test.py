import io
import sys
from app import app

class TestApp:
    '''Flask application in flask_app.py'''

def test_index_route():
    '''has a resource available at "/".'''
    response = app.test_client().get('/')
    assert response.status_code == 200

def test_index_text():
    '''displays "Python Operations with Flask Routing and Views" in h1 in browser.'''
    response = app.test_client().get('/')
    assert response.data.decode() == '<h1>Python Operations with Flask Routing and Views</h1>'

def test_print_route():
    '''has a resource available at "/print/<parameter>".'''
    response = app.test_client().get('/print/hello')
    assert response.status_code == 200

def test_print_text():
    '''displays text of route in browser.'''
    response = app.test_client().get('/print/hello')
    assert response.data.decode() == '<h3>Printed String: hello</h3>'

def test_print_text_in_console():
    '''displays text of route in console.'''
    captured_out = io.StringIO()
    sys.stdout = captured_out
    app.test_client().get('/print/hello')
    sys.stdout = sys.__stdout__
    assert captured_out.getvalue().strip() == 'hello'

def test_count_route():
    '''has a resource available at "/count/<parameter>".'''
    response = app.test_client().get('/count/5')
    assert response.status_code == 200

def test_count_range_10():
    '''counts through range of parameter in "/count/<parameter" on separate lines.'''
    response = app.test_client().get('/count/10')
    # Extract the text inside <pre> tags
    html = response.data.decode()
    start_index = html.find('<pre>') + 5
    end_index = html.find('</pre>')
    count = html[start_index:end_index].strip()

    expected_count = '\n'.join(str(i) for i in range(10))
    assert count == expected_count

def test_math_route():
    '''has a resource available at "/math/<parameters>".'''
    response = app.test_client().get('/math/5/+/5')
    assert response.status_code == 200

def test_math_add():
    '''adds parameters in "/math/" resource when operation is "+".'''
    response = app.test_client().get('/math/5/+/5')
    assert response.data.decode() == '10'

def test_math_subtract():
    '''subtracts parameters in "/math/" resource when operation is "-".'''
    response = app.test_client().get('/math/5/-/5')
    assert response.data.decode() == '0'

def test_math_multiply():
    '''multiplies parameters in "/math/" resource when operation is "*".'''
    response = app.test_client().get('/math/5/*/5')
    assert response.data.decode() == '25'

def test_math_divide():
    '''divides parameters in "/math/" resource when operation is "div".'''
    response = app.test_client().get('/math/5/div/5')
    assert response.data.decode() == '1.0'

def test_math_modulo():
    '''finds remainder of parameters in "/math/" resource when operation is "%".'''
    response = app.test_client().get('/math/5/%/5')
    assert response.data.decode() == '0'
