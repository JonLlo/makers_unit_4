from lib.ex import *

def test_say_hello():
    result = say_hello("Jonny")
    assert result == "hello Jonny"


# Intended output:
#
# > say_hello("kay")
# => "hello kay"
def test_encode():
    result = encode("Jonny")
    assert result == "hello Jonny"