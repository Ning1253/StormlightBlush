texts = [open("The Way of Kings.txt", "r", encoding = "utf8").read(), open("Words of Radiance.txt", "r", encoding = "utf8").read(), open("Oathbringer.txt", "r", encoding = "utf8").read()]
out = open("README.md", "w+", encoding = "utf8")

out.write("""## StormlightBlush
A directory for counting the amount of blushes in the Stormlight Archive (currently books 1 to 3, since I haven't read book 4 yet and don't want spoilers)\n\n""")

c = 0
a = 1
for text in texts:
    text = text.translate({ord(c): None for c in "1234567890"}).split(".")

    for s in range(len(text)):
        if "blush" in text[s] or "Blush" in text[s]:
            string = text[s-1] + ". " + text[s] + ". "
            i = 2
            while "”" in text[s-i+1]:
                string = text[s-i] + ". " + string
                i += 1

            string = text[s-i] + ". " + string
            i += 1
            while "”" in text[s-i+1]:
                string = text[s-i] + ". " + string
                i += 1
                
            while string[0] == " " or string[0] == "\n":
                string = string[1:]

            title = "The Way of Kings" if not c else "Words of Radiance" if c == 1 else "Oathbringer"
            out.write(f"# {a}. Sentence {s} of {title}: \n\n{string}\n\n\n")
            a += 1
    c += 1