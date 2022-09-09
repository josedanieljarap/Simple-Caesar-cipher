from caesar_cipher import encrypt

def test_encrypt_key_0():
    assert encrypt("a", 0) == "a"
    assert encrypt("azh", 0) == "azh"

def test_encrypt_key_1():    
    assert encrypt("a", 1) == "z"

def test_encrypt_complex():    
    assert encrypt("rf", 3) == "oc"
    assert encrypt("azh", 5) == "vuc"
