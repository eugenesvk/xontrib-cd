from .helper        	import get_sep_pos, lead_space_count
from xonsh.built_ins	import XSH

envx      = XSH.env or {}

_alt_symlink_flag     	= envx.get('XONTRIB_CD_ALTSYMLINKFLAG' 	, False)
_symlink_always_follow	= envx.get('XONTRIB_CD_SYMLINKAlWAYSON'	, False)

def listen_cmd_macro(        cmd, **kw):
  alt_sym_flag = ['cd -p ','cd -f ','cd -s ']
  if cmd.startswith('cd -P '):
    return   'cd -P! ' + cmd[6:]
  elif (_alt_symlink_flag    and                 # alt flags for following symlinks
    cmd[:6] in alt_sym_flag):
    return   'cd -P! ' + cmd[6:]
  elif\
  (cmd.startswith('cd '    ) and not
   cmd.startswith('cd -P! ')):                   # exclude previous matches
    if _symlink_always_follow:
      return 'cd -P! ' + cmd[3:]
    else:
      return 'cd! '    + cmd[3:]
  else:
    return               cmd

def listen_cmd_macro_symlink(cmd, **kw):         # alt functions for following symlinks
  alt_sym_funcs = ['cdp ','cdf ','cds ']
  if cmd[:4] in alt_sym_funcs:
    return   'cd -P! ' + cmd[4:]
  else:
    return               cmd
