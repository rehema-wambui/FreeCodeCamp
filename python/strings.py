# it prints the string Email: and the value of the email variable and the f combine the variabble with the string
email = "alice.johnson@company.com"
print(f"Email: {email}")

# it finds the position of a character @
at_position = email.find("@")
print(f"Position of @: {at_position}")

# it printed only the username which was before the at_position[start:stop] it shows where to start at and where to stop
username = email [:at_position]
print(f"Username: {username}")

# proved if there was @ in the value of email by printing true
has_at = "@" in email
print( f"Has @ symbol: { has_at}")
# proved that there was .com by printing true

has_com = ".com" in email
print(f"Has .com: {has_com}")

# prints the variable with ' '
messy_name = '  sARaH dAVis  '
print(f"Original name: '{messy_name}'")

# .title() capitalises the first letter of the string string while .strip removes whitespace
clean_name = messy_name.strip().title()
print(f"Cleaned name: '{clean_name}'")

# .lower converts the string to lowercase while .strip removes the white space like i said earlier
messy_email = "  SARAH.DAVIS@COMPANY.COM  "
clean_email = messy_email.strip().lower()
print(f"Original email: '{messy_email}'")
print(f"Cleaned email: '{clean_email}'")

# .upper converts the string welll the value of the variable to uppercase 
name_budge = clean_name.upper()
print(f"Name badge: {name_budge}")

# .find finds the position of thestated character while[:at_pos] selects the string from the start to the at_posposition
at_pos = clean_email.find("@")
email_user = clean_email[:at_pos]
print(f"Email: {clean_email}")
print(f"Username: {email_user}")

# .replace(old,new)you write the thing you want replaced on the old and what to replace it with on the new
display_name = email_user.replace(".", "").title()
print(f"Display name: {display_name}")

phone = str("123-456-7890")
phone_clean = phone.replace("-","")
print(f"Phone with dashes: {phone}")
print(f"Phone without dashes: {phone_clean}")

# .split(separator) splits a string into a list at each separator ,
full_address = "123 Main Street, Springfield, IL"
address_parts = full_address.split(', ')
print(f"Address parts: {address_parts}")

# .join(list) joins a list of strings into one using a separator basically the opposite of a .split
rejoined = " | ".join(address_parts)
print(f"Rejoined: {rejoined}")

# .startwith() to check how a string starts returning with true or false while .endswith checks how it ends
employee_code = "EMP-2024-SD"
starts_with_emp = employee_code.startswith("EMP")

ends_with_com = clean_email.endswith(".com")

print(f"Code: {employee_code}")
print(f"Starts with EMP: {starts_with_emp}")
print(f"Clean email: {clean_email}")
print(f"Ends with .com: {ends_with_com}")

# .count(substring) counts how many characters or signs are repeated
dot_count = clean_email.count(".")
dash_count = employee_code.count("-")

print(f"Dots in email: {dot_count}")
print(f"Dashes in code: {dash_count}")