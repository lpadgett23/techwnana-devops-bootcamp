#!/bin/bash



# check processes running for current user (USER env var)
# and print to console
# grep printenv | echo $USER | ps aux -U {$USER} -u {$USER}
ps aux | grep $USER 

# ask user for sort preference (mem or CPU)
echo -p "What is your sort preference? type mem or cpu"
  read {$1}

ps aux  --sort=-%{$1}

# how many does the user want to see? 
echo -p "How many do you want to see?"
  read {$2}

ps aux --sort=-%{$1} | head -n {$2}


