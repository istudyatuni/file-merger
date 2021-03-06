# File merger

Merge multiple files into one. Support inserting code as markdown code blocks.

*Configuration file*

| Key            | Description                                                                               | Default value |
|:---------------|:------------------------------------------------------------------------------------------|:--------------|
| files          | array with input files names <sup>1</sup>                                                 | -             |
| folder         | sub-folder, where files located                                                           | -             |
| output         | output file name with optional path, relative to config location                          | -             |
| extension      | extension for all input and output files <sup>2</sup>                                     | -             |
| add_file_names | add file name before its text, or not                                                     | `false`       |
| file_label     | what write before file name                                                               | `File: `      |
| remove_folder  | extract from 'folder/file.txt' only 'file.txt', for use in file name <sup>3</sup>         | `false`       |
| code_in_md     | write code in markdown file between back-tics \`\`\` with file extension for highlighting | `false`       |
| ask_overwrite  | ask for overwrite or not                                                                  | `false`       |
| empty          | generate empty file by path <sup>4</sup>                                                  | `false`       |
| use            | use this config file or not                                                               | `true`        |

<sup>1</sup> All the contents of the files are combined in the order of the files. In this list you can use key `text` instead of file name for inserting any text between file's content:

```yaml
files:
  - text: 'some text'
```

<sup>2</sup> If specified, you should write the names of all files without extensions.

<sup>3</sup> Used with the `add_file_names` flag enabled.

<sup>4</sup> If specified, no other parameters are needed:

```yaml
empty: path/to/result/file
```

## Running

```bash
python path/to/file_merger.py -f FOLDER -c CONFIG_NAME
```

`-f` - Absolute path to folder with project, default is from where script run.

`-c` - Config file name, default is `file-merger.yaml` (e.g. `folder/config.yaml`).
