import sys
from colorama import Fore, Style, init
from safety import input_guards, output_guards
from agents import orchestrator

init(autoreset=True)


def print_banner():
    print(Fore.MAGENTA + "=" * 60 + Style.RESET_ALL)
    print(Fore.CYAN + "  ATX WebDevQuizy - AI Knowledge Assistant" + Style.RESET_ALL)
    print(Fore.CYAN + "  Powered by Ollama + RAG + Multi-Agent System" + Style.RESET_ALL)
    print(Fore.MAGENTA + "=" * 60 + Style.RESET_ALL)
    print()


def ask(query, user_role="student"):
    print(Fore.YELLOW + f"\nQuestion: {query}" + Style.RESET_ALL)

    # step 1 - input guardrails
    guard_result = input_guards.check(query)

    if not guard_result["allowed"]:
        print(Fore.RED + f"\nRequest blocked: {guard_result['reason']}" + Style.RESET_ALL)
        return

    clean_query = guard_result["cleaned_input"]
    if clean_query != query:
        print(Fore.YELLOW + f"Input was cleaned: {clean_query}" + Style.RESET_ALL)

    # step 2 - run through agents
    result = orchestrator.run(clean_query, user_role=user_role)

    # step 3 - output guardrails
    output_check = output_guards.check(result["answer"], [])
    final_answer = output_check["answer"]

    # step 4 - print final answer
    print(Fore.GREEN + "\nAnswer:" + Style.RESET_ALL)
    print(final_answer)

    if result["citations"]:
        print(Fore.CYAN + f"\nSources: {', '.join(result['citations'])}" + Style.RESET_ALL)

    print(Fore.MAGENTA + f"\nCompleted in {result['trace']['rounds']} round(s)" + Style.RESET_ALL)


def main():
    print_banner()
    print("Type your web dev question below.")
    print("Type 'quit' to exit.\n")

    while True:
        try:
            query = input("You: ").strip()
            if not query:
                continue
            if query.lower() in ["quit", "exit", "q"]:
                print("\nGoodbye! Keep building!")
                break
            ask(query)
        except KeyboardInterrupt:
            print("\n\nGoodbye! Keep building!")
            break


if __name__ == "__main__":
    main()