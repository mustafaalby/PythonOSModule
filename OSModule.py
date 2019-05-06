import os
import sys
def main():
    folder=sys.argv[1]
    print(os.getcwd())#return get current working directory
    
    os.chdir(folder)#change working directory
    print(os.listdir())#list files in working directory
    
    os.makedirs("new follder/newFold")#creating folder in directory
    print(os.listdir())

    os.removedirs("new follder/newFold")#delete folders
    print(os.listdir())

    #os.rename("name of the file","new name of the file")
    #print(os.stat("file name")) information about file

    


main()