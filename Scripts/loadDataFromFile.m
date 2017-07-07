function data = loadDataFromFile(filename)
% loadDataFromFile - Load data from HuGaDB text file.
%   filename - path to HuGaDB text file
    data = dlmread(filename,'\t', 4,0);
end