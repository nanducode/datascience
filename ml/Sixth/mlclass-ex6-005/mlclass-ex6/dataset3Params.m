function [C, sigma] = dataset3Params(X, y, Xval, yval)
%EX6PARAMS returns your choice of C and sigma for Part 3 of the exercise
%where you select the optimal (C, sigma) learning parameters to use for SVM
%with RBF kernel
%   [C, sigma] = EX6PARAMS(X, y, Xval, yval) returns your choice of C and 
%   sigma. You should complete this function to return the optimal C and 
%   sigma based on a cross-validation set.
%

% You need to return the following variables correctly.
C = 1;
sigma = 0.3;
minval=100000;
values=[0 0.001 0.003 0.01 0.03 0.1 0.3 1 3 10];
values_length=length(values);
errorc=zeros(values_length ^2,1);
count=1;
for i=1:values_length
for j=1:values_length
model=svmTrain(X,y,values(i),@(x1,x2) gaussianKernel(x1,x2,values(j)));
predictions=svmPredict(model,Xval);
errorp=mean(double(predictions ~= yval));
errorc(count)=errorp;
if(errorp < minval )
fprintf('new values\n');
errorp
minval
C=values(i);
sigma=values(j);
C
sigma
minval=errorp;
end
count=count+1;
end
end
C
sigma
errorc
% ====================== YOUR CODE HERE ======================
% Instructions: Fill in this function to return the optimal C and sigma
%               learning parameters found using the cross validation set.
%               You can use svmPredict to predict the labels on the cross
%               validation set. For example, 
%                   predictions = svmPredict(model, Xval);
%               will return the predictions on the cross validation set.
%
%  Note: You can compute the prediction error using 
%        mean(double(predictions ~= yval))
%







% =========================================================================

end
