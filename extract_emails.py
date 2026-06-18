import re
with open("input.txt", "r") as file:
    content = file.read()
emails = re.findall(
    r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}',
    content
)
with open("emails.txt", "w") as file:
    for email in emails:
        file.write(email + "\n")
print("Email addresses extracted successfully!")
print("\nFound Emails:")
for email in emails:
    print(email)