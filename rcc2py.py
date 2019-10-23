'''
# Objective:
This solution should convert "*.rcc" file to "*.py" file.

# Requirements:
1. Will take input as direct path to the rcc file.
2. The .py file must be created on file path.
3. Name for the filename should be exactly equal to rcc file name.
4. **** Include pyside2-rcc.exe as intrinsic file *****: PyInstaller stuff.
OR
5. Get pyside-rcc.exe path from config file.

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


# Generate fileName for .py file from provided path of .rcc file.
def qrc2pyName():
	'''
	This function should generate filename for .py file.
	:param path: This is path of .rcc file(abs path)
	:return: 'filenameSTR.py', Normalized abs path for rcc file.
	:type: __str__
	'''
	qrcFilePath = clip.paste()
	if str(qrcFilePath).endswith('.qrc'):
		qrcFilePath = os.path.normpath(qrcFilePath)
		pattern = r'((\w+)\.qrc)'
		fileNameExt = re.search(pattern=pattern, string=qrcFilePath)
		fileName = fileNameExt.group(2)
		pyFileName = str(fileName) + '.py'
		return qrcFilePath, pyFileName
	else:
		print('The input file is missing or file format is unexpected.')
		return None


def qrc2py(qrcFilePATH, pyFileName):
	'''

	:param rccFilePATH: This abs path to the rcc file.
	:param pyFileName: This is output of
	:return: None
	'''
	
	# Paste the pyside2-rcc.exe in the working directory of tool.
	# Generate shell command: <uicEXEPath> <UI file path> -o <pyFileName> -x
	# Copy the file to project destination, essentially where the qrc file is located.
	
	shellCMD = 'pyside2-rcc.exe' + ' ' + qrcFilePATH + ' -o ' + pyFileName
	#print(shellCMD)
	sleep(1)
	qrcFileDir = os.path.dirname(qrcFilePATH)
	
	try:
		print(f'Executing:   {shellCMD}')
		os.popen(str(shellCMD))
	except:
		print('Something is Wrong!')
		os.popen('pause')
	
	
	# MOVE IT
	newPath = os.path.join(os.getcwd(), pyFileName)
	sleep(1)
	# os.startfile(os.getcwd())
	shutil.copy(newPath, qrcFileDir)
	return qrcFileDir


if __name__ == '__main__':
	path, filename = qrc2pyName()
	resultDir = qrc2py(qrcFilePATH=path, pyFileName=filename)
	sleep(1)
	os.startfile(resultDir)
	print('Finished')
