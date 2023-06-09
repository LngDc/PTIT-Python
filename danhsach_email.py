def main():
    emails = set()
    
    for email in open('CONTACT.in', 'r'):
        email = email.lower()
        emails.add(email)
        
    emails = sorted(list(emails))
    for email in emails:
        print(email)
        
        

if __name__ == '__main__':
    main()