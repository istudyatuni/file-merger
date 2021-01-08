import sys
import os
import yaml

def get_file_name(path, folder, file, ext):
	# when folder == '' result path looks like 'path//file.ext'
	if folder != '':
		folder += '/'
	if ext != '':
		ext = '.' + ext
	return path + '/' + folder + file + ext

def load_config(config_path):
	try:
		with open(config_path, encoding='utf-8', mode='r') as stream:
			config = yaml.safe_load(stream)
		return config
	except Exception as e:
		e_type = e.__class__
		if e_type == UnicodeDecodeError:
			msg = 'Please use UTF-8 encoding for config'
		elif e_type == FileNotFoundError:
			msg = 'Please create config.yml'
		else:
			msg = 'Unknown error. You can try check UTF-8 encoding'

		quit(str(e) + '\n' + msg)

def ask_overwrite(file_name, ask_for_overwrite = True):
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

def config_key(config, key):
	if key in config:
		return config[key]
	else:
		return ''

def merge_files(path, result_name, folder, files, ext, file_name_string, add_names):
	result_file = open(result_name, 'a')
	name = ''
	for file in files:
		if add_names:
			name = file_name_string + file + '\n\n'

		file_name = get_file_name(path, folder, file, ext)
		try:
			with open(file_name, 'r') as f:
				result_file.write(name + f.read() + '\n')
		except Exception as e:
			print(e)
	print('Successfully written')

def merge(config):
	if config_key(config, 'files') == '':
		quit('No input files specified')

	if config_key(config, 'use') == False:
		quit('Incorrect config path\nIf this behaviour is unexpected, check key "use" in config file')

	input_folder = config_key(config, 'folder')
	ext          = config_key(config, 'extension')

	# add file names to output file or not
	add_names    = config_key(config, 'add_file_names')
	if add_names == '':
		add_names = False

	# what write before file name
	file_name_string = config_key(config, 'file_name_string')
	if file_name_string == '':
		file_name_string = 'File: '

	current_path = os.getcwd()
	result_name = get_file_name(current_path, input_folder, config['output'], ext)

	if not ask_overwrite(result_name, config['ask_overwrite']):
		quit('Exiting')

	merge_files(current_path, result_name, input_folder, config['files'], ext, file_name_string, add_names)

if __name__ == '__main__':
	script_path = sys.path[0]

	# from where script run
	current_path = os.getcwd()

	# by default config located where script located
	if len(sys.argv) > 1:
	    config_path = current_path + '/' + sys.argv[1]
	else:
	    config_path = script_path + '/config.yml'

	config = load_config(config_path)

	merge(config)
