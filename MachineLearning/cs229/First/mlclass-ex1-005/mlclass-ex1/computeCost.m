function J = computeCost(X, y, theta)
%COMPUTECOST Compute cost for linear regression
%   J = COMPUTECOST(X, y, theta) computes the cost of using theta as the
%   parameter for linear regression to fit the data points in X and y

% Initialize some useful values
m = length(y); % number of training examples

% You need to return the following variables correctly 


J = 0;
t=theta';
xv=X';
h=t*xv;
htheta=h';
E=htheta-y;
E1=E .^ 2;
val=sum(E1);
J=(1/(2*m))*((val));
%%WORKING
%E=0;
%t=theta';
%h=0;
%for i=1:m,
%xv=X(i,:);
%h=t*xv';
%E=E+((h-y(i))^2);

%end;
%E=(E/2)*(1/m);
%E
%%WORKING
% ====================== YOUR CODE HERE ======================
% Instructions: Compute the cost of a particular choice of theta
%               You should set J to the cost.





% =========================================================================

end
