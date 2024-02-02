a=20; J=1023; x=(0:a/J:a)'; u0=1./(1+exp(-(2-x)/sqrt(2)));
ell=1; N=1023; T=1; epsilon=1; sigma=1;

tot=zeros(1024,1024,600);

for i=1:600
    disp(i)
    [t,ut]=spde_fd_n_exp(u0,T,a,N,J,epsilon,sigma,ell,@(u)u.*(1-u).*(u+0.5));
    tot(:,:,i)=ut;
end

save("variables.mat","t","x","tot",'-v7.3')
