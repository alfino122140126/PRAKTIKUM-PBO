# Tugas 2 Praktikum PBO
Program ini adalah simulasi pertarungan antara dua robot (Jaeger) yang terinspirasi dari film Pacific Rim. Program ini menggunakan konsep Pemrograman Berorientasi Objek (PBO) dengan dua kelas utama: Robot dan Game. Berikut deskripsi singkatnya:

1. Kelas Robot:
Setiap robot memiliki atribut: name (nama), hp (health points), max_hp (HP maksimum), attack (kekuatan serangan), dan defense_active (status pertahanan).
Metode yang tersedia:
basic_attack: Serangan dasar dengan 80% akurasi. Jika lawan dalam mode pertahanan, serangan akan dikurangi dan lawan mendapatkan HP tambahan.
special_attack: Serangan khusus (Plasma Cannon) dengan 60% akurasi dan damage lebih besar.
activate_defense: Mengaktifkan mode pertahanan untuk mengurangi damage serangan lawan.
is_alive: Mengecek apakah robot masih memiliki HP > 0.
status: Menampilkan status robot (HP dan mode pertahanan).

2. Kelas Game:
Mengatur alur pertarungan antara dua robot.
Atribut: robot1, robot2, current_round, dan max_rounds.
Metode yang tersedia:
display_status: Menampilkan status kedua robot di setiap ronde.
player_turn: Giliran pemain untuk memilih tindakan (serangan dasar, serangan khusus, atau bertahan).
ai_turn: Giliran AI untuk memilih tindakan secara acak.
play: Menjalankan pertarungan hingga salah satu robot kalah atau mencapai batas maksimum ronde.

3. Fungsi main:
Membuat dua objek robot: Gipsy Danger dan Striker Eureka.
Memungkinkan pemain memilih robot yang ingin dikendalikan.
Memulai pertarungan dengan memanggil metode play dari objek Game.

4. Mekanisme Pertarungan:
Pertarungan berlangsung dalam beberapa ronde.
Pemain dan AI bergantian memilih tindakan.
Jika HP salah satu robot habis atau mencapai batas ronde, pertarungan berakhir.

5. Fitur Menarik:
Mode Pertahanan: Mengurangi damage serangan lawan dan memberikan HP tambahan.
Serangan Khusus: Plasma Cannon dengan damage besar tetapi akurasi lebih rendah.
AI Sederhana: AI memilih tindakan secara acak dengan kecenderungan bertahan jika HP rendah.
