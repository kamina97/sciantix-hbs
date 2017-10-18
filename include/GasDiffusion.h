//////////////////////////////////////////////////
//                                              //
//           S C I A N T I X                    //
//           ---------------                    //
//                                              //
//  Version: 0.1                                //
//  Year   : 2016                               //
//  Authors: D. Pizzocri, T. Barani, A. Magni   //
//                                              //
//////////////////////////////////////////////////

#include <cmath>
#include <vector>
#include "GlobalVariables.h"
#include "Solver.h"
#include "FissionYield.h"
#include "GasDiffusionCoefficient.h"
#include "NucleationRate.h"
#include "ResolutionRate.h"
#include "TrappingRate.h"
#include "TrappingRateAtDislocations.h"
#include "DislocationRadiusOfInfluence.h"
#include "GasDiffusionIrradiation.h"
#include "GasDiffusionAnnealing.h"
#include <iostream>

void GasDiffusion( );
