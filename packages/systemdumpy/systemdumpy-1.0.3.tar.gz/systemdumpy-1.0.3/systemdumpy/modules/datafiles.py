## systemdump.py
## create and load a system dump for B&R PLC from the command line
##
## https://github.com/hilch/systemdump.py
##

import tarfile
import tempfile
import os
from .BrLoggerFile import BrLoggerFile

def unpackBrFiles(dump_file_name):
    with tempfile.TemporaryDirectory() as tmpDirName:
        tf = tarfile.open( dump_file_name, mode = 'r')
        tf.extractall(tmpDirName)
        dataDirName = tmpDirName + '/Data Files'
        dataFileNames = os.listdir(dataDirName)
        for fileName in dataFileNames:
            try:
                print("processing: " + fileName)                
                loggerFile = BrLoggerFile(dataDirName + '/' + fileName)
                entries = loggerFile.entries

            except TypeError:
                pass
            except Exception as e:
                pass
            pass

    pass

def extractLoggerFiles(dump_file_name):
    unpackBrFiles(dump_file_name)
    return {'result':'Ok'}