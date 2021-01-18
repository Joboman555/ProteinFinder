# ProteinFinder

This is a small application that allows you to find matching proteins from a tiny database of nucleotide codes.

## Using the Application

Please visit https://protein-finder-jspear.herokuapp.com/

Type a dna sequence into the text input and search away. For long-running queries the results will update every 1.5 seconds.

## Building the Application.

These are the steps to build the application on my operating system. The exact instructions may be different for your environment, 
but the high-level steps should be the same.


#### 1. Clone the Repository

```git clone git@github.com:Joboman555/ProteinFinder.git```

#### 2. Install redis. This is used by Celery, which manages the async processes.

```brew install redis```

#### 3. Install dependencies

```pip install -r requirements.txt```

#### 4. Run the server. I created a script that runs all 3 server components together and kills them as a package.

```bash start.sh```


## Things I learned

This was a really fun project. I learned and re-learned a lot of cool things. In no particular order, they were:
1. Refreshing django concepts
2. Polling asyncronously from a javascript frontend
3. Using celery for django async tasks
4. Using redis
5. Passing and parsing JSON responses from get requests.
6. How to configure heroku with django, celery, and postgres

## Areas for improvement

If I had more time to devote to this application, here are the things that I would make better.

#### 1. More beautiful user interface. 

Current UI is very bare/minimal; I didn't even use a css file. :o


#### 2. Add smart page reloading.

Currently the page reloads every 1.5 seconds, whether there is data that needs to be fetched or not. A better alternative is to store whether the backend is processing data, and only fetch more data while there are queries that are still running. If I did this then we could set the re-fetch time much lower than 1.5 milliseconds.


#### 3. Add a caching layer

A way to improve the result speed significantly would be to add caching using something like memcache. This would make queries that have been run before, run much faster.
