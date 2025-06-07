from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime, timedelta


def test_airbnb_search_and_book_flow():
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        print("Mengakses situs Airbnb...")
        driver.get("https://www.airbnb.com/")
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.TAG_NAME, "body")))
        print("Berhasil mengakses situs Airbnb.")
        time.sleep(3)

        # Menutup pop-up jika ada
        try:
            close_button = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, "button[aria-label='Close']"))
            )
            close_button.click()
            print("Menutup pop-up (jika ada).")
            time.sleep(1)
        except:
            print(
                "Tidak ada pop-up yang perlu ditutup atau tombol tutup tidak ditemukan.")

        # Mengklik kolom pencarian
        print("Mengklik kolom pencarian utama...")
        search_bar_trigger = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "div[data-testid='structured-search-input-field-split-destination']"))
        )
        search_bar_trigger.click()
        print("Kolom pencarian diklik.")
        time.sleep(1)

        # Memasukkan tujuan
        print("Memasukkan tujuan: 'Bali'...")
        destination_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.ID, "bigsearch-query-detached-query"))
        )
        destination_input.send_keys("Bali")
        print("Tujuan 'Bali' dimasukkan.")
        time.sleep(2)

        destination_input.send_keys(Keys.ENTER)
        print("Menekan Enter untuk mengonfirmasi tujuan.")
        time.sleep(2)

        # Memilih tanggal check-in dan check-out
        print("Memilih tanggal check-in dan check-out...")
        check_in_date = (datetime.now() + timedelta(days=7)
                         ).strftime("%Y-%m-%d")
        check_out_date = (datetime.now() + timedelta(days=14)
                          ).strftime("%Y-%m-%d")

        print(
            f"Menargetkan Check-in: {check_in_date}, Check-out: {check_out_date}")

        try:
            check_in_element = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, f"td[data-testid='datepicker-day-{check_in_date}']"))
            )
            check_in_element.click()
            print(f"Tanggal check-in {check_in_date} dipilih.")
            time.sleep(1)

            check_out_element = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, f"td[data-testid='datepicker-day-{check_out_date}']"))
            )
            check_out_element.click()
            print(f"Tanggal check-out {check_out_date} dipilih.")
            time.sleep(1)

        except Exception as e:
            print(
                f"Gagal memilih tanggal. Mungkin struktur kalender telah berubah atau tanggal tidak tersedia. Error: {e}")
            raise

        # Menambahkan tamu
        print("Menambahkan tamu...")
        guests_section = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "div[data-testid='structured-search-input-field-guests-button']"))
        )
        guests_section.click()
        print("Bagian 'Tamu' diklik.")
        time.sleep(1)

        add_adult_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "button[aria-label='Increase adults']"))
        )
        add_adult_button.click()
        time.sleep(0.5)
        add_adult_button.click()
        print("Menambahkan 2 orang dewasa.")
        time.sleep(1)

        # Mengklik tombol pencarian
        print("Mengklik tombol pencarian...")
        search_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "button[type='submit']"))
        )
        search_button.click()
        print("Tombol pencarian diklik.")
        time.sleep(5)

        # Verifikasi hasil pencarian
        print("Memverifikasi hasil pencarian...")
        current_url = driver.current_url
        print(f"URL saat ini setelah pencarian: {current_url}")

        assert "Bali" in current_url or "bali" in current_url.lower(
        ), f"Diharapkan 'Bali' ada di URL, tetapi ditemukan: {current_url}"
        assert f"checkin={check_in_date}" in current_url, f"Diharapkan tanggal check-in {check_in_date} ada di URL, tetapi tidak ditemukan: {current_url}"
        assert f"checkout={check_out_date}" in current_url, f"Diharapkan tanggal check-out {check_out_date} ada di URL, tetapi tidak ditemukan: {current_url}"

        print("Tes Berhasil: Pencarian untuk 'Bali' dengan tanggal dan tamu yang ditentukan berhasil dan diverifikasi melalui URL.")

    except Exception as e:
        print(f"\nTerjadi kesalahan selama pengujian: {e}")
        driver.save_screenshot("error_screenshot.png")
        print("Screenshot kesalahan disimpan sebagai error_screenshot.png")
        raise

    finally:
        print("Menutup browser.")
        driver.quit()


if __name__ == "__main__":
    test_airbnb_search_and_book_flow()
