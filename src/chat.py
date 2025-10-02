import sys
import argparse
from search import search_prompt

BANNER = "Faça sua pergunta (ou digite 'sair' para encerrar):"
EXIT_COMMANDS = {"sair", "exit", "quit", "q"}

def responder(pergunta: str):
    resposta = (search_prompt(pergunta) or "").strip()
    

def main():
    parser = argparse.ArgumentParser(
        description="Pergunte via CLI e receba a resposta (modo interativo)."
    )
    parser.add_argument("pergunta", nargs="*", help="Texto da pergunta (opcional).")
    args = parser.parse_args()

    if args.pergunta:
        pergunta_inicial = " ".join(args.pergunta).strip()
        if pergunta_inicial:
            responder(pergunta_inicial)

    # Entra no modo interativo
    print(BANNER)
    while True:
        try:
            pergunta = input("> ").strip()
        except EOFError:
            print()  # encerra graciosamente
            break
        except KeyboardInterrupt:
            print("\n(Use 'sair' para encerrar.)")
            continue

        if not pergunta:
            continue
        if pergunta.lower() in EXIT_COMMANDS:
            break

        responder(pergunta)

if __name__ == "__main__":
    main()
