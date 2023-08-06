Script ini untuk membuat jalurterbang Spraying untuk drone spraying FC JIYI.
Data yang dihasilkan adalah berupa garis(.shp).
Data garis(.shp) yang diperlukan menggunakan koordinat WGS_1984, Mohon tidak diproject ke UTM.
Bila menggunakan data DSM(.tif) boleh menggunakan koordinat WGS_1984, maupun koordinat UTM.


Data tersebut dilanjutkan di software Qgis, untuk diconvert menjadi (.kml), lalu di "dissolve".
Data hasil dissolve dapat digunakan dalam aplikasi "AgriAsistant"

Install
pip install avirtech_spraying_jiyi_lib

Usage
from avirtech_spraying_jiyi_lib.avirtech_spraying_jiyi import autocorrect