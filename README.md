# File merger

Merge separate file to one.

Configuration file:

`extension` - extension for all input and output files (optional parameter)

`folder` - sub-folder, where files located (optional parameter)

`files` - array with input file names without extension. Their content are merged in the order as in this list

`output` - resulting file name without extension

`use` - if `false`, this config file will not be used (optional parameter)

`ask_overwrite` - ask for overwrite or not

`add_file_names` - add file name before its text, or not (optional parameter)

Run:

```bash
python file_merger.py
```

The default config file location is the location of the script. You can specify a different file location:

```bash
python file_merger.py config.yml
```

For example, if you want to start from a different directory with your own config file, run:

```bash
python path/to/file_merger.py path/to/custom_config.yml
```
