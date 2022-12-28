from builtins import __xonsh__  # XonshSession (${...} is '__xonsh__.env')
envx = __xonsh__.env

_alt_symlink_flag      = envx.get('XONTRIB_CD_ALTSYMLINKFLAG' , False)
_alt_symlink_func      = envx.get('XONTRIB_CD_ALTSYMLINKFUNC' , False)
_symlink_always_follow = envx.get('XONTRIB_CD_SYMLINKAlWAYSON', False)

def listen_cmd_macro(        cmd, **kw):
  if cmd.startswith('cd -P '):
    return 'cd -P! ' + cmd[6:]
  elif (_alt_symlink_flag    and                 # alt flags for following symlinks
  (cmd.startswith('cd -p ')  or
   cmd.startswith('cd -f ')  or
   cmd.startswith('cd -s ') )):
    return   'cd -P! ' + cmd[6:]
  elif\
  (cmd.startswith('cd '    ) and not
   cmd.startswith('cd -P! ')):                   # exclude previous matches
    if _symlink_always_follow:
      return 'cd -P! ' + cmd[3:]
    else:
      return 'cd! '    + cmd[3:]
  else:
    return cmd

def listen_cmd_macro_symlink(cmd, **kw):         # alt functions for following symlinks
  if (_alt_symlink_func      and                 # duplicate check to main
  (cmd.startswith('cdp ')    or
   cmd.startswith('cdf ')    or
   cmd.startswith('cds ') )):
    return   'cd -P! ' + cmd[4:]
  else:
    return cmd
