function p = predict(Theta1, Theta2, X)
%PREDICT Predict the label of an input given a trained neural network
%   p = PREDICT(Theta1, Theta2, X) outputs the predicted label of X given the
%   trained weights of a neural network (Theta1, Theta2)

% Useful values
m = size(X, 1);
num_labels = size(Theta2, 1);

% You need to return the following variables correctly 
p = zeros(size(X, 1), 1);
f = ones(size(X,1),1);
%size(f)
newX=[f X];
%size(Theta1)
%size(newX)
layer=Theta1 * newX';
layer2=sigmoid(layer);
f1 = ones(size(layer2',1),1);
%size(layer2)
newlayer2=[f1 layer2'];
%size(Theta2)
%size(newlayer2)
htheta = Theta2 * newlayer2';
%size(htheta)
sightheta=sigmoid(htheta);
ht=sightheta';
%size(ht)

for i=1:m

[val,in]=max(ht(i,:));
p(i)=in;
if(in == 10)
p(i)=0;
end

%size(p)
% ====================== YOUR CODE HERE ======================
% Instructions: Complete the following code to make predictions using
%               your learned neural network. You should set p to a 
%               vector containing labels between 1 to num_labels.
%
% Hint: The max function might come in useful. In particular, the max
%       function can also return the index of the max element, for more
%       information see 'help max'. If your examples are in rows, then, you
%       can use max(A, [], 2) to obtain the max for each row.
%









% =========================================================================


end
