import sys
import os
import yaml

def get_file_name(path, folder, file, extension):
	# when folder == '' result path looks like 'path//file.extension'
	if folder != '':
		folder += '/'
	return path + '/' + folder + file + '.' + extension

def load_config(config_path):
	try:
		with open(config_path, 'r') as stream:
			config = yaml.safe_load(stream)
		return config
	except Exception as e:
		quit(str(e) + '\nPlease create config.yml')

def ask_overwrite(file_name):
	if os.path.exists(file_name):
		answer = input('File "%s" already exist. Overwrite? [y, n] ' % file_name)
		if answer == 'n':
			return False
		elif answer == 'y':
			# clear file content
			open(file_name, 'w').close()
			return True

def merge_files(result_name, files):
	result_file = open(result_name, 'a')
	for file in files:
		file_name = get_file_name(current_path, input_folder, file, config['extension'])
		try:
			with open(file_name, 'r') as f:
				result_file.write(f.read())
		except Exception as e:
			print(e)

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
	if config['files'] == None:
		quit('No input files specified')

	if 'folder' in config:
		input_folder = config['folder']
	else:
		input_folder = ''

	result_name = get_file_name(current_path, input_folder, config['output'], config['extension'])

	if not ask_overwrite(result_name):
		quit('Exiting')

	merge_files(result_name, config['files'])
