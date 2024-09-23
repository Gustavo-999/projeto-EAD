import string as st
import numpy as np

letras = st.ascii_letters
numeros = st.digits
especial = st.punctuation
algarismos = (letras+numeros+especial)
senha = np.random.choice(list(algarismos),10)
print(''.join(senha))