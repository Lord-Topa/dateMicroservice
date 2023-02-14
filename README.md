# dateMicroservice
A micro-service that I made for my CS361 class, can return date and day of the week
## Instructions:
1) Make sure that dateMicroservice.txt is located at the same location specified in the PATH varible in microservice.py
2) Run the command python3 microservice.py
3) Insert a command into dateMicroservice.txt
4) Result will be returned to dateMicroservice.txt at which point you are now ready to put in another command

## Commands:
*Note any other command than the ones specified below will result in "ERROR INVALID INPUT" being returned, at which point a valid command must be input to continue using the micro-service*

* *get date* -- This command will return the current date in a YYYY-MM-DD format 

* *get day* -- This command will return the current day of the week in lowercase letters

* *get full date* -- This command will return the date and day of the week in a YYYY-MM-DD,dayOfTheWeek format

* *exit* -- This command will clear the dateMicroservice.txt file and will kill the microservice process

## Sequence Diagram:

![UML](https://user-images.githubusercontent.com/48222621/218625540-7644d753-5b62-496c-83ea-0ad870059f81.png)

* The main program requests the date, day of the week, or both by writing a command to a textfile

* The micro-service processes the command and then clears the contents of the text file and replaces them with the output 
