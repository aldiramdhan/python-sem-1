import gempa as g
g.Gempa

gempa1 = g.Gempa("Banten", 1.2)
gempa2 = g.Gempa("Palu", 6.1)
gempa3 = g.Gempa("Cianjur", 5.6)
gempa4 = g.Gempa("Jayapura", 3.3)
gempa5 = g.Gempa("Garut", 4.0)

gempa1.dampak()
gempa2.dampak()
gempa3.dampak()
gempa4.dampak()
gempa5.dampak()

print ("%")
# Run Code
