# File merger

Merge separate file to one.

Configuration file:

`extension` - input and output files extension

`folder` - sub-folder, where files located (optional parameter)

`files` - array with input file names without extension. Their content are merged in the order as in this list

`output` - resulting file name without extension

`use` - if `false`, this config file will not be used (optional parameter)

`ask_overwrite` - ask for overwrite or not

Run:

```bash
python merger.py
```

The default config file location is the location of the script. You can specify a different file location:

```bash
python merger.py config.yml
```

For example, if you want to start from a different directory with your own config file, run:

```bash
python path/to/merger.py path/to/custom_config.yml
```
