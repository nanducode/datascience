function [J, grad] = costFunctionReg(theta, X, y, lambda)
%COSTFUNCTIONREG Compute cost and gradient for logistic regression with regularization
%   J = COSTFUNCTIONREG(theta, X, y, lambda) computes the cost of using
%   theta as the parameter for regularized logistic regression and the
%   gradient of the cost w.r.t. to the parameters. 

% Initialize some useful values
m = length(y); % number of training examples

% You need to return the following variables correctly 
J = 0;
lambda
grad = zeros(size(theta));
t=theta';
xt=X';
pre=t*xt;
prediction=pre';
%HERE COMPUTER Htheta
g=sigmoid(prediction);
minusy=-1 .* y;
logprediction=log(g);
firstterm=minusy .* logprediction;
oneminusy= 1 .- y;
oneminuspred= 1 .- g;
logoneminuspred=log(oneminuspred);
secondterm=oneminusy .* logoneminuspred;
j1=firstterm - secondterm;
j2=cumsum(j1);
%Till here its the same This is the first term
j3=j2(m)/m;
thetasquare=theta;
theta
thetasquare=theta .^ 2;
features=size(X,2);
thetasquare(1)=0;
reg1=cumsum(thetasquare);
reg2=lambda*reg1(features);
%reg2
reg3=reg2/(2*m);
reg3
j3
J=j3+reg3;
J
%j
%
%
gminusy=g .- y;
S=y;
for i=1:features,
S=gminusy .* X(:,i);
S2=cumsum(S);
grad(i)=S2(m)/m;
if(i>1)
{
fprintf("Hello fe %d\n",i);
grad(i)=grad(i)+((lambda/m)*theta(i));
}
endif
end; 

grad
% ====================== YOUR CODE HERE ======================
% Instructions: Compute the cost of a particular choice of theta.
%               You should set J to the cost.
%               Compute the partial derivatives and set grad to the partial
%               derivatives of the cost w.r.t. each parameter in theta






% =============================================================

end
