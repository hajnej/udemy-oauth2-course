#!/usr/bin/env python3

import pkce


def main():
    """Main function to be executed when executed directly, generates and prints pkce code_challenge and code_verifier"""
    code_verifier, code_challenge = pkce.generate_pkce_pair()
    print(f"Generated code_challange is {code_challenge}")
    print(f"Generated code_verifier is {code_verifier}")


if __name__ == "__main__":
    main()
