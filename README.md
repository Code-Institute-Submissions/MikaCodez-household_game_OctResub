# HouseHold Game
House Hold Game is a Python Command Line application that allows for users to be able to record their gaming titles to a library and have it
printed out to a spreadsheet and emailed over to them for their records.
![responiveimg](https://user-images.githubusercontent.com/65243328/154166477-c94db377-30bd-471c-ab8e-7ae8bd95a320.JPG)

## UX
### Users
The user should be able to interact with the command line and follow a series of questions that require input in order to advance to the next feature.
Once all the information has been inputted As as user I expect to receive this information recorded in a spreadsheet and sent over to the email that
I have provided.

The Instructions on the Command Line App are clear and concise and leaves little room for error.

### Application Structure
The Command line application will lead the user with a basic input of their gaming information:

1. Requests users information to be contacted in the form of an email.
2. Requests for Users Full name.
3. Requests for the current game title that they wish to input into the application.
4. Requests the information of what genre the game in question belongs to.
5. Requests which console platform the game belongs to (i.e. Playstation 5, Xbox One, Nintendo Switch, PC etc.)
6. Requests number of Hours played during game run time.
7. Requests what star rating would the user rank the game in their opinion (Star Rating ranging from 1* to 5*)
8. Updates details to worksheet and then once finished this will be recorded in a spreadsheet for the user.
9. The Terminal Displays the final details:
  •Users Email Address
  •Users Full Name
  •Game Title
  •Console
  •Hours Played
  •Star Rating
  
### WorkFlow
Below displays a FlowChart showing the logic of the Application Structure
![Flowchart](https://user-images.githubusercontent.com/65243328/153658851-b45ecb30-cef3-47ac-a846-11f63e7ddb05.JPG)


## Features
Entering Game data in to the console to be printed out to work sheet for users records.
![feature1](https://user-images.githubusercontent.com/65243328/154170380-cc3ddae4-e545-4294-a779-a2b634929ba4.JPG)

## Future Features
As the email function is currently not working properly we hope to implement A working system to deploy the records straight to the users inbox.

![feature2](https://user-images.githubusercontent.com/65243328/154171518-0e53d8d0-879c-49fd-b985-6481b06b1b46.JPG)


## Testing
### Bugs
Remaining Bugs: 
![bug1](https://user-images.githubusercontent.com/65243328/154169940-1852dbbe-f120-4762-81ff-b518e64547a2.JPG)


Validator Testing
PEP8:
Errors found in PEP*  online via pycodestyle as PEP8 Onine validator tool is offline
Some warnings found, and resolved by making changes requested. Details in Testing
Only error found is that line is too long. However for what this is specified for I kept it as it is, as I didnt want to break the code.
![image](https://user-images.githubusercontent.com/65243328/197505701-b9af854b-797c-41be-a5bb-fdb13e710f14.png)


## Deployment

The site was deployed to Heroku. The below steps were carried out to deploy.

Deployment steps
add the list of requirements by writing in the terminal "pip3 freeze > requirements.txt"

Git add and git commit the changes made

Log into Heroku or create a new account and log in

top right-hand corner click "New" and choose the option Create new app, if you are a new user, the "Create new app" button will appear in the middle of the screen

Write app name - it has to be unique, it cannot be the same as this app

Choose Region - Europe selected in this instance

Click "Create App"

The page of your project opens. 8. Choose "settings" from the menu on the top of the page 9. Go to section "Config Vars" and click button "Reveal Config Vars"

Go to git pod and copy the content of "creds.json" file

In the field for "KEY" enter "CREDS" - all capital letters

Paste the content of "creds.json" and paste to field "VALUE" Click button "Add"

Add another key "PORT" and value "8000"

Go to section "Build packs" and click "Add build pack"

in this new window - click Python and "Save changes"
click "Add build pack" again
in this new window - click Node.js and "Save changes"
take care to have those apps in this order: Python first, Node.js second, drag and drop if needed
Next go to "Deploy" in the menu bar on the top

Go to section "deployment method", choose "GitHub"

New section will appear "Connect to GitHub" - Search for the repository to connect to

type the name of your repository and click "search"

once Heroku finds your repository - click "connect"

Scroll down to the section "Automatic Deploys"

Click "Enable automatic deploys" or choose "Deploy branch" and manually deploy

Click "Deploy branch"

Once the program runs: you should see the message "the app was sussesfully deployed" 23. Click the button "View"

Forking the GitHub repository
By forking out of this repository you will be able to view and edit the code without affecting the original repository.

Locate the GitHub repository. Link can be found here: [HouseHold Game](https://github.com/MikaCodez/household_game)
Click the button in the top right-hand corner "Fork"
This will take you to your own repository to a fork that is called the same as the original branch.

Making a local clone
Locate the GitHub repository. Link can be found here.
Next to the green Gitpod button you will see a button "code" with an arrow pointing down
You are given the option to open with GitHub desktop or download zip
You can also copy https full link, go to git bash and write git clone and paste the full link

## Credits
Graphic for opening code sampled from [ASCII Art Archive](https://www.asciiart.eu/video-games/sonic-the-hedgehog)

SCOPE code credits to Code Institute, Love Sandwiches Walkthrough Project.
I have ammended the code to my command lines specification

Credits also due to Code Institute staff for helping in slack
Mentor Anthony
Also credits to Maya Claveau for assistance during project!
  
