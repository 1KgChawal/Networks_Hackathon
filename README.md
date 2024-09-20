# Networks_Hackathon

## The Servers
 You have access to 2 servers, one which communicates using HTTPS and other using TCP. To simulate these servers, there are 2 folders, namely https_server and tcp_server. These 2 servers store all files they get inside a folder called mem


## Problem Statement
File Sharing is very common over the internet, be it uploading some important document over cloud storage or downloading your favourite games!!</br>
As long as the data is small in size, it is not a very big problem to send the file as a whole. But when file sizes are large, it is very difficult to send the file all at once.</br>
To counter this problem, data is usually sent into smaller blocks called chunks, independently of each other.


Complete the 2 functions in the split_lib.py file which implements split_store(file) and split_fetch(file). You will be evaluated by running test.sh which launches the servers, imports the 2 functions from split_lib.py into client.py and then stores and retrieves the test.txt file. test.txt has been written so that after chunking each file will start with <server_name><chunk_no> and end with <chunk_no><server_name(in reverse)></br>
You may use the code present in the tmux_scripts directory to launch and kill the servers.</br> 
Note: The use of AI in any form will result in disqualification, although referring to documentation is allowed.

### split_store(file)
This function takes a file in your local device, splits this file into chunks of 1024 bytes and sends these chunks to the servers.</br>
We send every alternate chunk to the same server, for example say a file is split into 4 chunks.
* Chunk-1 is sent to the server communicating via HTTPS
* Chunk-2 is sent to the server communicating via TCP
* Chunk-3 is sent to the server communicating via HTTPS
* Chunk-4 is sent to the server communicating via TCP

Once the chunks of data are uploaded, they will be stored in the server, at <server_name>/mem

**Note that the files are split between two servers, one communicating via HTTPS and other via TCP**

### split_fetch(file)
This function makes a request to each of the servers. The server sends chunks of data to the client.

You are expected to appropriately handle these chunks of data and patch them to get your originally uploaded file back.

### Part 2:
Some important metrics of a well designed system are speed, security, scalability, etc. Redesign this server system to improve these metrics. (you are allowed to make changes to all the files for this part of the PS). Submit this as a seperate git pull request from your original PR. 

**Note** : You are not allowed to modify the server code while working on the first Problem Statement (completing the split_store(file) and split_fetch(file) functions)<br>

* However if you want to attempt some of the open-ended problems, you can create a new copy of entire codebase and work on it.
* Submit the new copy of codebase containing solutions to open ended problems **along with** the original codebase having basic functionalities, adding an appropriate README file by directly making a PR to the same repo you cloned the starter code from.

## Interacting with Server
To interact with the server, follow these steps :
* Clone this repository or download the  : 
```
git clone https://github.com/Proxihox/Networks_Hackathon.git
```
* Go to the directory `client/split_share.py` and write the libraries for your functions
* In the file `solution.py` fill the `split_store()` & `split_fetch()` functions
* Ensure that your ports 5000 & 65432 are free, run following commands :
```
kill -9 $(lsof -t -i :5000)
kill -9 $(lsof -t -i :65432)
```
*Note* : If they are already free, you will get `kill: not enough arguments` or `kill: usage: kill [-s sigspec | -n signum | -sigspec] pid | jobspec ... or kill -l [sigspec]`
* You can check the working of servers by using following command :
```
chmod +x launch_servers.sh
./launch_servers.sh
```
* Run the following commands (after stopping all previous processes) to test your solution :
```
chmod +x run.sh
./test.sh
```
*Note* : To end the process, use `^C`

## How to run individual files for debugging and testing
* When you want to run individual files for debugging and testing purposes, run it from the main directory of the codebase
* For instance if you want to run `server.py` present in `Networks_Hackathon/https_server`. Make sure that your terminal's current working directory is 
```
../Networks_Hackathon
```
* And not
```
../Networks_Hackathon/https_server
```
* After ensuring you are in the main directory, you can run the file by executing
```
python3 /https_server/ server.py
```
