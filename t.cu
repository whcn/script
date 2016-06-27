#include "opencv2/imgcodecs.hpp"
#include "opencv2/highgui.hpp"
#include "opencv2/imgproc.hpp"
#include "opencv2/core/utility.hpp"
#include "opencv2/highgui/highgui_c.h"

#include <cuda_runtime.h>
/* #include <thrust/count.h> */ 
/* #include <thrust/device_vector.h> */ 

#include <iostream>
#include <tuple> 

using namespace std;
using namespace cv;

#define WIDTH 3

struct pixel {
	/* pixel(){} */
	/* pixel(int red, int green, int blue): r(red), g(green), b(blue){} */
	int r;
	int g;
	int b;
};


__global__ void infaint( int *r, int *g, int *b, int rows, int cols, int *ret ) {

	int offsetX = blockDim.x * blockIdx.x + threadIdx.x;
	int offsetY = blockDim.y * blockIdx.y + threadIdx.y;
	int tid = offsetY * cols + offsetX;

	int tmp[10][10];
	for (int i = 0; i < 10; ++i) {
		for (int j = 0; j < 10; ++j) {
			tmp[i][j] = -2;
		} 
		 
	} 
	int counts[WIDTH * 3 + 1][WIDTH * 3 + 1] = {0};


	for (int i = 0; i < rows; ++i) {
		for (int j = 0; j < cols; ++j) {

			r[i * cols + j] = counts[i][j]+1;
		} 
		 
	} 

}

int main(int argc, char** argv )
{

	int rows = 10;
	int cols = 10;

	int *h_r, *h_g, *h_b;
    int *dev_r, *dev_g, *dev_b;

	int *h_ret;
	int *dev_ret;

    // allocate the memory on the CPU
	h_r = (int*)malloc(rows * cols * sizeof(int));
	h_g = (int*)malloc(rows * cols * sizeof(int));
	h_b = (int*)malloc(rows * cols * sizeof(int));
	h_ret = (int*)malloc(rows * cols * sizeof(int));

	// split Mat into rgb array
	for (int i = 0; i < rows; ++i) {
		for (int j = 0; j < cols; ++j) {
			h_r[i * cols + j] = 1;
			h_g[i * cols + j] = 1;
			h_b[i * cols + j] = 1;

			h_ret[i * cols + j] = -1;
			/* cout << h_r[i * cols + j] << ' ' << h_g[i * cols + j] << ' ' << h_b[i * cols + j] << endl; */
		}  
	} 

	for (int i = 0; i < rows; ++i) {
		for (int j = 0; j < cols; ++j) {
			cout << h_r[i * cols + j] << ' ';
		}
		cout << endl;
	}

    // allocate the memory on the GPU
	cudaError_t t;
    t = cudaMalloc( (void**)&dev_r, rows * cols * sizeof(int) );
    t = cudaMalloc( (void**)&dev_g, rows * cols * sizeof(int) );
    t = cudaMalloc( (void**)&dev_b, rows * cols * sizeof(int) );

    t = cudaMalloc( (void**)&dev_ret, rows * cols * sizeof(int) );

    // copy the host memory to device memory
    t = cudaMemcpy( dev_r, h_r, rows * cols * sizeof(int), cudaMemcpyHostToDevice );
    t = cudaMemcpy( dev_g, h_g, rows * cols * sizeof(int), cudaMemcpyHostToDevice );
    t = cudaMemcpy( dev_b, h_b, rows * cols * sizeof(int), cudaMemcpyHostToDevice );

t = cudaMemcpy( dev_ret, h_ret, rows * cols * sizeof(int), cudaMemcpyHostToDevice );

	dim3 threadsPerBlock(5, 5);
	dim3 blocksPerGrid(2, 2);


    infaint<<<blocksPerGrid, threadsPerBlock>>>( dev_r, dev_g, dev_b, rows, cols, dev_ret );

    // copy the array 'c' back from the GPU to the CPU
    t = cudaMemcpy( h_r, dev_r, rows * cols * sizeof(int), cudaMemcpyDeviceToHost );
    t = cudaMemcpy( h_g, dev_g, rows * cols * sizeof(int), cudaMemcpyDeviceToHost );
    t = cudaMemcpy( h_b, dev_b, rows * cols * sizeof(int), cudaMemcpyDeviceToHost );

t = cudaMemcpy( h_ret, dev_ret, rows * cols * sizeof(int), cudaMemcpyDeviceToHost );

	if (t != cudaSuccess) { 
		cout << "Failed"  << endl;
	} 

	// display image
	cout << endl;
	for (int i = 0; i < rows; ++i) {
		for (int j = 0; j < cols; ++j) {
			cout << h_r[i * cols + j] << ' ';
		}
		cout << endl;
	}

    // free the memory allocated on the CPU
    free( h_r );
    free( h_g );
    free( h_b );

    // free the memory allocated on the GPU
    cudaFree( dev_r );
    cudaFree( dev_g );
    cudaFree( dev_b );

    return 0;
}
