#Bestellen
print("\nBestellen:\nWelkom bij Mc Donalds, laten we beginnen met je bestelling.")

meenemen = False
waar_eten_str = input("\nWilt u de bestelling meenemen of hier opeten?\n")
waar_eten = waar_eten_str.upper()

if waar_eten == 'MEENEMEN':
  meenemen = True

print("\nWilt u een burger bestellen?\n- Hamburger\n- Cheeseburger\n- Big Mac\n- Qarter pounder\n- Nee\n")
burger_keuze_str = input()
burger_keuze = burger_keuze_str.upper()

if burger_keuze == "QUARTER POUNDER":
  kaas_keuze = input("Wilt u kaas op de Quater pounder? [ja/nee]\n")