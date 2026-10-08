def string_tools():
    text = input("Enter a string/sentence: ")
    print(f"Reversed: {text[::-1]}")
    print(f"Upper: {text.upper()}")
    print(f"Length: {len(text)}")
    print("Separated characters:", " | ".join(list(text)))

if __name__ == "__main__":
    string_tools()