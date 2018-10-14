function [J, grad] = linearRegCostFunction(X, y, theta, lambda)
%LINEARREGCOSTFUNCTION Compute cost and gradient for regularized linear 
%regression with multiple variables
%   [J, grad] = LINEARREGCOSTFUNCTION(X, y, theta, lambda) computes the 
%   cost of using theta as the parameter for linear regression to fit the 
%   data points in X and y. Returns the cost in J and the gradient in grad

% Initialize some useful values
m = length(y); % number of training examples

% You need to return the following variables correctly 
J = 0;
grad = zeros(size(theta));
t=theta';
xv=X';
h=t*xv;
htheta=h';
E=htheta-y;
E1=E .^ 2;
val=sum(E1);
t=theta;
%t
t(1)=0;
tsquare=t .^ 2;
%tsquare
%size(theta)
tcumsum=cumsum(tsquare);
%tcumsum
regval=tcumsum(size(theta,1));
%regval
reg=(lambda/(2*m))*regval;
J=((1/(2*m))*((val)))+reg;
%J
reg2=lambda .* t;
%size(E)
%size(X)
%size(reg2)
Xt=X';

E2=(Xt * E) ;
E4=E2 .+ reg2;
grad=(1/m) .* E4;

% ====================== YOUR CODE HERE ======================
% Instructions: Compute the cost and gradient of regularized linear 
%               regression for a particular choice of theta.
%
%               You should set J to the cost and grad to the gradient.
%












% =========================================================================

grad = grad(:);

end
