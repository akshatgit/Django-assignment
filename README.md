Sample user:  
  username: sample  
  password: India123  

Sample commands  
###Logout and new login  
logout  

###Creates a new board  
board -c new -n <name>  

###Display all board names and their IDs  
board -c show -a  

###Display lists and cards of a specific board  
board -c show -b <n>  

###Create new task list, attached to a specific board  
list -c new -n <name> -b <BoardID>  

###Display all list names and their IDs  
list -c show -a  

###Create new car, attached to a specific list  
card -c new -n <name> -l <ListID>  

###Display all cards and their IDs  
card -c show -a  

###Help commands  
help board  
help list  
help card  
  
