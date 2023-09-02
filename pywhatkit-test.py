import pywhatkit as pwk
import pandas as pd

# using Exception Handling to avoid unexpected errors
try:
    image = "waduh.jpg"
    df = pd.read_excel('python-wa-file.xlsx')

    for idx, row in df.iterrows():
     #    Script to send wa message
        pwk.sendwhatmsg_instantly(
            "+"+str(row['Number']), row["Message"], 10, tab_close=True)

     # Script to send wa message with images
     #    pwk.sendwhats_image(
     #        "+"+str(row['Number']), image, row["Message"], 10, True)

except Exception as e:
    print(e)
