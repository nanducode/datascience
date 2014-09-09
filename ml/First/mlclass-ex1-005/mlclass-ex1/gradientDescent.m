function [theta, J_history] = gradientDescent(X, y, theta, alpha, num_iters)
%GRADIENTDESCENT Performs gradient descent to learn theta
%   theta = GRADIENTDESENT(X, y, theta, alpha, num_iters) updates theta by 
%   taking num_iters gradient steps with learning rate alpha

% Initialize some useful values
m = length(y); % number of training examples
J_history = zeros(num_iters, 1);

for iter = 1:num_iters

%S=ones(m,1);
%for i=1:m
%t=theta';
%xv=X(i,:);
t=theta';
xv=X';
h=t*xv;
htheta=h';
E=htheta-y;
E2=[E E];
S=E2 .* X;
S=(alpha/m) .* S;
%S
S2=cumsum(S);
%S2
S3=S2(m,:);
%S3
theta=theta - S3';
%theta

%val=(t * xv') - y(i));


%end;

    % ====================== YOUR CODE HERE ======================
    % Instructions: Perform a single gradient step on the parameter vector
    %               theta. 
    %
    % Hint: While debugging, it can be useful to print out the values
    %       of the cost function (computeCost) and gradient here.
    %







    % ============================================================

    % Save the cost J in every iteration    
    J_history(iter) = computeCost(X, y, theta);

end

end