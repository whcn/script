#include <iostream> 
#include <tuple> 
#include <map> 

using namespace std;

struct pixel {
	/* pixel(){} */
	/* pixel(int red, int green, int blue): r(red), g(green), b(blue){} */
	int r;
	int g;
	int b;
};


int main(int argc, const char *argv[]) {

	tuple<int, int, int> t;
	get<0>(t) = 1;
	cout << get<0>(t) << endl;
	cout << get<1>(t) << endl;

/* 	pixel pixels[10]; */
/* 	for (int i = 0; i < 10; ++i) { */
/* 		pixel a; */
/* 		a.r=1; */
/* 		a.g=1; */
/* 		a.b=1; */
/* 		pixels[i] = a; */
/* 	} */ 
/* 	pixels[1].b=2; */

/* 	/1* for (int i = 0; i < 10; ++i) { *1/ */
/* 	/1* 	cout << pixels[0].r << ' ' <<  pixels[0].g << ' ' << pixels[0].b << endl; *1/ */
/* 	/1* } *1/ */
/* 	if (pixels[0].r == pixels[1].r && pixels[0].g == pixels[1].g && pixels[0].b == pixels[1].b) { */ 
/* 		cout << "true"  << endl; */
/* 	} */ 
/* 	else */
/* 		cout << "false"  << endl; */


/* 	/1* tuple<int, int, int> t3(1,9,3); *1/ */
/* 	/1* tuple<int, int, int> t1(1,2,3); *1/ */
/* 	/1* tuple<int, int, int> t2(1,2,3); *1/ */
/* 	/1* tuple<int, int, int> t4(1,2,3); *1/ */
/* 	/1* tuple<int, int, int> t5(1,9,3); *1/ */


/* 	/1* map<tuple<int, int, int>, int> m; *1/ */
/* 	/1* ++m[t1]; *1/ */   
/* 	/1* ++m[t2]; *1/ */   
/* 	/1* ++m[t3]; *1/ */   
/* 	/1* ++m[t4]; *1/ */   
/* 	/1* ++m[t5]; *1/ */   

/* 	/1* auto s = m.begin(); *1/ */
/* 	/1* for (auto i : m) { *1/ */
/* 	/1* 	cout << get<0>(i.first) << ' ' << get<1>(i.first) << ' ' << get<2>(i.first) << endl; *1/ */
/* 	/1* 	cout << i.second << endl; *1/ */
/* 	/1* } *1/ */ 
/* 	/1* cout << endl; *1/ */

	return 0;
}

