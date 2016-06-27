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

#define WIDTH 2

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


	if ((offsetX >= WIDTH) && (offsetX < (cols - WIDTH)) && (offsetY >= WIDTH) && (offsetY < (rows - WIDTH))) { 
		if ((r[tid] == 255) && (g[tid] == 255) && (b[tid] == 255)) { 

/* ret[tid] = offsetX; */

			pixel pixels[2 * WIDTH + 1][2 * WIDTH + 1];

			for (int is = offsetY - WIDTH, i = offsetY - WIDTH; i <= offsetY + WIDTH; ++i) {
				for (int js = offsetX - WIDTH, j = offsetX - WIDTH; j <= offsetX + WIDTH; ++j) {
					int sid = i * cols + j;
					pixel tmp;
					tmp.r = r[sid];
					tmp.g = g[sid];
					tmp.b = b[sid];
					pixels[i - is][j - js] = tmp;
				} 
			} 


			int counts[2 * WIDTH + 1][2 * WIDTH + 1] = {0};

			for (int i = 0; i < 2 * WIDTH + 1; ++i) {
				for (int j = 0; j < 2 * WIDTH + 1; ++j) {
					for (int p = 0; p < 2 * WIDTH + 1; ++p) {
						for (int q = 0; q < 2 * WIDTH + 1; ++q) {
							if ((pixels[i][j].r == pixels[p][q].r) && (pixels[i][j].g == pixels[p][q].g) && (pixels[i][j].b == pixels[p][q].b)) { 
								counts[i][j] += 1;
							} 
						}
					}  
				} 
			} 
	ret[tid] = pixels[0][0].r;



/* 			int ix = WIDTH, iy = WIDTH; */
/* 			int ic = -1; */
/* 			for (int i = 0; i < 2 * WIDTH + 1; ++i) { */
/* 				for (int j = 0; j < 2 * WIDTH + 1; ++j) { */
/* 					if (ic < counts[i][j]) { */ 
/* 						ic = counts[i][j]; */
/* 						ix = i; */
/* 						iy = j; */
/* 					} */ 
/* 				} */
/* 			} */
/* 			r[tid] = pixels[ix][iy].r; */
/* 			g[tid] = pixels[ix][iy].g; */
/* 			b[tid] = pixels[ix][iy].b; */
		} 
	} 
}

int main(int argc, char** argv )
{
	Mat img = imread("./data/extract.jpg", CV_LOAD_IMAGE_UNCHANGED);

	if (img.empty()) { 
		cout << "Load Image Fail!" << endl;
		return -1;
	} 

	/* cudaDeviceProp devProp; */
	/* cudaGetDeviceProperties(&devProp, 0); */
	/* cout << devProp.maxThreadsPerBlock  << endl; */
	/* for (int i = 0; i < 3; ++i) { */
	/* 		printf("Maximum dimension %d of block:  %d\n", i, devProp.maxThreadsDim[i]); */
	/* 		printf("Maximum dimension %d of gird:  %d\n", i, devProp.maxGridSize[i]); */
	/* } */
			

	int rows = img.rows;
	int cols = img.cols;
	int channels = img.channels();

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
			h_r[i * cols + j] = (int)img.at<Vec3b>(i, j)[0];
			h_g[i * cols + j] = (int)img.at<Vec3b>(i, j)[1];
			h_b[i * cols + j] = (int)img.at<Vec3b>(i, j)[2];

			h_ret[i * cols + j] = -1;
			/* cout << h_r[i * cols + j] << ' ' << h_g[i * cols + j] << ' ' << h_b[i * cols + j] << endl; */
		}  
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

	dim3 threadsPerBlock(32, 32);
	dim3 blocksPerGrid(15, 15);

	/* cout << h_r[0] << ' ' << h_g[0] << ' ' << h_b[0] << endl; */

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
	for (int i = 0; i < rows; ++i) {
		for (int j = 0; j < cols; ++j) {
			/* img.at<Vec3b>(i, j)[0] = h_r[i * cols + j]; */
			/* img.at<Vec3b>(i, j)[1] = h_g[i * cols + j]; */
			/* img.at<Vec3b>(i, j)[2] = h_b[i * cols + j]; */
			img.at<Vec3b>(i, j)[0] = h_r[i * cols + j];
			img.at<Vec3b>(i, j)[1] = h_g[i * cols + j];
			img.at<Vec3b>(i, j)[2] = h_b[i * cols + j];

		}  
	} 

	for (int i = 0; i < rows * cols; ++i) {
	/* for (int i = 0; i < 10; ++i) { */
		cout << h_ret[i] << ' ';
	} 
	cout << endl;

	namedWindow("image", CV_WINDOW_AUTOSIZE);
	imshow("image", img);
	waitKey(0);
	destroyWindow("image");

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
