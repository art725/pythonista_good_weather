# pythonista_good_weather
Get weather from Pythonista trough iOS URL Scheme and Weather Underground API

So my girlfriend said one day "So you like programming? Can't you make something that reminds us to go to the beach and have a nice after work picnic if the weather allows it?"

Challange accepted!

The system works like this:
1. iOS App: "Launch Center Pro" is scheduled to through an iOS URL Scheme launch a Workflow.
2. iOS App: "Workflow" analyzes if we have the children or not trough calendar events and if not runs Pythonista trough another iOS URL Scheme where we submit geolocation and Weather Underground API key to get if the weather is good for bathing.
3. iOS App: "Pythonista" with the script in this repository receives the request and sends back the answer through the clipboard and another URL Scheme transfer to Workflow.
4. iOS App: "Workflow" looks at the result and if the weather is good tomorrow it adds a calendar event in my and my girlfriends joint iOS calendar that reminds us to go to the beach after work. 
