## TempMailX
A python lib for reciving emails using 1secmail.com api.

---
### Example
```python
import time
from tempmailx import TempMail

mail = TempMail()
print(mail.email)

while True:
    emails = mail.fetch_emails()

    for email in emails:
        dat = email.fetch_data()
        print(dat['text'])
    time.sleep(5)
```