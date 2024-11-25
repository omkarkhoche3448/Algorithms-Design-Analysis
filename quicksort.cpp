// multithreaded quicksort

#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdlib>
#include <ctime>
#include <omp.h>

using namespace std;

class QuickSortMultiThreading {
public:
	QuickSortMultiThreading(int start, int end, vector<int>& arr) 
		: start_(start), end_(end), arr_(arr) {}
	
	// Finding random pivoted and partition
	// array on a pivot.
	// There are many different
	// partitioning algorithms.
	int partition(int start, int end, vector<int>& arr) {
		int i = start;
		int j = end;

		// Decide random pivot
		int pivoted = rand() % (j - i + 1) + i;

		// Swap the pivoted with end
		// element of array
		int t = arr[j];
		arr[j] = arr[pivoted];
		arr[pivoted] = t;
		j--;

		// Start partitioning
		// Elements smaller than the pivot are on the left.
		// Elements larger than the pivot are on the right.
		while (i <= j) {
			if (arr[i] <= arr[end]) {
				i++;
				continue;
			}
			if (arr[j] >= arr[end]) {
				j--;
				continue;
			}
			t = arr[j];
			arr[j] = arr[i];
			arr[i] = t;
			j--;
			i++;
		}

		// Swap pivoted to its
		// correct position
		t = arr[j + 1];
		arr[j + 1] = arr[end];
		arr[end] = t;
		return j + 1;
	}

	// Function to implement
	// QuickSort method
	void operator() () {
		// Base case
		if (start_ >= end_) {
			return;
		}

		// Find partition
		int p = partition(start_, end_, arr_);

		// Divide array Each thread handles one subarray, leveraging multithreading.
		QuickSortMultiThreading left(start_, p - 1, arr_);
		QuickSortMultiThreading right(p + 1, end_, arr_);

		// Left subproblem as separate thread
		#pragma omp parallel sections
		{
			#pragma omp section
			{
				left();
			}
			#pragma omp section
			{
				right();
			}
		}
	}

private:
	int start_;
	int end_;
	vector<int>& arr_;
};

int main() {
	int n = 7;
	vector<int> arr = {54, 64, 95, 82, 12, 32, 63};
	srand(time(NULL));
	QuickSortMultiThreading(0, n - 1, arr)();
	for (int i = 0; i < n; i++) {

		// Print sorted elements
		cout << arr[i] << " ";
	}
	cout << endl;
	return 0;
}

// Output : 12 32 54 63 64 82 95 


// Advantages of Multithreading
// Faster Execution: Threads utilize multiple cores, leading to faster computation.
// Efficient Resource Use: By keeping cores busy, threads prevent underutilization of CPU.
// Scalability: Programs can handle larger datasets by dividing work among threads.


// Potential Questions and Answers
// Questions on Partitioning
// Q1: Why is a random pivot chosen?

// A random pivot helps avoid worst-case performance in QuickSort (e.g., when the array is already sorted).
// Q2: What does the partition function return?

// It returns the final index of the pivot after rearranging the array.
// Questions on Multithreading
// Q3: What is OpenMP, and why is it used here?

// OpenMP is a parallel programming framework in C++ that simplifies multithreading. It is used here to split the QuickSort process into multiple threads, improving performance for large arrays.
// Q4: How does #pragma omp parallel sections work?

// It creates separate threads for each section:
// One thread processes the left subarray.
// Another thread processes the right subarray.

// Q5: Can this program handle very large arrays?
// Yes, but the number of threads is limited by the system's hardware. Beyond a certain size, the overhead of thread creation can outweigh the benefits.
// Questions on the QuickSort Algorithm

// Q6: What is the time complexity of QuickSort?
// Best/Average Case: 
// 𝑂(𝑛log⁡𝑛)
// O(nlogn)
// Worst Case: 
// 𝑂(𝑛2)

// which is rare due to the random pivot.
// Q7: What is the space complexity?

// 𝑂(log𝑛)
// O(logn) for the recursive stack.
// Q8: What is the base case in this implementation?

// The base case is when the start_ index is greater than or equal to the end_ index.
// General Questions
// Q9: How is the program tested?

// It is tested with a hardcoded array. For better testing, you can use dynamic input or benchmark it with larger datasets.
// Q10: Can this code sort in descending order?

// Yes, by modifying the conditions in partition to rearrange elements in descending order.

// What is the role of #pragma omp parallel sections?

// It splits the program into parallel threads for execution.
// How does this code avoid thread conflicts?

// Each thread works on a separate subarray, avoiding overlap.
// Can this code run faster on a single-core CPU?

// No, on a single-core CPU, threads execute sequentially, adding overhead without benefit.
// What happens if the array is very large?

// The program creates threads recursively, potentially causing memory or thread overhead.
// How does multithreading improve QuickSort?

// By sorting subarrays in parallel, the overall sorting time is reduced on multi-core CPUs.