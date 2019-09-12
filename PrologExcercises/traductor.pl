parserEspanol(M) --> nombreEspanol(N1), verboEspanol(N1,N2,M), prepEspanol(P), nombreEspanol(N2).

nombreEspanol(charles) --> [carlos].
nombreEspanol(maire) --> [maria].

verboEspanol(N1,N2,calls(N1,N2)) --> [llama].

prepEspanol(a) --> [a].

parserIngles(M) --> nombreIngles(N1), verboIngles(N1,N2,M), nombreIngles(N2).

nombreIngles(charles) --> [charles].
nombreIngles(maire) --> [maire].

verboIngles(N1,N2,calls(N1,N2)) --> [calls].

traduceESPaENG(X,OracionTraducida):- parserEspanol(Logica,X,[]), parserIngles(Logica,OracionTraducida,[]).
%% traduceESPaENG([carlos, llama, a, maria], OracionTraducida).