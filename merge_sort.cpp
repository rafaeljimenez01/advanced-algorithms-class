#include <iostream>
#include <vector>

using namespace std;
void helper_fun(vector <int> &v);
void mergeSort(int inicio, int fin, vector<int>&v);
void merge(int inicio, int fin, vector<int>& v);

void helper_fun(vector<int>& v)
{
	
	mergeSort(0, v.size() - 1,v);
	
}

/*
*		Función Merge Sort
*		Utiliza el metodo de ordenamiento Merge Sort
*		Parametros de entrada: Recibe el indice de inicio del vector, el indice de fin, 
*		el vector por referencia, un entero que guarda las comparaciones por referencia
*		Valor de retorno: Un contador del numero de comparaciones que realiza el metodo para ordenar el vector.
*		Complejidad: O(n log2(n))
*/

void mergeSort(int inicio, int fin, vector <int>& v)
{
	if (inicio < fin) {
		int centro = (inicio + fin) / 2;
		mergeSort(inicio, centro, v);
		mergeSort(centro + 1, fin, v);
	 merge(inicio, fin, v);
	}
}

/*
*		Utiliza el metodo de ordenamiento Merge Sort
*		Parametros de entrada: Recibe el indice de inicio del vector, el indice de fin, 
*		el vector por referencia, un entero que guarda las comparaciones por referencia
*		Valor de retorno: Ninguno.
*		Complejidad: O(n)
*/

void merge(int inicio, int fin, vector<int>&v)
{
	int half = (inicio + fin) / 2;
	int j = inicio;
	int k = half + 1;
	int size = fin - inicio + 1;
	vector <int> vauxiliar;
	for (int i = 0; i < size; i++) {
			if (j <= half && k <= fin) {
				
				if (v[j] < v[k]) {
					vauxiliar.push_back(v[j++]);
				}
				else {
					vauxiliar.push_back(v[k++]);
				}
			}
			else if (j <= half) {
				
				vauxiliar.push_back(v[j++]);
			}
			else {
				
				vauxiliar.push_back(v[k++]);
			}
	}
	for (int m = 0; m < size; m++) {
		v[inicio + m] = vauxiliar[m];
	}
}



int main(){

    vector<int> test{12,15,1,3,4,5,55,12,66,4};

 	helper_fun(test);

    for (auto i = test.begin(); i != test.end(); ++i){
        std::cout << *i << ' ';
    }
    cout << "test" << endl;

    return 0;
}

