//<FLAGS>
//#define __GPU
//#define __NOPROTO
//<\FLAGS>

//<INCLUDES>
#include "fargo3d.h"
//<\INCLUDES>

void UpdateVwind_cpu (real dt) {

//<USER_DEFINED>
#ifdef Y
  INPUT(Vx_temp);
  OUTPUT(Vx_temp);
#endif
//<\USER_DEFINED>

//<EXTERNAL>
    real radius;
    real epsilon;

 #ifdef Y
  real* vx_temp  = Vx_temp -> field_cpu;
  real* cs = Energy->field_cpu;

#endif
  int pitch  = Pitch_cpu;
  int stride = Stride_cpu;
  int size_x = Nx+2*NGHX;
  int size_y = Ny+2*NGHY;
  int size_z = Nz+2*NGHZ;
//<\EXTERNAL>

//<INTERNAL>
  int i; //Variables reserved
  int j; //for the topology
  int k; //of the kernels
  int ll;
  int llym;
//<\INTERNAL>

//<CONSTANT>
// real ALPHADW(1);
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
#ifdef Y
        ll = l;
        llym = lym;
        radius = Ymed(j);
	vx_temp[ll] -= dt*(3.0/4.0)*(ALPHADW*pow(cs[ll],2))/radius;

#endif
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



