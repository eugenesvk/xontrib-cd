from xonsh.lexer	import get_tokens

def get_sep_pos(text):
  if text.strip():
    try:
      tokens = get_tokens(text, tolerant=True) # → LexToken(type, value, lineno, lexpos)
    except Exception:
      return
    sep_pos = list()
    sep_type = ['SEMI','PIPE','AND','OR']#; | && ||
    for token in tokens:
      if (_type := token.type) in sep_type:
        if (_pos := token.lexpos) not in sep_pos:
          sep_pos += [_pos]
    sep_pos.sort()
    return sep_pos
  else:
    return list()

def lead_space_count(txt):
  return len(txt) - len(txt.lstrip(' '))
def trail_space_count(txt):
  return len(txt) - len(txt.rstrip(' '))
