import argparse
import string
import secrets

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

def main():
    parser = argparse.ArgumentParser(description='Generate a secure password')
    parser.add_argument('-l', '--length', type=int, default=12, help='Length of the password (default: 12)')

    args = parser.parse_args()

    password = generate_password(args.length)
    print(password)

if __name__ == '__main__':
    main()
