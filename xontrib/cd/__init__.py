from xonsh.built_ins       	import XSH
from xontrib.cd.event_hooks	import listen_cmd_macro, listen_cmd_macro_symlink

__all__ = ()

envx      = XSH.env or {}
eventx    = XSH.builtins.events

# Get user config environment variables
_alt_symlink_func      = envx.get('XONTRIB_CD_ALTSYMLINKFUNC' , False)

eventx.on_transform_command(listen_cmd_macro)
if _alt_symlink_func:
  eventx.on_transform_command(listen_cmd_macro_symlink)
