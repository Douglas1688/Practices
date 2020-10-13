import re
cadena = """Sofía era una niña de apenas 9 años, llena de curiosidad pero muy tímida. Como no tenía padres, vivía junto a otras niñas en un orfanato de Inglaterra. Le gustaba estar sola y no tenía muchos amigos. Un día, o mejor dicho, una noche, algo le llamó la atención. Esa noche Sofía no podía dormir, y se asomó a la ventana. Entonces le vio: era grande, muy grande... era un ¡gigante!

Al principio Sofía tuvo miedo. Pensó que el gigante le haría daño. Pero el gigante le trató desde el principio con dulzura. Resultó ser un gigante bonachón.

El gigante le llevó hasta el mundo en donde vivía. Le enseñó todos los secretos sobre su país y su gente. Por ejemplo, le contó por qué los gigantes tienen esas orejas tan grandes... ¿Quieres saberlo? Chsss.... pero es un secreto: Los gigantes pueden oír gracias a sus enormes orejas... ¡todos los secretos de las personas! Sí, los gigantes oyen sonidos que nadie puede escuchar. Escuchan los pensamientos y son capaces de oír a los corazones hablar.

Los gigantes son capaces de volar, siempre que se toman Gasipum, una bebida especial. Además, corren muy deprisa, gracias a sus larguísimas piernas."""
txtBuscar = "Sofía"
#print(re.search("aprender",cadena))
txtEncontrado = re.search(txtBuscar,cadena)
"""

if re.search(txtBuscar,cadena) is not None:
    print("He encontrado el texto")
else:
    print("no he encontrado el texto")"""
"""
print(txtEncontrado.start())
print(txtEncontrado.end())
print(txtEncontrado.span())"""

print(len(re.findall(txtBuscar,cadena)))