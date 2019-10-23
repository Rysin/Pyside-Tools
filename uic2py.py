'''
# Objective:
This solution should convert "*.ui" file to "*.py" file.

# Requirements:
1. Will take input as direct path to the ui file.
2. The .py file must be created on file path.
3. Name for the filename should be exactly equal to ui file name.
4. **** Include pyside2-uic.exe as intrinsic file *****: PyInstaller stuff.
OR
5. Get pyside-uic.exe path from config file.

# WorkFlow:
1. Get the path and normalize it - no need of validation.
2. Generate file name for complied .py file.
3. Generate shell command for final execution.
4. Run the command.

# Tests:


3.
'''
import os
import re
import shutil
from time import sleep

import pyperclip as clip


# Generate fileName for .py file from provided path of .ui file.
def ui2pyName():
	'''
	This function should generate filename for .py file.
	:return: 'filenameSTR.py', Normalized abs path for ui file.
	:type: __str__
	'''
	uiFilePath = clip.paste()
	if str(uiFilePath).endswith('.ui'):
		uiFilePath = os.path.normpath(uiFilePath)
		pattern = r'((\w+)\.ui)'
		fileNameExt = re.search(pattern=pattern, string=uiFilePath)
		fileName = fileNameExt.group(2)
		pyFileName = str(fileName) + '.py'
		return uiFilePath, pyFileName
	else:
		print('The input file is missing or file format is unexpected.')
		return None
	
	


def uic2py(uiFilePATH, pyFileName):
	'''
	
	:param uiFilePATH: This abs path to the ui file.
	:param pyFileName: This is output of
	:return: None
	'''
	
	# Paste the pyside2-uic.exe in the working directory of tool.
	# Generate shell command: <uicEXEPath> <UI file path> -o <pyFileName> -x
	# Copy the file to project destination, essentially where the ui file is located.
	
	shellCMD = 'pyside2-uic.exe' + ' ' + uiFilePATH + ' -o ' + pyFileName + ' -x'
	#print(shellCMD)
	sleep(1)
	uiFileDir = os.path.dirname(uiFilePATH)
	
	try:
		print(f'Executing:  {shellCMD}')
		os.popen(str(shellCMD))
	except:
		print('Something is Wrong!')
		os.popen('pause')
	
	# MOVE IT
	newPath = os.path.join(os.getcwd(),pyFileName)
	sleep(1)
	#os.startfile(os.getcwd())
	shutil.copy(newPath,uiFileDir)
	return uiFileDir
	

if __name__ == '__main__':
	path,filename = ui2pyName()
	resultDir = uic2py(uiFilePATH=path, pyFileName=filename)
	sleep(1)
	os.startfile(resultDir)
	print('Finished')
