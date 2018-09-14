import numpy as np
from scipy.special import psi
import time

# start = time.time()

def func(k, mu, T, ux, uxx, uy, uyy, uxy, x, y):
    a0 = (k**2*(-16.0*mu**2 + 4.0*ux + 8.0*uxx*x + 8.0*uy + 8.0*uyy*y)
          + 3.0*k**4.0 - mu**2*(16.0*ux + 32.0*uxx*x + 16.0*uy + 16.0*uyy*y)
          + 16.0*mu**4.0 + 8.0*ux*(uy + uyy*y) + 16.0*uxx*uy*x
          + 16.0*uxx*uyy*x*y - 16.0*uxy**2*x*y + 4.0*uy**2 + 8.0*uy*uyy*y) + 0.j
    a1 = 6.0*k**2 + 4.0*ux + 8.0*uxx*x + 8.0*uy + 8.0*uyy*y + 0.j
    a2 = 3.0+ 0.j
    """b0 = (((k**2 - 4.0*mu**2 + 2.0*uy)*np.heaviside(abs(k**2 - 4.0*mu**2 + 2.0*uy), 0)
           + 0.1*(1 - np.heaviside(abs(k**2 - 4.0*mu**2 + 2.0*uy), 0)))
          * (k**2*(-4.0*mu**2 + 2.0*ux + 4.0*uxx*x + 2.0*uy + 4.0*uyy*y)
             + k**4.0 - mu**2*(8.0*ux + 16.0*uxx*x) + 4.0*ux*(uy + 2.0*uyy*y))) + 0.j"""
    b0 = ((k**2 - 4.0*mu**2 + 2.0*uy)
          * (k**2*(-4.0*mu**2 + 2.0*ux + 4.0*uxx*x + 2.0*uy + 4.0*uyy*y)
             + k**4.0 - mu**2*(8.0*ux + 16.0*uxx*x) + 4.0*ux*(uy + 2.0*uyy*y))) + 0.j
    b1 = (k**2*(4.0*ux + 8.0*uxx*x + 8.0*uy + 8.0*uyy*y) + 3.0*k**4.0
          + mu**2*(16.0*ux + 32.0*uxx*x - 16.0*uy - 16.0*uyy*y) + 16.0*mu**4.0
          + 8.0*ux*(uy + uyy*y) + 16.0*uxx*uy*x + 16.0*uxx*uyy*x*y
          - 16.0*uxy**2*x*y + 4.0*uy**2 + 8.0*uy*uyy*y)+ 0.j
    b2 = 3.0*k**2 + 8.0*mu**2 + 2.0*ux + 4.0*uxx*x + 4.0*uy + 4.0*uyy*y+ 0.j

    aux0=((27.*(b0**2))+((4.*(b1**3.))+((-18.*(b0*(b1*b2)))+(4.*(b0*(b2**3.))))))-((b1**2)*(b2**2));
    aux1=(-2.*((b2**3.)*(T**12.)))+(3.*((np.sqrt(3.))*(np.sqrt((aux0*(T**24.))))));
    aux2=(T**8.)*(((-27.*(b0*(T**12.)))+((9.*(b1*(b2*(T**12.))))+aux1))**-0.333333);
    aux3=((27.*(b0**2))+((4.*(b1**3.))+((-18.*(b0*(b1*b2)))+(4.*(b0*(b2**3.))))))-((b1**2)*(b2**2));
    aux4=(-2.*((b2**3.)*(T**12.)))+(3.*((np.sqrt(3.))*(np.sqrt((aux3*(T**24.))))));
    aux5=(2.**0.666667)*(((-27.*(b0*(T**12.)))+((9.*(b1*(b2*(T**12.))))+aux4))**0.333333);
    aux6=(-2.*(b2*(T**4.)))+((-2.*((2.**0.333333)*(((3.*b1)-(b2**2))*aux2)))+aux5);
    A1=0.0416667*((np.pi**-2.)*((T**-6.)*aux6));

    aux0=(4.*((b1**3.)*(T**24.)))+((-18.*(b0*(b1*(b2*(T**24.)))))+(4.*(b0*((b2**3.)*(T**24.)))));
    aux1=(np.sqrt(3.))*(np.sqrt((((27.*((b0**2)*(T**24.)))+aux0)-((b1**2)*((b2**2)*(T**24.))))));
    aux2=(-27.*(b0*(T**12.)))+((9.*(b1*(b2*(T**12.))))+((-2.*((b2**3.)*(T**12.)))+(3.*aux1)));
    aux3=((768.*(b1*((np.pi**8.)*(T**8.))))+(-256.*((b2**2)*((np.pi**8.)*(T**8.)))))*(aux2**-0.333333);
    aux4=(2.**-0.666667)*((1.+((0.+1.j)*(np.sqrt(3.))))*((np.pi**-10.)*((T**-6.)*aux3)));
    aux5=(4.*((b1**3.)*(T**24.)))+((-18.*(b0*(b1*(b2*(T**24.)))))+(4.*(b0*((b2**3.)*(T**24.)))));
    aux6=(np.sqrt(3.))*(np.sqrt((((27.*((b0**2)*(T**24.)))+aux5)-((b1**2)*((b2**2)*(T**24.))))));
    aux7=(-27.*(b0*(T**12.)))+((9.*(b1*(b2*(T**12.))))+((-2.*((b2**3.)*(T**12.)))+(3.*aux6)));
    aux8=(2.**-0.333333)*((1.+((0.+-1.j)*(np.sqrt(3.))))*((np.pi**-2.)*((T**-6.)*(aux7**0.333333))));
    A2=(-0.0833333*(b2*((np.pi**-2.)*(T**-2.))))+((0.000325521*aux4)+(-0.0416667*aux8));

    aux0=(4.*((b1**3.)*(T**24.)))+((-18.*(b0*(b1*(b2*(T**24.)))))+(4.*(b0*((b2**3.)*(T**24.)))));
    aux1=(np.sqrt(3.))*(np.sqrt((((27.*((b0**2)*(T**24.)))+aux0)-((b1**2)*((b2**2)*(T**24.))))));
    aux2=(-27.*(b0*(T**12.)))+((9.*(b1*(b2*(T**12.))))+((-2.*((b2**3.)*(T**12.)))+(3.*aux1)));
    aux3=((768.*(b1*((np.pi**8.)*(T**8.))))+(-256.*((b2**2)*((np.pi**8.)*(T**8.)))))*(aux2**-0.333333);
    aux4=(2.**-0.666667)*((1.+((0.+-1.j)*(np.sqrt(3.))))*((np.pi**-10.)*((T**-6.)*aux3)));
    aux5=(4.*((b1**3.)*(T**24.)))+((-18.*(b0*(b1*(b2*(T**24.)))))+(4.*(b0*((b2**3.)*(T**24.)))));
    aux6=(np.sqrt(3.))*(np.sqrt((((27.*((b0**2)*(T**24.)))+aux5)-((b1**2)*((b2**2)*(T**24.))))));
    aux7=(-27.*(b0*(T**12.)))+((9.*(b1*(b2*(T**12.))))+((-2.*((b2**3.)*(T**12.)))+(3.*aux6)));
    aux8=(2.**-0.333333)*((1.+((0.+1.j)*(np.sqrt(3.))))*((np.pi**-2.)*((T**-6.)*(aux7**0.333333))));
    A3=(-0.0833333*(b2*((np.pi**-2.)*(T**-2.))))+((0.000325521*aux4)+(-0.0416667*aux8));

    aux0=(a0+(4.*(A1*((np.pi**2)*((T**2)*(a1+(4.*(A1*(a2*((np.pi**2)*(T**2)))))))))))*(psi(((-np.sqrt(A1)))));
    aux1=((A1**-0.5)*aux0)/(b1+(8.*(A1*((np.pi**2)*((T**2)*(b2+(6.*(A1*((np.pi**2)*(T**2))))))))));
    aux2=(a0+(4.*(A2*((np.pi**2)*((T**2)*(a1+(4.*(a2*(A2*((np.pi**2)*(T**2)))))))))))*(psi(((-np.sqrt(A2)))));
    aux3=((A2**-0.5)*aux2)/(b1+(8.*(A2*((np.pi**2)*((T**2)*(b2+(6.*(A2*((np.pi**2)*(T**2))))))))));
    aux4=(a0+(4.*(A3*((np.pi**2)*((T**2)*(a1+(4.*(a2*(A3*((np.pi**2)*(T**2)))))))))))*(psi(((-np.sqrt(A3)))));
    aux5=((A3**-0.5)*aux4)/(b1+(8.*(A3*((np.pi**2)*((T**2)*(b2+(6.*(A3*((np.pi**2)*(T**2))))))))));
    aux6=(a0+(4.*(A3*((np.pi**2)*((T**2)*(a1+(4.*(a2*(A3*((np.pi**2)*(T**2)))))))))))*(psi((np.sqrt(A3))));
    aux7=((A3**-0.5)*aux6)/(b1+(8.*(A3*((np.pi**2)*((T**2)*(b2+(6.*(A3*((np.pi**2)*(T**2))))))))));
    aux8=(a0+(4.*(A2*((np.pi**2)*((T**2)*(a1+(4.*(a2*(A2*((np.pi**2)*(T**2)))))))))))*(psi((np.sqrt(A2))));
    aux9=((A2**-0.5)*aux8)/(b1+(8.*(A2*((np.pi**2)*((T**2)*(b2+(6.*(A2*((np.pi**2)*(T**2))))))))));
    aux10=(a0+(4.*(A1*((np.pi**2)*((T**2)*(a1+(4.*(A1*(a2*((np.pi**2)*(T**2)))))))))))*(psi((np.sqrt(A1))));
    aux11=((A1**-0.5)*aux10)/(b1+(8.*(A1*((np.pi**2)*((T**2)*(b2+(6.*(A1*((np.pi**2)*(T**2))))))))));
    mat_sum=(-0.25*((np.pi**-2.)*((T**-2.)*((((aux1+(aux3+aux5))-aux7)-aux9)-aux11))))-(a0/b0);

    return np.real(mat_sum)

