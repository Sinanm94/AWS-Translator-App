import tkinter as tk
import boto3

root = tk.Tk()
root.geometry("400x240")
root.title("AWS Translator")

textExample = tk.Text(root, height=10)
textExample.pack()

def getText():
    aws_mag_con = boto3.session.Session(profile_name='demo_user')
    client = aws_mag_con.client(service_name='translate', region_name='us-east-1')

    # Get the text from the Text widget
    text_to_translate = textExample.get("1.0", tk.END)

    # Check if there is text to translate
    if not text_to_translate.strip():
        print("Please enter text to translate.")
        return

    # Call translate_text with the text to translate
    response = client.translate_text(
        Text=text_to_translate,
        SourceLanguageCode='en',
        TargetLanguageCode='ja'
    )

    # Display the translated text and other information
    print("Original Text: " + text_to_translate)
    print("Translated Text: " + response['TranslatedText'])
    print("Source Language Code: " + response['SourceLanguageCode'])
    print("Target Language Code: " + response['TargetLanguageCode'])

btnRead = tk.Button(root, height=1, width=10, text="Read", command=getText)
btnRead.pack()

root.mainloop()