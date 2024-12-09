CREATE OR REPLACE FUNCTION cek_nomor_hp(no_hp VARCHAR)
RETURNS VOID AS $$
DECLARE
jumlah INT;
BEGIN
SELECT COUNT(*) INTO jumlah
  FROM public.USER
  WHERE NoHP = no_hp;

  IF jumlah > 0 THEN
      RAISE EXCEPTION 'Nomor HP % sudah terdaftar.', no_hp;
  END IF;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION trigger_cek_nomor_hp()
RETURNS TRIGGER AS $$
BEGIN
  PERFORM cek_nomor_hp(NEW.NoHP);
  -- Lanjutkan proses insert
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER sebelum_insert_user
BEFORE INSERT ON public.USER
FOR EACH ROW
EXECUTE FUNCTION trigger_cek_nomor_hp();


CREATE OR REPLACE FUNCTION transfer_honor_transaksi()
RETURNS TRIGGER AS $$
DECLARE
    nominal_transaksi DECIMAL;
    id_pekerja UUID;
BEGIN
    -- Periksa apakah status pemesanan adalah "Pesanan selesai"
    IF (NEW.IdStatus IS NOT NULL) THEN
        -- Ambil nominal transaksi dan pekerja terkait
        SELECT 
            TotalBiaya, 
            IdPekerja 
        INTO 
            nominal_transaksi, 
            id_pekerja
        FROM 
            public.TR_PEMESANAN_JASA
        WHERE 
            Id = NEW.IdTrPemesanan;

        -- Tambahkan nominal transaksi ke saldo MyPay pekerja
        UPDATE 
            public.USER
        SET 
            SaldoMyPay = SaldoMyPay + nominal_transaksi
        WHERE Id = id_pekerja;


        -- Catat transaksi ke TR_MYPAY
        INSERT INTO public.TR_MYPAY (
            Id, UserId, Tgl, Nominal, KategoriId
        ) VALUES (
            gen_random_uuid(),      -- ID baru
            id_pekerja,             -- ID pekerja
            CURRENT_DATE,           -- Tanggal saat ini
            nominal_transaksi,      -- Nominal transaksi
            '41f85ca1-38dc-44fc-9283-25e2117f8d06' -- Kategori
        );
    END IF;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER proses_transfer_honor
AFTER UPDATE ON public.TR_PEMESANAN_STATUS
FOR EACH ROW
WHEN (NEW.IdStatus = 'd2d5bb1b-7c78-4e5e-b0ac-06e6da102a4a')
EXECUTE FUNCTION transfer_honor_transaksi();


CREATE OR REPLACE FUNCTION public.update_status(
    p_idtrpemesanan UUID
)
RETURNS VOID AS $$
DECLARE 
    current_status_id UUID;
BEGIN
    -- Fetch the current status ID
    SELECT idstatus 
    INTO current_status_id
    FROM public.tr_pemesanan_status
    WHERE idtrpemesanan = p_idtrpemesanan;

    -- Check if a record was found
    IF current_status_id IS NOT NULL THEN
        -- Update the status based on the current status ID
        IF current_status_id = '3fa85f64-5717-4562-b3fc-2c963f66afa6' THEN
            current_status_id := 'a7c7a58e-197b-4e25-a7c1-9fda1e0d60a9';
        ELSIF current_status_id = 'a7c7a58e-197b-4e25-a7c1-9fda1e0d60a9' THEN
            current_status_id := '5b5a0ce2-5c7f-4b9b-8c1e-1e2a11b3e3c3';
        ELSIF current_status_id = '5b5a0ce2-5c7f-4b9b-8c1e-1e2a11b3e3c3' THEN
            current_status_id := 'e0bebe06-5c2c-4f8a-92f4-b8fdd0a3d3c8';
        ELSIF current_status_id = 'e0bebe06-5c2c-4f8a-92f4-b8fdd0a3d3c8' THEN
            current_status_id := 'c86aed0f-4a2f-4e85-81bf-d4eecfa1c555';
        ELSIF current_status_id = 'c86aed0f-4a2f-4e85-81bf-d4eecfa1c555' THEN
            current_status_id := 'd2d5bb1b-7c78-4e5e-b0ac-06e6da102a4a';
        ELSE
            current_status_id := '7f9e3b98-9a3c-4f7a-b7e6-7a5e5e3d6f7c';
        END IF;

        -- Update the table
        UPDATE public.tr_pemesanan_status
        SET 
            idstatus = current_status_id, 
            tglwaktu = NOW()
        WHERE 
            idtrpemesanan = p_idtrpemesanan;

    ELSE
        -- Handle the case where no record was found
        RAISE NOTICE 'No record found for idtrpemesanan %', p_idtrpemesanan;
    END IF;
END;
$$ LANGUAGE plpgsql;

-- tambahkan sql trigger kalian