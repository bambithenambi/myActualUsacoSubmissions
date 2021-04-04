import java.util.*;
import java.io.*;

public class Acowdemia {
  static Scanner sc = new Scanner(System.in);
  public static void main(String[] args) {
    int n = sc.nextInt();
    int k = sc.nextInt();
    int l = sc.nextInt();
    int[] data = new int[n];
    for (int i = 0; i < n; i++) {
      data[i] = sc.nextInt();
    }
    Arrays.sort(data);
    int[] copy = data.clone();

    int comp = 0;
    int current;
    if (l>=n) {
      for (int i=0; i<n; i++) {
        data[i]+=k;
      }
      current = hIndex(data, n);
    }
    else {
      for (int j=0; j<k; j++) {
        for (int i=0; i<l; i++) {
          data[i]+=1;
        }
        Arrays.sort(data);
      }
      current = hIndex(data, n);
      if (n-(current+1)>0) {
        for (int c=0; c<(n-(current+1)); c++) {
          comp+=(data[c]-copy[c]);
        }
        data[n-(current+1)]+=comp;
        if (hIndex(data, n)>current) {
          current=hIndex(data, n);
        }
      }

    }
    System.out.println(current);
  }
static int hIndex(int[] citations, int n) {
  reverseArray(citations);
  int hindex = 0;
  // Set the range for binary search
  int low = 0, high = n - 1;
  while (low <= high) {
    int mid = (low + high) / 2;
    // Check if current citations is
    // possible
    if (citations[mid] >= (mid + 1)) {
        // Check to the right of mid
        low = mid + 1;
        // Update h-index
        hindex = mid + 1;
    }
    else {
        // Since current value is not
        // possible, check to the left
        // of mid
        high = mid - 1;
    }
  }
  reverseArray(citations);
  return hindex;
  }

  static void reverseArray(int arr[]){
   for (int start=0,end=arr.length-1;start<=end;start++,end--) {
      int temp = arr[start];
      arr[start] = arr[end];
      arr[end] = temp;
    }
  }


}
