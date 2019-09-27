function [J, grad] = costFunction(theta, X, y)
%COSTFUNCTION Compute cost and gradient for logistic regression
%   J = COSTFUNCTION(theta, X, y) computes the cost of using theta as the
%   parameter for logistic regression and the gradient of the cost
%   w.r.t. to the parameters.

% Initialize some useful values
m = length(y); % number of training examples

% You need to return the following variables correctly 
J = 0;
grad = zeros(size(theta));

% ====================== YOUR CODE HERE ======================
% Instructions: Compute the cost of a particular choice of theta.
%               You should set J to the cost.
%               Compute the partial derivatives and set grad to the partial
%               derivatives of the cost w.r.t. each parameter in theta
%
% Note: grad should have the same dimensions as theta
%

t=theta';
xt=X';
%xt
%t
pre=t*xt;
%pre
prediction=pre';
g=sigmoid(prediction);
%g
minusy=-1 .* y;
%minusy
%size(y)
%size(minusy)
%size(prediction)
logprediction=log(g);
%size(logprediction)
%logprediction
firstterm=minusy .* logprediction;
%firstterm
oneminusy= 1 .- y;
oneminuspred= 1 .- g;
logoneminuspred=log(oneminuspred);
secondterm=oneminusy .* logoneminuspred;
%secondterm
j1=firstterm - secondterm;
%secondterm
j2=cumsum(j1);
J=j2(m)/m;
%j
%
%
gminusy=g .- y;
features=size(X,2);
S=y;
for i=1:features
S=gminusy .* X(:,i);
S2=cumsum(S);
grad(i)=S2(m)/m;
end; 







% =============================================================

end
