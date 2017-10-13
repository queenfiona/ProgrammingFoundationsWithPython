import os
base_dir= os.path.dirname(os.path.dirname(__file__))
file_path=os.path.join(base_dir,'prank')
file_list=os.listdir('prank')
print(file_list,os.path.dirname(os.path.dirname(__file__)))