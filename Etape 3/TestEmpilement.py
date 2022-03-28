import Empilement
import Planchette


p = Planchette.cree(10, 2)

e = Empilement.cree(p, 6)
print('e=' + str(e))

print('planchette=' + str(Empilement.planchette(e)))
print('centreGeometrique=' + str(Empilement.centreGeometrique(e)))
print('masse=' + str(Empilement.masse(e)))
print('centreGravite=' + str(Empilement.centreGravite(e)))
print('desequilibre=' + str(Empilement.desequilibre(e)))

print('versChaine(e)=' + Empilement.versChaine(e))

Empilement.masse(e, 18)
Empilement.centreGravite(e, 8)
Empilement.desequilibre(e, True)
print('e=' + str(e))
print('versChaine(e)=' + Empilement.versChaine(e))
