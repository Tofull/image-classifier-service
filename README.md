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
	sudo pip3 install --upgrade https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-0.7.1-cp34-none-linux_x86_64.whl
```

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

Exemple of use : 
```
classify_path --out_path ./sorted ./path_to_classify/
```

Help :
```
classify_path -h
```

 
