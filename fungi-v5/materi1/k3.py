def show_result(draft_value):
    print("Result of Final Exam:")
    for name, val in draft_value.items():
        print(f"Name: {name}\tFinal Score: {val:.2f}")

def main():
    data = {
        "Mhs1": {"Nama":"Fico Yayan P", "Tugas":90, "UTS":92, "UAS":94},
        "Mhs2": {"Nama":"Mawarni Kenanga", "Tugas":100, "UTS":98, "UAS":89},
        "Mhs3": {"Nama":"Vadhini Nazra", "Tugas":98, "UTS":98, "UAS":96},
        "Mhs4": {"Nama":"Tatang Sudrajad", "Tugas":89, "UTS":89, "UAS":89}
    }

    draft_value = {}

    for mhs, details in data.items():
        nama = details["Nama"]
        avg = (details["Tugas"] + details["UTS"] + details["UAS"])/3
        draft_value[nama] = avg

    show_result(draft_value)

if __name__ == '__main__':
    main()