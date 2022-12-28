<p align="center">
<code>cd</code> to any path without escaping in <a href="https://xon.sh">xonsh shell</a>.
<br/>
Replaces <code>cd </code> at the start of a line with a <a href="https://xon.sh/tutorial_macros.html#subprocess-macros">subprocess macro</a> <code>cd! </code> 
</p>

<p align="center">  
If you like the idea click ⭐ on the repo and stay tuned.
</p>


## Installation

To install use pip:

```bash
xpip install xontrib-cd
# or: xpip install -U git+https://github.com/eugenesvk/xontrib-cd
```

This xontrib will get loaded automatically for interactive sessions; to stop this, set

```xonsh
$XONTRIBS_AUTOLOAD_DISABLED = {"cd", }
```

## Usage

Use `cd` as usual, but without the fear of copying&pasting arbitrary paths (e.g. `.../space separated/` or `.../[bracketed]/`)

```bash
xontrib load cd
cd ~/[Path] With Spaces	# equivalent to 'cd! ~/[Path] With Spaces'
cd C:/Program Files    	# equivalent to 'cd! C:/Program Files'
cd -P ~/SymlinkTo      	# follow symlinks, equivalent to 'cd -P! ~/SymlinkTo'
```

Set the following environment variables in your profile to enable __extra options__ (disabled by default):

  - `$XONTRIB_CD_ALTSYMLINKFLAG = True` to pass `-p`, `-f`, or `-s` flags (in addition to `-P`) to follow symlinks
  - `$XONTRIB_CD_ALTSYMLINKFUNC = True` to use `cdp`, `cdf`, or `cds` (in addition to `cd -P`) to follow symlinks
  - `$XONTRIB_CD_SYMLINKAlWAYSON = True` to make `cd` always follow symlinks (always pass `-P`)

## Known issues

To be discovered...

## Credits

This package was created with [xontrib cookiecutter template](https://github.com/xonsh/xontrib-cookiecutter) based on the idea of hooking into the command line input as implemented in [xontrib-sh](https://github.com/anki-code/xontrib-sh)
