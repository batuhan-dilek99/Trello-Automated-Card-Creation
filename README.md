# CRONTAB
execute 
```crontab -l```
to see if there are any crontab task you are currently running.<br />
if there isn't any, execute ```crontab -e``` to edit crontab task.
pick one text editor of your choosing. <br />

After choosing the editor, add
```
* * * * * cd your_appliacation_path && python trello.py
```
This ``` * * * * * ``` implies that our code will be executed at the beginning of every minute. <br />

## Crontab scheduling
![](https://i2.wp.com/www.adminschoice.com/wp-content/uploads/2009/12/crontab-layout.png?resize=640%2C284)
