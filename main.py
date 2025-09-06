meme_dict = {
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            "DELULU": "Sesuatu momen atau orang yang gila",
            "ROFL": "tanggapan terhadap lelucon",
            "SHEESH": "sedikit ketidaksetujuaan",
            "CREEPY": "menakutkan, tidak menyenangkan",
            "AGGRO": "untuk menjadi agresif/marah"
            }

for i in range(5):
    word = input("Ketik kata yang tidak Kamu mengerti (gunakan huruf kapital semua!): ").upper()
    if word in meme_dict.keys():
        print("Bahwa makna", word, "adalah", meme_dict[word])
    else:
        print("Kata itu emang tidak slang, itu kata omong kosong")
