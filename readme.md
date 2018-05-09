Final Project Description

How to use CloudAMQP?
1. Register a free cloud server at CloudAMQP, select Norhthern california for datacenter
2. After finish regsitration, go to your account and lcick into it for more detail. 
3. Copy the AMQP URL change the URL in both emit and receive_log file. 

Open three terminal windown. First run "python receive_log.py" in two different terminal window. And then run "python emit_log.py". Now you should get "hello world" for both receive windown. To send different message run "python emit_lot.py xxxxxxxx", then in the receive window, you should expect your custom message.

Link:
CloudAMQP: https://customer.cloudamqp.com/instance
Download python file: https://github.com/Mlu13