classdef ClassName
    properties
        Property1
    end

    methods
        function obj = ClassName(inputArg1)
            obj.Property1 = inputArg1^2;
            disp(obj.Property1);
            
        end
    end
end
%&
p = [1 2 -5]
g = [2 0 5 0 - 0]
Rp = roots(p)

&%