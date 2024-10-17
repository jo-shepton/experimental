from msilib.schema import File
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import skimage
from os import listdir
from os.path import isfile, join
import glob 
import json

print(np.__version__)
# reading in all filepaths for images 
FILEPATH = r"C:\Users\User\experimental\train"
image_names = [f for f in listdir(FILEPATH) if isfile(join(FILEPATH, f))]
filenames =[]
for file in image_names:
    filenames.append(join(FILEPATH, file))
# reading in the json file 
train_annotations = glob.glob(join(FILEPATH, '*.json'))
train_annotations_json= json.load(open(train_annotations[0]))

#choosing 10 random images to work with 
indices = np.random.randint(0, len(train_annotations_json['images']), size =10)
images = [filenames[i] for i in indices]
annotations =  [train_annotations_json['annotations'][i] for i in indices ]
thresh = 200
for a, img in zip(annotations, images):

    fig, ax = plt.subplots(1,3,figsize = (12,6))
    image = mpimg.imread(img)
    image_single_channel = image[:,:,0]
    test = image_single_channel>thresh
    ax[0].imshow(image_single_channel, cmap = 'grey')
    ax[1].imshow(test, cmap = 'grey')
    ax[2].hist(image_single_channel.flatten(), bins = 100)
    ax[2].axvline(thresh, color = 'orange')
    plt.show()
    # gives the points of the square around the tumor from the json file
    # segmentation = a['segmentation']
    # #reshaping it for cv2 polylines input 
    # segmentation = np.array(segmentation[0], dtype=np.int32).reshape(-1, 2)

    # # fig, ax = plt.subplots(figsize = (8,8))
    # # ax.imshow(image)
    # cv2.polylines(image, [segmentation], isClosed=True, color=(0,255,0), thickness=2)
    # cv2.imshow('image',  image)