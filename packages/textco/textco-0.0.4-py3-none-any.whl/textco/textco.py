
#***********************************************************************************************************
#*************************** WELCOME MESSAGE ****************************************************************
#***********************************************************************************************************

def textco():
  print("**********************************************************")
  print("Welcome to use TextCo: an innovative text analysis tool")
  print("**********************************************************")
  print("Contacts:")
  print("Dr Anna Sung")
  print("Prof Kelvin Leong")
  print("**********************************************************")


#***********************************************************************************************************
#*************************** WORD COUNT ****************************************************************
#***********************************************************************************************************


def count():
  # Step 1: Install necessary libraries (if not already installed)
  pip install pandas nltk

  # Step 2: Import the required libraries
  import pandas as pd
  from collections import Counter
  import io
  from google.colab import files
  import nltk
  from nltk.util import ngrams
  import csv

  # Step 3: Function to perform word count analysis with n-grams
  def word_count_analysis(csv_file, text_column, n):
      # Read the CSV file into a pandas DataFrame
      df = pd.read_csv(csv_file)

      # Combine all the text data into a single string
      text_data = " ".join(df[text_column].astype(str).tolist())

      # Tokenize the text data (split into words)
      words = text_data.split()

      # Generate n-grams from the words
      n_grams = list(ngrams(words, n))

      # Perform n-gram count using the Counter class
      n_gram_count = Counter(n_grams)

      return n_gram_count

  # Step 4: Allow the user to upload the CSV file
  uploaded = files.upload()

  # Step 5: Perform word count analysis and display the results
  if len(uploaded) > 0:
      # Get the uploaded file name
      csv_file_name = list(uploaded.keys())[0]

      # Get the column name that contains text data
      text_column = input("Enter the column name containing text data: ")

      # Get the desired n-gram length from the user
      n = int(input("Enter the desired n-gram length (e.g., 2 for bigrams, 3 for trigrams, etc.): "))

      # Get the number of rules the user wants to generate
      num_rules = int(input("Enter the number of rules you want to generate: "))

      # Perform word count analysis with n-grams
      n_gram_count_result = word_count_analysis(io.BytesIO(uploaded[csv_file_name]), text_column, n)

      # Get the top n n-grams and their counts
      top_n_n_grams = n_gram_count_result.most_common(num_rules)

      # Display the top n n-grams and their counts
      print(f"\nTop {num_rules} {n}-grams:")
      for n_gram, count in top_n_n_grams:
          print(f"{' '.join(n_gram)}: {count}")

      # Save the top n n-grams and their counts to a CSV file
      output_file_name = f"top_{n}_grams.csv"
      with open(output_file_name, 'w', newline='') as csvfile:
          csv_writer = csv.writer(csvfile)
          csv_writer.writerow([f"Top {n}-grams", "Count"])
          for n_gram, count in top_n_n_grams:
              csv_writer.writerow([' '.join(n_gram), count])

      # Provide a link to download the CSV file
      print(f"\nResults saved to: {output_file_name}")
  else:
      print("No file uploaded.")
