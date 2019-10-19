## Wechat Push Service

Wechat Push Service is to push **weather** and **luck** information to supcific *wechat* users. This is a rebuild version of the original project which has been at service for one and a half year. Almost all codes were rewrite and became more efficient and stable.

This project uses `.csv` files to manage the users list and push messages. It require python3 and packages: `itchat`, `requests`, `json` 



#### Structure and Function

---

+ login.py

  This module allows you to login with a QRCode on your wechat mobile app and keep login status as webpage login. You **MUST** keep this module running using `nohup ./login.py &` or as a daemon or service to enable other modules to send messages.

  *Be adviced: new wechat account may not be allowed to use wepage login function.*

+ weather_get.py

  This module gets weather information from HeWeather. A personal key is needed to get access to the weather data. My keys were **REMOVED** from source code. You have to apply one for yourself and add it into the source code. 

  The `weather_get.py` uses `/list/location.list` to read cities and get write in files. For that Beijing has a car plate number restriction policy, I put some code to add restriction information. If you don't need it just comment it out. 

  I haven't figured out how to change the car plate number every three month, so you **must** make a change yourself.

  *Key is free and very easy to apply*

+ forecast_get.py

  This module gets forecast information from HeWeather. This function is mostly like `weather_get.py` . As well, if you don't need car plate restriction information you can remove it from the code.

+ luck_get.py

  This module get luck information from `juhe.cn`. It writes 12 luck information into 12 files. This module also requires a key. You can get one from `juhe.cn` for free.

+ am_send.py & pm_send.py

  This two modules send final information to user in the list. It can check if the username belongs to a friend or a chatroom. When editing `amsend.list` and `pmsend.list`, follow examples below:

  > 用户,张三,weather,beijing
  >
  > 群,李四,forecast,shanghai
  >
  > 用户,王五,luck,shuangyu



#### Time and Cron

---

You must update the weather, forecast and luck information everyday before you send them to end users. It is recommended that weather report and luck information updating on 0600 CST, forecast report updating on 1800 CST. If you update them much earlier than the time recommended, information may go wrong.

Use crontab to manage the time each module runs.

