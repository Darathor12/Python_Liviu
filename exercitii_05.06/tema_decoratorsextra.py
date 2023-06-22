"""
Implementați o clasă User, cu următoarele cerințe:
– constructorul va primi nume, email, parola, și data nașterii
– o metoda login, care va primi email și parola ca parametrii; dacă acestea sunt corecte, userul va fi marcat ca logat
– o metoda get_info, care va returna toate informațiile despre user DOAR DACĂ acesta este logat, folosind un decorator `@require_login`
– o metoda logout, fara params, care delogheaza userul.


Se va testa apelarea metodei get_info inainte de logare, dupa logare, dupa delogare, și după încă o logare.

"""