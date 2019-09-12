s(M) --> nombre(N1), verbo(N1,N2,M), prep(P), nombre(N2).

nombre(adan) --> [adan].
nombre(eva) --> [eva].

verbo(N1,N2,ama(N1,N2)) --> [ama].

prep(a) --> [a].

ama(adan, eva).

llamaPredicado(X):- s(Logica,X,[]), call(Logica).
