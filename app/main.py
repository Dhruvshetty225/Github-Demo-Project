import argparse

def greet(name: str, excited: bool = False) -> str:
    msg = f"Hello, {name}! This is my GitHub demo."
    return msg.upper() if excited else msg

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Demo greeter")
    parser.add_argument("--name", default="World")
    parser.add_argument("--excited", action="store_true", help="Shout the greeting")
    args = parser.parse_args()
    print(greet(args.name, args.excited))
