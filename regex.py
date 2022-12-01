"""regex.py"""
import re

# metars have been shortened to 80 columns, but $ at the end was retained
metars = [
    "KJFK 010151Z 27023G30KT 10SM FEW080 BKN100 09/01 A2980 RMK AO2",
    "KLGA 010151Z 27017G27KT 10SM FEW040 SCT100 09/01 A2979 RMK AO2",
    "KBOS 010154Z 29016G26KT 8SM -RA FEW019 SCT036 OVC050 10/06 A2962 RMK AO2 $",
    "KSTL 010151Z 31007KT 10SM CLR M01/M11 A3042 RMK AO2 SLP314 T10061106 $",
    "KORD 010151Z 27019G31KT 10SM CLR M04/M12 A3022 RMK AO2 PK WND 27036/0115",
    "KMCI 010153Z 25005KT 10SM CLR M01/M13 A3042 RMK AO2 SLP313 T10111133",
    "KHOU 010153Z 04012KT 10SM CLR 13/M01 A3033 RMK AO2 SLP276 T01331006",
    "KMIA 010153Z 32011G23KT 10SM -RA BKN019CB BKN027 OVC033 24/21 A3012 $",
    "KDEN 010153Z 00000KT 10SM CLR M07/M11 A2994 RMK AO2 SLP196 T10671106",
    "KORD 302351Z 27016G34KT 10SM FEW036 M04/M11 A3018 RMK AO2",
    "KLAX 010153Z 21004KT 10SM BKN034 BKN043 14/09 A2998 RMK AO2 SLP151 $",
    "KSEA 010153Z 00000KT 3SM -SN BR FEW014 OVC026 01/M01 A2953 RMK AO2 SLP009"
]


def main():
    # compiles the regex KORD with a single space at the end
    station_ord = re.compile(r"KORD\s")

    # iterate through the strings searching for the regex string
    # print only those regex's that are found
    for station in metars:
        if re.search(station_ord, station):
            print(station)

    # The above as a list comprehension
    [print(station) for station in metars if re.search(station_ord, station)]


if __name__ == "__main__":
    import sys

    sys.exit(main())

