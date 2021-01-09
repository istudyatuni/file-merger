# File merger

Merge separate file to one.

Configuration file:

`extension` - extension for all input and output files (optional parameter)

If you specify `extension`, you must write all files without extensions

`folder` - sub-folder, where files located (optional parameter)

`files` - array with input file names without extension. Their content are merged in the order as in this list

`output` - resulting file name

`use` - if `false`, this config file will not be used (optional parameter)

`ask_overwrite` - ask for overwrite or not

`add_file_names` - add file name before its text, or not (optional parameter)

`file_label` - what write before file name, default is 'File: ' (optional parameter)

**Run**:

```bash
python path/to/file_merger.py -f FOLDER -c CONFIG_NAME
```

`-f` - Absolute path to folder with config, default is from where script run

`-c` - Config file name, default is config.yml
