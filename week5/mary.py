mary_text = "Mary had a little lamb,\
whose fleece was white as snow.\
\
And everywhere that Mary went,\
the lamb was sure to go."

with open('mary.txt', 'w') as outfile:
    outfile.write("Mary had a little lamb," + "\n" + "whose fleece was white as snow." + "\n" +
                  "And everywhere that Mary went," + "\n" + "the lamb was sure to go." + "\n")

with open('mary.txt', 'r') as infile:
    for line in infile:
        print(line.strip())
