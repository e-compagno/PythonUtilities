#Title: File container 
#Author: Enrico Compagno
#Version: 0.1.0
#todo:
#1. Add exception for non existing file 
#2. Add function to add files

import os

class FileContainer():
    # Container for file lists 
    def __init__(self,filelist):
        try:
            if not isinstance(filelist,list):
                raise TypeError('ERROR: input list cannot be empty')
            if len(filelist) == 0:
                raise IndexError('ERROR: input must be a list')
            
            self.filedic = {}
            for idx,fileread in enumerate(filelist):
                if not os.path.isfile(fileread):
                    raise FileNotFoundError('ERROR: file not found')
                self.filedic[idx] = self.FileClassify(fileread)

        except IndexError as msg_idxerr:
            print(msg_idxerr)
        except TypeError as msg_typeerr:
            print(msg_typeerr)
        except FileNotFoundError as msg_fnferr:
            print(msg_fnferr)

    def FileClassify(self,fileread):
        # Extract file information 
        file_name = os.path.basename(fileread)
        file_extension = os.path.splitext(fileread)[1].replace('.','').upper()
        filepath = os.path.dirname(fileread)
        return [file_name,filepath,file_extension]

    def __str__(self):
        print('\nFile list:')
        print('----------')
        file_list = ''
        for idx,val in enumerate(self.filedic):
            str_to_append = '{0}: {1}\n'.format(idx,self.filedic[val][0])
            file_list = file_list + str_to_append

        return file_list

    def info(self):
        print('\nFile Container info:')
        print('----------------------')
        print('Idx\tFilename\tPath\tExt')
        for idx,val in enumerate(self.filedic):
            value = self.filedic[val]
            print('{0}\t{1}\t{2}\t{3}'.format(idx,value[0],value[1],value[2]))

file1 = '/Users/enrico/Downloads/AirQualityUCI.zip'
list_of_files = [file1]    
cont = FileContainer(list_of_files)
print(cont)
cont.info()

