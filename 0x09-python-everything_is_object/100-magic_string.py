def magic_string():
    magic_string.n += 1
    return ("Holberton" * magic_string.n)
setattr(magic_string, 'n', 0)
