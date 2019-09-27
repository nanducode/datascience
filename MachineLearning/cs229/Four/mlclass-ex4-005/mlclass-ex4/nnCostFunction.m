function [J grad] = nnCostFunction(nn_params, ...
                                   input_layer_size, ...
                                   hidden_layer_size, ...
                                   num_labels, ...
                                   X, y, lambda)
%NNCOSTFUNCTION Implements the neural network cost function for a two layer
%neural network which performs classification
%   [J grad] = NNCOSTFUNCTON(nn_params, hidden_layer_size, num_labels, ...
%   X, y, lambda) computes the cost and gradient of the neural network. The
%   parameters for the neural network are "unrolled" into the vector
%   nn_params and need to be converted back into the weight matrices. 
% 
%   The returned parameter grad should be a "unrolled" vector of the
%   partial derivatives of the neural network.
%

% Reshape nn_params back into the parameters Theta1 and Theta2, the weight matrices
% for our 2 layer neural network
Theta1 = reshape(nn_params(1:hidden_layer_size * (input_layer_size + 1)), ...
                 hidden_layer_size, (input_layer_size + 1));

Theta2 = reshape(nn_params((1 + (hidden_layer_size * (input_layer_size + 1))):end), ...
                 num_labels, (hidden_layer_size + 1));

% Setup some useful variables
m = size(X, 1);
         
% You need to return the following variables correctly 
J = 0;
Theta1_grad = zeros(size(Theta1));
Theta2_grad = zeros(size(Theta2));

% ====================== YOUR CODE HERE ======================
% Instructions: You should complete the code by working through the
%               following parts.
%
% Part 1: Feedforward the neural network and return the cost in the
%         variable J. After implementing Part 1, you can verify that your
%         cost function computation is correct by verifying the cost
%         computed in ex4.m
%

%Part 1 a. Implement htheta
num_labels = size(Theta2, 1);

p = zeros(size(X, 1), 1);
%p
f = ones(size(X,1),1);
newX=[f X];
layer=Theta1 * newX';
layer2=sigmoid(layer);
f1 = ones(size(layer2',1),1);
newlayer2=[f1 layer2'];
htheta = Theta2 * newlayer2';
sightheta=sigmoid(htheta);
ht=sightheta';
%size(ht)
%size(y)
%ht
total=0;
for labels=1:num_labels
%term1
newY=(y==labels);
%size(newY)
minusnewY = -1 .* newY;
lht=ht(:,labels);

loghtheta = log(lht);
firstterm=minusnewY .* loghtheta;
%term2
oneminusnewY= 1 .+ minusnewY;
oneminushtheta= 1 .- lht;
logoneminushtheta=log(oneminushtheta);
secondterm= oneminusnewY .* logoneminushtheta;
final=firstterm .- secondterm;
f=cumsum(final);
 
%size(f)
total=total+f(m);
%total

end
t=total/m
J=t;

Theta1Square=Theta1 .^ 2;
temp=zeros(size(Theta1,1),1);
Theta1Square(:,1)=temp;
Theta1Sum=cumsum(Theta1Square);
Theta1Sum1=Theta1Sum(size(Theta1,1),:);
Theta1Sum2=cumsum(Theta1Sum1);
firstrr=lambda*((Theta1Sum2(size(Theta1,2)))/m);

Theta2Square=Theta2 .^ 2;
temp=zeros(size(Theta2,1),1);
Theta2Square(:,1)=temp;
Theta2Sum=cumsum(Theta2Square);
Theta2Sum1=Theta2Sum(size(Theta2,1),:);
Theta2Sum2=cumsum(Theta2Sum1);
secondrr=lambda*((Theta2Sum2(size(Theta2,2)))/m);

J=J+((firstrr+secondrr)/2);



% Part 2: Implement the backpropagation algorithm to compute the gradients
%         Theta1_grad and Theta2_grad. You should return the partial derivatives of
%         the cost function with respect to Theta1 and Theta2 in Theta1_grad and
%         Theta2_grad, respectively. After implementing Part 2, you can check
%         that your implementation is correct by running checkNNGradients
%
%size(Theta2_grad)
%size(Theta1_grad)
tr3=zeros(size(Theta2_grad));
tr2=zeros(size(Theta1_grad));
%m
for t=1:m
Xt=X(t,:);
f = ones(size(Xt,1),1);
newX=[f Xt];
%size(newX)

layer=Theta1 * newX';
layer2=sigmoid(layer);
f1 = ones(size(layer2',1),1);
newlayer2=[f1 layer2'];
htheta = Theta2 * newlayer2';
sightheta=sigmoid(htheta);
ht=sightheta';
%size(ht)
newY=zeros(size(ht));
%newY
newY(y(t,:))=1;
%newY

%size(ht')
%size(newY')
%t
delta3=ht' .- newY';
%size(delta3)
%size(newlayer2')
%size(layer)
%size(Theta2)

delta2=(Theta2' * delta3) .* [0;sigmoidGradient(layer)];
%delta2
delta2=delta2(2:end);
%delta2
%size(delta2)

tr3=tr3 .+ (delta3 * (newlayer2));
%size(tr3)
%size(newX)
tr2=tr2 .+ (delta2 * (newX));
%size(tr2)
end
Theta1Reg=Theta1(:,2:end);
Theta2Reg=Theta2(:,2:end);
size(Theta1Reg)
size(Theta2Reg)
%size(tr2)
%size(tr3)
t1=zeros(size(Theta1Reg,1),1);
t2=zeros(size(Theta2Reg,1),1);
Theta1Reg1=[t1 Theta1Reg];
Theta2Reg1=[t2 Theta2Reg];
Theta1Reg2= lambda .* Theta1Reg1;
Theta2Reg2= lambda .* Theta2Reg1;
size(tr2)
size(Theta1Reg2)
tr2 = tr2 + Theta1Reg2;
tr3 = tr3 + Theta2Reg2;
Theta1_grad = (1/m) .* tr2;
Theta2_grad = (1/m) .* tr3;
%size(Theta1_grad)
%Theta1_grad(:)
%Theta2_grad(:)




%         Note: The vector y passed into the function is a vector of labels
%               containing values from 1..K. You need to map this vector into a 
%               binary vector of 1's and 0's to be used with the neural network
%               cost function.
%
%         Hint: We recommend implementing backpropagation using a for-loop
%               over the training examples if you are implementing it for the 
%               first time.
%
% Part 3: Implement regularization with the cost function and gradients.
%
%         Hint: You can implement this around the code for
%               backpropagation. That is, you can compute the gradients for
%               the regularization separately and then add them to Theta1_grad
%               and Theta2_grad from Part 2.
%



















% -------------------------------------------------------------

% =========================================================================

% Unroll gradients
grad = [Theta1_grad(:) ; Theta2_grad(:)];


end
