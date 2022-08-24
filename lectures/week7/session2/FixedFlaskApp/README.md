# flaskSessionDebugErrors

# 1. CLONE this project into your machine
# 2. ACTIVATE your virtual environment, if it isn't already
# 3. RUN the project
# 4. READ the error messages
# 5. FIX as many of the bugs as you can. There are 7 bugs.
# 6. Have it checked!


## BEGINNER ERRORS ##
1. Logging in ---- index.html > form > no post method
2. Logging in ---- KeyError > 'firstName' = solution change values for first name and last name entries to match server
3. No actual error just missing data on leaderboaord ---- The session user's name not showing = solution > add session to route, changed html to read our var we set for session
4. Adding friends ---- KeyError > 'first' > added post method to form and to route

## INTERMEDIATE ERRORS ##
5. redirect() got an unexpected keyword argument 'first' > the route's redirect is passing in info but should just be the path/route
6. No actual error but no data displaying > solution put friends in session
7. KeyError > since our friends haven't been added into session yet html doesn't understand 'first' > solution is if statement on route if not in session load page with first = ''

## Advanced Errors ##
8. All show routes show friend #3's name not who should be there > adding int to route path
9. Clicking the show route before adding Friends give KeyError for which ever friend wasn't added > if friend in session show link otherwise show nothing

