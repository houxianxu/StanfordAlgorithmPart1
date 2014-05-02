/* count the number of inversion pair of an array of int
 * @file countInversionPair.cpp 
 * the idea is related merge sort, i.e. count while sort
 * the data comes from http://spark-public.s3.amazonaws.com/algo1/programming_prob/IntegerArray.txt */
#include <iostream>
#include <fstream>
#include <vector>
#include <climits> // the result is bigger than INT_MAX or LONG_MAX
using namespace std;

// sort arr[], and return return the No. of inversion pair
// when the first item in the right part is the smaller than the first item in the left part, then count
long long int mergeCount(int arr[], int left, int mid, int right) { // left part and right part are sorted
	int i = left;
	int j = mid + 1;
	int res[right - left + 1]; // store the result
	int k = 0; // index of res
	long long int count = 0;

	while (i <= mid && j <= right) {
		if (arr[i] <= arr[j]) {
			res[k] = arr[i];
			k++;
			i++;
		} else {
			count += mid - i + 1;
			res[k] = arr[j];
			k++;
			j++;
		}
	}

	while (i <= mid) {
		res[k] =arr[i];
		i++;
		k++;
	}

	while (j <= right) {
		res[k] =arr[j];
		j++;
		k++;
	}

	// copy the res to arr to complete sort
	k = 0;
	for (i = left; i <= right; i++) {
		arr[i] = res[k];
		k++;
	}

	return count;
}

long long int mergeSortCountRec(int arr[], int left, int right) {
	if (left >= right) {
		return 0;
	} else {
		int mid = (left + right) / 2;
		long long int leftCount = mergeSortCountRec(arr, left, mid);
		long long int rightCount = mergeSortCountRec(arr, mid + 1, right);
		long long int midCount = mergeCount(arr, left, mid, right);
		return leftCount + rightCount + midCount;
	}
}


long long int countInversionPair(int arr[], int n) {
	return mergeSortCountRec(arr, 0, n - 1);
}

void printArray(int arr[], int n) {
	for (int i = 0; i < n; i++) {
		cout << arr[i] << " ";
	}
	cout << endl;
}
	
int main(int argc, char const *argv[])	
{
	
	vector<int> data;
	ifstream infile("IntegerArray.txt");
	int val;
	while (infile >> val) {
		data.push_back(val);
	}

	int n = data.size();
	cout << n << endl;

	int arr[n];
	
	for (int i = 0; i < n; i++) {
		arr[i] = data[i];
	}

	// printArray(arr, n);
	long long int res = countInversionPair(arr, n);
	cout << res << endl;
	// int test[] = {30, 20, 1, 14, 13};
	// cout << countInversionPair(test, 5) << endl;

	cout << "INT_MAX - > " << INT_MAX << endl;
	cout << "LONG_MAX- > " << LONG_MAX << endl;
	return 0;
}