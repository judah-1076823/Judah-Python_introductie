#String

ship = 'Titanic'
print(ship)

ship = "Titanic"
print(ship)

ship = """Titanic\n"""
print(ship)

#quotes gebruiken in een string
zonder_escape = 'This is a "good" plan.'
print(zonder_escape)

met_escape = "This is a \"good\" plan.\n"
print(met_escape)

#""" """ gebruiken voor een paragraaf
paragraaf = """Computer Technology means all designs, drawings, procedures (including design, manufacturing, test and maintenance procedures), specifications, software (other than as described within the meaning of the term "Software" defined elsewhere herein), printed circuit board art work, integrated circuit masks, test equipment, tools, fixtures, documentation, training materials, and information, in whatever form, related to, useful, utilizable or necessary in the design, manufacture, test and/or maintenance of the computer system, or relate to any Technology Licenses.\n\n"""
print(paragraaf)

#met de len() functie kan je vragen hoeveel karakters er in een string zitten
character_in_paragraph = len(paragraaf)
print(f"{paragraaf}The paragraph has {character_in_paragraph} characters.\n\n")

year = 1936
inventor = "Alan Turing"
name_of_maschine = "automatic machine"
invention = f'The Turing machine was invented in {year} by {inventor}, who called it an "a-machine" ({name_of_maschine}).'
print(invention)
