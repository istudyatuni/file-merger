import argparse
import os
import yaml

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
	return path + '/' + folder + file + ext

def load_config(config_path):
	try:
		with open(config_path, mode='r') as stream: # encoding='utf-8'
			config = yaml.safe_load(stream)
		return config
	except Exception as e:
		e_type = e.__class__
		if e_type == UnicodeDecodeError:
			msg = 'Please use UTF-8 encoding for config'
		elif e_type == FileNotFoundError:
			msg = 'Please create config.yml or run from right location'
		else:
			msg = 'Unknown error: %s. You can try check file encoding' % e_type.__name__

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

def config_key(config, key, default = ''):
	if key in config:
		return config[key]
	else:
		return default

def merge_files(path, result_name, folder, files, ext, file_label = '', add_names = False):
	result_file = open(result_name, 'a')
	name = ''
	was_error = False

	for file in files:
		if 'text' in file:
			# write some text instead of file
			result_file.write(file['text'] + '\n')
			continue

		if add_names:
			name = file_label + file + '\n\n'

		file_name = get_file_name(path, folder, file, ext)
		try:
			with open(file_name, 'r') as f:
				result_file.write(name + f.read() + '\n')
		except Exception as e:
			print(e, '\nFile: %s\n'%file_name)
			was_error = True

	result_file.close()
	if was_error:
		print('Written with errors')
	else:
		print('Successfully written')

def merge(config, current_path = os.getcwd()):
	if not config_key(config, 'use', True):
		quit('This config file is marked unused')

	if not config_key(config, 'files'):
		quit('No input files specified')

	input_folder = config_key(config, 'folder')
	ext          = config_key(config, 'extension')

	# add file names to output file or not
	add_names = config_key(config, 'add_file_names', False)

	# what write before file name
	file_label = config_key(config, 'file_label', 'File: ')

	result_name = get_file_name(current_path, input_folder, config['output'], ext)

	if not ask_overwrite(result_name, config['ask_overwrite']):
		quit('Exiting')

	merge_files(current_path, result_name, input_folder, config['files'], ext, file_label, add_names)

if __name__ == '__main__':
	args = get_args()

	current_path = args.folder
	config_path = current_path + '/' + args.config

	config = load_config(config_path)

	merge(config, current_path)
