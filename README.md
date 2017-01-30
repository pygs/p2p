# p2p
P2P network written in python. 

###Funcs:
  - class Connection:
    - init(path, timeout) : getting path to file with peers and timeout(for socket connection) as float in seconds, returns nothing
    - getPeers() : returning array of peers
    - connect() : returning array of sockets

#### TODO:
  - make TODO list
  - check at 2017.02.15
 

####Example
```python
  test = Connection("test.txt")
  print test.getPeers() #that will print array of peers
```
