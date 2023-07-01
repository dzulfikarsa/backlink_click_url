import openpyxl
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def click_link(driver, url, anchor_text_list):
    driver.get(url)

    try:
        found = False
        for anchor_text in anchor_text_list:
            elements = driver.find_elements(By.XPATH, f"//a[contains(text(), '{anchor_text}')]")
            if elements:
                for element in elements:
                    element.click()
                    print(f"Berhasil mengklik tautan '{anchor_text}' di URL: {url}")
                    write_to_report(url)
                found = True
                break

        if not found:
            print(f"Tidak ada tautan dengan kata kunci yang sesuai di URL: {url}")
            write_to_report_gagal(url)
    except:
        print(f"Gagal menemukan atau mengklik tautan di URL: {url}")
        write_to_report_gagal(url)

def write_to_report(url):
    with open("file/report.txt", "a") as file:
        file.write(f"{url}\n")

def write_to_report_gagal(url):
    with open("file/report_gagal.txt", "a") as file:
        file.write(f"{url}\n")

def process_excel(file_path, url_column):
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Menjalankan Chrome dalam mode latar belakang
    driver = webdriver.Chrome(options=chrome_options)  # Ganti dengan driver yang sesuai (misalnya Firefox)

    if chrome_options.headless:
        print("Program berjalan dalam mode headless")
    else:
        print("Program berjalan dengan tampilan grafis")

    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active

    header_row = next(sheet.iter_rows(min_row=1, max_row=1, values_only=True))
    column_index = None
    for index, header in enumerate(header_row):
        if header == url_column:
            column_index = index + 1
            break

    if column_index is None:
        print(f"Tidak dapat menemukan kolom '{url_column}' dalam file Excel.")
        return

    for row in sheet.iter_rows(min_row=2, values_only=True):
        if len(row) >= column_index:
            url = row[column_index - 1]
            anchor_text_list = [
                "Kuliah Gratis",
                "KAMPUS KOMPUTER BANYAK BEASISWA",
                "Kampus Komputer banyak beasiswa",
                "Kampus Online di Jakarta",
                "Kuliah gratis",
                "Go to link",
                "budiluhur.ac.id",
                "https://budiluhur.ac.id"
            ]
            click_link(driver, url, anchor_text_list)
        else:
            print(f"Indeks kolom '{url_column}' di luar jangkauan pada baris: {row}")

    driver.quit()

# Ubah file_path ke path file Excel yang sesuai
file_path = 'file/dataset.xlsx'

# Ubah url_column ke nama kolom yang berisi URL
url_column = 'URL'

process_excel(file_path, url_column)
