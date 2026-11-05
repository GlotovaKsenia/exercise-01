def divide_word(wort: str) -> dict[int, str]:
    tabelle = {}
    for i in range(1, len(wort) + 1):
        tabelle[i] = wort[:i]
    return tabelle

for nummer, teilwort in divide_word("test").items():
    print(nummer, teilwort)