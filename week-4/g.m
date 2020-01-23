% x = [theta1,theta1_dot]
A= [0,1;0,0]
eig(A)
B = [0;1]
cm = ctrb(A,B)
rank(cm)

'----------------'
% find characteristic equation
syms x k1 k2
A = sym([0,1;-k1,-k2])
polyA = charpoly(A,x)

