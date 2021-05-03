# HospitalBedsAvailability

This is a project cum helping hand to those who wants to fetch the quick results for the details of the hospital near them with vacant ICU or Non ICU beds. Here you just have to talk to your bot and your bot willgive you the compplete details about the hospital including the contact number, Hospital name, location, vacant beds, etc. 
Now let's start by setting up the project on your system to make it work and lets fetch the real-time resultys from it.

**Project Setup:
**

First of all create pull the git repository on your system with the given command,

**git clone https://github.com/ashus3868/HospitalBedsAvailability.git**

Now when you have pulled the image on your local system, now create a new virtual environment on your system and activate it, as follows,

**virtualenv -p python3.8 venv
source venv/bin/activate**

Now when you have a new virtual environment created and activated. Now move inside the project directory and install the dependencies inside the requirements file,

**cd HospitalBedsAvailability
pip install -r requirements.txt**

This will install all the dependencies for your project so that you can get started with the project and test it's functionality. It will take some time to setup and install all the packages on your system. 

Now when you have all the dependencies installed, run the given commands parallelly on two terminals to start the action server and the rasa server. 

**rasa run --model models --enable-api --cors "*" --debug**

and in second terminal,

**rasa run actions**

with these commands your rasa chatbot it activated and ready to talk and help you. Now open **index.html** file on the browser and see the chatbot in action.




