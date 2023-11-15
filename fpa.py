import numpy
import pandas
import scipy
pandas.set_option('display.max_columns', None)

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
        
        seleksi = pandas.DataFrame({
                'Random' : real_acak,
                'Switch Probability' : switch_prob
            }, 
            index = self.__nama_baris
        )

        seleksi['Penyerbukan'] = numpy.where(
            seleksi['Random'] < self.switch_probability,
            'GLOBAL',
            'LOKAL'
        )

        return(seleksi)
    
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
    
    def penyerbukan(
        self, 
        posisi : pandas.DataFrame
    ) -> pandas.DataFrame:

        hasil_seleksi = self.seleksi_penyerbukan()

        index_terbaik_bunga = f'Bunga {index_bunga_terbaik + 1}'
        posisi_bunga_terbaik = posisi.loc[index_terbaik_bunga]
        
        for i in range(self.banyak_bunga):
            index_bunga = f'Bunga {i+1}'
            posisi_bunga = posisi.loc[index_bunga]
            
            if(hasil_seleksi.loc[index_bunga]['Penyerbukan'] == 'GLOBAL'):
                hasil_penyerbukan = self.penyerbukan_global(
                    posisi = posisi_bunga,
                    posisi_terbaik = posisi_bunga_terbaik
                )

            else:
                hasil_penyerbukan = self.penyerbukan_lokal(
                    posisi_bunga
                )

            if(i == 0):
                posisi_bunga_baru = pd.DataFrame([hasil_penyerbukan])
            else:
                posisi_baru = pd.Series(
                    hasil_penyerbukan, 
                    index = [j for j in range(banyak_pelanggan)]
                )

                posisi_bunga_baru = posisi_bunga_baru.append(
                    posisi_baru, 
                    ignore_index = True
                )

        posisi_bunga_baru.index = self.__nama_baris
        posisi_bunga_baru.columns = self.__nama_kolom

        return(posisi_bunga_baru)

        
