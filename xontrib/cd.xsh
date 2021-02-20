import xonsh

__all__ = ()

_alt_symlink_flag      = __xonsh__.env.get('XONTRIB_CD_ALTSYMLINKFLAG' , False)
_alt_symlink_func      = __xonsh__.env.get('XONTRIB_CD_ALTSYMLINKFUNC' , False)
_symlink_always_follow = __xonsh__.env.get('XONTRIB_CD_SYMLINKAlWAYSON', False)

@events.on_transform_command
def _cd_macro(cmd, **kw):
  if cmd.startswith('cd -P '):
    return 'cd -P! ' + cmd[6:]
  elif (_alt_symlink_flag and                    # alt flags for following symlinks
       (cmd.startswith('cd -p ') or
        cmd.startswith('cd -f ') or
        cmd.startswith('cd -s ') )):
    return 'cd -P! ' + cmd[6:]
  elif (cmd.startswith('cd ') and not
        cmd.startswith('cd -P! ')):              # exclude previous matches
    if _symlink_always_follow:
      return 'cd -P! ' + cmd[3:]
    else:
      return 'cd! '    + cmd[3:]
  return cmd

@events.on_transform_command
def _cd_macro_symlink(cmd, **kw):                 # alt functions for following symlinks
  if (_alt_symlink_func and
     (cmd.startswith('cdp ') or
      cmd.startswith('cdf ') or
      cmd.startswith('cds ') )):
    return 'cd -P! ' + cmd[4:]
  return cmd
