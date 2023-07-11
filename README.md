# Email Automation

This is a Python script that provides functionality for email automation, including sending emails and checking emails using IMAP. The script utilizes the `smtplib` and `imaplib` libraries for sending and receiving emails, respectively.

## Prerequisites

- Python 3.x
- `smtplib` library (included in Python standard library)
- `imaplib` library (included in Python standard library)

## Getting Started

1. Clone the repository or download the project files.
2. Make sure you have Python installed on your system.
3. Run the script using the following command:

```shell
python email_automation.py
```

## Usage

Upon running the script, you will be presented with a menu where you can choose between sending emails and checking emails.

### Sending Emails

To send an email, select option `1` from the menu. Follow the prompts to provide the necessary information:

- Enter your email: Enter the email address you want to send the email from.
- Enter your password: Enter the password associated with the sender's email address.
- Enter the recipient's email: Enter the email address of the recipient.
- Enter the email subject: Enter the subject line of the email.
- Enter the email message: Enter the body of the email.
- Enter the file path (optional): If you want to attach a file to the email, enter the file path here. This is optional.

### Checking Emails

To check emails, select option `2` from the menu. Follow the prompts to provide the necessary information:

- Enter your email address: Enter the email address you want to check.
- Enter your email password: Enter the password associated with the email address.
- Enter the date (YYYY-MM-DD): Enter the date in the format `YYYY-MM-DD`. The script will retrieve all emails received on or after this date.

The script will then display the subject, sender, date, and any attachments for each email matching the specified date.

## File Structure

- `email_automation.py`: The main Python script containing the email automation functionality.

## License

This project is licensed under the [MIT License](LICENSE).

Feel free to modify and distribute the code as per your needs.

## Acknowledgments

This project was inspired by the need for automating email tasks, such as sending automated notifications or retrieving specific emails. It serves as a starting point for building more advanced email automation systems.
