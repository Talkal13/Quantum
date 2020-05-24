syms a b

pretty(R_x(pi/2).*[a,b])
disp([1,0]*R_x(pi/2)*R_z(pi/2))


function r = R_x(o)
   r = [complex(cos(o/2), 0), complex(0, -sin(o/2)); complex(0, -sin(o/2)), complex(cos(o/2), 0)];
end

function r = R_z(o)
    r = [exp(complex(0, -o/2)), 0; 0, exp(complex(0, -o/2))];
end
