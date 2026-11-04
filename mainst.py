# i dont get it
from pyscript import display, document

element_symbol = {
    'Hydrogen' : 'H',
    'Helium' : 'He',
    'Carbon'  : 'C',
    'Nitrogen' : 'N',
    'Oxygen' : 'O',
    'Fluorine' : 'F',
    'Neon' : 'Ne',
    'Phosphorus' : 'P',
    'Sulfur' : 'S',
    'Chlorine' : 'Cl',
    'Argon' : 'Ar',
    'Selenium' : 'Se',
    'Bromine' : 'Br',
    'Krypton' : 'Kr',
    'Iodine' : 'I',
    'Xenon' : 'Xe',
    'Radon' : 'R',
}

atomicno_atomicmass = {
     1 : 1.008,
     2 : 4.0026,
     6 : 12.011,
     7 : 14.007,
     8 : 15.999,
     9 : 18.998,
     10 : 20.180,
     15 : 30.974,
     16 : 32.06,
     17 : 35.45,
     18 : 39.948,
     34 : 78.971,
     35 : 79.904,
     36 : 83.798,
     53 : 126.9045,
     54 : 131.293,
     86 : '~222 (No stable mass; mass number)'

}

def collect_nonmetal(e):
    elementfinder = (document.getElementById('elementfinder').value)
elementfinder = element_symbol.values # tried (<- emphasis) to correlate elementfinder to symbol (values) in element_symbol, so that when user inputs symbol, they get the element_symbol as a whole + the atomicno_atomicmass

ultimate_elementbiothing = dict(zip(element_symbol, atomicno_atomicmass)) # tried to merge in proper order, only shows element and atomic number (the first two) 
elementfinder = display(ultimate_elementbiothing, target='output') # unfortunately shows the whole thing, and also makes the input textbox (and finding one element) redundant

# Hydrogen, Carbon, Nitrogen, Oxygen, Phosphorus, Sulfur, Selenium, Fluorine, Chlorine, Bromine, Iodine, Helium, Neon, Argon, Krypton, Xenon, and Radon.