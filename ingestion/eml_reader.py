import email
from email import policy
from email.parser import BytesParser

def extract_text_from_eml(file_path):
    with open(file_path, 'rb') as f:
        msg = BytesParser(policy=policy.default).parse(f)

    body = ""
    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() == 'text/plain':
                body += part.get_content()
    else:
        body = msg.get_content()

    return body.strip()
