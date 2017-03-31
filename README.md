# Image classification as a service

*messed_path_to_classify.py* has been created by Loic MESSAL (Student at the French National School of Geomatics).
24 March 2016

Install python3 :
```sh 
$ sudo apt-get install python3 
```
> Currently, "sudo apt-get install python3" loads alias python3 as python3.4.
*messed_path_to_classify.py* uses python3.5 (for folder manager) and python3.4 (for artificial intelligence algorithm)


Install Tensorflow
	You need to install first pip3 for manage module	
```sh
	$ sudo apt-get install python3-pip python3-dev
```
Then, install Tensorflow :
```sh
	sudo pip3 install --upgrade <link>
```
> Choose your link on [tensorflow documentation](https://www.tensorflow.org/install/install_linux#the_url_of_the_tensorflow_python_package)
Because of some difficulties to install tensorflow with cuda and cudnn libraries, I used : 
> sudo pip3 install --upgrade https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-1.0.1-cp35-cp35m-linux_x86_64.whl



## Demonstration : 
I would love to sort my pictures from my holidays in Cambridge. I have a folder where I put all my cambridge holidays pictures... 

![messed_path](assets/image/cambridge_mess.png)

> In fact, these pictures are a groundtruth for computer vision algorithms from [Washington University](http://imagedatabase.cs.washington.edu/groundtruth/)

With this command, I am now able to sort my pictures into topical path
```
python3.5 messed_path_to_classify.py --out_path ./example/sorted ./example/cambridge
```

Here is the result of the classification : 

![messed_path](assets/image/sorted_path.png)

Oh dear god ! My computer analysed my picture and recognized by its own all the churches of my cambridge holidays pictures and put it in the same folder : 

![messed_path](assets/image/churches.png)


# Create an alias
Place ImageDossier in the directory of your choice. Keep it in mind.
for exemple : /home/Intelligence/

Then, edit your alias file to use the messed_path_to_classify.py easily
```sh
$ nano ~/.bashrc
```
add this ending line : 
> alias classify_path="python3.5 /home/Intelligence/ImageDossier/messed_path_to_classify.py"

close the alias file by press ctrl+X and type 'O' and press enter


Now have fun and classify your folder ! 

## Usage : 
- Mainly used : 
```
classify_path --out_path ./sorted ./path_to_classify/
```

- Help :
```
classify_path -h
```

 
