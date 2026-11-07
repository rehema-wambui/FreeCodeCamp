# This file defines a simple email system with three main parts:
# 1) Email objects that represent messages.
# 2) User objects that can send emails and keep an inbox.
# 3) Inbox objects that store emails received by a user.

import datetime

# The Email class represents a single email message.
# Each email has information about who sent it, who it is for,
# the subject, the message body, and whether it has been read.
class Email:
    # The __init__ method is called automatically when a new Email object is created.
    # It sets up the attributes for the email.
    def __init__(self, sender, receiver, subject, body):
        # 'sender' stores the User object sending the email.
        self.sender = sender
        # 'receiver' stores the User object receiving the email.
        self.receiver = receiver
        # 'subject' stores the email subject line.
        self.subject = subject
        # 'body' stores the main text content of the email.
        self.body = body
        # 'read' starts as False because a newly received email has not been opened yet.
        self.timestamp = datetime.datetime.now()
        self.read = False
        # Use the same timestamp wherever the email's sent time is displayed.
        self.sent_at = self.timestamp

    # Return a brief summary of the email.
    def __str__(self):
        status = "Read" if self.read else "Unread"
        return f"[{status}] From: {self.sender.name} | Subject: {self.subject}| Time: {self.timestamp.strftime('%Y-%m-%d %H:%M')}"

    # This method marks the email as read.
    # It changes the 'read' attribute from False to True.
    def mark_as_read(self):
        self.read = True

    # Display the email's details and mark it as read when viewed.
    def display_full_email(self):
        self.mark_as_read()
        print("\n--- Email ---")
        print(f"From: {self.sender.name}")
        print(f"To: {self.receiver.name}")
        print(f"Subject: {self.subject}")
        print(f"Sent: {self.sent_at.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Body: {self.body}")
        print("------------\n")

# The User class represents a person using the email system.
# Each user has a name and their own inbox.
class User:
    # The constructor creates a user with a name and an Inbox object.
    def __init__(self, name):
        # 'name' stores the person's name.
        self.name = name
        # 'inbox' is created automatically for every user.
        # It allows the user to receive and store messages.
        self.inbox = Inbox()

    # This method is used to send an email to another user.
    # It creates an Email object and adds it to the receiver's inbox.
    def send_email(self, receiver, subject, body):
        # Create a new Email object.
        # The sender is 'self' (the current user object),
        # the receiver is the User object passed into the method,
        # and the subject/body are the text provided by the sender.
        email = Email(self, receiver, subject, body)

        # Call the receiver's inbox method to store the email.
        receiver.inbox.receive_email(email)
        print(f"Email sent from {self.name} to {receiver.name}!")

    def check_inbox(self):
        print(f"{self.name}'s Inbox:")
        self.inbox.list_emails()

    def read_email(self, index):
        self.inbox.read_email(index)

    def delete_email(self, index):
        self.inbox.delete_email(index)



# The Inbox class stores all emails that a user receives.
# It acts like a mailbox or list of messages.
class Inbox:
    # The constructor initializes an empty list of emails.
    def __init__(self):
        # 'emails' is a list that will hold Email objects.
        self.emails = []

    # This method receives an email and adds it to the inbox list.
    def receive_email(self, email):
        # Append adds the email object to the end of the list.
        self.emails.append(email)

    def list_emails(self):
        if not self.emails:
            print("Your inbox is empty.")
            return
        print("\nYour Emails:")
        for i, email in enumerate(self.emails, start=1):
            print(f"{i}. {email}")
    def read_email(self, index):
        if not self.emails:
            print("Inbox is empty.\n")
            return
        if index < 1 or index > len(self.emails):
            print("Invalid email number.\n")
            return
        self.emails[index - 1].display_full_email()
    def delete_email(self, index):
        if not self.emails:
            print("Inbox is empty.\n")
            return
        if index < 1 or index > len(self.emails):
            print("Invalid email number.\n")
            return
        del self.emails[index - 1]
        print("Email deleted.\n")


def main():
    tory = User("Troy")
    ramy = User("Ramy")
    tory.send_email(ramy, "Hello", "Hi Ramy, just saying hello!")
    ramy.send_email(tory, "Re: Hello", "Hi Tory, hope you are fine.")
    ramy.check_inbox()
    ramy.read_email(1)
    ramy.delete_email(1)
    ramy.check_inbox()


if __name__ == "__main__":
    main()