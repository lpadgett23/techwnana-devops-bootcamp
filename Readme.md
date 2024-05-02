O5 - Cloud - IaaS 

Scratch notes:

Good practices:
default is usually, public accessible on all ports
--> close access to ports by default, then selectively open the ones you want by setting up a firewall and inbound rules


ssh default port = port 22 with TCP
set it to your IP address or small range only

outbound rules -- what can your server connect to externally?
inbound rules, who can connect to your server (droplet)


Summary:  When you set up a server:
1. Configure firewall rules
2. apply them to your server
3. connect to the server from terminal with ssh root@<the ip address>
4. you're operating on teh server as the root user now
5. install what you need
6. apt update , apt get..

common request/process to do: 
1/ build a jar file locally
2/ copy it to the remote server
3/ run the app on that remote server















.
