# toolbox
Kaveh's toolbox

## Find files or directories recursively

### `fileutils.find_recursive` function:

`base_dir`: The Directory under which we look for files/subdirectories

`extention`: File extentions to use for. Note that it can also be a substring that directories or extention-less file names end with

`ftype`: 'd' for directory, 'f' for file

`max_depth`: Maximum depth to look for in the directory tree structure. Use `None` (default) if no depth limit is needed.
