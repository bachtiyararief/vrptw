import fpa
import vrptw
import warnings
warnings.filterwarnings('ignore')

FPA = fpa.FlowerPollination(
    banyak_bunga = 5,
    step_size = 0.1,
    switch_probability = 0.5,
    lamda = 0.1,
    dimensi = 25
)

vrptw = VehicleRoutingProblemwithTimeWindows()

posisi = FPA.bangkitkan_posisi_bunga()
print(posisi)

permutasi = vrptw.urutkan_posisi(posisi)
print(permutasi)
