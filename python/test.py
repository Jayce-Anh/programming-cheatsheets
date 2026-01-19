log_entry = "  INFO: User 'admin' logged in successfully.  \n"
parts = log_entry.strip().split(':')
print(parts)
message_text = parts[1].strip()
print(message_text)