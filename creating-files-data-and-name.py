# Creating files VisDrone.data and classes.names
# for training in Darknet framework
#
# Algorithm:
# Setting up full path --> Reading file classes.txt -->
# --> Creating file classes.names -->
# --> Creating file ts_data.data
#
# Result:
# Files classes.names and ts_data.data needed to train
# in Darknet framework


"""
Start of:
Setting up full path to directory with VisDrone images
"""

full_path_to_images = 'C:/Users/00427X744/Desktop/Git/Train/images'

"""
End of:
Setting up full path to directory with VisDrone images
"""


"""
Start of:
Creating file classes.names
"""

# Defining counter for classes
c = 0


with open(full_path_to_images + '/' + 'classes.names', 'w') as names, \
     open(full_path_to_images + '/' + 'classes.txt', 'r') as txt:

    # Going through all lines in txt file and writing them into names file
    for line in txt:
        names.write(line)  # Copying all info from file txt to names

        # Increasing counter
        c += 1

"""
End of:
Creating file classes.names
"""


"""
Start of:
Creating file VisDrone.data
"""

with open(full_path_to_images + '/' + 'VisDrone.data', 'w') as data:
    # Writing needed 5 lines
    # Number of classes
    # By using '\n' we move to the next line
    data.write('classes = ' + str(c) + '\n')

    # Location of the train.txt file
    data.write('train = ' + full_path_to_images + '/' + 'train.txt' + '\n')

    # Location of the test.txt file
    data.write('valid = ' + full_path_to_images + '/' + 'test.txt' + '\n')

    # Location of the classes.names file
    data.write('names = ' + full_path_to_images + '/' + 'classes.names' + '\n')

    # Location where to save weights
    data.write('backup = backup')

"""
End of:
Creating file VisDrone.data
"""
