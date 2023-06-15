import os


# This directory must be in the same directory as the script
# If not then change the os.getcwd() to the directory
directoryName = "circles"

def main():
    # Get all files in the current directory
    circles = os.listdir(os.getcwd()+"/"+directoryName)

    # Open the output file
    with open('output.txt', 'w') as output:
        # Loop through all files
        for file in circles:
            tempFile = os.getcwd() + "/" +directoryName+ "/" + file
            
            # Open the file
            with open(tempFile, 'r') as f:
               lines= ["{} {}".format(file,x) for x in f.readlines()]
               output.writelines(lines)
            
if __name__ == '__main__':
    main()