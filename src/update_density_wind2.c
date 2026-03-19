//<FLAGS>
//#define __GPU
//#define __NOPROTO
//<\FLAGS>

//<INCLUDES>
#include "fargo3d.h"    
//<\INCLUDES>

void UpdateDensityWind2_cpu(real dt,Field *DENSITY) {

//<USER_DEFINED>
  INPUT(DENSITY);
  OUTPUT(DENSITY);
//<\USER_DEFINED>

//<EXTERNAL>
  real* dens = DENSITY->field_cpu;
  real* cs = Energy->field_cpu;
  real radius;
  real omega;
  int size_x = Nx+2*NGHX;
  int size_y = Ny+2*NGHY-1;
  int size_z = Nz+2*NGHZ;
//<\EXTERNAL>

//<INTERNAL>
  int i;
  int j; 
  int k; 
  int ll;
  int llyp;
//<\INTERNAL>

//<CONSTANT>
// real ALPHADW(1); 
// real LAMBDA(1);
//<\CONSTANT>
 
//<MAIN_LOOP>

  i = j = k = 0;

#ifdef Z  
  for (k=0; k<size_z; k++) {
#endif
#ifdef Y
    for (j=0; j<size_y; j++) {
#endif
#ifdef X
      for (i=0; i<size_x; i++) {
#endif
//<#>
     	ll = l;
        llyp = lyp;
  radius = ymed(j);
  omega = sqrt(1/ (radius*radius*radius));
 
dens[ll] += dt*(-3.0/4.0)*(ALPHADW*dens[ll]*pow(cs[ll], 2.0))/((LAMBDA-1.0)*radius*radius*omega);
//<\#>
#ifdef X
      }
#endif
#ifdef Y
    }
#endif
#ifdef Z
  }
#endif
//<\MAIN_LOOP>
}

