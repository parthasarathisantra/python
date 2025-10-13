letter = '''dear <|name|>,
you are selected
<|date|> '''

print(letter.replace("<|name|>", "harry").replace("<|date|>", "24 september 2050"))