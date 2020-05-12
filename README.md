# Trversal-vue
A reworking of my capstone as a full Vue.js CLI application.  
View the old app repo <a href="https://github.com/tabathadelane/trversal">here</a>.

## Project Overview
The MVP version of Trversal is an itenerary building app that lets the trip planner input places of interest and save them to each day of their trip in a list view that calculates and provides the travel times between the locations, so the user can get a preview of what will realistically fit into their day.  

This version will aim to maintain all of that functionality in a new format. The front end will be Vue.js using the full CLI instead of just the CDN on the map page.  

The goal is to create a smooth SPA with reduced load times, or at least some UI elements that provide loading animations to inform the user that their change is taking place. 

## Features

**_"When I prepare a trip, I want a more accurate timeline of places and travel times so that I can make the most realistic plan."_**

**Tasks:**  
Create user models that can create and save an itenerary/trip model.  
Allow the user to list they want to go in a given day.  
Implement a map API that calculates route times between each location and its previous location.  
Display route times and timestamps for user to see.  
Allow the user to provide an estimated time to spend at each location.  
Add this time to the timeline at each location of the itenerary.  
Provide a layout of each day with timestamps so the user can track their day.  

**_"If my plans change, I want to be able to edit times and order of locations."_**  

**Tasks:**  
Allow the user to rearrange locations to optimize their routes.  
Build the app so that the route times automatically recalculate when this happens.  

**_"If I am walking/driving, I want to get accurate travel times based on my method of transportation."_**

**Tasks:**  
Implement the map API's travel method feature.  
Allow the user to choose/edit which method.  

**_"I like to make use of my entire day, so I want the app to help me check if the place I want to go to dinner will still be open when I plan to arrive."_**

**Tasks:**  
STRETCH GOAL  
Add a feature that checks the API result for each place with time of arrival/time staying against the OPEN value  
Display a warning if FALSE is returned  

**_"If the weather is nice, I want to go to a park or walk to lunch instead of drive."_**

**Tasks:**  
STRETCH GOAL  
Implement a weather app   
If the trip is within the forecast range, display weather info to the user  

## Data Model

### Models:  
**TRIP**  
NAME - name of trip, string  
DATE - date of trip, date object  
START_TIME - start time for the day, time object  
START_LOC - start address, lat/lang  
CREATOR - relationship to user model  

**LOCATIONS**  
G_NAME -  name of location for display only provided by GMAPS API search, string  
LAT_LONG - the precide longitude and latitude of the location use for directions calculations, avoids ASCII errors, Integer  
DURATION - estimated time staying at each location , time object  
TRIP - relationship to trip model  

**USERS**  
basic user information needed for Auth  
Basic profile functions, like small bio, city, avatar?

**_WEATHER_**  
*major stretch goal, will learn more later after choosing an API*  
weather icon  
temp high  
temp lo  
conditions  
location  
link to day model  

## Schedule

As most of the map calculating and API configuring has already been done for me, I only forsee a few big unknowns. I would like to get this done in 2 weeks. I would also like to give myself a weekend, so this is technically going to be 10 days of work. Here is a rough plan for myself:  

**Day 1-3** May 11-13  
Get Started!  
One of my biggest challenges will be getting user authentication to work. I have tried using JWT in Django before and not had much luck chasing errors. I would like to try again from a clean project. If I cannot get it figured out in a resonable amount of time (3days?) I would like to look into trying to use Firebase or something related for User Auth. I will need to also put in the time to research my options and learn how to use them.  
However, the plan is:  
- Build a basic Django app with a simple model. 
- Put together a DjangoREST API the sends over the model data.
- Build a basic Vue app with a template that displays the data. This will help me flesh out any CORS or syntax errors and make sure that two parts are communicating effectively. (Day 1)
- Take a break! This is a big step. 
- Add a User Model and try JWT again. (Day 2)
- If I cannot get this to work, I need to spend the rest of the day looking for an alternative and getting it working. (Day 3)

**Day 4** May 14  
Once you have the basic peices working, expand the application and get it ready for Google Maps. 
- Create router-links for your basic pages. Probably a user profile, a map view page, and a create and edit trip page?
- Expand the models (use the ones from the old application)
- Update DjangoREST with this
- Probably fill in some dummy data to make sure that the templates are still filling out currectly. 
- Cute! Take a break.

**Day 5** May 15  
Now that we know that everything is talking so far, complete the CRUD functionality. Prove that it works!
- Add CRUD views to DjangoREST
- Build a basic form and get it sending information to the backend successfully. 
  
**Day 6** May 18  
After the dummy app is functioning, the next big hurdle is finding out how well Google Maps API plays with Vue. The big task today and getting a map to show up!
- Get the map to initialize on the page!

**Day 7** May 19  
The next big issue with Google Maps is getting the autocomplete bar and the map to show up on the same page. The code is very finicky. for Day 6 and 7, this will either just work or it will be a huge task. I am giving myself plenty of time to try to work through this. If it goes smooth, then I will just be ahead!
- Connect the autosearch bar to a form input element and get it to work. 
- Get it to also work with the map. 

**Day 8** May 20  
If everyone is being friends at thing point, the only big thing left to do is add the gmaps.py functions that calculate and update the timestamps.
- Do what I just said. 
- Prove that it works. 

**Day 9-10** May 21-22  
Hopefully everything went according to plan. Now the only thing left to do is to fine tune a layout and start styling!! Yay!

**Extra** May 25-29

- I should look into Gridsome or Nuxt.js. Decide which one will be best for my app.

- Find out if this will upload on my PythonAnywhere acount. If not, I should also implement PostgreSQL and deploy this to Heroku, or similar. 
