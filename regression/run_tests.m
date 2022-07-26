clear all
close all
clc

tic

%% Regression test [A. Magni, D. Pizzocri]
% This function performs the regression test of the SCIANTIX version 
% placed in this folder (i.e., sciantix.exe, line 16).
% mode_GOLD = 0: execute all the simulations of the database and gives back (for each simulation)
% PASSED if the output file is equal to the output_gold file (in the folders),
% FAILED, otherwise.
% mode_GOLD = 1: replace the output_gold files with the output produced by the current executable file.

% 0 = regression test function
% 1 = gold function
mode_GOLD = 1;

% name of the executable to be tested
exe_name = 'sciantix.exe'; 

% name of the input_settings.txt file, copied and pasted in all the
% subdirectories being tested
input_settings_name = "input_settings.txt";

% add a folder name to add a test
test_list = ["test_Baker1977__1273K", ...
             "test_Baker1977__1373K", ...
             "test_Baker1977__1473K", ...
             "test_Baker1977__1573K", ...
             "test_Baker1977__1673K", ...
             "test_Baker1977__1773K", ...
             "test_Baker1977__1873K", ...
             "test_Baker1977__1973K", ...
             "test_Baker1977__2073K", ...
             "test_White2004_4000-1", ...
             "test_White2004_4000-2", ...
             "test_White2004_4000-3", ...
             "test_White2004_4000-4", ...
             "test_White2004_4000-5", ...
             "test_White2004_4004-1", ...
             "test_White2004_4004-2", ...
             "test_White2004_4004-3", ...
             "test_White2004_4004-4", ...
             "test_White2004_4004-5", ...
             "test_White2004_4004-6", ...
             "test_White2004_4005-1", ...
             "test_White2004_4005-2", ...
             "test_White2004_4005-3", ...
             "test_White2004_4005-4", ...
             "test_White2004_4005-5", ...
             "test_White2004_4064-1", ...
             "test_White2004_4064-2", ...
             "test_White2004_4064-3", ...
             "test_White2004_4064-4", ...
             "test_White2004_4064-5", ...
             "test_White2004_4065-1", ...
             "test_White2004_4065-2", ...
             "test_White2004_4065-3", ...
             "test_White2004_4065-4", ...
             "test_White2004_4065-5", ...
             "test_White2004_4135-1", ...
             "test_White2004_4135-2", ...
             "test_White2004_4135-3", ...
             "test_White2004_4136-1", ...
             "test_White2004_4136-2", ...
             "test_White2004_4136-3", ...
             "test_White2004_4136-4", ...
             "test_White2004_4140-1", ...
             "test_White2004_4140-2", ...
             "test_White2004_4162-1", ...
             "test_White2004_4162-2", ...
             "test_White2004_4162-3", ...
             "test_White2004_4162-4", ...
             "test_White2004_4163-1", ...
             "test_White2004_4163-2", ...
             "test_White2004_4163-3", ...
             "test_White2004_4163-4", ...
             ];


test_num  = length(test_list);

root = strcat(pwd,"\");

for ii = 1 : test_num
   
   test_path = strcat(root, test_list(ii), '\');
        
   copyfile(exe_name, strcat(test_path, exe_name));
   copyfile(input_settings_name, strcat(test_path, input_settings_name));
        
   disp(strcat("Running      ", test_list(ii)));

   cd (test_path)
   [status,result] = system(exe_name);
   
   if(~mode_GOLD)
     gold = importdata('output_gold.txt');
     test = importdata('output.txt');
     % The two output file MUST have the same numbers of colums with the
     % same labelling! Adding a new column, removing one or simply changing
     % the name, provokes the test to FAIL!
     if(isequaln(gold.data, test.data)) 
          fprintf(  "............................PASSED\n");
     else fprintf(2,"............................FAILED\n");
     end

   end

   if(mode_GOLD)
     copyfile("output.txt", "output_gold.txt");
     fprintf(  "..............................GOLD\n");
   end
   
   delete('execution.txt');
   delete('overview.txt');
   delete('input_check.txt');
   delete(exe_name);
   
   cd ..
end

toc


