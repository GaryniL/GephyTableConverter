# GephyTableConverter

### About
This project includes two parts: 

1. Text to Speech Conversion
2. Speech to Text Conversion

However, to help transcribing voice recording to text easier, the main propose of this project is generating a well-organized file that includes each sentence of yoru voice recording files.

### Setup

Put the files in same folder
![Folder.png](images/Folder.png)

### Requirements
* Run it with Python 2

### Input
CSV file with this kind of format (You can make or transform it with Excel)

![input.png](images/input.png)

### Output

Output will be two csv files and both can import to Gephy

* Edge data:
![test_edge.png](images/test_edge.png)


* Node data:
![test_node.png](images/test_node.png)

### Parameter

![transform1_py.png](images/transform1_py.png)


### How to import to Gephy

* Open your file with Audicity and choose "Analyze → Silence Finder..."

![audacity1.jpg](images/audacity1.jpg)

* Change the settings, then press "OK"

![audacity2.jpg](images/audacity2.jpg) 

* Click "File → Export Multiple..."

![audacity3.jpg](images/audacity3.jpg)

* Check export format and name files as the following settings, then export all files to same directory

![audacity4.jpg](images/audacity4.jpg)

### License

MIT License