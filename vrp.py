import numpy 
import pandas

class VehicleRoutingProblemwithTimeWindows():

    def __init__(self):
        pass

    def urutkan_posisi(
        self, 
        posisi
    ) -> pandas.DataFrame:
        
        urutkan_nilai = numpy.argsort(
            posisi.values,
            axis = 1
        )

        # Mengganti nilai dengan label sesuai urutan
        pelabelan = numpy.argsort(
            urutkan_nilai,
            axis = 1
        ) + 1

        # Membuat DataFrame dari label
        hasil = pd.DataFrame(
            pelabelan,
            columns = posisi.columns,
            index = posisi.index
        )

        # Menampilkan DataFrame
        return(hasil)
