import os
# Dynamic path to folder containing the files
base_dir=os.path.dirname(os.path.dirname(__file__))
file_path=os.path.join(base_dir,'prank')
def rename_files():
	file_list = os.listdir('prank')
	print(file_list,file_path)
	os.chdir('prank')
	for file_name in file_list:
		os.renames(file_name,file_name.translate(None,"0123456789"))
	os.chdir(os.getcwd())

rename_files()
