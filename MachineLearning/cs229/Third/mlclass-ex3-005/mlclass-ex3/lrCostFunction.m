function [J, grad] = lrCostFunction(theta, X, y, lambda)
%LRCOSTFUNCTION Compute cost and gradient for logistic regression with 
%regularization
%   J = LRCOSTFUNCTION(theta, X, y, lambda) computes the cost of using
%   theta as the parameter for regularized logistic regression and the
%   gradient of the cost w.r.t. to the parameters. 

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
% Hint: The computation of the cost function and gradients can be
%       efficiently vectorized. For example, consider the computation
%
%           sigmoid(X * theta)
%
%       Each row of the resulting matrix will contain the value of the
%       prediction for that example. You can make use of this to vectorize
%       the cost function and gradient computations. 
%
% Hint: When computing the gradient of the regularized cost function, 
%       there're many possible vectorized solutions, but one solution
%       looks like:
%           grad = (unregularized gradient for logistic regression)
%           temp = theta; 
%           temp(1) = 0;   % because we don't add anything for j = 0  
%           grad = grad + YOUR_CODE_HERE (using the temp variable)
%










% =============================================================
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
%theta
thetasquare=theta .^ 2;
features=size(X,2);
thetasquare(1)=0;
reg1=cumsum(thetasquare);
reg2=lambda*reg1(features);
%reg2
reg3=reg2/(2*m);
%reg3
%j3
J=j3+reg3;
%J
%j
%
%
gminusy=g .- y;
S=y;
%gminusy

xtranspose=X';
S=X' * gminusy;
Stemp=(1/m) .* S;

thetatemp=theta;
thetatemp(1)=0;
thetatemplambda=(lambda/m) .* thetatemp;

grad=Stemp .+ thetatemplambda;
%grad

grad = grad(:);

%grad
end
