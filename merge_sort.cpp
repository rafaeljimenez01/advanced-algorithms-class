#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

void mergeSort(const int &SIZE, float v[]);
void mergeSort(int start, int end, float v[]);
void merge(int start, int end, float v[]);

void mergeSort(float v[], const int &SIZE)
{	
	mergeSort(0, SIZE - 1, v);
}

/*
*		Función Merge Sort
*		Utiliza el metodo de ordenamiento Merge Sort
*		Parametros de entrada: Recibe el indice de inicio del vector, el indice de fin, 
*		el vector por referencia, un entero que guarda las comparaciones por referencia
*		Valor de retorno: Un contador del numero de comparaciones que realiza el metodo para ordenar el vector.
*		Complejidad: O(n log2(n))
*/

void mergeSort(int start, int end, float v[])
{
	if (start < end) {
		int mid = (start + end) / 2;

		mergeSort(start, mid, v);
		mergeSort(mid + 1, end, v);
	 	merge(start, end, v);
	}
}

/*
*		Utiliza el metodo de ordenamiento Merge Sort
*		Parametros de entrada: Recibe el indice de inicio del vector, el indice de fin, 
*		el vector por referencia, un entero que guarda las comparaciones por referencia
*		Valor de retorno: Ninguno.
*		Complejidad: O(n)
*/

void merge(int start, int end, float v[])
{
	const int MID = (start + end) / 2;
	const int SIZE = end - start + 1;
	int j = start;
	int k = MID + 1;
 	float vauxiliar[SIZE];

	for (int i = 0; i < SIZE; i++) {
			if (j <= MID && k <= end) {
				
				if (v[j] < v[k]) {
					vauxiliar[i] = v[j++];
				}
				else {
					vauxiliar[i] = v[k++];
				}
			}
			else if (j <= MID) {
				
				vauxiliar[i] = v[j++];
			}
			else {
				
				vauxiliar[i] = v[k++];
			}
	}

	for (int m = 0; m < SIZE; m++) {
		v[start + m] = vauxiliar[m];
	}
}



int main() {
	std::ifstream file("tests.txt");
	
	if(file.is_open()) {
		while(!file.eof()) {
			int tmp;
			file >> tmp;

			const int SIZE = tmp;
			float input[SIZE];

			for(int i = 0; i < SIZE; ++i) {
				file >> input[i];
			}

			mergeSort(input, SIZE);

			for (int i = 0; i < SIZE; ++i){
				std::cout << input[i] << ' ';
			}

			std::cout << '\n';
		}
	}

    return 0;
}
