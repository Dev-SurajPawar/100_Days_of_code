PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("./Input/Letters/mailBody.txt") as mail_file:
    mail_contents = mail_file.read()
    for name in names:
        stripped_name = name.strip()
        new_mail = mail_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/Mail_for_{stripped_name}.txt", mode="w") as completed_mail:
            completed_mail.write(new_mail)