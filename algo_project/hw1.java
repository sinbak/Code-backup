import java.util.*;

public class hw1 {
    public static void main(String[] args) {
        Scanner keyboard = new Scanner(System.in);

        System.out.println("N M = ");
        int intN = keyboard.nextInt();
        int intM = keyboard.nextInt();

        int []array = new int[intN];

        for(int i = 0; i < intN; i++)
                array[i] = (1 + i) ;

        if (intN <= 10 && intM <= 10) {
            System.out.print("T0: "); // T0 Asc
            for (int i = 0; i < array.length; i++) {
                System.out.print(array[i]);
                if (i != array.length-1)
                    System.out.print(" ");
            }
            System.out.println();

            if (intM >= 1) { // T1 Desc
                System.out.print("T1: ");
                for (int i = array.length-1; i >= 0; i--) {
                    System.out.print(array[i]);
                    if (i != 0)
                        System.out.print(" ");
                }
                System.out.println();

                if (intM >= 2) {
                    // T2

                    int []arrayT2 = new int[intN];
                    arrayT2 = ranArray(intN);

                    System.out.print("T2: "); // T2 Asc
                    for (int i = 0; i < intN; i++) {
                        System.out.print(arrayT2[i]);
                        if (i != intN-1)
                            System.out.print(" ");
                    }
                    System.out.println();

                    if (intM >= 3) {
                        // T3 ~
                        for (int k = 3; k < intM; k++) {
                            array = ranArray(intN);
                            System.out.print("T" + k + ": "); // T0 Asc
                            for (int i = 0; i < array.length; i++) {
                                System.out.print(array[i]);
                                if (i != array.length - 1)
                                    System.out.print(" ");
                            }
                            System.out.println();
                        }
                    }

                    System.out.println();

                    // End T Print
                    System.out.println("[T2] <bubble sort>");
                    bubbleSort(arrayT2, intN);
                    System.out.println();

                    System.out.println("[T2] <selection sort>");
                    selectionSort(arrayT2, intN);
                    System.out.println();

                    System.out.println("[T2] <insertion sort>");
                    insertionSort(arrayT2, intN);
                    System.out.println();


                }
            }

        }
        else { // NOT (N <= 10 and M <= 10)
            // Real test
            for (int k = 0; k < intM; k++) {
                array = ranArray(intN);
                for (int i = 0; i < array.length; i++) {}
            }
            System.out.println(intM + " test case inputs generated.");
            System.out.println(intN + " integers ineach test case.");
        }
    }


    public static int []ranArray(int N) { //  랜덤 배열 생성
        int[] array = new int[N];

        for (int i = 0; i < N; i++) {
            array[i] = (int)(Math.random() * (N) + 1);
            for (int j = 0; j < i; j++) { // 중복제거
                if(array[i] == array[j]) { i--; break; }
            }
        }
        return array;
    }

    public static void bubbleSort(int []arr, int n) {
        int tmp;
        int[] array = arr.clone();

        // Print L0
        System.out.print("L0: ");
        for (int k = 0; k < array.length; k++) {
            System.out.print(array[k]);
            if (k != array.length - 1)
                System.out.print(" ");
        }
        System.out.println();

        for (int i = 0; i < n-1; i++) {
            for (int j = 0; j < n-1-i; j++){ // 오름차순
                if (array[j] > array[j+1]) {
                    tmp = array[j];
                    array[j] = array[j+1];
                    array[j+1] = tmp;
                }
            }
            System.out.print("L" + (i+1) + ": "); // T0 Asc
            for (int k = 0; k < array.length; k++) {
                System.out.print(array[k]);
                if (k != array.length - 1)
                    System.out.print(" ");
            }
            System.out.println();
        }
    }

    public static void selectionSort(int []arr, int n) {
        int tmp;
        int[] array = arr.clone();

        // Print L0
        System.out.print("L0: ");
        for (int k = 0; k < array.length; k++) {
            System.out.print(array[k]);
            if (k != array.length - 1)
                System.out.print(" ");
        }
        System.out.println();

        for (int i = 0; i < n-1; i++) {
            for (int j = i+1; j < n; j++) {
                if (array[i] > array[j]) {
                    tmp = array[i];
                    array[i] = array[j];
                    array[j] = tmp;
                }
            }
            System.out.print("L" + (i+1) + ": "); // T0 Asc
            for (int k = 0; k < array.length; k++) {
                System.out.print(array[k]);
                if (k != array.length - 1)
                    System.out.print(" ");
            }
            System.out.println();
        }
    }

    public static void insertionSort(int []arr, int n) {
        int j, key;
        int[] array = arr.clone();

        // Print L0
        System.out.print("L0: ");
        for (int k = 0; k < array.length; k++) {
            System.out.print(array[k]);
            if (k != array.length - 1)
                System.out.print(" ");
        }
        System.out.println();

        for (int i = 1; i < n; i++) {
            key = array[i];
            for (j=i-1; j>=0 && array[j]>key;j--) {
                array[j+1] = array[j];
            }
            array[j+1] = key;

            System.out.print("L" + i + ": "); // T0 Asc
            for (int k = 0; k < array.length; k++) {
                System.out.print(array[k]);
                if (k != array.length - 1)
                    System.out.print(" ");
            }
            System.out.println();
        }
    }
}