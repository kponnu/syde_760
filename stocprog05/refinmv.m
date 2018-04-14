%Refiner slp for a small illustrative problem
function[f, g] = refinery(x)
crude = x(1);
pg = x(2);
%f = 0.0341 * crude + 0.19 * pg; %original
f = 3.41 * crude + 19 * pg; %original * 100

%f = -f; %for maximization

g(1) = crude - 100;
g(2) = -pg + 10;
g(3) = -0.27 * crude + pg + 10;
g(4) = -f + 600;

%for markovitz, minimize variance
varcrude = 1;
varpg = 9;
f = varcrude * crude^2 + varpg * pg^2;