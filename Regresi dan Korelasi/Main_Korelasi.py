import Dataset_Korelasi
import Korelasi


def main():

    """
    Iterates the three available sets of data
    and calls function to calculate rho.
    Then prints the data and Pearson Correlation Coefficient.
    """

    print("Korelasi Linear")
    print("Nama : Rizaldi Fadilah - 152017131")
    print("Pemograman Simulasi Kelas C")

    independent = []
    dependent = []

    for d in range(1, 4):

        if Dataset_Korelasi.populatedata(independent, dependent, d) == True:

            rho = Korelasi.pearson_correlation(independent, dependent)

            print("Dataset %d\n---------" % d)
            print("Independent data: " + (str(independent)))
            print("Dependent data:   " + (str(dependent)))
            print("Pearson Correlation Coefficient rho = %1.2f\n" % rho)
        else:
            print("Cannot populate Dataset %d" % d)


main()