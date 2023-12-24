# Poison - Quebrador de Hash MD5

Um script de ataque de força bruta em hashes MD5 que envolve tentar adivinhar a entrada original que corresponde a um determinado hash MD5. O MD5 é um algoritmo de hash criptográfico que produz uma sequência de 32 caracteres hexadecimais, independentemente do comprimento ou conteúdo da entrada original.
![bandicam 2023-12-24 06-36-40-885](https://github.com/BearSmithRiver/Poison/assets/150410689/aed096d4-11db-48e5-a96c-ce5a621c1e77)
![bandicam 2023-12-24 06-43-07-904](https://github.com/BearSmithRiver/Poison/assets/150410689/66d4295c-b646-4098-aba4-d2dc8063d6e9)

## Requisitos

- Python 3.x

## Uso

1. Clone o repositório:

    ```bash
    git clone https://github.com/BearSmithRiver/Poison
    ```

2. Navegue até o diretório do script:

    ```bash
    cd Poison
    ```

3. Execute o script:

    ```bash
    python3 poison.py -t <hash> -w <caminho_wordlist> -v
    ```

    Substitua `<hash>` pelo hash MD5 alvo, e `<caminho_wordlist>` pelo caminho para sua wordlist.

4. Verifique a saída para a senha que corresponde ao hash, se encontrada.

## Opções

- `-t` ou `--target-hash`: A hash MD5 alvo ou o caminho para o arquivo contendo a hash.
- `-w` ou `--wordlist`: O caminho para a wordlist.
- `-v` ou `--verbose`: Ativar modo verbose.

## Exemplo


python3 poison.py -t hash -w wordlist.txt -v

![storage_emulated_0_Android_data_com fawazapp blackhole_files_DCIM_XABNG1TD8QT73OUOR8M5_1](https://github.com/BearSmithRiver/Poison/assets/150410689/4c22150d-52c9-46f5-97ee-fcfacc9b833a)
