import numpy
import pandas
import scipy

class FlowerPollination():

    def __init__(
        self, 
        **parameter
    ):
        self.banyak_bunga = parameter.get('banyak_bunga')
        self.step_size = parameter.get('step_size')
        self.switch_probability = parameter.get('switch_probability')
        self.lamda = parameter.get('lamda')
        self.dimensi = parameter.get('dimensi')

        self.__nama_kolom = [f'{kolom + 1}' for kolom in range(self.dimensi)]
        self.__nama_baris = [f'Bunga {baris + 1}' for baris in range(self.banyak_bunga)]

        self.sigma = ((scipy.special.gamma(1 + self.lamda) * numpy.sin(numpy.pi * (self.lamda / 2)))
                      /(scipy.special.gamma((1 + self.lamda) / 2) * self.lamda * (2 ** ((self.lamda - 1) / 2))))**(1 / self.lamda)

    
    def bangkitkan_posisi_bunga(self) -> pandas.DataFrame:
        real_acak = numpy.random.rand(
            self.banyak_bunga, 
            self.dimensi
        )

        posisi_bunga = pandas.DataFrame(
            real_acak,
            columns = self.__nama_kolom,
            index = self.__nama_baris,
        )

        return(posisi_bunga)
    
    def solusi_terbaik(
        self, 
        fitness : list, 
        tipe = 'min'
    ) -> tuple:
        if(tipe.lower() == 'min'):
            nilai_optimum = min(fitness)
        else:
            nilai_optimum = max(fitness)

        index_bunga_terbaik = hasil.index(nilai_optimum)
        return(nilai_optimum, index_bunga_terbaik)

    def seleksi_penyerbukan(self) -> pandas.DataFrame:
        real_acak = numpy.random.rand(self.banyak_bunga)
        switch_prob = [self.switch_probability] * self.banyak_bunga
        
        kriteria_penyerbukan = pandas.DataFrame({
                'Random' : real_acak,
                'Switch Probability' : switch_prob
            }, 
            index = self.__nama_baris
        )

        # Pembagian kriteria penyerbukan
        kriteria_penyerbukan['Penyerbukan'] = numpy.where(
            kriteria_penyerbukan['Random'] < self.switch_probability,
            'GLOBAL',
            'LOKAL'
        )

        return(kriteria_penyerbukan)
    
    def penyerbukan_lokal(
        self, 
        posisi : list
    ) -> list:
        
        hasil = list()
        banyak_dimensi = len(posisi)
        
        for i in range(banyak_data):
            epsilon = numpy.random.rand()

            int_acak = numpy.arange(0, banyak_dimensi)  
            int_acak = numpy.setdiff1d(int_acak, i)

            j = numpy.random.choice(int_acak)
            int_acak = numpy.setdiff1d(int_acak, j)

            k = numpy.random.choice(int_acak)

            posisi_baru = posisi[i] + epsilon*(posisi[j] - posisi[k])
            hasil.append(posisi_baru)
        
        return(hasil)
    
    def penyerbukan_global(
        self, 
        posisi, 
        posisi_terbaik
    ) -> list:

        hasil = []
        banyak_dimensi = len(posisi)

        u = numpy.random.normal(
            loc = 0,
            scale = 1,
            size = (1, banyak_dimensi)
        )

        v = numpy.random.normal(
            loc = 0,
            scale = 1,
            size = (1, banyak_dimensi)
        )

        u = u.flatten()
        v = v.flatten()

        for i in range(banyak_dimensi):
            s = (u[i] * self.sigma)/((numpy.abs(v[i]))**(1 / self.lamda))
            L = ((self.lamda * scipy.special.gamma(self.lamda) * numpy.sin(numpy.pi/2 * self.lamda))/numpy.pi) *
                (1/(numpy.abs(s) ** (1 + self.lamda)))
            posisi_baru = posisi[i] + self.stepsize * L * (posisi_terbaik[i] - posisi[i])
            hasil.append(posisi_baru)

        return(hasil)