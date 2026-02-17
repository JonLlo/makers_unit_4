from lib.ex import *

def test_encode():
    result = encode('theswiftfoxjumpedoverthelazydog', 'secretkey')
    assert result == "EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL"

def test_decode():
    result = encode('EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL', 'secretkey')
    assert result == "theswiftfoxjumpedoverthelazydog"



