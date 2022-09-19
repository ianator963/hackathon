# hackathon
UB Hackathon
City Honors group #2's UB Hackathon Project Decription and Prerequesits.
In order to begin running the code, the operator must have the following things downloaded on their computer: python, panda
For our project at first we planned on data scraping off of a website like the CDC website for covid-19 stats and convert their data into a live tracker and graph. This idea unfortunately did not work so we ditched the data scraper, and made a code through pandas that takes a csv file of all the states' data on covid-19 and download it locally as "all_states_history.csv". The csv shows the most recent data for each of the 50 states. This data is uploaded to a web app through flask, and a graph is created using that data and put on the web app through Matplotlib and panda. The data and graph should all be conveniently located on the web app, easily viewable by the user.
Some problems that we ran into were: Chosing a language, The fact that the data scraper did not work because BeautifulSoup cannot read JavaScript, and all of the websites we could find were dynamiccally coded with JavaScript and HTML
Update: We could not finish the project because of the time limit. Attatched to the github is all of the components but we could not connect them, so this is pretty much raw code.

THE API THAT THIS PROGRAM SCRAPES FROM HAS BEEN DEPRECATED AND THE CODE DOES NOT WORK TO DATE
