import argparse
import os, re, yaml

code_extensions = [
	'c',
	'cpp',
	'css',
	'h',
	'html',
	'py',
	'yaml',
	'yml',
]

default_config = {
	'extension': '',
	'folder': '',
	'files': [],
	'output': '',
	'ask_overwrite': False,
	'add_file_names': False,
	'use': True,
	'file_label': 'File: ',
	'remove_folder': False,
	'code_in_md': False
}

def get_args():
	parser = argparse.ArgumentParser()

	# os.getcwd() is from where script run
	parser.add_argument('-f', '--folder', default=os.getcwd(), help='Absolute path to folder with files')
	parser.add_argument('-c', '--config', default='file-merger.yml', help='Config file name, or with folder: folder/config.yml')

	return parser.parse_args()

def get_file_name(path, folder, file, ext):
	# when folder == '' result path looks like 'path//file.ext'
	if folder:
		folder += '/'
	if ext:
		ext = '.' + ext
		file = file + ext
	return os.path.join(path, folder, file)
	# not testing, so while not removed
	# return path + '/' + folder + file + ext

def load_config(config_path):
	try:
		# encoding='utf-8'
		with open(config_path, mode='r') as stream:
			config = yaml.safe_load(stream)

		temp_conf = default_config
		for key in config:
			temp_conf[key] = config[key]

		return temp_conf

	except Exception as e:
		e_type = e.__class__
		if e_type == UnicodeDecodeError:
			msg = 'Please use UTF-8 encoding for config'
		elif e_type == FileNotFoundError:
			msg = 'Please create config.yml or run from right location'
		else:
			msg = 'Unknown error: %s. You can try check file encoding' % e_type.__name__

		quit(str(e) + '\n' + msg)

def ask_overwrite(file_name, ask_for_overwrite = False):
	if os.path.exists(file_name):
		answer = 'y'
		if ask_for_overwrite:
			answer = input('File "%s" already exist. Overwrite? [y, n] ' % file_name)

		if answer == 'y':
			# clear file content
			open(file_name, 'w').close()
			return True
		else:
			return False

	# not exist, create
	return True

def merge_files(path, result_name, config):
	result_file = open(result_name, 'a')
	name = ''
	was_error = False

	for file in config['files']:
		if 'text' in file:
			# write some text instead of file
			result_file.write(file['text'] + '\n')
			continue

		# if is code, add back-tics
		file_ext = re.search(r'\.([a-z]+)', file)
		file_ext = file_ext.group(1) if file_ext else ''
		if config['code_in_md'] and file_ext in code_extensions:

			start_tics = '```' + file_ext + '\n'
			end_tics = '```\n\n'
		else:
			start_tics = ''
			end_tics = ''

		if config['add_names'] and config['remove_folder']:
			file_name_label = re.search(r'/([a-z0-9\.]+)', file)
			file_name_label = file_name_label.group(1) if file_name_label else file

		if config['add_names']:
			name = config['file_label'] + file_name_label + '\n\n' + start_tics

		file_name = get_file_name(path, config['folder'], file, config['ext'])
		try:
			with open(file_name, 'r') as f:
				result_file.write(name + f.read() + end_tics)
		except Exception as e:
			print(e, '\nFile: %s\n'%file_name)
			was_error = True

	result_file.close()
	if was_error:
		print('Written with errors')
	else:
		print('Successfully written')

def setup_merge(config, current_path = os.getcwd()):
	if not config['use']:
		quit('This config file is marked unused')

	if not config['files']:
		quit('No input files specified')

	result_name = get_file_name(current_path, config['folder'], config['output'], config['extension'])

	if not ask_overwrite(result_name, config['ask_overwrite']):
		quit('Exiting')

	merge_files(current_path, result_name, config)

if __name__ == '__main__':
	args = get_args()

	current_path = args.folder
	if os.path.exists(args.config):
		config_path = args.config
	else:
		config_path = current_path + '/' + args.config

	config = load_config(config_path)

	setup_merge(config, current_path)
