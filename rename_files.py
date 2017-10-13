import os
# Dynamic path to folder containing the files
base_dir=os.path.dirname(os.path.dirname(__file__))
file_path=os.path.join(base_dir,'prank')
def rename_files():
	file_list = os.listdir('prank')
	print(file_list)

rename_files()
