Email Sender Application
=========================

This is a Python script that sends emails using a Gmail account. It uses email templates to customize the email content.

Configuration
-------------

The email configuration is stored in the `EmailConfig` class:

* `SENDER_EMAIL`: the Gmail address used to send emails
* `SENDER_PASSWORD`: the password for the Gmail account (consider using environment variables for sensitive data)
* `SMTP_SERVER`: the SMTP server used to send emails (smtp.gmail.com)
* `SMTP_PORT`: the port used for the SMTP server (465)

Email Content
-------------

The email content is stored in the `EmailContent` class:

* `TEMPLATES_DIR`: the directory where email templates are stored (templates)

Usage
-----

To use this script, follow these steps:

1. Enter the receiver's email address
2. Enter the subject of the email
3. Enter the template name (hello or follow_up)
4. Enter the name to be used in the email template
5. Enter the sender's name

The script will then send an email to the receiver using the specified template and placeholders.

Templates
----------

Email templates are stored in the `templates` directory. Each template is a text file with placeholders in the format `{{placeholder}}`. The script will replace these placeholders with the actual values provided by the user.

Dependencies
------------

This script requires the following Python modules:

* `ssl`
* `smtplib`
* `email.message`
* `os`

Make sure to install these modules before running the script.

License
-------

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
