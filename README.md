# Socket_project
This program allows user to call another user via ascii char video call on LAN

The purpose of this project was to learn about low level networking and the use of sockets.

This program implements custom library: py_express that TRIES to mimic express.js functionality.

Work on this project has stopped in order to further develop py_express library.

This is a version with minimal functionality. At this stage you can only send 'video' to another person if that person is actively listening to incoming 'video'.
# ascii to live video 
To test only ascii to video functionality run this command in project directory
```
$python src/img_to_ascii.py
```
# example of one frame from 'video'
![image](https://github.com/juris12/Socket_project/assets/102772784/c19f954e-ae2d-4153-9b06-8eb2621f34e0)

# To start:
    1.Go to /src and run main.py(server)

    2.Open separate terminal window and run client.py

    3.Login or register

    5.If user wants to wait for call type command “o”

    6.Open separate terminal window and run client.py

    7.Login or register

    8. Scroll with “down” or “up” commands to select wright user

    9.If user is waiting for call “status true” then call with command “c”
