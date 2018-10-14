function [mu sigma2] = estimateGaussian(X)
%ESTIMATEGAUSSIAN This function estimates the parameters of a 
%Gaussian distribution using the data in X
%   [mu sigma2] = estimateGaussian(X), 
%   The input X is the dataset with each n-dimensional data point in one row
%   The output is an n-dimensional vector mu, the mean of the data set
%   and the variances sigma^2, an n x 1 vector
% 

% Useful variables
[m, n] = size(X);
m
n
% You should return these values correctly
mu = zeros(n, 1);
sigma2 = zeros(n, 1);

% ====================== YOUR CODE HERE ======================
% Instructions: Compute the mean of the data and the variances
%               In particular, mu(i) should contain the mean of
%               the data for the i-th feature and sigma2(i)
%               should contain variance of the i-th feature.
%

for feature=1:n
x1=X(:,feature);
%size(x1)
x2=cumsum(x1);
%size(x2)
%x2(m)
mu(feature,:)=(1/m) * x2(m,1);
meanv=mu(feature,:)
s=(x1 .- meanv);
s1=s .^ 2;

s2=cumsum(s1);
%s2(m)
sigma2(feature,1)=s2(m)/m;
end
%mu
%sigma2







% =============================================================


end
