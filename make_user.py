#!/usr/bin/env python3

# This is another quick and dirty script to help devs speed up interacting with POFIS.

import argparse

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("-u", "--username", required=True, type=str, help="The username to add")
    parser.add_argument("-p", "--password", required=True, type=str, help="The password to use with username.")

    args = parser.parse_args()

    from pofis.auth import Authenticator

    Authenticator().create_user(args.username, args.password)

if __name__ == "__main__":
    main()