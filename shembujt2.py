# Shembujt nga prezantimi i Anika Banjskës.
# print shfaq tekstin në terminal.
print("Rregulli i Laplace-it")
print("Formula: p = (pozitive + 1) / (totali + 2)")
print("pozitive është numri i vlerësimeve pozitive.")
print("totali është numri i përgjithshëm i vlerësimeve.")
print("Shtojmë teorikisht një vlerësim pozitiv dhe një negativ vetëm për llogaritje.")
print("Prandaj numëruesi rritet me 1 dhe emëruesi me 2.")
print("Të dhënat fillestare nuk ndryshojnë.")
print("p vlerëson probabilitetin që vlerësimi i ardhshëm të jetë pozitiv, sipas modelit.")
print()

# Produkti A: ruajmë të dhënat fillestare në variabla.
pozitive = 10
totali = 10
p = (pozitive + 1) / (totali + 2)  # Zbatojmë formulën.
p_A = p  # Ruajmë rezultatin pa rrumbullakim.

# Në një f-string, shprehjet brenda {} japin vlerat e tyre.
print("Produkti A")
print(f"{pozitive} vlerësime pozitive nga {totali}")
# * 100 e kthen raportin në përqindje; .0f shfaq zero shifra pas presjes.
print(f"Përqindja fillestare: {pozitive / totali * 100:.0f}%")
print(f"Laplace: ({pozitive} + 1) / ({totali} + 2) = {pozitive + 1} / {totali + 2}")
# .2f rrumbullakos vetëm shfaqjen në dy shifra pas presjes.
print(f"Rezultati: {p * 100:.2f}%")
print()  # Rresht bosh për të ndarë shembujt.

# Produkti B: përdorim të njëjtën formulë me të dhënat e B.
pozitive = 48
totali = 50
p = (pozitive + 1) / (totali + 2)
p_B = p  # Ruajmë veçmas rezultatin pa rrumbullakim.

print("Produkti B")
print(f"{pozitive} vlerësime pozitive nga {totali}")
print(f"Përqindja fillestare: {pozitive / totali * 100:.0f}%")
print(f"Laplace: ({pozitive} + 1) / ({totali} + 2) = {pozitive + 1} / {totali + 2}")
print(f"Rezultati: {p * 100:.2f}%")
print()

# Produkti C: llogarisim dhe ruajmë rezultatin e tretë.
pozitive = 186
totali = 200
p = (pozitive + 1) / (totali + 2)
p_C = p  # Ruajmë veçmas rezultatin pa rrumbullakim.

print("Produkti C")
print(f"{pozitive} vlerësime pozitive nga {totali}")
print(f"Përqindja fillestare: {pozitive / totali * 100:.0f}%")
print(f"Laplace: ({pozitive} + 1) / ({totali} + 2) = {pozitive + 1} / {totali + 2}")
print(f"Rezultati: {p * 100:.2f}%")
print()

print("Krahasimi i rezultateve")
# > do të thotë "më i madh se"; and kërkon të dy kushtet.
# if ekzekuton rreshtat brenda tij kur kushti është i vërtetë.
# Krahasojmë rezultatet e plota, pa rrumbullakim.
if p_B > p_C and p_C > p_A:
    print("Renditja sipas Laplace-it: B, C, A")
    print(f"B ({p_B * 100:.2f}%) > C ({p_C * 100:.2f}%) > A ({p_A * 100:.2f}%)")
    print("B ka rezultatin më të lartë sipas Laplace-it.")
    print("Kjo nuk garanton cilësinë e produktit.")
    print("Rezultati i B vlerëson probabilitetin që vlerësimi i ardhshëm për B të jetë pozitiv.")
    print("Ai nuk është probabiliteti që B të jetë produkti më i mirë.")