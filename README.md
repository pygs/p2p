# p2p
P2P network written in python. 90% of this project has been done in the classroom at school, because lessons were too boring

***

###Funcs:
####class Connection:
   
    Func | Returns
    --- | ---
    **init**(path, ip(as string), port(as int), timeout=0.5(optional)) | nothing
    **getPeers**() | array of peers(string)
    **connect**() | array of sockets
    **broadcast(message)** | number of sended messages
    **server()** | nothing
    **sendinfo()** | nothing

###Libs:
####- pycrypto

#### TODO:
  - make TODO list
  - check at 2017.02.15
  - add progressbar from offchuck/textprogressbar to Connection.connect()
  - listening thread
  - add something like "datachain" with addresses of connected users
 

####Example
```python
  test = Connection("test.txt", 0.5)
  print test.getPeers() #will print array of peers
  test.connect()
  test.broadcast("test")
  test.server()
```
