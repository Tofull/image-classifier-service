# Copyright 2016 Loic Messal. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================


""" Classify a messed folder with Inception.

Run image classification with Inception trained on ImageNet 2012 Challenge data
set.

This program use an image classification program which creates a graph from a saved GraphDef protocol buffer,
and runs inference on an input JPEG image. It outputs human readable
strings of the top 5 predictions along with their probabilities. 

This program decode these top 5 predictions and move the processed image into the right directory.

Change the --out_path to specifie the directory wherin are stored the classified images from the messed path

The required argument is the path to classify. 


Please see the tutorial and website for a detailed description of how
to use this script to perform image recognition.

https://tensorflow.org/tutorials/image_recognition/
"""

import subprocess
import glob
import os
import shutil
import argparse
import sys

def progress(count, total, suffix=''):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)

    
    sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', suffix))
    sys.stdout.flush()  # As suggested by Rom Ruben


# Argument input
parser = argparse.ArgumentParser(description='Process to classify a path.')
parser.add_argument('messed_path', metavar='messed_path', type=str,
                   help='the absolute path of the directory of the path to classify')
parser.add_argument('--out_path', metavar='out_path', type=str,
                   help='the absolute path of the directory wherin are stored the classified images from the messed path. Will be created if not exists. WARNING : if already exists, will be remplaced.')
parser.add_argument('--replace_path', metavar = 'replace_path', type=bool, default=False, 
                    help='if True, out_path will be replaced. Default : False')
parser.add_argument('--threshold', metavar = 'threshold', type=float, default=0.20, 
                    help='threshold which reflects the percentage of certitude of the artificial intelligence algorithm to classify')
args = parser.parse_args()


# allowed extension
filetype = ["JPG","jpg"]

# parse input argument
out_path = os.path.abspath((args.out_path if args.out_path else 'sorted'))
path_to_classify = os.path.abspath((args.messed_path if args.messed_path else './path_to_classify'))

if args.replace_path:
    if os.path.exists(out_path):
        shutil.rmtree(out_path, ignore_errors=True)
os.makedirs(out_path, exist_ok=True)


# list of images to process
filenamelist = [];
for extension in filetype:
	filenamelist += glob.glob(path_to_classify+'/**/*.'+extension, recursive=True) 

# progress parameters initialized
imax = len(filenamelist)
i=0

# process
for filename in filenamelist:
    # update progress
    progress(i,imax)
    i+=1

    # processed image
    image = filename.split(path_to_classify+'/')[-1]


    # use artificial intelligence algorithm
    print(os.path.dirname(__file__)) 
    cmd = 'python3.5 '+os.path.dirname(os.path.abspath(__file__))+'/classify_image.py --model_dir '+os.path.dirname(os.path.abspath(__file__))+'/imagenet'+' --image_file '+'%r' %path_to_classify +'/' +'%r' % image
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    out, err = p.communicate()

    # parse result of the artificial intelligence algorithm
    result = out.decode('utf-8').split('\n')
    shapeDetected = result[0]
    shapeDetected = shapeDetected.split('score = ')
    title = shapeDetected[0]
    title = title.split(',')[0]
    title = title.split('(')[0]
    score = shapeDetected[-1]
    score = score.split(')')[0]

    # Threshold the score
    if float(score)<args.threshold:
        title = "not_matched"

    # prepare the copy
    os.makedirs(out_path+'/'+title, exist_ok=True)

    # copy the image file to its right directory
    if not os.path.exists(out_path+'/'+title+'/'+image.split('/')[-1]):  # folder exists, file does not
        shutil.copy(filename, out_path+'/'+title+'/'+image.split('/')[-1])
    else:  # folder exists, file exists as well
        ii = 1
        baseName = image.split('/')[-1].split('.')[0]
        extension  = image.split('/')[-1].split('.')[-1]
        while True:
            new_name = os.path.join(out_path+'/'+title+'/'+baseName + "_" + str(ii) + extension)
            if not os.path.exists(new_name):
                shutil.copy(filename, new_name)
                break 
            ii += 1

# update the progress bar
progress(i,imax)
print()
