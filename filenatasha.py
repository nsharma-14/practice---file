import pandas as pd

directory = '/path/to/your/directory'  # Replace with your directory path
all_files = os.listdir(directory)
csv_files = [file for file in all_files if file.endswith('.csv')]

final_df = []
for file in csv_files:
    df = pd.read_csv(os.path.join(directory, file))
    filtered_df = df[df['cpt_code'] in ["CPT000EGFR", "CPT000UACR"]]
    if len(filtered_df) > 0:
        final_df.append(filtered_df)

final_df.to_csv("filetered_data_CPT_Code.csv")

df_sorted = final_df.sort_values(by='Date', ascending=False)

data = df_sorted.drop_duplicates(subset='ID', keep='first')

egfr = data[data['cpt_code'] in ["CPT000EGFR"]]["result_value"]
uacr = data[data['cpt_code'] in ["CPT000UACR"]]["result_value"]
ids =  data["ID"]

CKD_Stage = []
for i in egfr:
    if egfr >= 90:
        CKD_Stage.append("G1")
    if egfr in range(60,90) :
        CKD_Stage.append("G2")
    if egfr in range(45,60):
        CKD_Stage.append("G3a")
    if egfr in range(30,45):
        CKD_Stage.append("G3b")
    if egfr in range(15,30):
        CKD_Stage.append("G4")
    if egfr <= 15:
        CKD_Stage.append("G5")

UACR_Level = []
for i in uacr:
    if uacr <= 30:
        UACR_Level.append("A1")
    if uacr in range(30,301):
        UACR_Level.append("A2")
    if uacr >300:
        UACR_Level.append("A3")


final_data = pd.DataFrame({
    'ID': ids,
    'EGFR': egfr,
    'UACR': uacr,
    'CKD_Stage': CKD_Stage,
    'UACR_Level': UACR_Level
})

final_data.to_csv("Final_data.csv")

