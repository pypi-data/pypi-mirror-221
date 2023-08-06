# FileMan

FileMan is a file management utility package.

## Installation

You can install FileMan using pip:

```
pip install fileman
```

## Usage

Here is an example of how to use FileMan:

```python
>>>from File_Man import FileMan
>>>fileman = FileMan()

>>># Collect Dir+SubDirs+Content => JSON
>>>tree = fileman.get_tree(path)

>>># Or for OneLevel:
>>>fileman.file_list(path)

>>># 0: File_Name; 1: DATA; 2: Delimiter; 3:ReadWriteMode
>>>fileman.write_file(file_name, data, delim, rwm)
>>>fileman.read_file(file_name, delim)

```
