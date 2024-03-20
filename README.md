# PyAutoMailer
    An application to automatically send multiple emails with the same format and documentation

This is a limited program, my interest is to maintain it and update it little by little.
This program for now allows you to attach a file and a message to send to a mailing list
The user and password configuration is done from the config file
     You will need to insert the user and the password
To specify the emails you must list them in the Reciver_List.txt file but in the program configuration you can change the file name.
     They must be inserted as in the example in the file.
The message to be attached must be in the message.txt file which will be attached to the body of the email during execution
     You can also insert a custom path by placing it in message_path
After that you can run the program directly.

To attach a file you will need to enable it in the config file (Changing the status from false to true) and specify the file name in attachment_name and the path in attachment_path

Please do not touch the rest of the configuration if it is not necessary, otherwise I will not be responsible for it not working.
The components:
     smtp_server => Indicates the smtp server (in this case it is configured for Google accounts.)
     smtp_port => Indicates the SMTP port, this is usually this by convention, but if it is not this it can cause errors.
