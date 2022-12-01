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


def search_list_strings(list_strings, pattern) -> None:
    """Iterates through a list of strings searching for the pattern.
    pattern should be a non compiled regex raw string. Prints the full
    string if the pattern is found in the string. A list compreshension
    is also shown.

    Example call:
        search_list_strings(metars, r"KORD\s")

    parameters:
        list_strings: list[str]: List of strings to search
        pattern r[str]: raw stirng to search for
    """
    pattern = re.compile(pattern)

    for string in list_strings:
        if re.search(pattern, string):
            print(string)

    [print(string) for string in list_strings if re.search(pattern, string)]


def main():
    sta_ord = metars[-3]
    print(sta_ord)
    found = re.search(re.compile(r"KORD\s"), sta_ord)
    print(found)

if __name__ == "__main__":
    import sys

    sys.exit(main())

