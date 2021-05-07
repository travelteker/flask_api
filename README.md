# Plytix - Api RestFul - Words

## Requirements
For this exercise I consider the next requirements:
- Endpoints:
    - GET /words
    > For this case will be show all words registered in database mongo
    - POST /words {"word": "calle", "position": 3}
    > For this case a new word will be inserted if not just exists in database
    > If positions are busy by another word then it will be inserted in the position declared
    > and the previous word his position will be incremented by +1
    - PATCH /words/calle {"position": 5}
    > This method will be used only update action, so if the word not exists previously then the
    > action updated will be forbidden.
    - GET /words/asco/anagrams
    > For this case, it will receive all posibilities that matched with word requested
    - DELETE /words/calle
    > If the word exists in database, it will be erased
  
## Conditions
- All libraries I have used are declared in the requirements.txt file
- I used factory method to Flask framework to try focused development using POO
- For the scaffolding I used structural division
- For internal structure data I used dataclasses like interfaces
- All request need headers <X-Api-Key> and <X-Api-Version>
- An auxiliar endpoint was added to reset database for my operations
- I added log files to register some information

## Observations
- I implemented a small transaction version for multiple operations
- I did unit tests for some files excluding those related to the framework directly because I 
  consider that they can be tested with the integration tests  
    
- I did an example for integration tests using library Robotframework
- Html files were added to view coverage and integration test report


