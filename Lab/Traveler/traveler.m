


v = [1, 0, 0, 0];
vp = [1/sqrt(2), -1/sqrt(2)];
v = v * hadamard(2);
v(2) = -1;

x = [0, 1; 1, 0];
z = [-1, 0; 0, 1];
Us = 2 * [1, 0; 0, 0] - eye(2);
disp(Us);
disp(hadamard(1) * z * hadamard(1));
cz = [1, 0, 0, 0; 0, -1, 0, 0; 0, 0, -1, 0; 0, 0, 0, -1];
disp(vp * hadamard(1) * z * hadamard(1));

function result = Uf(v)
    result = zeros(8);
    result(1,5) = 1;
    result(5, 5) = 1;
    result(9, 10) = 1;
    result(13, 16) = 1;
    result = result / 2;
    result = v*result;
end
    
function h = hadamard(n)
    gate = 1/sqrt(2) * [1, 1; 1, -1];
    h = gate;
    for i = 1:n-1
        h = kron(h,gate);
    end
    
end