while True:
    print("1. Konversi Celcius")
    print("2. Konversi Fahrenheit")
    print("3. Konversi Kelvin")
    print("4. Konversi Rankine")
    print("5. Keluar")

    choice = input("Pilih opsi (1/2/3/4/5): ")
    
    if choice == '5':
        print("Terimakasih!")
        break       
        
    if choice == '1':
        temperature = float(input("Masukan angka yang akan dikonversi: "))
        print("1. From Fahrenheit")
        print("2. From Kelvin")
        print("3. From Rankine")
        
        sec_choice = input("Pilih basis satuan: ")
                
        if sec_choice == '1':
            hasil_fc = (temperature - 32) / 1.8
            print(hasil_fc, "Celcius")
        elif sec_choice == '2':
            hasil_kc = (temperature - 273.15)
            print(hasil_kc, "Celcius")
        elif sec_choice == '3':
            hasil_rc = (temperature - 491.67) / 1.8
            print(hasil_rc, "Celcius")
        else:
            print("Pilihan tidak valid. Coba lagi")
        continue

    if choice == '2':
        temperature = float(input("Masukan angka yang akan dikonversi: "))
        print("1. From Celcius")
        print("2. From Kelvin")
        print("3. From Rankine")

        sec_choice = input("Pilih basis satuan: ")
                
        if sec_choice == '1':
            hasil_cf = (temperature * 1.8) + 32
            print(hasil_cf, "Fahrenheit")
        elif sec_choice == '2':
            hasil_kf = (temperature * 1.8) - 459.67
            print(hasil_kf, "Fahrenheit")
        elif sec_choice == '3':
            hasil_rf = (temperature - 491.67)
            print(hasil_rf, "Fahrenheit")
        else:
            print("Pilihan tidak valid. Coba lagi")
        continue    

    if choice == '3':
        temperature = float(input("Masukan angka yang akan dikonversi: "))
        print("1. From Celcius")
        print("2. From Fahrenheit")
        print("3. From Rankine")

        sec_choice = input("Pilih basis satuan: ")
                
        if sec_choice == '1':
            hasil_ck = (temperature + 273.15)
            print(hasil_ck, "Kelvin")
        elif sec_choice == '2':
            hasil_fk = (temperature - 32) / 1.8 + 273.15
            print(hasil_fk, "Kelvin")
        elif sec_choice == '3':
            hasil_rk = (temperature / 1.8)
            print(hasil_rk, "Kelvin")
        else:
            print("Pilihan tidak valid. Coba lagi")
        continue    

    if choice == '4':
        temperature = float(input("Masukan angka yang akan dikonversi: "))
        print("1. From Celcius")
        print("2. From Fahrenheit")
        print("3. From Kelvin")

        sec_choice = input("Pilih basis satuan: ")
                
        if sec_choice == '1':
            hasil_cr = (temperature + 273.15) * 1.8
            print(hasil_cr, "Rankine")
        elif sec_choice == '2':
            hasil_fr = (temperature + 459.67)
            print(hasil_fr, "Rankine")
        elif sec_choice == '3':
            hasil_kr = (temperature * 1.8)
            print(hasil_kr, "Rankine")
        else:
            print("Pilihan tidak valid. Coba lagi")
        continue     

    else:
        print("Opsi tidak valid. Silakan pilih 1, 2, 3, 4 atau 5.")
