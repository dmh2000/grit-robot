A = [2,0;1,-1];
B = [1;1];
%p = [-0.1+1i,-0.1-1i];
%p = [-0.5+1i,-0.5-1i];
%p=[-.5,-1];
p = [-5,-4]
K=place(A,B,p);
x=[1;1];
t=0;
tf=5.0;
dt=0.01;
X=[];
T=[];
while(t<tf);
    X=[X,x];
    T=[T,t];
    x=x+dt.*(A-B*K)*x;
    t=t+dt;
end;

hold on
plot(T,X(1,:));