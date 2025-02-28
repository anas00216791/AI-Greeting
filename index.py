import time

def ai_greeting():
    ai_art = """
     █████╗ ██╗
    ██╔══██╗██║
    ███████║██║
    ██╔══██║██║
    ██║  ██║██║
    ╚═╝  ╚═╝╚═╝
    """
    print(ai_art)
    
    print("🔹 Booting AI System... 🤖")
    time.sleep(1)
    print("🔹 Establishing Secure Neural Link... ⚡")
    time.sleep(1)

    name = input("\n🔹 Enter Your Identification (Name): ")
    
    time.sleep(1)
    print("\n🔹 Scanning User Data... ✅")
    time.sleep(1)
    
    print(f"\n🔹 Greetings, {name}! 🌟")
    print("🔹 I am your advanced AI companion, optimized for maximum efficiency. 🚀")
    print("🔹 Ready to assist you with any task. Let's innovate together! 💡")

# Run the AI greeting function
ai_greeting()
