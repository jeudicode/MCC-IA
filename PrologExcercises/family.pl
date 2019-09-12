casado(mauricio,maria).
casado(javier,mireya).
casado(maria,mauricio).
casado(mireya,javier).

padre(saul,mauricio).
padre(fabian,mauricio).
padre(wendy,mauricio).
padre(laura,mauricio).

padre(mauricio,felipe).
padre(carlos,felipe).
padre(maria,narciso).
padre(mireya,narciso).

padre(li,javier).
padre(aiko,javier).
padre(saito,javier).
padre(natzuko,javier).
padre(hiroito,javier).

madre(saul,maria).
madre(fabian,maria).
madre(wendy,maria).
madre(laura,maria).

madre(mauricio,lidia).
madre(carlos,lidia).
madre(maria,teresa).
madre(mireya,teresa).

madre(li,mireya).
madre(aiko,mireya).
madre(saito,mireya).
madre(natzuko,mireya).
madre(hiroito,mireya).

hermano(X,Y):- padre(X,Z),padre(Y,Z).
hermano(X,Y):- madre(X,Z),madre(Y,Z).

primo(X,Y):- padre(X,Z),padre(Y,W),hermano(Z,W).
primo(X,Y):- madre(X,Z),madre(Y,W),hermano(Z,W).

tiosangre(X,Y):- padre(X,Z),hermano(Z,Y).
tiosangre(X,Y):- madre(X,Z),hermano(Z,Y).
tiopolitico(X,Y):- casado(Z,Y),tiosangre(X,Z).
tio(X,Y):- tiopolitico(X,Y).
tio(X,Y):- tiosangre(X,Y).