from hashlib import sha1

def hex_has(string,salt=None):
    str = '*&'+string+'&*'
    if salt:
        str = str + salt
    sh = sha1()
    sh.update(str.encode('utf-8'))
    return sh.hexdigest()
