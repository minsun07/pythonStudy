#복소수
a = 8+24j  # j=복소수i
print(a)  #(8+24j)
print(type(a))  #<class 'complex'>
print(a.real)  #실수부분
print(a.imag)  #허수부분
print(a.conjugate())  #켤레복소수
d = 1j
print(d)    # (0)+1j
print(d.conjugate()) #(0)-1j
print(d*d.conjugate())  #(1+0j)
