# p2p
P2P network written in python. 

###Funcs:
  - class Connection:
    - init(path, timeout) : getting path to file with peers and timeout(for socket connection) as float in seconds, returns nothing
    - getPeers() : returning array of peers
    - connect() : returning array of sockets
    - broadcast(message) : sending message to all, returns number of sended messages

#### TODO:
  - make TODO list
  - check at 2017.02.15
  - add progressbar from offchuck/textprogressbar to Connection.connect()
 

####Example
```python
  test = Connection("test.txt", 0.5)
  test.getPeers()
  print test.connect()
  test.broadcast("test")
```
