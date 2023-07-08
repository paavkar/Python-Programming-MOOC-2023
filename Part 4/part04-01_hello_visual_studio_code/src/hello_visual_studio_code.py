# Write your solution here
while True:
    editor = input("Editor: ")
    if(editor.lower() == "visual studio code"):
        print("an excellent choice!")
        break
    else:
        if(editor.lower() == "notepad" or editor.lower() == "word"):
            print("awful")
        else:
            print("not good")