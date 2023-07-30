# GetNaFood

![preview](https://github.com/PhyoeKyawThan/getNaFood/blob/43c455d46f05fc0b36d288534d20049f1b39e0e5/preview/Screenshot%20from%202023-07-24%2020-49-37.png?raw=true)

---
## low UI with pure js , html and css

 Just a fun project to build my random thoughts in pure form, no encypt is use. Flask as web framwork and no built in auth module in use. Closely to MVC but I don't think so. Just a normal pj implemented all of the feature in pure python.

## Details
After running the project the client home page will be aviable on "`http://127.0.0.1:5000`".
for the orders u have to login or sigup account first. After sign up or login server will add a session name `user` with `username` and `password` include in this session. I made login button as dynamic when ur logged in the login text will be Logout text and it's redirect to  "`logout_session`" that method under `/logout` route and u can see it in the `views.py` under `app` folder.

### Admin

admin dashboard will be aviable "`/manage/admin`" and u need to login. u can look up the username and password under `app/login.py` but here is details Username "`domak`" and Password "`password`". After logged in, u can edit and delete the products. To update the product touch the area of the data which u want to update. U can look up it under clip.

<div align="center">
<video controls>
  <source src="https://github.com/PhyoeKyawThan/getNaFood/blob/master/preview/adminpanel.webm" type="video/webm">
</video>
</div>

i wrote admin dashboard in one applicaiton with home page for client, that'll take a lots of issues in production I know. as a beginner I want to practice my sills.
