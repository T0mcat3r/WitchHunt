# WitchHunt (猎巫)
##### This honeypot is used for fast tracking e-identity information of the prey.
<br /><br />

###### Progress:
20/1:
- Initialize v1.0 of WitchHunt backend endpoint and RestAPI design documentation

21/1:
- Develop a script on server for WitchHunt Github Repo auto deployment
- Configure Flask to interpret HTTP_X_FORWARDED_FOR from Nginx
- Remove Frontend part from Backend for decoupling

22/1:
- Re-design Pots database and methods.
- Refactor naming conventions
- Created an oo for common db interface

23/1:
- Separated Database Insertion function from pot interface module and wrapped it into DB module.
- Added Deletion and Expiration functions in pot module.
- Updated the main server to use the newly created pot module :p

26/1:
- Fixed Dynamic Field parameter passing problem
- Added Size function for core db module
- Tested pot module's basic interfaces

28/1:
- Added RestAPI endpoint that returns all honeypots' Information
- Optimized honeypot trigger logic, merged information fetching process into a new thread with sendmail

29/1:
- 
<br /><br /><br />


TODO:
<br />
- Add attack modules for user device exploitation (ref. BeeF framework)
- Wechat: Add honeypots via messaging & Notification
- Add Analysis module for the prey information (Common IPs recognition)
- Add Status Code as an option.
- Add Reverse Proxy as an setup option
- Beautify UI
<br /> <br /> <br />

DONE:
<br />
- Test SendEmail function. (Tested & Added Error handling functionality)
- Implement expiry time logic for traps. (Done, also added conditional checks to clean DB)
<br /> <br />


##### It features the following compare to a traditional honeypot:
- Setting up via any portable mobile device
- Super fast setup process
- Customize honeypot webpage source code
- Automatically obtain the prey's physical location and ISP information
- Precise email notification when the trap is triggered
- Pre-set the valid expiry time for the webpage (Yet to be implemented)

<br />

How-To:
- Goto `http://your-site-here.com/set` to config and add new honeypots.

<br />

Installation:
- Install Python 3.X on your machine. ( e.g. 3.5.3 )
- `pip install flask dataset selenium`
- Get PhantomJS:
 - Windows: https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-windows.zip , unzip the phantomjs.exe and put it under the WitchHunt directory.
 - Linux: `apt-get install phantomjs`

<br /><br />
