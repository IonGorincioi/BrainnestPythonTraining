file = open("mbox-short.txt", "r")
content = file.readlines()
file.close()

word_str = ""
for word in content:
    word_str = word_str + word
    if word_str.startswith('From') or word_str.startswith('From:'):
        lines = word_str.split("From:")
        for line in lines:
            line = line.split(" ")
            print(line)
            for element in line:
                element = element.split(", ")
                print(element)

                for email in element:
                    print(email[1])