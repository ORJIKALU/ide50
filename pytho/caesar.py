from cryptography.fernet import Fernet

key = 'TluxwB3fV_GWuLkR1_BzGs1Zk90TYAuhNMZP_0q4WyM='

# Oh no! The code is going over the edge! What are you going to do?
message = b'gAAAAABckWsrXl-gcxyNTNa-fX0cSViQgSKnpmhJypylbeEF23449IHAgyszOtyL0fkqj-Ve8HXmVz-SDisoJEdOqgaWlJcpdQBHmiO8U-itd7Xge6QyluDtBQFailktmPLEXVjk2lnYHnhR330NltXzRsahIO6EI-BgwkHsC-7vUDwQwRQmaOMFfLL7o6LUNKo-GYAaebzn'

def main():
    f = Fernet(key)
    print(f.decrypt(message))


if __name__ == "__main__":
    main()
