from xonsh.built_ins import XonshSession

__all__ = ()

def _load_xontrib_(xsh: XonshSession, **_):
  # Get user config environment variables
  _alt_symlink_func      = xsh.env.get('XONTRIB_CD_ALTSYMLINKFUNC' , False)

  from .event_hooks import listen_cmd_macro, listen_cmd_macro_symlink
  xsh.builtins.events.on_transform_command(listen_cmd_macro)
  if _alt_symlink_func:
    xsh.builtins.events.on_transform_command(listen_cmd_macro_symlink)
