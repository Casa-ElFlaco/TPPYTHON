Base = 4
Fromage = 800.0
Eau = 2
Ail = 2
Pain = 400
nbconvives = int(input("Combien de convives y aura t-il ? "))
nvfromage = (Fromage * nbConvives) / Base
nveau = (Eau * nbConvives) / Base
nvail = (Ail * nbConvives) / Base
nvpain = (Pain * nbConvives) / Base
print("Pour faire une fondue fribourgeoise pour", nbConvives," personnes, il vous faut :", nvfromage,"g de fromage, ",nveau,"L d'eau",nvail,"gousses d'ail", nvpain, "gr de pain")
