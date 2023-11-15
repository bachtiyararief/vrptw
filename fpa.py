import numpy
import pandas

class FlowerPollination():

    def __init__(self, **parameter):
        self.banyak_bunga = parameter.get('banyak_bunga')
        self.step_size = parameter.get('step_size')
        self.switch_probability = parameter.get('switch_probability')
        self.lamda = parameter.get('lamda')
        self.dimensi = parameter.get('dimensi')
    
    def bangkitkan_posisi_bunga(self) -> pandas.DataFrame:
        real_acak = numpy.random.rand(
            self.banyak_bunga, 
            self.dimensi
        )

        nama_kolom = [f'{col_name + 1}' for col_name in range(self.dimensi)]
        nama_baris = [f'Bunga {row_name + 1}' for row_name in range(self.banyak_bunga)]

        posisi_bunga = pd.DataFrame(
            real_acak,
            columns = nama_kolom,
            index = nama_baris,
        )

        return(posisi_bunga)
    
    def solusi_terbaik(self, ):
        min_value = min(hasil)

        index = hasil.index(min_value)

        # Menampilkan hasil
        print(f'Nilai minimum :{min_value : .2f}')
        print(f'Pada bunga ke-{index + 1}')
        return(min_value, index)

