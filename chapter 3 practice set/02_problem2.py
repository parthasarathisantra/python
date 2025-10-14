letter = '''Dear <|Name|>,
  You are selected!
 <|Date|>'''

print(letter.replace("<|Name|>", "harry").replace("<|Date|>", "20 october 2025"))
