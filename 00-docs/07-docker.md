# Module 07 - Docker
## Favorite takeaways
- Categorizing the commands simplified things better in my memory: create/run/remove things versus a group of inspect/troubleshoot commands
- Went through many many main commands and used them, much clearer this time around

## Config / Major issues
#### Mongo-express container refuses to find mongo container when it's renamed with --name mongodb on docker run
- Startup script gets stuck at looking up a tcp to 'mongo' (rather than to mongodb, I believe)
- But then a loop of other issues repeated each other before that:  Ssl certificate/network problem, then error to connect, then misisng npm modules, one after another, every time I tried
- Got it to run with container name as "mongo", but this means I would need to adjust provided code in multiple places to get several iterations of the class demo to actually ever run?
- Research came up with:
  1. Conflict with docker hub images for mongo:latest and mongo-express:latest, not totally unheard of
  2. Did I leave enough time for Mongodb container to start up?
  3. Try with mongo:7.0 image? --> less confusing to modify that in the code than mongodb/mongo?
  4. Try on a different wifi network; couldn't find a proxy, 'child lock', etc in the Internet gateway admin panel up but you've had problems before on that network.
  5. (Don't think it's a WSL or file system problem)
  6. Go back to basics re: review node app fundamentals/the set up for that --> you're doing it on WSL instead of windows this time.
