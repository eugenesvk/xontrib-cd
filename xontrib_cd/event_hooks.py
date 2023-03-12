from .helper        	import get_sep_pos, lead_space_count
from xonsh.built_ins	import XSH

envx      = XSH.env or {}

_alt_symlink_flag     	= envx.get('XONTRIB_CD_ALTSYMLINKFLAG' 	, False)
_symlink_always_follow	= envx.get('XONTRIB_CD_SYMLINKAlWAYSON'	, False)
_last_cmd             	= envx.get('XONTRIB_CD_LASTCMD'        	, False)

def _sub_cmd(                cmd):
  alt_sym_flag = ['cd -p ','cd -f ','cd -s ']
  if  (cmd.startswith('cd! '   )\
  or   cmd.startswith('cd -P! ')):               # already transformed, pass thru
    return                        cmd
  elif cmd.startswith('cd -P '):
    return            'cd -P! ' + cmd[6:]        # 6=len('cd -P ')
  elif (_alt_symlink_flag\
  and  cmd[:6] in alt_sym_flag):                 # alt flags for following symlinks
    return            'cd -P! ' + cmd[6:]        # 6=len('cd -p ')
  elif cmd.startswith('cd '    ):
    if _symlink_always_follow:
      return          'cd -P! ' + cmd[3:]        # 3=len('cd ')
    else:
      return          'cd! '    + cmd[3:]

def listen_cmd_macro(        cmd, **kw):
  cmd_sub = _sub_cmd(cmd)
  if cmd_sub:      # check first command
    return               cmd_sub
  elif _last_cmd:  # check last  command
    if (sep_pos := get_sep_pos(cmd)):
      last_cmd_i  	= sep_pos[-1]
      pre_cmd     	= cmd[:last_cmd_i+1 ]
      last_cmd    	= cmd[ last_cmd_i+1:]
      lead_sp     	= ' ' * lead_space_count(last_cmd)
      last_cmd_sub	= _sub_cmd(last_cmd.lstrip(' '))
      if (len(lead_sp) < 2) and last_cmd_sub:
        cmd_sub = pre_cmd + lead_sp + last_cmd_sub
        return           cmd_sub
    return               cmd
  else:
    return               cmd

def _sub_cmd_alt_sym(        cmd):
  alt_sym_funcs = ['cdp ','cdf ','cds ']
  if  (cmd.startswith('cd! '   )\
  or   cmd.startswith('cd -P! ')):               # already transformed, pass thru
    return                        cmd
  elif cmd[:4] in alt_sym_funcs:
    return            'cd -P! ' + cmd[4:]        # 4=len('cdp ')

def listen_cmd_macro_symlink(cmd, **kw):         # alt functions for following symlinks
  cmd_sub = _sub_cmd_alt_sym(cmd)
  if cmd_sub:      # check first command
    return               cmd_sub
  elif _last_cmd: # check last  command
    if (sep_pos := get_sep_pos(cmd)):
      last_cmd_i  	= sep_pos[-1]
      pre_cmd     	= cmd[:last_cmd_i+1 ]
      last_cmd    	= cmd[ last_cmd_i+1:]
      lead_sp     	= ' ' * lead_space_count(last_cmd)
      last_cmd_sub	= _sub_cmd_alt_sym(last_cmd.lstrip(' '))
      if (len(lead_sp) < 2) and last_cmd_sub:
        cmd_sub = pre_cmd + lead_sp + last_cmd_sub
        return           cmd_sub
    return               cmd
  else:
    return               cmd
