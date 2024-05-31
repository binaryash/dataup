import pandas as pd
import os
from django.shortcuts import render, redirect
from .models import Upload
from .forms import UploadForm

def upload_file(request):
    # If the request is POST, processes the data. 
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            uploaded_file = form.instance.file 
            summary_data = process_data(uploaded_file)
            return render(request, 'upload_success.html', {'summary_data': summary_data})
    # If the request is GET, returns the form 
    else:
        form = UploadForm()
    return render(request, 'upload.html', {'form': form})

def process_data(uploaded_file):
  
  #checks whether the file is excel or csv. If none, returns error
  filename, extension = os.path.splitext(uploaded_file.name)
  if extension.lower() == '.xlsx':
    df = pd.read_excel(uploaded_file.path)
  elif extension.lower() == '.csv':
    df = pd.read_csv(uploaded_file.path)
  else:
    raise ValueError(f"Unsupported file format: {extension}")

  data = df.groupby('Cust State').agg(
      DPD = ('DPD', 'count'), # Number of DPD 
      Count = ('Cust Pin', 'nunique') # count of unique customer pins
  ).reset_index()

  return data.to_html()
