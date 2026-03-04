import random
import string

def text_captcha(length=6):
    alphabet = string.ascii_uppercase + string.digits
    code = "".join(random.choice(alphabet) for _ in range(length))

    # Add harmless visual noise (spaces and random separators)
    noisy = " ".join(code)
    noisy = noisy.replace(" ", random.choice([" ", "  ", "   "]))
    border = random.choice(["-", "=", "~", "*"]) * (len(noisy) + 6)

    print(border)
    print(f"   {noisy}   ")
    print(border)

    guess = input("Type the code (no spaces): ").strip().upper().replace(" ", "")
    return guess == code

if __name__ == "__main__":
    if text_captcha():
        print("✅ Verified.")
    else:
        print("❌ Incorrect.")