# Project

## Abstract
This piece of code creates new cards into the specified board and list [Trello](https://trello.com/) every minute.

# Trello
1. First [create an account](https://trello.com/signup).<br />
2. After creating an account, create a board and a list. <br />
3. Then, go to [Trello REST API](https://developer.atlassian.com/cloud/trello/rest/api-group-actions/) <br />
4. Then go here : [Trello REST API Introduction](https://developer.atlassian.com/cloud/trello/guides/rest-api/api-introduction/) <br />
5. This page explains how to create an app key and token. You can simply click on this link : [Trello get app key](https://trello.com/app-key)<br />
Follow the guide and acquire a key and a token.

## trello.py
Now go paste your key and token to the variables respectively. <br />
At the lines ```24``` and ```40``` you should place your board and list name. <br />
you can change date as whatever you want. It will be the description of the card. <br />
You can specify a name too. In this code it is called "test".

All done! All we have to do is to schedule tasks to run this script. For this purpose, I used [crontab](https://crontab.guru/)

# CRONTAB
## What is crontab
The crontab is a list of commands that you want to run on a regular schedule, and also the name of the command used to manage that list. ([source](https://www.geeksforgeeks.org/crontab-in-linux-with-examples/))<br />

## Creating a crontab task
execute 
```crontab -l```
to see if there are any crontab task you are currently running.<br />
if there isn't any, execute ```crontab -e``` to edit crontab task.
pick one text editor of your choosing. <br />

After choosing the editor, add:
```
* * * * * cd your_appliacation_path && python trello.py
```
save and quit. Done!

### Important note
To kill a crontab task, simply execute ```crontab -r```.<br />

## Crontab scheduling
This ``` * * * * * ``` implies that our code will be executed at the beginning of every minute. <br />
![](https://i2.wp.com/www.adminschoice.com/wp-content/uploads/2009/12/crontab-layout.png?resize=640%2C284)

