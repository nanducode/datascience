function [theta, J_history] = gradientDescentMulti(X, y, theta, alpha, num_iters)
%GRADIENTDESCENTMULTI Performs gradient descent to learn theta
%   theta = GRADIENTDESCENTMULTI(x, y, theta, alpha, num_iters) updates theta by
%   taking num_iters gradient steps with learning rate alpha

% Initialize some useful values
m = length(y); % number of training examples
J_history = zeros(num_iters, 1);
features=size(X,2);
for iter = 1:num_iters
t=theta';
xv=X';
h=t*xv;
htheta=h';
E=htheta-y;
%E2=[E E];
S=X;
for f=1:features,
S(:,f)=E .* X(:,f);
end
S=(alpha/m) .* S;
%S
S2=cumsum(S);
%S2
S3=S2(m,:);
%S3
theta=theta - S3';

    % ====================== YOUR CODE HERE ======================
    % Instructions: Perform a single gradient step on the parameter vector
    %               theta. 
    %
    % Hint: While debugging, it can be useful to print out the values
    %       of the cost function (computeCostMulti) and gradient here.
    %











    % ============================================================

    % Save the cost J in every iteration    
    J_history(iter) = computeCostMulti(X, y, theta);

end

end
