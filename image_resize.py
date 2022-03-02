from PIL import Image   # Image manipulation stuff. The PIL module is included in Anaconda installations.
import os               # Module for dealing with file navigation
import re               # Regex for more convenient filename manipulation/recognition

os.chdir("/Users/matthewgimpelevich/Desktop/Photos APF9 open  copy/")    # Set working directory to wherever the image files are located

for filename in os.listdir():                   # Cycle through all files in the directory

    # not re.search() omits filenames with the word 'resize' or 'DS_Store' in them
    # os.path.isfile() checks if 'filename' is a file (as opposed to a folder)
    if not re.search('.*(resize|DS_Store).*', filename) and os.path.isfile(filename):
        
        img = Image.open(filename)  # Open image by name+extension

        imgWidth, imgHeight = img.size[0], img.size[1]  # Record image dimensions

        adj = 0.1  # Size adjustment

        imgWidth = round(imgWidth * adj)    # round() ensures that the output number is an integer
        imgHeight = round(imgHeight * adj)    

        resized_img = img.resize((imgWidth, imgHeight)) # Resize the file according to specifications
        resized_img.save('resize_' + filename)          # Save the result

        print(filename) # Print file name for good measure