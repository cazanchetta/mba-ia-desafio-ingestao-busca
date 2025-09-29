import sys
import argparse
from search import search_prompt

BANNER = "Faça sua pergunta:\n"

def main():
    parser = argparse.ArgumentParser(
        description="Pergunte via CLI e receba a resposta."
    )
    parser.add_argument("pergunta", nargs="*", help="Texto da pergunta.")
    args = parser.parse_args()

    if args.pergunta:
        question = " ".join(args.pergunta).strip()
    else:
        if not sys.stdin.isatty():
            question = sys.stdin.read().strip()
        else:
            question = input(BANNER).strip()

    if not question:
        print("Pergunta vazia.")
        sys.exit(1)

    search_prompt(question)


if __name__ == "__main__":
    main()