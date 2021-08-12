from enchant.checker import SpellChecker

chkr = SpellChecker("en_US")

chkr.set_text("This is sme sample txt with erors.")

for err in chkr:

    print("ERROR:", err.word)