import sys
import os
import yaml

def get_file_name(path, folder, file, extension):
	return path + '/' + folder + '/' + file + '.' + extension

if __name__ == '__main__':
	script_path = sys.path[0]

	# by default config located where script located
	if len(sys.argv) > 1:
	    config_path = sys.argv[1]
	else:
	    config_path = script_path + '/config.yml'

	# from where script run
	current_path = os.getcwd()

	# load config
	try:
		with open(config_path, 'r') as stream:
			config = yaml.safe_load(stream)
	except Exception as e:
		quit(str(e) + '\nPlease create config.yml')

	print(config)

	if 'folder' in config:
		input_folder = config['folder']
	else:
		input_folder = ''

	result_name = get_file_name(current_path, input_folder, config['output'], config['extension'])

	# check file existing
	if os.path.exists(result_name):
		answer = input('File already exist. Overwrite? [y, n]')
		if answer == 'n':
			quit('Exiting')
		elif answer == 'y':
			# clear file content
			open(result_name, 'w').close()

	# merge
	result_file = open(result_name, 'a')
	for file in config['files']:
		file_name = get_file_name(current_path, input_folder, file, config['extension'])
		try:
			with open(file_name, 'r') as f:
				result_file.write(f.read())
		except Exception as e:
			print(e)
