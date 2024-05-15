import aiml

# Create a kernel
kernel = aiml.Kernel()

# Load AIML files
kernel.learn("std-startup.xml")
kernel.learn("basic_chat.aiml")  # Load your AIML files here

# Enter the conversation loop
while True:
    input_text = input(">Human: ")
    response = kernel.respond(input_text)
    print(">CustomerBot: " + response)
