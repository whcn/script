#include "opencv2/imgcodecs.hpp"
#include "opencv2/highgui.hpp"
#include "opencv2/imgproc.hpp"
#include "opencv2/core/utility.hpp"
#include "opencv2/highgui/highgui_c.h"

#include <iostream>
#include <map> 
#include <tuple> 
#include <fstream> 
#include <algorithm> 
#include <cuda_runtime.h>

using namespace std;
using namespace cv;


#define WIDTH 1

int main(int argc, char** argv )
{
	ofstream ofs;
	ofs.open("o.txt");

	Mat img = imread("./data/extract.jpg", CV_LOAD_IMAGE_UNCHANGED);
	Mat res(img.rows, img.cols, CV_8UC3, Scalar(255, 255, 255));

	if (img.empty()) { 
		cout << "Load Image Fail!" << endl;
		return -1;
	} 

	vector<Mat> channels;
	split(img, channels);


	for (int i = WIDTH; i < img.rows - WIDTH; ++i) {
		for (int j = WIDTH; j < img.cols - WIDTH; ++j) {

			if ((channels[0]<uchar>(i, j) == 255) && (channels[1]<uchar>(i, j) == 255) && (channels[2]<uchar>(i, j) == 255) { 

				ofs << "(" << i << "," << j << ")"<< endl;

			/* 	map<tuple<int, int, int>, int> m; */
			/* 	for (int p = i - WIDTH; p <= i + WIDTH; ++p) { */
			/* 		for (int q = j - WIDTH; q <= j + WIDTH; ++q) { */
			/* 			tuple<int, int, int> tmp; */
			/* 			get<0>(tmp) = img.at<Vec3b>(p, q)[0]; */
			/* 			get<1>(tmp) = img.at<Vec3b>(p, q)[1]; */
			/* 			get<2>(tmp) = img.at<Vec3b>(p, q)[2]; */
			/* 			++m[tmp]; */
			/* 		} */
			/* 	} */ 
			/* 	for (auto i : m) { */
			/* 		ofs << i.second << ' '; */

			/* 	} */ 
			/* 	ofs << endl; */
			/* 	/1* int c = -1; *1/ */
			/* 	/1* pair<tuple<int, int, int>, int> p; *1/ */
			/* 	/1* for (auto i : m) { *1/ */
			/* 	/1* 	if (i.second > c) { *1/ */ 
			/* 	/1* 		c = i.second; *1/ */
			/* 	/1* 		p = i; *1/ */
			/* 	/1* 	} *1/ */ 
			/* 	/1* } *1/ */ 
			/* 	/1* cout << endl; *1/ */

			/* 	auto x = std::max_element(m.begin(), m.end(), */
			/* 				[](const pair<tuple<int, int, int>, int>& p1, const pair<tuple<int, int, int>, int>& p2) { */
			/* 				return p1.second < p2.second; }); */
			/* 	ofs << x->second << endl; */

				/* res.at<Vec3b>(i, j)[0] = 0; */
				/* res.at<Vec3b>(i, j)[1] = 0; */
				/* res.at<Vec3b>(i, j)[2] = 0; */
				img.at<Vec3b>(i, j)[0] = 0;
				img.at<Vec3b>(i, j)[1] = 0;
				img.at<Vec3b>(i, j)[2] = 0;
				/* img1.at<Vec3b>(i, j)[0] = get<0>(x->first); */
				/* img1.at<Vec3b>(i, j)[1] = get<1>(x->first); */
				/* img1.at<Vec3b>(i, j)[2] = get<2>(x->first); */
			} 
			else { 
				/* res.at<Vec3b>(i, j)[0] = img.at<Vec3b>(i, j)[0]; */
				/* res.at<Vec3b>(i, j)[1] = img.at<Vec3b>(i, j)[1]; */
				/* res.at<Vec3b>(i, j)[2] = img.at<Vec3b>(i, j)[2]; */
			} 
		}
	} 

	namedWindow("image", CV_WINDOW_AUTOSIZE);
	imshow("image", channels[0]);
	imshow("image1", channels[1]);
	imshow("image2", channels[2]);
	waitKey(0);
	destroyWindow("image");

	ofs.close();
    return 0;
}

