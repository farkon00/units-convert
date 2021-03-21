#Mass metric to metric
class from_kg:
    @staticmethod
    def to_t(input_int):
        return input_int / 1000
    @staticmethod
    def to_mg(input_int):
        return float(input_int * 1000000)
    @staticmethod
    def to_g(input_int):
        return float(input_int * 1000)
    @staticmethod
    def to_c(input_int):
        return input_int / 100

class from_g:
    @staticmethod
    def to_t(input_int):
        return input_int / 1000000
    @staticmethod
    def to_mg(input_int):
        return float(input_int * 1000)
    @staticmethod
    def to_kg(input_int):
        return input_int / 1000
    @staticmethod
    def to_c(input_int):
        return input_int / 100000

class from_mg:
    @staticmethod
    def to_t(input_int):
        return input_int / 1000000000
    @staticmethod
    def to_g(input_int):
        return input_int / 1000
    @staticmethod
    def to_kg(input_int):
        return input_int / 1000000
    @staticmethod
    def to_c(input_int):
        return input_int / 100000000

class from_t:
    @staticmethod
    def to_mg(input_int):
        return float(input_int * 1000000000)
    @staticmethod
    def to_g(input_int):
        return float(input_int * 1000000)
    @staticmethod
    def to_kg(input_int):
        return float(input_int * 1000)
    @staticmethod
    def to_c(input_int):
        return float(input_int * 10)

class from_c:
    @staticmethod
    def to_mg(input_int):
        return float(input_int * 100000000)
    @staticmethod
    def to_g(input_int):
        return float(input_int * 100000)
    @staticmethod
    def to_kg(input_int):
        return float(input_int * 100)
    @staticmethod
    def to_t(input_int):
        return input_int / 10


#Lenth metric to metric
class from_m:
    @staticmethod
    def to_cm(input_int):
        return float(input_int * 100)
    @staticmethod
    def to_mm(input_int):
        return float(input_int * 1000)
    @staticmethod
    def to_km(input_int):
        return input_int / 1000
    @staticmethod
    def to_dm(input_int):
        return float(input_int * 10)

class from_km:
    @staticmethod
    def to_cm(input_int):
        return float(input_int * 100000)
    @staticmethod
    def to_mm(input_int):
        return float(input_int * 1000000)
    @staticmethod
    def to_m(input_int):
        return float(input_int * 1000)
    @staticmethod
    def to_dm(input_int):
        return float(input_int * 10000)

class from_mm:
    @staticmethod
    def to_cm(input_int):
        return input_int / 10
    @staticmethod
    def to_km(input_int):
        return input_int / 1000000
    @staticmethod
    def to_m(input_int):
        return input_int / 1000
    @staticmethod
    def to_dm(input_int):
        return input_int / 100

class from_dm:
    @staticmethod
    def to_cm(input_int):
        return float(input_int * 10)
    @staticmethod
    def to_km(input_int):
        return input_int / 100
    @staticmethod
    def to_m(input_int):
        return input_int / 10
    @staticmethod
    def to_mm(input_int):
        return float(input_int * 100)

class from_cm:
    @staticmethod
    def to_mm(input_int):
        return float(input_int * 10)
    @staticmethod
    def to_km(input_int):
        return input_int / 100000
    @staticmethod
    def to_m(input_int):
        return input_int / 100
    @staticmethod
    def to_dm(input_int):
        return input_int / 10


#Area metric to metric
class from_sm:
    @staticmethod
    def to_scm(input_int):
        return float(input_int * 10000)
    @staticmethod
    def to_smm(input_int):
        return float(input_int * 1000000)
    @staticmethod
    def to_skm(input_int):
        return input_int / 1000000
    @staticmethod
    def to_sdm(input_int):
        return float(input_int * 100)

class from_skm:
    @staticmethod
    def to_scm(input_int):
        return float(input_int * 1000000000)
    @staticmethod
    def to_smm(input_int):
        return float(input_int * 1000000000000)
    @staticmethod
    def to_sm(input_int):
        return float(input_int * 1000000)
    @staticmethod
    def to_sdm(input_int):
        return float(input_int * 100000000)

class from_smm:
    @staticmethod
    def to_scm(input_int):
        return input_int / 100
    @staticmethod
    def to_skm(input_int):
        return input_int / 1000000000000
    @staticmethod
    def to_sm(input_int):
        return input_int / 1000000
    @staticmethod
    def to_sdm(input_int):
        return input_int / 10000

class from_sdm:
    @staticmethod
    def to_scm(input_int):
        return float(input_int * 100)
    @staticmethod
    def to_skm(input_int):
        return input_int / 10000
    @staticmethod
    def to_sm(input_int):
        return input_int / 100
    @staticmethod
    def to_smm(input_int):
        return float(input_int * 10000)

class from_scm:
    @staticmethod
    def to_smm(input_int):
        return float(input_int * 100)
    @staticmethod
    def to_skm(input_int):
        return input_int / 10000000000
    @staticmethod
    def to_sm(input_int):
        return input_int / 10000
    @staticmethod
    def to_sdm(input_int):
        return input_int / 100


#Volume metric to metric
class from_mс:
    @staticmethod
    def to_cmс(input_int):
        return float(input_int * 1000000)
    @staticmethod
    def to_mmс(input_int):
        return float(input_int * 1000000000)
    @staticmethod
    def to_kmс(input_int):
        return input_int / 1000000000
    @staticmethod
    def to_dmс(input_int):
        return float(input_int * 1000)

class from_kmс:
    @staticmethod
    def to_cmс(input_int):
        return float(input_int * 1000000000000000)
    @staticmethod
    def to_mmс(input_int):
        return float(input_int * 1000000000000000000)
    @staticmethod
    def to_mс(input_int):
        return float(input_int * 1000000000)
    @staticmethod
    def to_dmс(input_int):
        return float(input_int * 1000000000000)

class from_mmс:
    @staticmethod
    def to_cmс(input_int):
        return input_int / 1000
    @staticmethod
    def to_kmс(input_int):
        return input_int / 1000000000000000000
    @staticmethod
    def to_mс(input_int):
        return input_int / 1000000000
    @staticmethod
    def to_dmс(input_int):
        return input_int / 1000000

class from_dmс:
    @staticmethod
    def to_cmс(input_int):
        return float(input_int * 1000)
    @staticmethod
    def to_kmс(input_int):
        return input_int / 1000000
    @staticmethod
    def to_mс(input_int):
        return input_int / 1000
    @staticmethod
    def to_mmс(input_int):
        return float(input_int * 1000000)

class from_cmс:
    @staticmethod
    def to_mmс(input_int):
        return float(input_int * 1000)
    @staticmethod
    def to_kmс(input_int):
        return input_int / 1000000000000000
    @staticmethod
    def to_mс(input_int):
        return input_int / 1000000
    @staticmethod
    def to_dmс(input_int):
        return input_int / 1000
