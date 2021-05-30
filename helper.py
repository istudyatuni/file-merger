import argparse
import os, yaml

default_config = {
	'empty': False,
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
			answer = input('File "%s" already exist. Overwrite? [Y,n] ' % file_name)

		if answer == 'y':
			# clear file content
			open(file_name, 'w').close()
			return True
		else:
			return False

	# not exist, create
	return True
