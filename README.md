# OMDB_API
Purpose:  To get the rating of movies.

Environment: Operating System should be LINUX. Docker environment should be setup at the user end.

Procedure to run the script:

1. Pull the image:
   docker pull  njlsri/omdb_python_script:omdb 

2. To obtain IMAGE ID
   docker images

3. Run image as container by putting IMAGE ID
   docker run -ti -d IMAGE ID

4. To obtain CONTAINER ID
   docker ps

5. Enter in the container by putting CONTAINER ID
   docker exec -it CONTAINER ID /bin/bash

6. Run the OMDb.py script with MovieName
   python3 OMDb.py MovieName
   
7. Output:
   Movie name: Bharat
   Rotten Tomatoes Rating is 29%.

Error handled: Movie name not found, API key wrong, Invalid movie name, Rotten tomatoes rating not available.
