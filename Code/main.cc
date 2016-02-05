/*
   This file is part of the Mandelbox program developed for the course
    CS/SE  Distributed Computer Systems taught by N. Nedialkov in the
    Winter of 2015 at McMaster University.

    Copyright (C) 2015 T. Gwosdz and N. Nedialkov

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
*/
#include <stdlib.h>
#include <stdio.h>
#include "camera.h"
#include "renderer.h"
#include "mandelbox.h"
#include "mpi.h"
#include <sys/time.h>
#include <iostream>


void getParameters(char *filename, CameraParams *camera_params, RenderParams *renderer_params,
		   MandelBoxParams *mandelBox_paramsP);
void init3D       (CameraParams *camera_params, const RenderParams *renderer_params);
void renderFractal(const CameraParams &camera_params, const RenderParams &renderer_params, unsigned char* image, int p, int my_rank);
void saveBMP      (const char* filename, const unsigned char* image, int width, int height);

MandelBoxParams mandelBox_params;

int main(int argc, char** argv)
{
  struct timeval t0;
  struct timeval t1;
  CameraParams    camera_params;
  RenderParams    renderer_params;
  int my_rank, p;
  gettimeofday(&t0,0);
  
   /* Start up MPI */
  MPI_Init(&argc, &argv);

  /* Find out process rank  */
  MPI_Comm_rank(MPI_COMM_WORLD, &my_rank);

  /* Find out number of processes */
  MPI_Comm_size(MPI_COMM_WORLD, &p);
  
 
  getParameters(argv[1], &camera_params, &renderer_params, &mandelBox_params);
  
  int image_size = renderer_params.width * renderer_params.height;
  /* temporary image that has sections created by each processor */
  unsigned char *image = (unsigned char*)malloc(3*image_size*sizeof(unsigned char));
  /* Image that will be output */
  unsigned char *lastimage = (unsigned char*)calloc(3*image_size*sizeof(unsigned char),sizeof(unsigned char));
      
  init3D(&camera_params, &renderer_params);
   
  renderFractal(camera_params, renderer_params, image, p, my_rank);
  /* adds all the images to last image */
  MPI_Reduce(image, lastimage, 3*image_size*sizeof(unsigned char), MPI_UNSIGNED_CHAR,MPI_SUM,0, MPI_COMM_WORLD);
  
  if (my_rank == 0){
    saveBMP(renderer_params.file_name, lastimage, renderer_params.width, renderer_params.height);
    
    free(image);
    gettimeofday(&t1,0);
    double elapsed = (double)((t1.tv_sec-t0.tv_sec)*1000000LL + t1.tv_usec-t0.tv_usec)/(double)(1e6);
    FILE *outFile = fopen("stats.txt", "a");
    fprintf(outFile, "%s %f %s\n", renderer_params.file_name, elapsed, "seconds.");
    fclose(outFile);
  }


  MPI_Finalize();
  return 0;
}
