from django.db import connection

def reset():
    with connection.cursor() as cursor:
        cursor.execute(
            '''
            delete from public.TR_MYPAY;
            delete from public.tr_pemesanan_status;
            delete from public.testimoni;
            delete from public.TR_PEMESANAN_JASA;
            delete from public.tr_pembelian_voucher;
            delete from public.KATEGORI_TR_MYPAY;
            delete from public.Promo;
            delete from public.Voucher;
            delete from public.Diskon;
            delete from public.Sesi_layanan;
            delete from public.Subkategori_jasa;
            delete from public.pekerja_kategori_jasa;
            delete from public.KATEGORI_JASA;
            delete from public.PELANGGAN;
            delete from public.PEKERJA;
            delete from public.Session;
            delete from public.USER;
            delete from public.status_pesanan;
            delete from public.metode_bayar;

            INSERT INTO public.metode_bayar (Id, Nama) VALUES
            ('f3bdee97-1a7b-4d8f-b8c0-2a7cba2677cb', 'MyPay'),
            ('a9c2f9e6-5d3a-4f7b-9e0e-3c6d5f8e1b2c', 'GoPay'),
            ('c7d3e8f9-6b4c-4a8d-af1e-4d5e6f7e8f9a', 'BCA'),
            ('d8e4f0a1-7c5d-4b9e-b0af-5e6f7e8f9a0b', 'Mandiri'),
            ('e9f5a1b2-8d6e-4c0f-c1b0-6f7e8f9a0b1c', 'BNI'),
            ('f0a6b2c3-9e7f-4d1f-d2c1-7e8f9a0b1c2d', 'ShopeePay');

            INSERT INTO public.status_pesanan (Id, Status) VALUES
            ('3fa85f64-5717-4562-b3fc-2c963f66afa6', 'Menunggu Pembayaran'),
            ('a7c7a58e-197b-4e25-a7c1-9fda1e0d60a9', 'Pembayaran Dikonfirmasi'),
            ('5b5a0ce2-5c7f-4b9b-8c1e-1e2a11b3e3c3', 'Mencari Pekerja Terdekat'),
            ('e0bebe06-5c2c-4f8a-92f4-b8fdd0a3d3c8', 'Pekerja Sedang Menuju Lokasi'),
            ('c86aed0f-4a2f-4e85-81bf-d4eecfa1c555', 'Pekerjaan Sedang Dilaksanakan'),
            ('d2d5bb1b-7c78-4e5e-b0ac-06e6da102a4a', 'Pekerjaan Selesai'),
            ('7f9e3b98-9a3c-4f7a-b7e6-7a5e5e3d6f7c', 'Ulasan Diberikan');

            INSERT INTO public.USER (Id, Nama, JenisKelamin, NoHP, Pwd, TglLahir, Alamat, SaldoMyPay) VALUES
            ('449bd0dd-234f-45a2-9372-3c4efe31b78e', 'Brett Morales', 'P', 54916602468, 'wkwt5yGe6s', '1981-12-14', '46627 Arthur Spurs Garciamouth, ND 84367', 41706.4),
            ('d7b19de3-804b-424c-a606-421a7afb2c72', 'Steven Young', 'L', 87896445962, 'k9aXEwsoFH', '1992-10-05', '326 Brian Mills Suite 399 East Barryfort, MN 52602', 44045.07),
            ('92ca766f-b63a-4867-9fdd-0872d12e41c3', 'Donna Maldonado', 'L', 22409428586, 'v173ry1srh', '1987-02-24', '14019 Harris Walks West Brandon, AK 60918', 42804.37),
            ('5e42b91b-35fb-4176-8de5-4e227a49e2cf', 'Kristen Miller', 'P', 26333292043, 'TEjDE3NEWq', '1988-09-04', '5740 Ramirez Turnpike Apt. 100 Estradamouth, AR 43717', 83117.42),
            ('ab1beb35-bfcb-429a-985e-1657bb07f5d4', 'Maxwell Duncan', 'P', 12344873578, '6Sy1Jlrc0n', '2004-02-08', '303 Smith Avenue Edwardport, WV 57957', 54351.97),
            ('99e7da77-1d61-4e7f-b7d2-cd8f5533a7af', 'Karen Gates', 'L', 33090443919, 'Xdh62Pz1xb', '1993-09-29', '37108 Powers Dale Suite 589 Huntborough, IL 77931', 51076.61),
            ('bf777476-d869-48b3-962d-5980d0699db7', 'John Murray', 'L', 67700142384, 'V6LQy9LlNW', '1978-05-30', '929 Santos Locks Acostaburgh, VA 69971', 72337.76),
            ('fc9713d5-f091-4034-8a5f-4cdadbe65a83', 'Mary Mcclain', 'P', 37606207672, 'hBLxRVoXpg', '2006-09-02', 'USNV Rios FPO AE 86607', 25789.29),
            ('43ff7137-7338-4a66-b63b-299489dd6de9', 'Matthew Benitez', 'P', 21479512858, 'zBs60e1mOB', '1971-01-26', '693 Lucero Crest Lake Stephenstad, FL 16942', 78933.59),
            ('41b78933-2eb2-4753-b24a-ffe53d4c0201', 'Dawn Jones', 'P', 13922977214, '7r3NKT7wFi', '1990-03-05', '0146 Munoz Cove Apt. 376 Tracyview, ND 94381', 34917.82);


            INSERT INTO public.pekerja (Id, NamaBank, NomorRekening, NPWP, LinkFoto, Rating, jmlpsnananselesai) VALUES
            ('41b78933-2eb2-4753-b24a-ffe53d4c0201', 'BCA', 66596550, 5423710525472926, 'https://dummyimage.com/200x200', 3.06, 86),
            ('d7b19de3-804b-424c-a606-421a7afb2c72', 'BCA', 93164236, 6113769174512041, 'https://www.lorempixel.com/200/200', 1.04, 22),
            ('ab1beb35-bfcb-429a-985e-1657bb07f5d4', 'BCA', 30416484, 5691483255505346, 'https://placekitten.com/200/200', 3.86, 26),
            ('bf777476-d869-48b3-962d-5980d0699db7', 'BCA', 77014880, 7239876109507875, 'https://www.lorempixel.com/200/200', 5.97, 97),
            ('449bd0dd-234f-45a2-9372-3c4efe31b78e', 'BNI', 77162578, 5728507554994395, 'https://placekitten.com/200/200', 3.1, 4);


            INSERT INTO public.pelanggan (Id, Level) VALUES
            ('99e7da77-1d61-4e7f-b7d2-cd8f5533a7af', 'Gold'),
            ('43ff7137-7338-4a66-b63b-299489dd6de9', 'Basic'),
            ('fc9713d5-f091-4034-8a5f-4cdadbe65a83', 'Gold'),
            ('92ca766f-b63a-4867-9fdd-0872d12e41c3', 'Gold'),
            ('5e42b91b-35fb-4176-8de5-4e227a49e2cf', 'Basic');

            INSERT INTO public.kategori_jasa (Id, NamaKategori) VALUES
            ('f47ac10b-58cc-4372-a567-0e02b2c3d479', 'Home cleaning'),
            ('c9bf9e57-1685-4c89-bafb-ff5af830be8a', 'Deep cleaning'),
            ('7c9e6679-7425-40de-944b-e07fc1f90ae7', 'Cloth cleaning'),
            ('e4eaaaf2-d142-11e1-b3e4-080027620cdd', 'Car cleaning'),
            ('1b4e28ba-2fa1-11d2-883f-0016d3cca427', 'Shoes cleaning');


            INSERT INTO public.pekerja_kategori_jasa (PekerjaId, KategoriJasaId) VALUES
            ('449bd0dd-234f-45a2-9372-3c4efe31b78e', 'f47ac10b-58cc-4372-a567-0e02b2c3d479'),
            ('449bd0dd-234f-45a2-9372-3c4efe31b78e', 'e4eaaaf2-d142-11e1-b3e4-080027620cdd'),
            ('d7b19de3-804b-424c-a606-421a7afb2c72', '1b4e28ba-2fa1-11d2-883f-0016d3cca427'),
            ('d7b19de3-804b-424c-a606-421a7afb2c72', 'e4eaaaf2-d142-11e1-b3e4-080027620cdd'),
            ('ab1beb35-bfcb-429a-985e-1657bb07f5d4', 'f47ac10b-58cc-4372-a567-0e02b2c3d479'),
            ('ab1beb35-bfcb-429a-985e-1657bb07f5d4', 'e4eaaaf2-d142-11e1-b3e4-080027620cdd'),
            ('bf777476-d869-48b3-962d-5980d0699db7', 'e4eaaaf2-d142-11e1-b3e4-080027620cdd'),
            ('bf777476-d869-48b3-962d-5980d0699db7', 'c9bf9e57-1685-4c89-bafb-ff5af830be8a'),
            ('41b78933-2eb2-4753-b24a-ffe53d4c0201', '1b4e28ba-2fa1-11d2-883f-0016d3cca427'),
            ('41b78933-2eb2-4753-b24a-ffe53d4c0201', '7c9e6679-7425-40de-944b-e07fc1f90ae7');


            INSERT INTO public.subkategori_jasa (Id, NamaSubkategori, Deskripsi, KategoriJasaId) VALUES
            ('4e5c6f50-ff92-4ddd-9a87-1e54b877d1b6', 'Menyapu', 'Layanan menyapu untuk kategori kj1.', 'f47ac10b-58cc-4372-a567-0e02b2c3d479'),
            ('9a4b55a1-1e06-487a-96a1-96e6def15536', 'Mengepel', 'Layanan mengepel untuk kategori kj1.', 'f47ac10b-58cc-4372-a567-0e02b2c3d479'),
            ('fbb3c87c-6ef0-4abc-b47e-101e34418e5a', 'Cuci Sofa', 'Layanan cuci sofa untuk kategori kj2.', 'c9bf9e57-1685-4c89-bafb-ff5af830be8a'),
            ('76162ca9-1f74-4ee9-9e22-1bed774c14da', 'Polish Furniture', 'Layanan polish furniture untuk kategori kj2.', 'c9bf9e57-1685-4c89-bafb-ff5af830be8a'),
            ('a0a915e9-3dcc-42f0-9833-7eba5a6c799d', 'Laundry Biasa', 'Layanan laundry biasa untuk kategori kj3.', '7c9e6679-7425-40de-944b-e07fc1f90ae7'),
            ('c0d686c8-66da-4d2d-ad55-d473c71afecb', 'Dry Cleaning', 'Layanan dry cleaning untuk kategori kj3.', '7c9e6679-7425-40de-944b-e07fc1f90ae7'),
            ('2cc2f4ac-bda2-4475-a811-5310c6c22f20', 'Cuci Eksterior', 'Layanan cuci eksterior untuk kategori kj4.', 'e4eaaaf2-d142-11e1-b3e4-080027620cdd'),
            ('b3e7de9f-4353-4c78-8c1d-1f1e6b5da16d', 'Cuci Interior', 'Layanan cuci interior untuk kategori kj4.', 'e4eaaaf2-d142-11e1-b3e4-080027620cdd'),
            ('b704f9f7-bedb-4e49-b751-e3764e91712e', 'Cuci Sneakers', 'Layanan cuci sneakers untuk kategori kj5.', '1b4e28ba-2fa1-11d2-883f-0016d3cca427'),
            ('fe9cc4a3-8f35-43bd-924a-92910a70caca', 'Cuci Boots', 'Layanan cuci boots untuk kategori kj5.', '1b4e28ba-2fa1-11d2-883f-0016d3cca427');


            INSERT INTO public.sesi_layanan (SubkategoriId, Sesi, Harga) VALUES
            ('4e5c6f50-ff92-4ddd-9a87-1e54b877d1b6', 1, 116.92),
            ('4e5c6f50-ff92-4ddd-9a87-1e54b877d1b6', 2, 175.8),
            ('4e5c6f50-ff92-4ddd-9a87-1e54b877d1b6', 3, 50.04),
            ('9a4b55a1-1e06-487a-96a1-96e6def15536', 1, 210.86),
            ('9a4b55a1-1e06-487a-96a1-96e6def15536', 2, 479.33),
            ('9a4b55a1-1e06-487a-96a1-96e6def15536', 3, 317.03),
            ('fbb3c87c-6ef0-4abc-b47e-101e34418e5a', 1, 266.49),
            ('fbb3c87c-6ef0-4abc-b47e-101e34418e5a', 2, 298.99),
            ('fbb3c87c-6ef0-4abc-b47e-101e34418e5a', 3, 461.96),
            ('76162ca9-1f74-4ee9-9e22-1bed774c14da', 1, 461.93),
            ('76162ca9-1f74-4ee9-9e22-1bed774c14da', 2, 183.6),
            ('76162ca9-1f74-4ee9-9e22-1bed774c14da', 3, 151.66),
            ('a0a915e9-3dcc-42f0-9833-7eba5a6c799d', 1, 341.26),
            ('a0a915e9-3dcc-42f0-9833-7eba5a6c799d', 2, 56.02),
            ('a0a915e9-3dcc-42f0-9833-7eba5a6c799d', 3, 479.69),
            ('c0d686c8-66da-4d2d-ad55-d473c71afecb', 1, 278.99),
            ('c0d686c8-66da-4d2d-ad55-d473c71afecb', 2, 89.64),
            ('c0d686c8-66da-4d2d-ad55-d473c71afecb', 3, 472.72),
            ('2cc2f4ac-bda2-4475-a811-5310c6c22f20', 1, 336.51),
            ('2cc2f4ac-bda2-4475-a811-5310c6c22f20', 2, 59.2),
            ('2cc2f4ac-bda2-4475-a811-5310c6c22f20', 3, 103.47),
            ('b3e7de9f-4353-4c78-8c1d-1f1e6b5da16d', 1, 67.97),
            ('b3e7de9f-4353-4c78-8c1d-1f1e6b5da16d', 2, 266.87),
            ('b3e7de9f-4353-4c78-8c1d-1f1e6b5da16d', 3, 337.65),
            ('b704f9f7-bedb-4e49-b751-e3764e91712e', 1, 323.98),
            ('b704f9f7-bedb-4e49-b751-e3764e91712e', 2, 163.3),
            ('b704f9f7-bedb-4e49-b751-e3764e91712e', 3, 336.54),
            ('fe9cc4a3-8f35-43bd-924a-92910a70caca', 1, 488.48),
            ('fe9cc4a3-8f35-43bd-924a-92910a70caca', 2, 164.76),
            ('fe9cc4a3-8f35-43bd-924a-92910a70caca', 3, 90.1);


            INSERT INTO public.diskon (Kode, Potongan, MinTrPemesanan) VALUES
            ('2ZU8H33BDH3JUSCCI6Y5XKE6R2V3UR', 26.58, 2),
            ('QJCW3A60IDQ7I2RTXJ6TE2ZWOLS89O', 41.31, 8),
            ('1XXNAS7KAE1ZC7BVH658PDRP5R0QU6', 37.34, 3),
            ('ZIYN8T1CX8U88ACCFIUAKGLGVTICOI', 15.65, 2),
            ('TE6KY1379GO8OSKKGZR0U9VR408WR3', 27.24, 6),
            ('W5RPZ0AHX4AH940S5A90N85H2D83HS', 30.72, 6),
            ('40ICJUD7QUBTBW8SZUHI4TVBH95WGG', 31.08, 6),
            ('3MHNW9RSN7QQ4QI9MBK33XFCXA9ZTY', 26.96, 10),
            ('XE5GZ07V4AQUJTMUEDRV5W6KECNAX0', 10.46, 8),
            ('44Y76QPDQORNY99QOCUIRQ2PBP7RIB', 11.12, 1),
            ('HAZW5H18JY83G4LCISR6QWKJ6YON5I', 49.9, 2),
            ('TMVM5TRX7WPSUJ6L3O41VMGLM9LBO3', 36.69, 6),
            ('221AKEQ7054WNZ7JDF37RSXQYZS7LY', 45.86, 8),
            ('Z461U2OFGKWGQUFBZT514FSA3PC6EO', 17.56, 8),
            ('WC1MQGPHLOX2PJJ8HWKYI3GY51ZSA0', 31.19, 4),
            ('7G3H0G4IWOHONWP81F2R1ILVTQUNP8', 18.71, 7),
            ('GUOPFFXMROX38EDKZFTEXY7KTB9KNS', 17.37, 2),
            ('MW6GTHCXY5TVF30IDEIE7AW97KVT0K', 45.14, 5),
            ('M2I6JI18TEMSM59NBQQJLKUKWNBO14', 27.26, 8),
            ('X8RJUW0IOXWVRB066ZU6KRR0IJPJAJ', 8.11, 4);


            INSERT INTO public.voucher (Kode, JmlHariBerlaku, KuotaPenggunaan, Harga) VALUES
            ('HAZW5H18JY83G4LCISR6QWKJ6YON5I', 12, 42, 51.53),
            ('2ZU8H33BDH3JUSCCI6Y5XKE6R2V3UR', 20, 18, 20.02),
            ('1XXNAS7KAE1ZC7BVH658PDRP5R0QU6', 8, 22, 26.68),
            ('221AKEQ7054WNZ7JDF37RSXQYZS7LY', 1, 31, 55.24),
            ('XE5GZ07V4AQUJTMUEDRV5W6KECNAX0', 26, 79, 22.47),
            ('WC1MQGPHLOX2PJJ8HWKYI3GY51ZSA0', 29, 14, 37.95),
            ('GUOPFFXMROX38EDKZFTEXY7KTB9KNS', 9, 43, 93.74),
            ('TE6KY1379GO8OSKKGZR0U9VR408WR3', 19, 75, 44.81),
            ('X8RJUW0IOXWVRB066ZU6KRR0IJPJAJ', 3, 11, 24.27),
            ('Z461U2OFGKWGQUFBZT514FSA3PC6EO', 19, 26, 80.89);


            INSERT INTO public.promo (Kode, TglAkhirBerlaku) VALUES
            ('ZIYN8T1CX8U88ACCFIUAKGLGVTICOI', '2024-07-17'),
            ('W5RPZ0AHX4AH940S5A90N85H2D83HS', '2024-01-31'),
            ('QJCW3A60IDQ7I2RTXJ6TE2ZWOLS89O', '2024-05-10'),
            ('MW6GTHCXY5TVF30IDEIE7AW97KVT0K', '2024-02-03'),
            ('3MHNW9RSN7QQ4QI9MBK33XFCXA9ZTY', '2024-04-14'),
            ('7G3H0G4IWOHONWP81F2R1ILVTQUNP8', '2024-06-20'),
            ('40ICJUD7QUBTBW8SZUHI4TVBH95WGG', '2024-12-17'),
            ('M2I6JI18TEMSM59NBQQJLKUKWNBO14', '2024-12-09'),
            ('44Y76QPDQORNY99QOCUIRQ2PBP7RIB', '2024-04-19'),
            ('TMVM5TRX7WPSUJ6L3O41VMGLM9LBO3', '2024-03-23');

            INSERT INTO public.kategori_tr_mypay (Id, Nama) VALUES
            ('41f85ca1-38dc-44fc-9283-25e2117f8d06', 'Transaksi'),
            ('8c7f9ffd-b369-470f-a59e-8bba08086923', 'Transfer'),
            ('cbf1aba9-2d20-45d6-844f-115cfabd252e', 'Topup'),
            ('ec3e3a32-84b4-419a-8717-f8eae1c75f60', 'Withdraw'),
            ('b92106c1-9b77-4a61-9e2f-a7d1860c3e5f', 'Null');


            INSERT INTO public.tr_pembelian_voucher (Id, TglAwal, TglAkhir, TelahDigunakan, IdPelanggan, IdVoucher, IdMetodeBayar) VALUES
            ('f4e522fc-20e9-49aa-b89a-713da76d60c0', '2024-12-17', '2024-08-24', 4, 'fc9713d5-f091-4034-8a5f-4cdadbe65a83', 'HAZW5H18JY83G4LCISR6QWKJ6YON5I', 'e9f5a1b2-8d6e-4c0f-c1b0-6f7e8f9a0b1c'),
            ('90bbd449-15e5-43c1-af64-e24ada0e2b33', '2024-04-02', '2024-02-13', 8, '43ff7137-7338-4a66-b63b-299489dd6de9', 'WC1MQGPHLOX2PJJ8HWKYI3GY51ZSA0', 'f3bdee97-1a7b-4d8f-b8c0-2a7cba2677cb'),
            ('19c8330d-1bda-4fbc-9e2d-51785e4f4536', '2024-12-05', '2024-12-14', 10, '99e7da77-1d61-4e7f-b7d2-cd8f5533a7af', 'GUOPFFXMROX38EDKZFTEXY7KTB9KNS', 'f0a6b2c3-9e7f-4d1f-d2c1-7e8f9a0b1c2d'),
            ('588c4221-4172-42d2-a2cf-2031c381a8ee', '2024-12-02', '2024-03-02', 5, 'fc9713d5-f091-4034-8a5f-4cdadbe65a83', 'WC1MQGPHLOX2PJJ8HWKYI3GY51ZSA0', 'e9f5a1b2-8d6e-4c0f-c1b0-6f7e8f9a0b1c'),
            ('fbacc87f-ad83-4b10-b75a-7d3231bd7713', '2024-07-11', '2024-08-19', 2, '92ca766f-b63a-4867-9fdd-0872d12e41c3', '221AKEQ7054WNZ7JDF37RSXQYZS7LY', 'e9f5a1b2-8d6e-4c0f-c1b0-6f7e8f9a0b1c'),
            ('d9ee6126-a7bf-47be-a3b2-92b420ed770e', '2024-06-24', '2024-07-04', 3, 'fc9713d5-f091-4034-8a5f-4cdadbe65a83', 'HAZW5H18JY83G4LCISR6QWKJ6YON5I', 'e9f5a1b2-8d6e-4c0f-c1b0-6f7e8f9a0b1c'),
            ('299cd9b2-56af-4241-b36d-6357604829e2', '2024-08-11', '2024-01-27', 7, '99e7da77-1d61-4e7f-b7d2-cd8f5533a7af', '2ZU8H33BDH3JUSCCI6Y5XKE6R2V3UR', 'e9f5a1b2-8d6e-4c0f-c1b0-6f7e8f9a0b1c'),
            ('a6e0241a-bd4c-46ab-995c-336742548ede', '2024-03-08', '2024-01-04', 4, '99e7da77-1d61-4e7f-b7d2-cd8f5533a7af', '221AKEQ7054WNZ7JDF37RSXQYZS7LY', 'd8e4f0a1-7c5d-4b9e-b0af-5e6f7e8f9a0b'),
            ('446922a7-dc06-4c68-9a14-f22881e6adc1', '2024-02-24', '2024-02-11', 4, '5e42b91b-35fb-4176-8de5-4e227a49e2cf', '221AKEQ7054WNZ7JDF37RSXQYZS7LY', 'f3bdee97-1a7b-4d8f-b8c0-2a7cba2677cb'),
            ('8c656b08-b742-44b4-b700-9301041dcb51', '2024-11-29', '2024-09-12', 5, '43ff7137-7338-4a66-b63b-299489dd6de9', 'XE5GZ07V4AQUJTMUEDRV5W6KECNAX0', 'd8e4f0a1-7c5d-4b9e-b0af-5e6f7e8f9a0b'),
            ('ecd68501-1d76-4bc4-98a6-118b5fca15b4', '2024-11-09', '2024-04-24', 0, 'fc9713d5-f091-4034-8a5f-4cdadbe65a83', 'WC1MQGPHLOX2PJJ8HWKYI3GY51ZSA0', 'f0a6b2c3-9e7f-4d1f-d2c1-7e8f9a0b1c2d'),
            ('1b78fac0-5d1c-4c68-bf5c-892ff6a28eb9', '2024-09-11', '2024-10-29', 4, '5e42b91b-35fb-4176-8de5-4e227a49e2cf', 'HAZW5H18JY83G4LCISR6QWKJ6YON5I', 'a9c2f9e6-5d3a-4f7b-9e0e-3c6d5f8e1b2c'),
            ('bb6a6ea5-7752-48e7-acd5-3fb32369271e', '2024-11-23', '2024-01-27', 2, '99e7da77-1d61-4e7f-b7d2-cd8f5533a7af', 'GUOPFFXMROX38EDKZFTEXY7KTB9KNS', 'd8e4f0a1-7c5d-4b9e-b0af-5e6f7e8f9a0b'),
            ('7045891d-2aa6-4afa-b623-db9db938431e', '2024-08-16', '2024-08-07', 8, '99e7da77-1d61-4e7f-b7d2-cd8f5533a7af', '1XXNAS7KAE1ZC7BVH658PDRP5R0QU6', 'e9f5a1b2-8d6e-4c0f-c1b0-6f7e8f9a0b1c'),
            ('446d53ca-c833-4236-ba15-f55cf3225c9f', '2024-08-10', '2024-06-04', 9, '5e42b91b-35fb-4176-8de5-4e227a49e2cf', 'WC1MQGPHLOX2PJJ8HWKYI3GY51ZSA0', 'e9f5a1b2-8d6e-4c0f-c1b0-6f7e8f9a0b1c'),
            ('1d533445-0a2a-46d3-9e4c-af3db7a5031b', '2024-12-17', '2024-11-02', 7, '92ca766f-b63a-4867-9fdd-0872d12e41c3', 'TE6KY1379GO8OSKKGZR0U9VR408WR3', 'a9c2f9e6-5d3a-4f7b-9e0e-3c6d5f8e1b2c'),
            ('16b6c122-9f87-4e12-8894-efb6d176cb51', '2024-10-22', '2024-03-03', 10, '99e7da77-1d61-4e7f-b7d2-cd8f5533a7af', 'HAZW5H18JY83G4LCISR6QWKJ6YON5I', 'c7d3e8f9-6b4c-4a8d-af1e-4d5e6f7e8f9a'),
            ('84369729-bf3d-4ef8-92b6-6d46028b1526', '2024-06-09', '2024-02-29', 0, '92ca766f-b63a-4867-9fdd-0872d12e41c3', 'XE5GZ07V4AQUJTMUEDRV5W6KECNAX0', 'd8e4f0a1-7c5d-4b9e-b0af-5e6f7e8f9a0b');

            INSERT INTO public.tr_pemesanan_jasa (Id, TglPemesanan, TglPekerjaan, WaktuPekerjaan, TotalBiaya, IdPelanggan, IdPekerja, IdKategoriJasa, Sesi, IdDiskon, IdMetodeBayar) VALUES
            ('06bc4df1-3fc6-4b19-89a2-e053c9262433', '2024-11-13', '2024-01-07', '2024-01-01 09:07:00', 568.62, '5e42b91b-35fb-4176-8de5-4e227a49e2cf', 'bf777476-d869-48b3-962d-5980d0699db7', '4e5c6f50-ff92-4ddd-9a87-1e54b877d1b6', 2, 'QJCW3A60IDQ7I2RTXJ6TE2ZWOLS89O', 'd8e4f0a1-7c5d-4b9e-b0af-5e6f7e8f9a0b'),
            ('ffc73de3-251d-4c22-a892-6ad53602de3a', '2024-03-29', '2024-06-06', '2024-01-01 08:20:00', 471.38, '92ca766f-b63a-4867-9fdd-0872d12e41c3', 'd7b19de3-804b-424c-a606-421a7afb2c72', '2cc2f4ac-bda2-4475-a811-5310c6c22f20', 2, '7G3H0G4IWOHONWP81F2R1ILVTQUNP8', 'd8e4f0a1-7c5d-4b9e-b0af-5e6f7e8f9a0b'),
            ('a1d1ac3a-5d4d-4d88-810b-a914808a1266', '2024-01-11', '2024-10-13', '2024-01-01 01:29:00', 874.58, '99e7da77-1d61-4e7f-b7d2-cd8f5533a7af', 'd7b19de3-804b-424c-a606-421a7afb2c72', 'a0a915e9-3dcc-42f0-9833-7eba5a6c799d', 3, 'X8RJUW0IOXWVRB066ZU6KRR0IJPJAJ', 'a9c2f9e6-5d3a-4f7b-9e0e-3c6d5f8e1b2c'),
            ('1d8da023-f56d-4a19-a108-030f6ea981d4', '2024-05-20', '2024-04-16', '2024-01-01 04:56:00', 473.36, 'fc9713d5-f091-4034-8a5f-4cdadbe65a83', 'bf777476-d869-48b3-962d-5980d0699db7', '4e5c6f50-ff92-4ddd-9a87-1e54b877d1b6', 1, 'WC1MQGPHLOX2PJJ8HWKYI3GY51ZSA0', 'c7d3e8f9-6b4c-4a8d-af1e-4d5e6f7e8f9a'),
            ('594b03c6-396f-4074-a541-cbb099ef2d44', '2024-04-17', '2024-10-03', '2024-01-01 07:00:00', 791.51, '99e7da77-1d61-4e7f-b7d2-cd8f5533a7af', '449bd0dd-234f-45a2-9372-3c4efe31b78e', '4e5c6f50-ff92-4ddd-9a87-1e54b877d1b6', 3, '2ZU8H33BDH3JUSCCI6Y5XKE6R2V3UR', 'f0a6b2c3-9e7f-4d1f-d2c1-7e8f9a0b1c2d'),
            ('80a1f173-f481-4ee5-aa83-87559434e4f6', '2024-08-27', '2024-02-10', '2024-01-01 21:55:00', 371.78, 'fc9713d5-f091-4034-8a5f-4cdadbe65a83', '41b78933-2eb2-4753-b24a-ffe53d4c0201', '2cc2f4ac-bda2-4475-a811-5310c6c22f20', 2, '1XXNAS7KAE1ZC7BVH658PDRP5R0QU6', 'e9f5a1b2-8d6e-4c0f-c1b0-6f7e8f9a0b1c'),
            ('b2c737f3-effd-40a4-ac99-9cde846d8008', '2024-06-05', '2024-01-05', '2024-01-01 14:05:00', 829.07, '5e42b91b-35fb-4176-8de5-4e227a49e2cf', 'ab1beb35-bfcb-429a-985e-1657bb07f5d4', '9a4b55a1-1e06-487a-96a1-96e6def15536', 1, '44Y76QPDQORNY99QOCUIRQ2PBP7RIB', 'd8e4f0a1-7c5d-4b9e-b0af-5e6f7e8f9a0b'),
            ('4381db86-a504-4609-bd18-449695bf3f9b', '2024-04-11', '2024-08-31', '2024-01-01 02:26:00', 976.37, '92ca766f-b63a-4867-9fdd-0872d12e41c3', 'bf777476-d869-48b3-962d-5980d0699db7', '2cc2f4ac-bda2-4475-a811-5310c6c22f20', 3, '7G3H0G4IWOHONWP81F2R1ILVTQUNP8', 'e9f5a1b2-8d6e-4c0f-c1b0-6f7e8f9a0b1c'),
            ('ad046db0-c2e9-416b-8166-ed687f83852c', '2024-03-17', '2024-03-10', '2024-01-01 03:51:00', 363.06, '5e42b91b-35fb-4176-8de5-4e227a49e2cf', '449bd0dd-234f-45a2-9372-3c4efe31b78e', '2cc2f4ac-bda2-4475-a811-5310c6c22f20', 1, 'Z461U2OFGKWGQUFBZT514FSA3PC6EO', 'f3bdee97-1a7b-4d8f-b8c0-2a7cba2677cb'),
            ('dd6a5ac9-6842-4d41-9082-3e5a5617576f', '2024-09-02', '2024-05-02', '2024-01-01 05:16:00', 795.84, '43ff7137-7338-4a66-b63b-299489dd6de9', '449bd0dd-234f-45a2-9372-3c4efe31b78e', '9a4b55a1-1e06-487a-96a1-96e6def15536', 2, 'MW6GTHCXY5TVF30IDEIE7AW97KVT0K', 'f0a6b2c3-9e7f-4d1f-d2c1-7e8f9a0b1c2d'),
            ('c94d2bfb-9046-4fdc-8f84-f9bb0f363788', '2024-06-28', '2024-07-22', '2024-01-01 00:55:00', 933.85, '5e42b91b-35fb-4176-8de5-4e227a49e2cf', 'd7b19de3-804b-424c-a606-421a7afb2c72', '2cc2f4ac-bda2-4475-a811-5310c6c22f20', 3, '2ZU8H33BDH3JUSCCI6Y5XKE6R2V3UR', 'e9f5a1b2-8d6e-4c0f-c1b0-6f7e8f9a0b1c'),
            ('4981eea2-0d18-4cdb-9047-03677e2f5096', '2024-12-09', '2024-06-25', '2024-01-01 23:24:00', 501.23, '43ff7137-7338-4a66-b63b-299489dd6de9', 'ab1beb35-bfcb-429a-985e-1657bb07f5d4', '2cc2f4ac-bda2-4475-a811-5310c6c22f20', 1, 'XE5GZ07V4AQUJTMUEDRV5W6KECNAX0', 'f3bdee97-1a7b-4d8f-b8c0-2a7cba2677cb'),
            ('0ac2aa38-55d9-4604-acea-9b890c870f27', '2024-12-22', '2024-05-20', '2024-01-01 03:14:00', 806.3, '43ff7137-7338-4a66-b63b-299489dd6de9', '449bd0dd-234f-45a2-9372-3c4efe31b78e', 'b3e7de9f-4353-4c78-8c1d-1f1e6b5da16d', 1, 'W5RPZ0AHX4AH940S5A90N85H2D83HS', 'd8e4f0a1-7c5d-4b9e-b0af-5e6f7e8f9a0b'),
            ('52c07ca5-9de4-4eb0-a56c-2b3c6fe6bb3c', '2024-03-13', '2024-03-17', '2024-01-01 20:28:00', 283.27, 'fc9713d5-f091-4034-8a5f-4cdadbe65a83', 'd7b19de3-804b-424c-a606-421a7afb2c72', 'b3e7de9f-4353-4c78-8c1d-1f1e6b5da16d', 2, '221AKEQ7054WNZ7JDF37RSXQYZS7LY', 'e9f5a1b2-8d6e-4c0f-c1b0-6f7e8f9a0b1c'),
            ('e9d535bd-a6cd-456c-acbd-0a559ef7ccb0', '2024-04-14', '2024-08-25', '2024-01-01 19:50:00', 810.32, 'fc9713d5-f091-4034-8a5f-4cdadbe65a83', '449bd0dd-234f-45a2-9372-3c4efe31b78e', 'fbb3c87c-6ef0-4abc-b47e-101e34418e5a', 2, 'ZIYN8T1CX8U88ACCFIUAKGLGVTICOI', 'f3bdee97-1a7b-4d8f-b8c0-2a7cba2677cb'),
            ('e682815a-7361-405f-b842-95ddc3e4f42d', '2024-11-23', '2024-03-29', '2024-01-01 00:11:00', 346.43, '43ff7137-7338-4a66-b63b-299489dd6de9', 'ab1beb35-bfcb-429a-985e-1657bb07f5d4', 'c0d686c8-66da-4d2d-ad55-d473c71afecb', 2, 'X8RJUW0IOXWVRB066ZU6KRR0IJPJAJ', 'f0a6b2c3-9e7f-4d1f-d2c1-7e8f9a0b1c2d'),
            ('ab79aa93-fbd7-4efa-ad7f-ef7ad846cbf4', '2024-06-17', '2024-03-09', '2024-01-01 14:32:00', 700.25, '5e42b91b-35fb-4176-8de5-4e227a49e2cf', 'bf777476-d869-48b3-962d-5980d0699db7', 'b3e7de9f-4353-4c78-8c1d-1f1e6b5da16d', 3, '40ICJUD7QUBTBW8SZUHI4TVBH95WGG', 'c7d3e8f9-6b4c-4a8d-af1e-4d5e6f7e8f9a'),
            ('fba97395-62d3-43ee-b134-9930376d94c1', '2024-01-22', '2024-08-03', '2024-01-01 20:20:00', 563.91, '92ca766f-b63a-4867-9fdd-0872d12e41c3', 'd7b19de3-804b-424c-a606-421a7afb2c72', 'b3e7de9f-4353-4c78-8c1d-1f1e6b5da16d', 1, '221AKEQ7054WNZ7JDF37RSXQYZS7LY', 'a9c2f9e6-5d3a-4f7b-9e0e-3c6d5f8e1b2c'),
            ('3879d12f-c7d3-415a-a64e-8ca68a0d890e', '2024-03-13', '2024-01-19', '2024-01-01 23:31:00', 839.34, '99e7da77-1d61-4e7f-b7d2-cd8f5533a7af', 'bf777476-d869-48b3-962d-5980d0699db7', 'b3e7de9f-4353-4c78-8c1d-1f1e6b5da16d', 2, 'XE5GZ07V4AQUJTMUEDRV5W6KECNAX0', 'f0a6b2c3-9e7f-4d1f-d2c1-7e8f9a0b1c2d'),
            ('061abc67-c6a8-4784-81e1-6afcbf0b0658', '2024-08-20', '2024-05-09', '2024-01-01 06:11:00', 607.85, '99e7da77-1d61-4e7f-b7d2-cd8f5533a7af', 'd7b19de3-804b-424c-a606-421a7afb2c72', 'b3e7de9f-4353-4c78-8c1d-1f1e6b5da16d', 1, 'ZIYN8T1CX8U88ACCFIUAKGLGVTICOI', 'd8e4f0a1-7c5d-4b9e-b0af-5e6f7e8f9a0b'),
            ('27519dee-a5e5-4d85-b2c8-307d07be15e9', '2024-04-12', '2024-04-28', '2024-01-01 00:58:00', 562.95, '43ff7137-7338-4a66-b63b-299489dd6de9', 'd7b19de3-804b-424c-a606-421a7afb2c72', 'b3e7de9f-4353-4c78-8c1d-1f1e6b5da16d', 1, 'TMVM5TRX7WPSUJ6L3O41VMGLM9LBO3', 'c7d3e8f9-6b4c-4a8d-af1e-4d5e6f7e8f9a'),
            ('2b82a51e-25aa-4583-ad77-9a707d3ee2bd', '2024-09-04', '2024-04-06', '2024-01-01 12:22:00', 112.04, '99e7da77-1d61-4e7f-b7d2-cd8f5533a7af', 'd7b19de3-804b-424c-a606-421a7afb2c72', 'b704f9f7-bedb-4e49-b751-e3764e91712e', 1, 'ZIYN8T1CX8U88ACCFIUAKGLGVTICOI', 'a9c2f9e6-5d3a-4f7b-9e0e-3c6d5f8e1b2c'),
            ('8296db3a-1d5e-4c64-9aed-d09abad21340', '2024-09-21', '2024-06-29', '2024-01-01 13:23:00', 599.66, '43ff7137-7338-4a66-b63b-299489dd6de9', 'ab1beb35-bfcb-429a-985e-1657bb07f5d4', 'b3e7de9f-4353-4c78-8c1d-1f1e6b5da16d', 3, 'W5RPZ0AHX4AH940S5A90N85H2D83HS', 'c7d3e8f9-6b4c-4a8d-af1e-4d5e6f7e8f9a'),
            ('90ae6377-ab86-4745-8ebd-17079535fcba', '2024-11-04', '2024-09-22', '2024-01-01 05:07:00', 235.71, '5e42b91b-35fb-4176-8de5-4e227a49e2cf', 'bf777476-d869-48b3-962d-5980d0699db7', 'b3e7de9f-4353-4c78-8c1d-1f1e6b5da16d', 1, 'TMVM5TRX7WPSUJ6L3O41VMGLM9LBO3', 'e9f5a1b2-8d6e-4c0f-c1b0-6f7e8f9a0b1c'),
            ('edccb6df-52b3-4e33-ad75-96087a126a32', '2024-06-30', '2024-04-20', '2024-01-01 18:16:00', 151.75, '92ca766f-b63a-4867-9fdd-0872d12e41c3', '41b78933-2eb2-4753-b24a-ffe53d4c0201', 'b3e7de9f-4353-4c78-8c1d-1f1e6b5da16d', 2, 'M2I6JI18TEMSM59NBQQJLKUKWNBO14', 'c7d3e8f9-6b4c-4a8d-af1e-4d5e6f7e8f9a');

            INSERT INTO public.testimoni (IdTrPemesanan, Tgl, Teks, Rating) VALUES
            ('c94d2bfb-9046-4fdc-8f84-f9bb0f363788', '2024-09-11', 'Surface attention audience exactly hair often difference whole.', 6),
            ('a1d1ac3a-5d4d-4d88-810b-a914808a1266', '2024-11-01', 'Successful support continue across child machine skin thing.', 8),
            ('fba97395-62d3-43ee-b134-9930376d94c1', '2024-08-19', 'See born newspaper cell agree town fund question whether.', 7),
            ('8296db3a-1d5e-4c64-9aed-d09abad21340', '2024-11-10', 'Loss behavior guy agency bring one capital view reason yet concern party tough.', 5),
            ('b2c737f3-effd-40a4-ac99-9cde846d8008', '2024-04-16', 'Development pressure effort teach inside material seek.', 7),
            ('80a1f173-f481-4ee5-aa83-87559434e4f6', '2024-04-24', 'Later right theory why quite peace bad use father statement out improve.', 2),
            ('e682815a-7361-405f-b842-95ddc3e4f42d', '2024-03-23', 'Region last animal along there system alone current nor few.', 2),
            ('fba97395-62d3-43ee-b134-9930376d94c1', '2024-10-08', 'Debate after time room author pay debate reality language.', 0),
            ('e9d535bd-a6cd-456c-acbd-0a559ef7ccb0', '2024-03-04', 'Decision time nice provide either consumer would.', 5),
            ('ad046db0-c2e9-416b-8166-ed687f83852c', '2024-08-14', 'Poor program two and lay table reduce fall same.', 10),
            ('b2c737f3-effd-40a4-ac99-9cde846d8008', '2024-08-29', 'Figure century military concern firm them seven sea.', 4),
            ('2b82a51e-25aa-4583-ad77-9a707d3ee2bd', '2024-03-10', 'Alone cause cold then reason hotel general.', 1),
            ('2b82a51e-25aa-4583-ad77-9a707d3ee2bd', '2024-12-17', 'Career table identify early federal up.', 8),
            ('90ae6377-ab86-4745-8ebd-17079535fcba', '2024-03-28', 'Claim perform number rise challenge allow only camera them know water.', 5),
            ('fba97395-62d3-43ee-b134-9930376d94c1', '2024-12-12', 'Person somebody wind difficult floor bed public hope clear across.', 1),
            ('27519dee-a5e5-4d85-b2c8-307d07be15e9', '2024-07-14', 'Sport deal director guy seek where remain whose dinner put large imagine.', 8),
            ('ab79aa93-fbd7-4efa-ad7f-ef7ad846cbf4', '2024-03-24', 'How war central owner administration certain subject might it stage sing clearly eat.', 1);

            INSERT INTO public.tr_pemesanan_status (IdTrPemesanan, IdStatus, TglWaktu) VALUES
            ('fba97395-62d3-43ee-b134-9930376d94c1', '5b5a0ce2-5c7f-4b9b-8c1e-1e2a11b3e3c3', '2024-01-01 17:50:00'),
            ('c94d2bfb-9046-4fdc-8f84-f9bb0f363788', 'c86aed0f-4a2f-4e85-81bf-d4eecfa1c555', '2024-01-01 22:13:00'),
            ('90ae6377-ab86-4745-8ebd-17079535fcba', '3fa85f64-5717-4562-b3fc-2c963f66afa6', '2024-01-01 09:09:00'),
            ('ffc73de3-251d-4c22-a892-6ad53602de3a', 'e0bebe06-5c2c-4f8a-92f4-b8fdd0a3d3c8', '2024-01-01 19:27:00'),
            ('ffc73de3-251d-4c22-a892-6ad53602de3a', '3fa85f64-5717-4562-b3fc-2c963f66afa6', '2024-01-01 01:42:00'),
            ('1d8da023-f56d-4a19-a108-030f6ea981d4', '7f9e3b98-9a3c-4f7a-b7e6-7a5e5e3d6f7c', '2024-01-01 17:58:00'),
            ('fba97395-62d3-43ee-b134-9930376d94c1', '7f9e3b98-9a3c-4f7a-b7e6-7a5e5e3d6f7c', '2024-01-01 05:31:00'),
            ('27519dee-a5e5-4d85-b2c8-307d07be15e9', 'e0bebe06-5c2c-4f8a-92f4-b8fdd0a3d3c8', '2024-01-01 09:01:00'),
            ('52c07ca5-9de4-4eb0-a56c-2b3c6fe6bb3c', '3fa85f64-5717-4562-b3fc-2c963f66afa6', '2024-01-01 08:19:00'),
            ('1d8da023-f56d-4a19-a108-030f6ea981d4', 'c86aed0f-4a2f-4e85-81bf-d4eecfa1c555', '2024-01-01 07:01:00'),
            ('b2c737f3-effd-40a4-ac99-9cde846d8008', '3fa85f64-5717-4562-b3fc-2c963f66afa6', '2024-01-01 11:50:00'),
            ('dd6a5ac9-6842-4d41-9082-3e5a5617576f', 'a7c7a58e-197b-4e25-a7c1-9fda1e0d60a9', '2024-01-01 14:22:00'),
            ('dd6a5ac9-6842-4d41-9082-3e5a5617576f', 'c86aed0f-4a2f-4e85-81bf-d4eecfa1c555', '2024-01-01 04:47:00'),
            ('1d8da023-f56d-4a19-a108-030f6ea981d4', 'e0bebe06-5c2c-4f8a-92f4-b8fdd0a3d3c8', '2024-01-01 05:45:00'),
            ('594b03c6-396f-4074-a541-cbb099ef2d44', 'a7c7a58e-197b-4e25-a7c1-9fda1e0d60a9', '2024-01-01 11:28:00'),
            ('c94d2bfb-9046-4fdc-8f84-f9bb0f363788', '3fa85f64-5717-4562-b3fc-2c963f66afa6', '2024-01-01 09:02:00'),
            ('27519dee-a5e5-4d85-b2c8-307d07be15e9', 'a7c7a58e-197b-4e25-a7c1-9fda1e0d60a9', '2024-01-01 06:41:00'),
            ('3879d12f-c7d3-415a-a64e-8ca68a0d890e', 'e0bebe06-5c2c-4f8a-92f4-b8fdd0a3d3c8', '2024-01-01 20:38:00'),
            ('06bc4df1-3fc6-4b19-89a2-e053c9262433', 'd2d5bb1b-7c78-4e5e-b0ac-06e6da102a4a', '2024-01-01 07:13:00'),
            ('52c07ca5-9de4-4eb0-a56c-2b3c6fe6bb3c', '5b5a0ce2-5c7f-4b9b-8c1e-1e2a11b3e3c3', '2024-01-01 14:30:00'),
            ('e9d535bd-a6cd-456c-acbd-0a559ef7ccb0', '3fa85f64-5717-4562-b3fc-2c963f66afa6', '2024-01-01 10:21:00'),
            ('dd6a5ac9-6842-4d41-9082-3e5a5617576f', '3fa85f64-5717-4562-b3fc-2c963f66afa6', '2024-01-01 06:23:00'),
            ('8296db3a-1d5e-4c64-9aed-d09abad21340', '7f9e3b98-9a3c-4f7a-b7e6-7a5e5e3d6f7c', '2024-01-01 16:53:00'),
            ('0ac2aa38-55d9-4604-acea-9b890c870f27', '7f9e3b98-9a3c-4f7a-b7e6-7a5e5e3d6f7c', '2024-01-01 17:52:00'),
            ('3879d12f-c7d3-415a-a64e-8ca68a0d890e', '5b5a0ce2-5c7f-4b9b-8c1e-1e2a11b3e3c3', '2024-01-01 19:17:00'),
            ('90ae6377-ab86-4745-8ebd-17079535fcba', '7f9e3b98-9a3c-4f7a-b7e6-7a5e5e3d6f7c', '2024-01-01 08:20:00'),
            ('a1d1ac3a-5d4d-4d88-810b-a914808a1266', '5b5a0ce2-5c7f-4b9b-8c1e-1e2a11b3e3c3', '2024-01-01 13:26:00'),
            ('061abc67-c6a8-4784-81e1-6afcbf0b0658', '3fa85f64-5717-4562-b3fc-2c963f66afa6', '2024-01-01 09:42:00'),
            ('06bc4df1-3fc6-4b19-89a2-e053c9262433', '3fa85f64-5717-4562-b3fc-2c963f66afa6', '2024-01-01 21:45:00'),
            ('ab79aa93-fbd7-4efa-ad7f-ef7ad846cbf4', 'e0bebe06-5c2c-4f8a-92f4-b8fdd0a3d3c8', '2024-01-01 19:40:00'),
            ('80a1f173-f481-4ee5-aa83-87559434e4f6', 'e0bebe06-5c2c-4f8a-92f4-b8fdd0a3d3c8', '2024-01-01 02:54:00'),
            ('90ae6377-ab86-4745-8ebd-17079535fcba', 'a7c7a58e-197b-4e25-a7c1-9fda1e0d60a9', '2024-01-01 02:18:00'),
            ('0ac2aa38-55d9-4604-acea-9b890c870f27', 'c86aed0f-4a2f-4e85-81bf-d4eecfa1c555', '2024-01-01 00:39:00'),
            ('edccb6df-52b3-4e33-ad75-96087a126a32', '5b5a0ce2-5c7f-4b9b-8c1e-1e2a11b3e3c3', '2024-01-01 16:40:00'),
            ('ab79aa93-fbd7-4efa-ad7f-ef7ad846cbf4', '7f9e3b98-9a3c-4f7a-b7e6-7a5e5e3d6f7c', '2024-01-01 17:23:00');

            INSERT INTO public.tr_mypay (Id, UserId, Tgl, Nominal, KategoriId) VALUES
            ('6fb2ab13-c559-4993-9598-234d7735bbe3', 'd7b19de3-804b-424c-a606-421a7afb2c72', '2024-10-19', '399.49', '8c7f9ffd-b369-470f-a59e-8bba08086923'),
            ('820c1348-0770-4292-a2c9-3f603f021182', '43ff7137-7338-4a66-b63b-299489dd6de9', '2024-10-19', '-399.49', '8c7f9ffd-b369-470f-a59e-8bba08086923'),
            ('be570e7a-d7ce-46db-b19e-aa1740735a81', '99e7da77-1d61-4e7f-b7d2-cd8f5533a7af', '2024-08-14', '-271.44', 'ec3e3a32-84b4-419a-8717-f8eae1c75f60'),
            ('9dc2f6fd-299e-4b94-bbd2-b859156e4f9e', 'bf777476-d869-48b3-962d-5980d0699db7', '2024-04-13', '530.44', '8c7f9ffd-b369-470f-a59e-8bba08086923'),
            ('f35be4b2-5b21-4fce-84f6-8c6946f722b2', '43ff7137-7338-4a66-b63b-299489dd6de9', '2024-04-13', '-530.44', '8c7f9ffd-b369-470f-a59e-8bba08086923'),
            ('057e52f6-524e-425e-94a0-30cfa3e528c3', 'bf777476-d869-48b3-962d-5980d0699db7', '2024-07-26', '661.19', 'cbf1aba9-2d20-45d6-844f-115cfabd252e'),
            ('caf2e4bc-309b-44a8-93d3-b48167103ee3', 'd7b19de3-804b-424c-a606-421a7afb2c72', '2024-01-09', '-599.59', 'ec3e3a32-84b4-419a-8717-f8eae1c75f60'),
            ('cf5d4c56-7ea0-4f9a-9d28-90ca6497ac49', '41b78933-2eb2-4753-b24a-ffe53d4c0201', '2024-03-26', '778.05', '8c7f9ffd-b369-470f-a59e-8bba08086923'),
            ('f26721bf-cae5-41f6-9372-a83831018501', '92ca766f-b63a-4867-9fdd-0872d12e41c3', '2024-03-26', '-778.05', '8c7f9ffd-b369-470f-a59e-8bba08086923'),
            ('6fffc22b-c471-4490-99c4-7330f8d31b94', '92ca766f-b63a-4867-9fdd-0872d12e41c3', '2024-05-18', '-683.09', 'ec3e3a32-84b4-419a-8717-f8eae1c75f60'),
            ('aa3e4c95-da08-48ef-916e-fbce2f792dcd', '41b78933-2eb2-4753-b24a-ffe53d4c0201', '2024-08-26', '436.48', '8c7f9ffd-b369-470f-a59e-8bba08086923'),
            ('299a0975-14b1-40de-ab19-be63b5cbd4cc', 'fc9713d5-f091-4034-8a5f-4cdadbe65a83', '2024-08-26', '-436.48', '8c7f9ffd-b369-470f-a59e-8bba08086923'),
            ('4e094ffb-798f-4f7b-b5f8-a6865a1e7bf4', '5e42b91b-35fb-4176-8de5-4e227a49e2cf', '2024-01-23', '777.63', '8c7f9ffd-b369-470f-a59e-8bba08086923'),
            ('ad68acb5-7f72-4a63-be34-0e02347c5c56', '449bd0dd-234f-45a2-9372-3c4efe31b78e', '2024-01-23', '-777.63', '8c7f9ffd-b369-470f-a59e-8bba08086923'),
            ('b736b6a8-f4a3-4bf4-b32e-1de6a4e99d4b', 'd7b19de3-804b-424c-a606-421a7afb2c72', '2024-10-28', '203.35', '8c7f9ffd-b369-470f-a59e-8bba08086923'),
            ('e8fc638b-e5d4-4e6e-a3ae-49a606e18a76', 'ab1beb35-bfcb-429a-985e-1657bb07f5d4', '2024-10-28', '-203.35', '8c7f9ffd-b369-470f-a59e-8bba08086923'),
            ('e8ac1a94-49db-413c-8831-382a84e9c236', 'bf777476-d869-48b3-962d-5980d0699db7', '2024-10-08', '575.25', '8c7f9ffd-b369-470f-a59e-8bba08086923'),
            ('86fec0ac-0796-425a-b405-c193c9e53fd5', 'ab1beb35-bfcb-429a-985e-1657bb07f5d4', '2024-10-08', '-575.25', '8c7f9ffd-b369-470f-a59e-8bba08086923'),
            ('d3a0efe2-3668-4e4b-8ff4-29e0b2cee88c', '92ca766f-b63a-4867-9fdd-0872d12e41c3', '2024-12-19', '-957.6', 'ec3e3a32-84b4-419a-8717-f8eae1c75f60'),
            ('4224c0a2-f5dc-41b2-b09a-d53c912c782d', '5e42b91b-35fb-4176-8de5-4e227a49e2cf', '2024-12-12', '576.59', 'cbf1aba9-2d20-45d6-844f-115cfabd252e'),
            ('41cf9ca4-5a33-43a6-9303-8a5235a1e09b', 'bf777476-d869-48b3-962d-5980d0699db7', '2024-12-23', '985.79', 'cbf1aba9-2d20-45d6-844f-115cfabd252e'),
            ('ddf8b86c-04fa-4c85-9fab-f2518e370634', 'fc9713d5-f091-4034-8a5f-4cdadbe65a83', '2024-12-26', '-380.46', 'ec3e3a32-84b4-419a-8717-f8eae1c75f60'),
            ('efbe530d-d8b9-4659-aa39-a9e1d4b4d7be', 'ab1beb35-bfcb-429a-985e-1657bb07f5d4', '2024-11-07', '853.45', 'cbf1aba9-2d20-45d6-844f-115cfabd252e'),
            ('84e90e19-b0bb-4853-b7fc-796de4ebb393', '92ca766f-b63a-4867-9fdd-0872d12e41c3', '2024-11-07', '-377.72', '41f85ca1-38dc-44fc-9283-25e2117f8d06'),
            ('7d0d6d91-f585-4139-b3a3-0d70791273e0', 'fc9713d5-f091-4034-8a5f-4cdadbe65a83', '2024-12-19', '34.03', '8c7f9ffd-b369-470f-a59e-8bba08086923'),
            ('58b5c6d2-207d-4a70-887b-e373acda017b', '41b78933-2eb2-4753-b24a-ffe53d4c0201', '2024-12-19', '-34.03', '8c7f9ffd-b369-470f-a59e-8bba08086923'),
            ('6856eda4-3568-4848-a9b1-15369fa2737c', '449bd0dd-234f-45a2-9372-3c4efe31b78e', '2024-12-02', '312.95', '8c7f9ffd-b369-470f-a59e-8bba08086923'),
            ('ee4f9851-67b7-4fb9-a365-c2b5012d602b', '41b78933-2eb2-4753-b24a-ffe53d4c0201', '2024-12-02', '-312.95', '8c7f9ffd-b369-470f-a59e-8bba08086923'),
            ('cac15467-3577-4b89-835a-fca61eb7c464', '43ff7137-7338-4a66-b63b-299489dd6de9', '2024-10-29', '-310.62', '41f85ca1-38dc-44fc-9283-25e2117f8d06'),
            ('a86a73ec-94f3-4d0b-8d6a-21106124b219', '41b78933-2eb2-4753-b24a-ffe53d4c0201', '2024-05-25', '281.56', 'cbf1aba9-2d20-45d6-844f-115cfabd252e'),
            ('f472f127-de4f-4608-92ab-11a217e28069', 'ab1beb35-bfcb-429a-985e-1657bb07f5d4', '2024-05-15', '487.89', '8c7f9ffd-b369-470f-a59e-8bba08086923'),
            ('63cbcffc-55e7-4ab0-b79b-f7a519b45d66', '99e7da77-1d61-4e7f-b7d2-cd8f5533a7af', '2024-05-15', '-487.89', '8c7f9ffd-b369-470f-a59e-8bba08086923'),
            ('14f43cd1-cd90-4263-98e2-ca846ee9e517', 'ab1beb35-bfcb-429a-985e-1657bb07f5d4', '2024-10-18', '206.91', '8c7f9ffd-b369-470f-a59e-8bba08086923'),
            ('b8e02fbb-8f51-473a-b845-c486442b7cbb', '449bd0dd-234f-45a2-9372-3c4efe31b78e', '2024-10-18', '-206.91', '8c7f9ffd-b369-470f-a59e-8bba08086923'),
            ('64ad2f87-686d-453e-9aca-c3264c57e336', 'fc9713d5-f091-4034-8a5f-4cdadbe65a83', '2024-01-21', '-473.19', 'ec3e3a32-84b4-419a-8717-f8eae1c75f60'),
            ('2c82b29a-a2ba-4d3a-ac5e-85219bba6818', 'ab1beb35-bfcb-429a-985e-1657bb07f5d4', '2024-04-18', '-475.85', 'ec3e3a32-84b4-419a-8717-f8eae1c75f60');
            '''
        )