<p align="center">
<code>cd</code> to any path without escaping in <a href="https://xon.sh">xonsh shell</a>.
<br/>
Replaces <code>cd </code> at the start of a line with a <a href="https://xon.sh/tutorial_macros.html#subprocess-macros">subprocess macro</a> <code>cd! </code> 
</p>

<p align="center">  
If you like the idea click ⭐ on the repo and stay tuned.
</p>


## Install

```xsh
xpip install xontrib-cd
# or: xpip install -U git+https://github.com/eugenesvk/xontrib-cd
```

This xontrib will get loaded automatically for interactive sessions; to stop this, set

```xonsh
$XONTRIBS_AUTOLOAD_DISABLED = {"cd", }
```

## Configure

Set the following environment variables in your profile to enable __extra options__ (disabled by default):

  - `$XONTRIB_CD_ALTSYMLINKFLAG = True` to pass `-p`, `-f`, or `-s` flags (in addition to `-P`) to follow symlinks
  - `$XONTRIB_CD_ALTSYMLINKFUNC = True` to use `cdp`, `cdf`, or `cds` (in addition to `cd -P`) to follow symlinks
  - `$XONTRIB_CD_SYMLINKAlWAYSON = True` to make `cd` always follow symlinks (always pass `-P`)
  - `$XONTRIB_CD_LASTCMD = True` to make `cd` also work when it's the last command in a multi-command line


## Use

Use `cd` as usual, but without the fear of copying&pasting arbitrary paths (e.g. `.../space separated/` or `.../[bracketed]/`)

```xsh
xontrib load cd
cd ~/[Path] With Spaces	# equivalent to 'cd! ~/[Path] With Spaces'
cd C:/Program Files    	# equivalent to 'cd! C:/Program Files'
cd -P ~/SymlinkTo      	# follow symlinks, equivalent to 'cd -P! ~/SymlinkTo'
```

Add a space before ` cd` to disable adding `!`

## Known issues

- Xontrib autoload can't be disabled and prevents user configured environment vars from being read on time due to a [xonsh bug](https://github.com/xonsh/xonsh/issues/5020), so if you want to change the default configs via env vars, install the deauto branch `xpip install -U git+https://github.com/eugenesvk/xontrib-cd@deauto`
- Multiple commands per line like `cd ~; echo 1` will fail since `cd` is replaced with `cd!`, and everything after `!` is treated as a single string argument, ignoring the `;` separators
- But `echo 1; cd ~` will work with `$XONTRIB_CD_LASTCMD`

## Credits

This package was created with [xontrib cookiecutter template](https://github.com/xonsh/xontrib-cookiecutter) based on the idea of hooking into the command line input as implemented in [xontrib-sh](https://github.com/anki-code/xontrib-sh)
