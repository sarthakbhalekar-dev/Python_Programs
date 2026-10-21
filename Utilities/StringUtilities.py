
# ---------- STRING TOOLS ----------

def string_tools():
    print("\n===== STRING TOOLS =====")

    text = input("Enter a string or sentence: ")

    while True:
        print("\n========== MENU ==========")
        print("1. Reverse Text")
        print("2. Uppercase")
        print("3. Lowercase")
        print("4. Character Count")
        print("5. Word Count")
        print("6. Count Vowels and Consonants")
        print("7. Separate Characters")
        print("8. Palindrome Checker")
        print("9. Replace a Word")
        print("10. Remove Extra Spaces")
        print("11. Count Word Occurrences")
        print("12. Enter New Text")
        print("0. Exit")
        print("==========================")

        choice = input("\nSelect an option: ").strip()

        if choice == "1":
            print("Reversed:", text[::-1])

        elif choice == "2":
            print("Uppercase:", text.upper())

        elif choice == "3":
            print("Lowercase:", text.lower())

        elif choice == "4":
            print("Total characters:", len(text))

        elif choice == "5":
            words = text.split()
            print("Total words:", len(words))

        elif choice == "6":
            vowels = "aeiou"

            vowel_count = 0
            consonant_count = 0

            for char in text.lower():
                if char.isalpha():
                    if char in vowels:
                        vowel_count += 1
                    else:
                        consonant_count += 1

            print("Vowels:", vowel_count)
            print("Consonants:", consonant_count)

        elif choice == "7":
            print("Separated characters:")
            print(" | ".join(text))

        elif choice == "8":
            cleaned = "".join(
                char.lower()
                for char in text
                if char.isalnum()
            )

            if cleaned == cleaned[::-1]:
                print("This text is a palindrome!")
            else:
                print("This text is not a palindrome.")

        elif choice == "9":
            old = input("Enter text to replace: ")

            if not old:
                print("Please enter something to replace.")
                continue

            new = input("Replace with: ")

            if old not in text:
                print("Text not found.")
            else:
                text = text.replace(old, new)
                print("Updated text:", text)

        elif choice == "10":
            text = " ".join(text.split())
            print("Cleaned text:", text)

        elif choice == "11":
            word = input("Enter word to count: ").strip()

            if not word:
                print("Please enter a word.")
                continue

            words = text.lower().split()

            # Ignore common punctuation around words
            words = [
                item.strip(".,!?;:\"'()[]")
                for item in words
            ]

            count = words.count(word.lower())

            print(f"'{word}' appears {count} time(s).")

        elif choice == "12":
            text = input("Enter new text: ")
            print("Text updated!")

        elif choice == "0":
            print("Thanks for using String Tools!")
            break

        else:
            print("Invalid option! Please try again.")


# ---------- START ----------

if __name__ == "__main__":
    string_tools()
