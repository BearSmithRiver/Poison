import argparse
import hashlib
import pyfiglet

def generate_banner(text, font="ascii9", color="blue", text_color="white"):
    custom_fig = pyfiglet.Figlet(font=font)
    banner = custom_fig.renderText(text)
    return banner


text_to_display = "POISON"
banner = generate_banner(text_to_display, font="ascii9")
print(banner)

def crack_md5_hash(target_hash, wordlist_path, verbose=False):
    with open(wordlist_path, 'r', encoding='utf-8') as wordlist_file:
        for line in wordlist_file:
            password = line.strip()

            
            print(f"Testando senha: {password} ({hashlib.md5(password.encode()).hexdigest()})")

            hashed_password = hashlib.md5(password.encode()).hexdigest()

            if hashed_password == target_hash:
                return password

    return None

def main():
    parser = argparse.ArgumentParser(description="Quebrar hash MD5 usando uma wordlist.")
    parser.add_argument("-t", "--target-hash", required=True, help="A hash MD5 alvo ou o caminho para o arquivo contendo a hash.")
    parser.add_argument("-w", "--wordlist", required=True, help="O caminho para a wordlist.")
    parser.add_argument("-v", "--verbose", action="store_true", help="Ativar modo verbose.")

    args = parser.parse_args()

    
    if "/" in args.target_hash or "\\" in args.target_hash:
       
        with open(args.target_hash, 'r', encoding='utf-8') as hash_file:
            target_hash = hash_file.read().strip()
    else:
        
        target_hash = args.target_hash

    wordlist_path = args.wordlist
    verbose_mode = args.verbose

    cracked_password = crack_md5_hash(target_hash, wordlist_path, verbose=verbose_mode)

    if cracked_password:
        print(f"A senha correspondente ao hash é: {cracked_password}")
    else:
        print("Senha não encontrada na wordlist.")

if __name__ == "__main__":
    main()
